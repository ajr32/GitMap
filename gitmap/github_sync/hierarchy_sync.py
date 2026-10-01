from gitmap.github_sync.github_representation import MilestoneMapping, should_use_section_issue, \
	should_use_feature_issue, map_section_issue, map_feature_issue
from gitmap.github_sync.issue_lookup import get_existing_issues, find_existing_issue, classify_existing_issue
from gitmap.github_sync.milestone_sync import get_existing_milestones, find_existing_milestone


def build_hierarchy_issue_body(mapping):
    """Build the body for a Section or Feature GitHub Issue."""

    body = mapping.description.strip()

    if mapping.gitmap_id:
        body += f"\n\nGitMap-ID: {mapping.gitmap_id}"

    body += f"\nGitMap: {mapping.number}"
    body += f"\nGitMap-Type: {mapping.hierarchy_type}"

    return body


def create_hierarchy_issue(repository, mapping, milestone, labels=None):
    """Create a GitHub Issue representing a Section or Feature."""

    return repository.create_issue(
        title=mapping.title,
        body=build_hierarchy_issue_body(mapping),
        milestone=milestone,
        labels=labels or [],
    )


def sync_hierarchy_issue(
    repository,
    mapping,
    expected_operation=None,
    roadmap=None,
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

    labels = []

    if roadmap is not None:
        labels.append(f"GitMap: {roadmap.name}")

    if existing:
        existing.edit(
            title=mapping.title,
            body=build_hierarchy_issue_body(mapping),
            milestone=milestone,
            labels=labels,
        )
        return existing, False

    issue = create_hierarchy_issue(
        repository,
        mapping,
        milestone,
        labels=labels,
    )

    return issue, True


def sync_hierarchy_issues(
    repository,
    roadmap,
    mappings=None,
    expected_operation=None,
    progress_start=0,
    progress_total=None,
    progress_callback=None,
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

        message = (
            f"{action} hierarchy {mapping.hierarchy_type.title()}: "
            f"{mapping.number} {mapping.title}"
        )

        if progress_callback is not None:
            progress_callback(
                "Hierarchy Issues",
                progress - progress_start,
                len(mappings),
                message,
            )

        result, created = sync_hierarchy_issue(
            repository,
            mapping,
            expected_operation=expected_operation,
            roadmap=roadmap,
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
