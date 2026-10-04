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
        input={"sub_issue_id": child_issue.id},
    )


def remove_sub_issue(repository, parent_issue, child_issue):
    """Remove a GitHub Issue from a GitMap-managed parent Issue."""
    repository._requester.requestJsonAndCheck(
        "DELETE",
        f"{repository.url}/issues/{parent_issue.number}/sub_issue",
        input={"sub_issue_id": child_issue.id},
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
    """Build desired child->parent relationships and managed parent Issues."""
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
                    if child_issue is not None and feature_issue is not None:
                        desired_parents[child_issue.id] = (
                            child_issue,
                            feature_issue,
                        )

            for issue in section.issues:
                child_issue = find_github_issue_by_gitmap_id(
                    issue.gitmap_id,
                    existing_issues,
                )
                if child_issue is not None and section_issue is not None:
                    desired_parents[child_issue.id] = (
                        child_issue,
                        section_issue,
                    )

    return desired_parents, managed_parent_issues


def _build_current_parent_map(repository, managed_parent_issues):
    """Fetch each managed parent's sub-issues once and build child->parent map."""
    current_parent_by_child_id = {}
    for parent_issue in managed_parent_issues:
        for sub_issue in get_sub_issues(repository, parent_issue):
            child_id = sub_issue.get("id")
            if child_id is not None:
                current_parent_by_child_id[child_id] = parent_issue
    return current_parent_by_child_id


def sync_sub_issue_relationships(
    repository,
    roadmap,
    progress_callback=None,
    result_collector=None,
):
    """Reconcile GitHub parent/child Issue relationships."""
    existing_issues = get_existing_issues(repository, roadmap=roadmap)
    desired_parents, managed_parent_issues = _build_desired_relationships(
        roadmap,
        existing_issues,
    )
    current_parent_by_child_id = _build_current_parent_map(
        repository,
        managed_parent_issues,
    )

    existing_by_id = {issue.id: issue for issue in existing_issues}
    for child_id in list(current_parent_by_child_id):
        if child_id in desired_parents:
            continue
        child_issue = existing_by_id.get(child_id)
        if child_issue is not None:
            desired_parents[child_id] = (child_issue, None)

    total = len(desired_parents)
    results = []

    for current, (child_id, relationship) in enumerate(
        desired_parents.items(),
        start=1,
    ):
        child_issue, desired_parent = relationship
        current_parent = current_parent_by_child_id.get(child_id)

        try:
            if (
                current_parent is not None
                and desired_parent is not None
                and current_parent.id == desired_parent.id
            ):
                action = "unchanged"
            elif current_parent is None and desired_parent is not None:
                add_sub_issue(repository, desired_parent, child_issue)
                current_parent_by_child_id[child_id] = desired_parent
                action = "added"
            elif current_parent is not None and desired_parent is None:
                remove_sub_issue(repository, current_parent, child_issue)
                current_parent_by_child_id.pop(child_id, None)
                action = "removed"
            elif current_parent is not None and desired_parent is not None:
                remove_sub_issue(repository, current_parent, child_issue)
                add_sub_issue(repository, desired_parent, child_issue)
                current_parent_by_child_id[child_id] = desired_parent
                action = "reparented"
            else:
                action = "unchanged"
        except Exception as error:
            if result_collector is not None:
                result_collector.failed(
                    "Relationship",
                    child_issue.title,
                    str(error),
                )
            raise

        if desired_parent is None:
            description = f"Parent removed from {child_issue.title}"
            message = f"{action}: removed parent from {child_issue.title}"
        else:
            description = f"{desired_parent.title} → {child_issue.title}"
            message = f"{action}: {description}"

        if result_collector is not None:
            if action == "unchanged":
                result_collector.skipped(
                    "Relationship",
                    description,
                    "Already up to date",
                )
            else:
                result_collector.updated(
                    "Relationship",
                    description,
                    action.capitalize(),
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
