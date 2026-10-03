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

    repository._requester.requestJsonAndCheck(
        "POST",
        f"{repository.url}/issues/{parent_issue.number}/sub_issues",
        input={
            "sub_issue_id": child_issue.id,
        },
    )


def remove_sub_issue(repository, parent_issue, child_issue):
    """Remove a GitHub Issue from a GitMap-managed parent Issue."""

    repository._requester.requestJsonAndCheck(
        "DELETE",
        f"{repository.url}/issues/{parent_issue.number}/sub_issue",
        input={
            "sub_issue_id": child_issue.id,
        },
    )


def count_desired_relationships(roadmap):
    """Count parent/child relationships represented by the roadmap."""

    total = 0

    for milestone in roadmap.milestones:
        for section in milestone.sections:
            total += len(section.features)
            total += len(section.issues)

            for feature in section.features:
                total += len(feature.issues)

    return total


def _build_desired_relationships(roadmap, existing_issues):
    """
    Build the desired GitMap parent relationship for each GitHub child Issue.

    Returns:
        desired_parents:
            child_issue.id -> (child_issue, desired_parent_issue)

        managed_parent_issues:
            GitHub Issues that GitMap is allowed to manage as parents.
    """

    desired_parents = {}
    managed_parent_issues = []

    for milestone in roadmap.milestones:
        for section in milestone.sections:
            section_issue = find_github_issue_by_gitmap_id(
                section.gitmap_id,
                existing_issues,
            )

            if section_issue is not None:
                managed_parent_issues.append(section_issue)

            for feature in section.features:
                feature_issue = find_github_issue_by_gitmap_id(
                    feature.gitmap_id,
                    existing_issues,
                )

                if feature_issue is not None:
                    managed_parent_issues.append(feature_issue)

                    if section_issue is not None:
                        desired_parents[feature_issue.id] = (
                            feature_issue,
                            section_issue,
                        )

                for issue in feature.issues:
                    child_issue = find_github_issue_by_gitmap_id(
                        issue.gitmap_id,
                        existing_issues,
                    )

                    if (
                        child_issue is not None
                        and feature_issue is not None
                    ):
                        desired_parents[child_issue.id] = (
                            child_issue,
                            feature_issue,
                        )

            for issue in section.issues:
                child_issue = find_github_issue_by_gitmap_id(
                    issue.gitmap_id,
                    existing_issues,
                )

                if (
                    child_issue is not None
                    and section_issue is not None
                ):
                    desired_parents[child_issue.id] = (
                        child_issue,
                        section_issue,
                    )

    return desired_parents, managed_parent_issues


def _build_current_parent_map(
    repository,
    managed_parent_issues,
    progress_callback=None,
):
    """
    Fetch every managed parent's sub-issues exactly once.

    Returns:
        child_issue_id -> parent_issue
    """

    current_parent_by_child_id = {}

    total = len(managed_parent_issues)

    for current, parent_issue in enumerate(
        managed_parent_issues,
        start=1,
    ):
        if progress_callback is not None:
            progress_callback(
                "Relationship Inspection",
                current - 1,
                total,
                f"Checking relationships for {parent_issue.title}",
            )

        sub_issues = get_sub_issues(
            repository,
            parent_issue,
        )

        for sub_issue in sub_issues:
            child_id = sub_issue.get("id")

            if child_id is not None:
                current_parent_by_child_id[child_id] = parent_issue

        if progress_callback is not None:
            progress_callback(
                "Relationship Inspection",
                current,
                total,
                f"Checked relationships for {parent_issue.title}",
            )

    return current_parent_by_child_id


def sync_sub_issue_relationships(
    repository,
    roadmap,
    progress_callback=None,
):
    """
    Reconcile GitHub parent/child Issue relationships.

    GitHub relationship state is fetched once per managed parent and
    then reconciled from that in-memory snapshot.
    """

    existing_issues = get_existing_issues(
        repository,
        roadmap=roadmap,
    )

    (
        desired_parents,
        managed_parent_issues,
    ) = _build_desired_relationships(
        roadmap,
        existing_issues,
    )

    current_parent_by_child_id = _build_current_parent_map(
        repository,
        managed_parent_issues,
    )

    # Anything currently parented by GitMap but no longer represented
    # in the roadmap must have its GitMap-managed parent removed.
    existing_by_id = {
        issue.id: issue
        for issue in existing_issues
    }

    for child_id, current_parent in current_parent_by_child_id.items():
        if child_id in desired_parents:
            continue

        child_issue = existing_by_id.get(child_id)

        if child_issue is not None:
            desired_parents[child_id] = (
                child_issue,
                None,
            )

    total = len(desired_parents)
    results = []

    for current, (
        child_id,
        relationship,
    ) in enumerate(
        desired_parents.items(),
        start=1,
    ):
        child_issue, desired_parent = relationship

        current_parent = current_parent_by_child_id.get(
            child_id
        )

        if (
            current_parent is not None
            and desired_parent is not None
            and current_parent.id == desired_parent.id
        ):
            action = "unchanged"

        elif (
            current_parent is None
            and desired_parent is not None
        ):
            add_sub_issue(
                repository,
                desired_parent,
                child_issue,
            )

            current_parent_by_child_id[child_id] = desired_parent
            action = "added"

        elif (
            current_parent is not None
            and desired_parent is None
        ):
            remove_sub_issue(
                repository,
                current_parent,
                child_issue,
            )

            current_parent_by_child_id.pop(
                child_id,
                None,
            )

            action = "removed"

        elif (
            current_parent is not None
            and desired_parent is not None
        ):
            remove_sub_issue(
                repository,
                current_parent,
                child_issue,
            )

            add_sub_issue(
                repository,
                desired_parent,
                child_issue,
            )

            current_parent_by_child_id[child_id] = desired_parent
            action = "reparented"

        else:
            action = "unchanged"

        if desired_parent is None:
            message = (
                f"{action}: removed parent from "
                f"{child_issue.title}"
            )
        else:
            message = (
                f"{action}: "
                f"{desired_parent.title} → {child_issue.title}"
            )

        if progress_callback is not None:
            progress_callback(
                "Parent/Child Relationships",
                current,
                total,
                message,
            )

        results.append(
            {
                "child": child_issue,
                "parent": desired_parent,
                "action": action,
            }
        )

    return results