from dataclasses import dataclass

from gitmap.github_mapping import collect_hierarchy_issue_mappings
from gitmap.mapping_mod.mapping import LabelMapping, MilestoneMapping, map_issue
from gitmap.mapping_mod.mapping_issues import (
    build_issue_body,
    find_existing_issue,
    get_existing_issues,
    sync_hierarchy_issue,
)
from gitmap.mapping_mod.mapping_labels import (
    find_existing_label,
    get_existing_labels,
    sync_labels,
)
from gitmap.mapping_mod.mapping_milestones import (
    find_existing_milestone,
    get_existing_milestones,
    sync_milestones,
)


def create_issue(repository, mapping, milestone, labels):
    """Create a GitHub issue from an issue mapping."""

    return repository.create_issue(
        title=mapping.title,
        body=build_issue_body(mapping),
        milestone=milestone,
        labels=labels,
    )


def sync_issue(repository, mapping):
    """Create or update an issue from a roadmap mapping."""

    existing_issues = get_existing_issues(repository)
    existing = find_existing_issue(mapping, existing_issues)

    milestone, labels = resolve_issue_targets(
        repository,
        mapping,
    )

    if existing:
        existing.edit(
            title=mapping.title,
            body=build_issue_body(mapping),
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


def sync_issues(
    repository,
    roadmap,
    issues_to_sync=None,
    progress_start=0,
    progress_total=None,
):
    """Synchronize changed roadmap issues with GitHub."""

    sync_milestones(repository, roadmap)
    sync_labels(repository, roadmap)
    sync_hierarchy_issues(repository, roadmap)

    if issues_to_sync is not None:
        issues_to_sync = {id(issue) for issue in issues_to_sync}

    if progress_total is None:
        progress_total = len(issues_to_sync) if issues_to_sync is not None else 0

    progress = progress_start
    results = []

    for milestone in roadmap.milestones:
        for issue in milestone.issues:
            if issues_to_sync is not None and id(issue) not in issues_to_sync:
                continue

            progress += 1
            print(
                f"[{progress}/{progress_total}] Processing {issue.number} {issue.title}"
            )

            mapping = map_issue(issue, milestone)
            try:
                result, created = sync_issue(repository, mapping)
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

            except Exception as error:
                remaining = progress_total - progress

                raise SynchronizationError(
                    message=f"Failed to synchronize {issue.number} {issue.title}",
                    completed=len(results),
                    failed=issue,
                    remaining=remaining,
                    original_error=error,
                ) from error

        for section in milestone.sections:
            for issue in section.issues:
                if issues_to_sync is not None and id(issue) not in issues_to_sync:
                    continue

                progress += 1
                print(
                    f"[{progress}/{progress_total}] "
                    f"Processing {issue.number} {issue.title}"
                )

                mapping = map_issue(issue, milestone, section)
                try:
                    result, created = sync_issue(repository, mapping)
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

            for feature in section.features:
                for issue in feature.issues:
                    if issues_to_sync is not None and id(issue) not in issues_to_sync:
                        continue

                    progress += 1
                    print(
                        f"[{progress}/{progress_total}] "
                        f"Processing {issue.number} {issue.title}"
                    )

                    mapping = map_issue(
                        issue,
                        milestone,
                        section,
                        feature,
                    )
                    try:
                        result, created = sync_issue(repository, mapping)
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

    return results


def sync_removed_issues(
    removed_issues,
    progress_start=0,
    progress_total=None,
):
    """Close GitHub issues that were removed from the roadmap."""

    if progress_total is None:
        progress_total = progress_start + len(removed_issues)

    progress = progress_start
    results = []

    for issue in removed_issues:
        if issue.state != "open":
            continue

        progress += 1

        print(
            f"[{progress}/{progress_total}] "
            f"Closing removed issue #{issue.number} {issue.title}"
        )

        try:
            issue.edit(state="closed")
            results.append(issue)

        except Exception as error:
            remaining = progress_total - progress

            raise SynchronizationError(
                message=f"Failed to close removed issue #{issue.number}",
                completed=progress - 1,
                failed=issue,
                remaining=remaining,
                original_error=error,
            ) from error

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


def sync_hierarchy_issues(repository, roadmap):
    """Synchronize Section and Feature hierarchy issues."""

    results = []

    for mapping in collect_hierarchy_issue_mappings(roadmap):
        result, created = sync_hierarchy_issue(
            repository,
            mapping,
        )

        results.append((result, created))

    return results
