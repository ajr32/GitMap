from dataclasses import dataclass

from gitmap.github_sync.github_representation import (
    LabelMapping,
    MilestoneMapping,
    map_issue,
)
from gitmap.github_sync.hierarchy_sync import (
    classify_hierarchy_issues,
    count_hierarchy_classifications,
    sync_hierarchy_issues,
)
from gitmap.github_sync.issue_lookup import find_existing_issue, get_existing_issues
from gitmap.github_sync.label_sync import (
    find_existing_label,
    get_existing_labels,
    sync_labels,
)
from gitmap.github_sync.milestone_sync import (
    find_existing_milestone,
    get_existing_milestones,
    sync_milestones,
)
from gitmap.github_sync.relationship_sync import sync_sub_issue_relationships
from gitmap.roadmap.traversal import iter_roadmap_issues


def build_issue_body(mapping):
    """Build the GitHub issue body from a roadmap issue mapping."""

    body = mapping.description.strip()

    if mapping.work_steps:
        body += "\n\n**Work Steps:**\n"

        for work_step in mapping.work_steps:
            body += f"- [ ] {work_step.title}\n"

    if mapping.requirements:
        body += "\n\n**End Goal:**\n"

        for requirement in mapping.requirements:
            body += f"- {requirement.text}\n"

    if mapping.gitmap_id:
        body += f"\nGitMap-ID: {mapping.gitmap_id}"

    body += f"\nGitMap: {mapping.number}"

    return body


def create_issue(repository, mapping, milestone, labels):
    """Create a GitHub issue from an issue mapping."""

    return repository.create_issue(
        title=mapping.title,
        body=build_issue_body(mapping),
        milestone=milestone,
        labels=labels,
    )


def preserve_work_step_checkboxes(existing_body: str, new_body: str) -> str:
    """Preserve completed GitHub Work Step checkboxes during an issue update."""

    checked_steps = set()

    for line in existing_body.splitlines():
        stripped = line.strip()

        if stripped.startswith("- [x] ") or stripped.startswith("- [X] "):
            checked_steps.add(stripped[6:])

    lines = []

    for line in new_body.splitlines():
        stripped = line.strip()

        if stripped.startswith("- [ ] "):
            step_title = stripped[6:]

            if step_title in checked_steps:
                line = line.replace("- [ ] ", "- [x] ", 1)

        lines.append(line)

    return "\n".join(lines)


def sync_issue(repository, mapping, expected_operation=None):
    """Create or update an issue from a roadmap mapping."""

    existing_issues = get_existing_issues(repository)
    existing = find_existing_issue(mapping, existing_issues)

    if expected_operation == "update" and existing is None:
        raise RuntimeError(
            f"Approved hierarchy update no longer exists: {mapping.title}"
        )

    if expected_operation == "create" and existing is not None:
        raise RuntimeError(
            f"Approved hierarchy create became an update: {mapping.title}"
        )

    milestone, labels = resolve_issue_targets(
        repository,
        mapping,
    )

    if existing:
        new_body = build_issue_body(mapping)

        new_body = preserve_work_step_checkboxes(
            existing.body or "",
            new_body,
        )

        existing.edit(
            title=mapping.title,
            body=new_body,
            milestone=milestone,
            labels=[label.name for label in labels],
        )
        return existing, False

    issue = create_issue(
        repository,
        mapping,
        milestone,
        labels,
    )

    return issue, True


def apply_roadmap_label_to_existing_issues(repository, roadmap):
    """Apply the roadmap-specific label to existing roadmap Issues."""

    existing_issues = get_existing_issues(repository)

    for milestone in roadmap.milestones:
        issue_locations = [(issue, None, None) for issue in milestone.issues]

        for section in milestone.sections:
            issue_locations.extend((issue, section, None) for issue in section.issues)

            for feature in section.features:
                issue_locations.extend(
                    (issue, section, feature) for issue in feature.issues
                )

        for issue, section, feature in issue_locations:
            mapping = map_issue(
                issue,
                milestone,
                section,
                feature,
                roadmap=roadmap,
            )

            existing = find_existing_issue(
                mapping,
                existing_issues,
            )

            if existing is None:
                continue

            roadmap_label = f"GitMap: {roadmap.name}"

            if any(
                label.name.casefold() == roadmap_label.casefold()
                for label in existing.labels
            ):
                continue

            existing.add_to_labels(roadmap_label)


