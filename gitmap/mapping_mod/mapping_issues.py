from dataclasses import dataclass

from gitmap.mapping_mod.mapping import (
    LabelMapping,
    MilestoneMapping,
    has_explicit_github_representation,
    map_feature_issue,
    map_issue,
    map_section_issue,
    should_use_feature_issue,
    should_use_section_issue,
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
        for line in (issue.body or "").splitlines():
            if line.strip() == marker:
                return issue
    return None


def find_all_existing_issue_matches(mapping, existing_issues):
    """Return all GitHub issues that could represent a GitMap mapping."""

    matches = []

    for issue in existing_issues:
        body = issue.body or ""

        gitmap_id = get_gitmap_id_from_github_issue(issue)

        id_matches = mapping.gitmap_id and gitmap_id == mapping.gitmap_id

        number_matches = any(
            line.strip() == f"GitMap: {mapping.number}" for line in body.splitlines()
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

    return repository.create_issue(
        title=mapping.title,
        body=build_hierarchy_issue_body(mapping),
        milestone=milestone,
    )


def sync_hierarchy_issue(
    repository,
    mapping,
    expected_operation=None,
):
    """Create or update a Section or Feature GitHub Issue."""

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

    missing_mappings = [entry["mapping"] for entry in classifications["missing"]]

    return sync_hierarchy_issues(
        repository,
        roadmap,
        mappings=missing_mappings,
        expected_operation="create",
    )


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
):
    """Synchronize changed roadmap issues with GitHub."""

    sync_milestones(repository, roadmap)
    sync_labels(repository, roadmap)
    results = []

    if issues_to_sync is not None:
        issues_to_sync = {id(issue) for issue in issues_to_sync}

    if update_issues is not None:
        update_issues = {id(issue) for issue in update_issues}

    if progress_total is None:
        progress_total = len(issues_to_sync) if issues_to_sync is not None else 0

    progress = progress_start + len(hierarchy_mappings_to_sync or [])

    if hierarchy_mappings_to_sync:
        hierarchy_results = sync_hierarchy_issues(
            repository,
            roadmap,
            mappings=hierarchy_mappings_to_sync,
            expected_operation=hierarchy_expected_operation,
            progress_start=progress_start,
            progress_total=progress_total,
        )
        results.extend(hierarchy_results)

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


def sync_hierarchy_issues(
    repository,
    roadmap,
    mappings=None,
    expected_operation=None,
    progress_start=0,
    progress_total=None,
):
    """Synchronize Section and Feature hierarchy issues."""

    if mappings is None:
        mappings = collect_hierarchy_issue_mappings(roadmap)

    if progress_total is None:
        progress_total = progress_start + len(mappings)

    progress = progress_start

    results = []

    for mapping in mappings:
        progress += 1

        action = (
            "Updating"
            if expected_operation == "update"
            else "Creating"
            if expected_operation == "create"
            else "Synchronizing"
        )

        print(f"[{progress}/{progress_total}] {action} hierarchy {mapping.title}")

        result, created = sync_hierarchy_issue(
            repository,
            mapping,
            expected_operation=expected_operation,
        )
        results.append((result, created))

    return results


def collect_hierarchy_issue_mappings(roadmap):
    """Collect Section and Feature hierarchy issues."""

    mappings = []

    use_sections = should_use_section_issue(roadmap)
    use_features = should_use_feature_issue(roadmap)

    for milestone in roadmap.milestones:
        for section in milestone.sections:
            if use_sections:
                mappings.append(
                    map_section_issue(
                        section,
                        milestone,
                        roadmap.hierarchy_issue_title_style,
                    )
                )

            if use_features:
                for feature in section.features:
                    mappings.append(
                        map_feature_issue(
                            feature,
                            milestone,
                            section,
                            roadmap.hierarchy_issue_title_style,
                        )
                    )

    return mappings


def classify_hierarchy_issues(roadmap, existing_issues):
    """Classify requested hierarchy issues as existing, missing, or conflicting."""

    results = {
        "existing": [],
        "missing": [],
        "conflicts": [],
    }

    for mapping in collect_hierarchy_issue_mappings(roadmap):
        status, matches = classify_existing_issue(
            mapping,
            existing_issues,
        )

        entry = {
            "mapping": mapping,
            "matches": matches,
        }

        if status == "conflict":
            results["conflicts"].append(entry)
        else:
            results[status].append(entry)

    return results


def count_hierarchy_classifications(classifications):
    """Count Section and Feature hierarchy issue classifications."""

    counts = {
        "existing": {
            "section": 0,
            "feature": 0,
        },
        "missing": {
            "section": 0,
            "feature": 0,
        },
        "conflicts": {
            "section": 0,
            "feature": 0,
        },
    }

    for status, entries in classifications.items():
        for entry in entries:
            mapping = entry["mapping"]
            issue_type = mapping.hierarchy_type

            if issue_type in ("section", "feature"):
                counts[status][issue_type] += 1

    return counts


def display_hierarchy_classifications(counts):
    """Display hierarchy Issue status for an existing roadmap."""

    print()
    print("Hierarchy Issues")
    print()

    print("Existing:")
    print(f"  Sections: {counts['existing']['section']}")
    print(f"  Features: {counts['existing']['feature']}")
    print()

    print("Missing:")
    print(f"  Sections: {counts['missing']['section']}")
    print(f"  Features: {counts['missing']['feature']}")
    print()

    print("Conflicts:")
    print(f"  Sections: {counts['conflicts']['section']}")
    print(f"  Features: {counts['conflicts']['feature']}")


def confirm_missing_hierarchy_issues(counts):
    """Ask whether missing hierarchy Issues should be created."""

    missing_sections = counts["missing"]["section"]
    missing_features = counts["missing"]["feature"]

    total_missing = missing_sections + missing_features

    if total_missing == 0:
        return False

    print()
    response = (
        input(f"Create the {total_missing} missing hierarchy Issues? [(y)es/(n)o]: ")
        .strip()
        .lower()
    )

    return response in ("y", "yes")


def detect_changed_hierarchy_issues(roadmap, existing_issues):
    """Return existing Section and Feature issues that differ from the roadmap."""

    changed = []

    for mapping in collect_hierarchy_issue_mappings(roadmap):
        existing = find_existing_issue(mapping, existing_issues)

        if existing is None:
            continue

        expected_body = build_hierarchy_issue_body(mapping)

        changes = []

        if existing.title != mapping.title:
            changes.append("title")

        if (existing.body or "").strip() != expected_body.strip():
            changes.append("body")

        if changes:
            changed.append(
                {
                    "mapping": mapping,
                    "github_issue": existing,
                    "changes": changes,
                }
            )

    return changed
