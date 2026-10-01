from gitmap.github_sync.issue_lookup import get_existing_issues


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


def find_github_issue_by_gitmap_id(gitmap_id, existing_issues):
    """Find a GitHub Issue by its permanent GitMap ID."""

    marker = f"GitMap-ID: {gitmap_id}"

    for issue in existing_issues:
        if marker in (issue.body or ""):
            return issue

    return None


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


def sync_sub_issue_relationships(
    repository,
    roadmap,
    progress_callback=None,
):
    """Synchronize GitHub parent/child Issue relationships."""

    existing_issues = get_existing_issues(
        repository,
        roadmap=roadmap,
    )

    relationships = []

    for milestone in roadmap.milestones:
        for section in milestone.sections:
            section_issue = find_github_issue_by_gitmap_id(
                section.gitmap_id,
                existing_issues,
            )

            if section_issue is not None:
                for feature in section.features:
                    feature_issue = find_github_issue_by_gitmap_id(
                        feature.gitmap_id,
                        existing_issues,
                    )

                    if feature_issue is not None:
                        relationships.append(
                            (section_issue, feature_issue)
                        )

                for issue in section.issues:
                    child_issue = find_github_issue_by_gitmap_id(
                        issue.gitmap_id,
                        existing_issues,
                    )

                    if child_issue is not None:
                        relationships.append(
                            (section_issue, child_issue)
                        )

            for feature in section.features:
                feature_issue = find_github_issue_by_gitmap_id(
                    feature.gitmap_id,
                    existing_issues,
                )

                if feature_issue is None:
                    continue

                for issue in feature.issues:
                    child_issue = find_github_issue_by_gitmap_id(
                        issue.gitmap_id,
                        existing_issues,
                    )

                    if child_issue is not None:
                        relationships.append(
                            (feature_issue, child_issue)
                        )

    total = len(relationships)
    results = []

    for current, (parent_issue, child_issue) in enumerate(
        relationships,
        start=1,
    ):
        message = f"Linking {parent_issue.title} → {child_issue.title}"

        if progress_callback is not None:
            progress_callback(
                "Parent/Child Relationships",
                current,
                total,
                message,
            )

        created = add_sub_issue(
            repository,
            parent_issue,
            child_issue,
        )

        results.append(
            (parent_issue, child_issue, created)
        )

    return results