def inspect_existing_roadmap_hierarchy(
    repository,
    roadmap,
):
    """Inspect hierarchy Issues for an existing synchronized roadmap."""

    existing_issues = get_existing_issues(repository)

    classifications = classify_hierarchy_issues(
        roadmap,
        existing_issues,
    )

    counts = count_hierarchy_classifications(
        classifications,
    )

    return {
        "classifications": classifications,
        "counts": counts,
        "missing_mappings": [
            entry["mapping"]
            for entry in classifications["missing"]
        ],
    }


def sync_issues(
    repository,
    roadmap,
    issues_to_sync=None,
    hierarchy_mappings_to_sync=None,
    update_issues=None,
    hierarchy_expected_operation="update",
    progress_start=0,
    progress_total=None,
    roadmap_path=None,
    progress_callback=None,
):
    """Synchronize changed roadmap issues with GitHub."""

    if progress_callback is not None:
        progress_callback(
            "Milestones",
            None,
            None,
            "Synchronizing GitHub milestones...",
        )

    sync_milestones(repository, roadmap)

    if progress_callback is not None:
        progress_callback(
            "Labels",
            None,
            None,
            "Synchronizing GitHub labels...",
        )

    sync_labels(repository, roadmap)

    results = []

    if issues_to_sync is not None:
        issues_to_sync = {id(issue) for issue in issues_to_sync}

    if update_issues is not None:
        update_issues = {id(issue) for issue in update_issues}

    if progress_total is None:
        progress_total = (
            len(issues_to_sync)
            if issues_to_sync is not None
            else 0
        )

    progress = progress_start + len(hierarchy_mappings_to_sync or [])

    if hierarchy_mappings_to_sync:
        hierarchy_results = sync_hierarchy_issues(
            repository,
            roadmap,
            mappings=hierarchy_mappings_to_sync,
            expected_operation=hierarchy_expected_operation,
            progress_start=progress_start,
            progress_total=progress_total,
            progress_callback=progress_callback,
        )

        results.extend(hierarchy_results)

    for issue, milestone, section, feature in iter_roadmap_issues(roadmap):
        if issues_to_sync is not None and id(issue) not in issues_to_sync:
            continue

        progress += 1

        message = f"Processing {issue.number} {issue.title}"

        if progress_callback is not None:
            progress_callback(
                "Issues",
                progress - progress_start,
                max(progress_total - progress_start, 0),
                message,
            )

        mapping = map_issue(
            issue,
            milestone,
            section,
            feature,
            roadmap=roadmap,
        )

        try:
            expected_operation = (
                "update"
                if update_issues is not None and id(issue) in update_issues
                else "create"
            )

            result, created = sync_issue(
                repository,
                mapping,
                expected_operation=expected_operation,
            )

            results.append((result, created))

        except Exception as error:
            remaining = progress_total - progress

            raise SynchronizationError(
                message=f"Failed to synchronize {issue.number} {issue.title}",
                completed=len(results),
                failed=issue,
                remaining=remaining,
                original_error=error,
            ) from error

    sync_sub_issue_relationships(
        repository,
        roadmap,
        progress_callback=progress_callback,
    )

    return results


@dataclass
class SynchronizationError(Exception):
    """Raised when synchronization stops after a GitHub operation fails."""

    def __init__(
        self,
        message,
        completed,
        failed,
        remaining,
        original_error,
    ):
        super().__init__(message)

        self.completed = completed
        self.failed = failed
        self.remaining = remaining
        self.original_error = original_error


def resolve_issue_targets(repository, mapping):
    """Resolve the GitHub milestone and labels for an issue."""

    milestones = get_existing_milestones(repository)
    labels = get_existing_labels(repository)

    milestone_mapping = MilestoneMapping(
        number=mapping.number,
        title=mapping.milestone,
    )

    milestone = find_existing_milestone(
        milestone_mapping,
        milestones,
    )

    issue_labels = []

    for label_name in mapping.labels:
        label_mapping = LabelMapping(name=label_name)
        label = find_existing_label(label_mapping, labels)

        if label:
            issue_labels.append(label)

    return milestone, issue_labels