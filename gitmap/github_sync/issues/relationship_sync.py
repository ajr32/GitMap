from gitmap.github_sync.issues.issue_lookup import (
    find_github_issue_by_gitmap_id,
    get_existing_issues,
)

def get_sub_issues(repository, parent_issue):
    """Return the existing GitHub sub-issues for an Issue."""

    _, data = repository._requester.requestJsonAndCheck(
        "GET",
        f"{repository.url}/issues/{parent_issue.number}/sub_issues",
    )

    return data


def add_sub_issue(repository, parent_issue, child_issue):
    """Add a GitHub Issue as a sub-issue of another Issue."""

    sub_issues = get_sub_issues(
        repository,
        parent_issue,
    )

    if any(sub_issue["id"] == child_issue.id for sub_issue in sub_issues):
        return False

    repository._requester.requestJsonAndCheck(
        "POST",
        f"{repository.url}/issues/{parent_issue.number}/sub_issues",
        input={
            "sub_issue_id": child_issue.id,
        },
    )

    return True

def remove_sub_issue(repository, parent_issue, child_issue):
    """Remove a GitHub Issue from a GitMap-managed parent Issue."""

    sub_issues = get_sub_issues(
        repository,
        parent_issue,
    )

    if not any(
        sub_issue["id"] == child_issue.id
        for sub_issue in sub_issues
    ):
        return False

    repository._requester.requestJsonAndCheck(
        "DELETE",
        f"{repository.url}/issues/{parent_issue.number}/sub_issue",
        input={
            "sub_issue_id": child_issue.id,
        },
    )

    return True

def sync_section_feature_relationships(repository, roadmap, existing_issues):
    """Create Section-to-Feature GitHub sub-issue relationships."""

    for milestone in roadmap.milestones:
        for section in milestone.sections:
            parent_issue = find_github_issue_by_gitmap_id(
                section.gitmap_id,
                existing_issues,
            )

            if parent_issue is None:
                continue

            for feature in section.features:
                child_issue = find_github_issue_by_gitmap_id(
                    feature.gitmap_id,
                    existing_issues,
                )

                if child_issue is None:
                    continue

                add_sub_issue(
                    repository,
                    parent_issue,
                    child_issue,
                )


def sync_feature_issue_relationships(repository, roadmap, existing_issues):
    """Create Feature-to-Issue GitHub sub-issue relationships."""

    for milestone in roadmap.milestones:
        for section in milestone.sections:
            for feature in section.features:
                parent_issue = find_github_issue_by_gitmap_id(
                    feature.gitmap_id,
                    existing_issues,
                )

                if parent_issue is None:
                    continue

                for issue in feature.issues:
                    child_issue = find_github_issue_by_gitmap_id(
                        issue.gitmap_id,
                        existing_issues,
                    )

                    if child_issue is None:
                        continue

                    add_sub_issue(
                        repository,
                        parent_issue,
                        child_issue,
                    )


def sync_section_issue_relationships(repository, roadmap, existing_issues):
    """Create Section-to-Issue GitHub sub-issue relationships."""

    for milestone in roadmap.milestones:
        for section in milestone.sections:
            parent_issue = find_github_issue_by_gitmap_id(
                section.gitmap_id,
                existing_issues,
            )

            if parent_issue is None:
                continue

            for issue in section.issues:
                child_issue = find_github_issue_by_gitmap_id(
                    issue.gitmap_id,
                    existing_issues,
                )

                if child_issue is None:
                    continue

                add_sub_issue(
                    repository,
                    parent_issue,
                    child_issue,
                )


def find_current_gitmap_parent(
    repository,
    child_issue,
    managed_parent_issues,
):
    """
    Find the current GitMap-managed parent of a GitHub Issue.

    Only parents supplied in managed_parent_issues are inspected, so
    unrelated GitHub relationships are never treated as GitMap-owned.
    """

    for parent_issue in managed_parent_issues:
        sub_issues = get_sub_issues(
            repository,
            parent_issue,
        )

        if any(
            sub_issue["id"] == child_issue.id
            for sub_issue in sub_issues
        ):
            return parent_issue

    return None


def sync_sub_issue_relationships(repository, roadmap, progress_callback=None):
    """Reconcile GitHub parent/child Issue relationships."""
    existing_issues = get_existing_issues(repository, roadmap=roadmap)
    managed_parent_issues = []
    desired_parents = {}

    for milestone in roadmap.milestones:
        for section in milestone.sections:
            section_issue = find_github_issue_by_gitmap_id(section.gitmap_id, existing_issues)
            if section_issue is not None:
                managed_parent_issues.append(section_issue)

            for feature in section.features:
                feature_issue = find_github_issue_by_gitmap_id(feature.gitmap_id, existing_issues)
                if feature_issue is not None:
                    managed_parent_issues.append(feature_issue)
                    desired_parents[feature_issue.id] = (feature_issue, section_issue)

                for issue in feature.issues:
                    child_issue = find_github_issue_by_gitmap_id(issue.gitmap_id, existing_issues)
                    if child_issue is not None:
                        desired_parents[child_issue.id] = (child_issue, feature_issue)

            for issue in section.issues:
                child_issue = find_github_issue_by_gitmap_id(issue.gitmap_id, existing_issues)
                if child_issue is not None:
                    desired_parents[child_issue.id] = (child_issue, section_issue)

    # Include managed children that currently have a managed parent but
    # no longer have a desired parent in the roadmap.
    for child_issue in existing_issues:
        if child_issue.id in desired_parents:
            continue
        current_parent = find_current_gitmap_parent(
            repository, child_issue, managed_parent_issues
        )
        if current_parent is not None:
            desired_parents[child_issue.id] = (child_issue, None)

    total = len(desired_parents)
    results = []

    for current, (child_issue, desired_parent) in enumerate(
        desired_parents.values(), start=1
    ):
        current_parent = find_current_gitmap_parent(
            repository, child_issue, managed_parent_issues
        )

        if (
            current_parent is not None
            and desired_parent is not None
            and current_parent.id == desired_parent.id
        ):
            action = "unchanged"
        elif current_parent is None and desired_parent is not None:
            add_sub_issue(repository, desired_parent, child_issue)
            action = "added"
        elif current_parent is not None and desired_parent is None:
            remove_sub_issue(repository, current_parent, child_issue)
            action = "removed"
        elif current_parent is not None and desired_parent is not None:
            remove_sub_issue(repository, current_parent, child_issue)
            add_sub_issue(repository, desired_parent, child_issue)
            action = "reparented"
        else:
            action = "unchanged"

        if desired_parent is None:
            message = f"{action}: removed parent from {child_issue.title}"
        else:
            message = f"{action}: {desired_parent.title} → {child_issue.title}"

        if progress_callback is not None:
            progress_callback(
                "Parent/Child Relationships", current, total, message
            )

        results.append({
            "child": child_issue,
            "parent": desired_parent,
            "action": action,
        })

    return results
