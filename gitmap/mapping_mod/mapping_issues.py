from dataclasses import dataclass

from gitmap.github_mapping import (
    classify_hierarchy_issues,
    collect_hierarchy_issue_mappings,
    confirm_missing_hierarchy_issues,
    count_hierarchy_classifications,
    display_hierarchy_classifications,
)
from gitmap.mapping_mod.mapping import (
    LabelMapping,
    MilestoneMapping,
    has_explicit_github_representation,
    map_issue,
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
from gitmap.parser import write_github_representation_to_roadmap
from gitmap.roadmap_menus import choose_github_representation


def get_existing_issues(repository):
    """Retrieve GitMap-managed issues from a GitHub repository."""

    return [
        issue
        for issue in repository.get_issues(state="all")
        if is_gitmap_managed_issue(issue)
    ]

def has_existing_gitmap_issues(repository):
    """Return whether the repository already contains synchronized GitMap issues."""

    return bool(get_existing_issues(repository))

def get_gitmap_id_from_github_issue(issue) -> str:
    """Return the permanent GitMap ID stored in a GitHub issue body."""

    body = issue.body or ""

    for line in body.splitlines():
        if line.startswith("GitMap-ID:"):
            return line.removeprefix("GitMap-ID:").strip()

    return ""


def find_existing_issue_by_gitmap_id(mapping, existing_issues):
    """Find an existing GitHub issue by permanent GitMap ID."""

    if not mapping.gitmap_id:
        return None

    for issue in existing_issues:
        if get_gitmap_id_from_github_issue(issue) == mapping.gitmap_id:
            return issue

    return None


def find_existing_issue(mapping, existing_issues):
    """Find an existing GitHub issue by permanent ID or roadmap number."""

    existing = find_existing_issue_by_gitmap_id(
        mapping,
        existing_issues,
    )

    if existing is not None:
        return existing

    # Backward-compatible fallback for roadmaps that have not
    # yet been migrated to permanent GitMap IDs.
    marker = f"GitMap: {mapping.number}"

    for issue in existing_issues:
        if marker in (issue.body or ""):
            return issue

    return None

def find_all_existing_issue_matches(mapping, existing_issues):
    """Return all GitHub issues that could represent a GitMap mapping."""

    matches = []

    for issue in existing_issues:
        body = issue.body or ""

        gitmap_id = get_gitmap_id_from_github_issue(issue)

        id_matches = (
            mapping.gitmap_id
            and gitmap_id == mapping.gitmap_id
        )

        number_matches = any(
            line.strip() == f"GitMap: {mapping.number}"
            for line in body.splitlines()
        )

        if id_matches or number_matches:
            matches.append(issue)

    return matches

def classify_existing_issue(mapping, existing_issues):
    """Classify a GitMap mapping as existing, missing, or conflicting."""

    matches = find_all_existing_issue_matches(
        mapping,
        existing_issues,
    )

    if not matches:
        return "missing", []

    if len(matches) == 1:
        return "existing", matches

    return "conflict", matches


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


def is_gitmap_managed_issue(issue):
    """Return True if the GitHub issue is managed by GitMap."""

    body = issue.body or ""

    return "GitMap-ID:" in body or "GitMap:" in body


def build_hierarchy_issue_body(mapping):
    """Build the body for a Section or Feature GitHub Issue."""

    body = mapping.description.strip()

    if mapping.gitmap_id:
        body += f"\n\nGitMap-ID: {mapping.gitmap_id}"

    body += f"\nGitMap: {mapping.number}"
    body += f"\nGitMap-Type: {mapping.hierarchy_type}"

    return body


def create_hierarchy_issue(repository, mapping, milestone):
    """Create a GitHub Issue representing a Section or Feature."""

    return create_issue(
        title=mapping.title,
        body=build_hierarchy_issue_body(mapping),
        milestone=milestone,
    )


def sync_hierarchy_issue(repository, mapping):
    """Create or update a Section or Feature GitHub Issue."""

    existing_issues = get_existing_issues(repository)
    existing = find_existing_issue(mapping, existing_issues)

    milestones = get_existing_milestones(repository)

    milestone_mapping = MilestoneMapping(
        number=mapping.number,
        title=mapping.milestone,
    )

    milestone = find_existing_milestone(
        milestone_mapping,
        milestones,
    )

    if existing:
        existing.edit(
            title=mapping.title,
            body=build_hierarchy_issue_body(mapping),
            milestone=milestone,
        )
        return existing, False

    issue = create_hierarchy_issue(
        repository,
        mapping,
        milestone,
    )

    return issue, True


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


def sync_existing_roadmap_hierarchy_issues(
    repository,
    roadmap,
    roadmap_path=None,
):
    """Handle hierarchy Issues safely for an existing synchronized roadmap."""

    if not has_explicit_github_representation(roadmap):
        roadmap_structure = getattr(
            roadmap,
            "structure",
            "sections_and_features",
        )

        roadmap.github_representation = choose_github_representation(roadmap_structure)

        if roadmap_path is not None:
            write_github_representation_to_roadmap(
                roadmap_path,
                roadmap,
            )

    existing_issues = get_existing_issues(repository)

    classifications = classify_hierarchy_issues(
        roadmap,
        existing_issues,
    )

    counts = count_hierarchy_classifications(
        classifications,
    )

    display_hierarchy_classifications(counts)

    if not confirm_missing_hierarchy_issues(counts):
        return []

    missing_mappings = [
        entry["mapping"]
        for entry in classifications["missing"]
    ]

    return sync_hierarchy_issues(
        repository,
        roadmap,
        mappings=missing_mappings,
    )


def sync_issues(
    repository,
    roadmap,
    issues_to_sync=None,
    progress_start=0,
    progress_total=None,
    roadmap_path=None,
):
    """Synchronize changed roadmap issues with GitHub."""

    sync_milestones(repository, roadmap)
    sync_labels(repository, roadmap)

    if has_existing_gitmap_issues(repository):
        sync_existing_roadmap_hierarchy_issues(
            repository,
            roadmap,
        )
    else:
        sync_existing_roadmap_hierarchy_issues(
            repository,
            roadmap,
            roadmap_path,
        )

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


def sync_hierarchy_issues(repository, roadmap, mappings=None):
    """Synchronize Section and Feature hierarchy issues."""

    if mappings is None:
        mappings = collect_hierarchy_issue_mappings(roadmap)

    results = []

    for mapping in mappings:
        result, created = sync_hierarchy_issue(
            repository,
            mapping,
        )
        results.append((result, created))

    return results
