from dataclasses import dataclass

from github import Github

from gitmap.mapping_mod.mapping import (
    LabelMapping,
    MilestoneMapping,
    map_feature_issue,
    map_issue,
    map_section_issue,
    should_use_feature_issue,
    should_use_section_issue,
)
from gitmap.mapping_mod.mapping_issues import (
    build_hierarchy_issue_body,
    build_issue_body,
    classify_existing_issue,
    find_existing_issue,
    find_existing_issue_by_gitmap_id,
    get_gitmap_id_from_github_issue,
)
from gitmap.mapping_mod.mapping_labels import find_existing_label, get_existing_labels
from gitmap.mapping_mod.mapping_milestones import (
    find_existing_milestone,
    get_existing_milestones,
)
from gitmap.mapping_mod.mapping_state import iter_roadmap_issues

DEFAULT_LABEL_COLOR = "0366d6"
FIRST_GITMAP_ID = "goredsox"


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
                    )
                )

            if use_features:
                for feature in section.features:
                    mappings.append(
                        map_feature_issue(
                            feature,
                            milestone,
                            section,
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
    print(f'  Sections: {counts["existing"]["section"]}')
    print(f'  Features: {counts["existing"]["feature"]}')
    print()

    print("Missing:")
    print(f'  Sections: {counts["missing"]["section"]}')
    print(f'  Features: {counts["missing"]["feature"]}')
    print()

    print("Conflicts:")
    print(f'  Sections: {counts["conflicts"]["section"]}')
    print(f'  Features: {counts["conflicts"]["feature"]}')

def confirm_missing_hierarchy_issues(counts):
    """Ask whether missing hierarchy Issues should be created."""

    missing_sections = counts["missing"]["section"]
    missing_features = counts["missing"]["feature"]

    total_missing = missing_sections + missing_features

    if total_missing == 0:
        return False

    print()
    response = input(
        f"Create the {total_missing} missing hierarchy Issues? "
        "[(y)es/(n)o]: "
    ).strip().lower()

    return response in ("y", "yes")

def get_github_client(token):
    """Create an authenticated GitHub client."""

    return Github(token)


def increment_gitmap_id(gitmap_id: str) -> str:
    """Return the next GitMap ID using outside-in paired counting."""

    if len(gitmap_id) != 8 or not gitmap_id.isalpha() or not gitmap_id.islower():
        raise ValueError(f"Invalid GitMap ID: {gitmap_id}")

    letters = list(gitmap_id)

    pairs = [
        (0, 7),  # positions 1 & 8
        (1, 6),  # positions 2 & 7
        (2, 5),  # positions 3 & 6
        (3, 4),  # positions 4 & 5
    ]

    for left, right in pairs:
        # Each pair is one base-26 wheel.
        #
        # Left moves forward.
        # Right moves backward.
        #
        # The right character tells us whether this wheel
        # has completed its 26-position cycle.
        start_right = FIRST_GITMAP_ID[right]

        letters[left] = "a" if letters[left] == "z" else chr(ord(letters[left]) + 1)

        letters[right] = "z" if letters[right] == "a" else chr(ord(letters[right]) - 1)

        # If this pair has NOT returned to its starting
        # right-hand character, this increment is finished.
        if letters[right] != start_right:
            return "".join(letters)

        # This pair completed a full cycle.
        # Restore it and carry into the next pair.
        letters[left] = FIRST_GITMAP_ID[left]
        letters[right] = FIRST_GITMAP_ID[right]

    raise ValueError("GitMap ID space exhausted.")


def assign_missing_gitmap_ids(roadmap) -> list:
    """Assign unique permanent GitMap IDs to roadmap issues."""

    issues = [issue for issue, _, _, _ in iter_roadmap_issues(roadmap)]

    existing_ids = {issue.gitmap_id for issue in issues if issue.gitmap_id}

    # Existing duplicates are an error; do not make the situation worse.
    if len(existing_ids) != sum(1 for issue in issues if issue.gitmap_id):
        raise ValueError("Duplicate GitMap IDs detected.")

    next_id = FIRST_GITMAP_ID
    assigned = []

    for issue in issues:
        if issue.gitmap_id:
            continue

        while next_id in existing_ids:
            next_id = increment_gitmap_id(next_id)

        issue.gitmap_id = next_id
        existing_ids.add(next_id)
        assigned.append(issue)

        next_id = increment_gitmap_id(next_id)

    return assigned


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


def detect_new_roadmap_items(roadmap, existing_issues):
    """Return roadmap issues that do not yet exist on GitHub."""

    new_items = []

    for issue, milestone, section, feature in iter_roadmap_issues(roadmap):
        mapping = map_issue(
            issue,
            milestone,
            section,
            feature,
        )

        existing = find_existing_issue(
            mapping,
            existing_issues,
        )

        if existing is None:
            new_items.append(issue)

    return new_items


def detect_changed_roadmap_items(roadmap, existing_issues):
    """Return roadmap issues that differ from their GitHub issues."""

    changed = []

    for issue, milestone, section, feature in iter_roadmap_issues(roadmap):
        mapping = map_issue(
            issue,
            milestone,
            section,
            feature,
        )
        existing = find_existing_issue(mapping, existing_issues)

        if existing is None:
            continue

        expected_body = build_issue_body(mapping)

        changes = []

        if existing.title != mapping.title:
            changes.append("title")

        if (existing.body or "").strip() != expected_body.strip():
            changes.append("body")

        if changes:
            changed.append(
                {
                    "issue": issue,
                    "github_issue": existing,
                    "changes": changes,
                }
            )

    return changed




def detect_matching_roadmap_items(roadmap, existing_issues):
    """Return roadmap issues that already match their GitHub issues."""

    matching = []

    for issue, milestone, section, feature in iter_roadmap_issues(roadmap):
        mapping = map_issue(
            issue,
            milestone,
            section,
            feature,
        )
        existing = find_existing_issue(mapping, existing_issues)

        if existing is None:
            continue

        expected_body = build_issue_body(mapping)

        if (
            existing.title == mapping.title
            and (existing.body or "").strip() == expected_body.strip()
        ):
            matching.append(issue)

    return matching


def detect_renumbered_roadmap_items(roadmap, existing_issues):
    """Return roadmap issues whose GitMap number has changed."""

    renumbered = []

    for issue, milestone, section, feature in iter_roadmap_issues(roadmap):
        if not issue.gitmap_id:
            continue

        mapping = map_issue(
            issue,
            milestone,
            section,
            feature,
        )

        existing = find_existing_issue_by_gitmap_id(
            mapping,
            existing_issues,
        )

        if existing is None:
            continue

        body = existing.body or ""
        old_number = None

        for line in body.splitlines():
            if line.startswith("GitMap:"):
                old_number = line.removeprefix("GitMap:").strip()
                break

        if old_number and old_number != issue.number:
            renumbered.append((issue, old_number, issue.number))

    return renumbered


def summarize_roadmap_differences(roadmap, existing_issues):
    """Summarize roadmap differences before synchronization."""

    return {
        "new": detect_new_roadmap_items(roadmap, existing_issues),
        "changed": detect_changed_roadmap_items(roadmap, existing_issues),
        "hierarchy_changed": detect_changed_hierarchy_issues(
            roadmap,
            existing_issues,
        ),
        "renumbered": detect_renumbered_roadmap_items(
            roadmap,
            existing_issues,
        ),
        "matching": detect_matching_roadmap_items(roadmap, existing_issues),
        "removed": detect_removed_roadmap_items(roadmap, existing_issues),
    }


def detect_removed_roadmap_items(roadmap, existing_issues):
    """Return previously tracked GitMap issues removed from the roadmap."""

    roadmap_ids = {
        issue.gitmap_id
        for issue, _, _, _ in iter_roadmap_issues(roadmap)
        if issue.gitmap_id
    }

    removed = []

    for github_issue in existing_issues:
        if github_issue.state != "open":
            continue

        gitmap_id = get_gitmap_id_from_github_issue(github_issue)

        if not gitmap_id:
            continue

        if gitmap_id not in roadmap_ids:
            removed.append(github_issue)

    return removed


if __name__ == "__main__":
    from pathlib import Path

    from gitmap.parser import parse_roadmap

    roadmap = parse_roadmap(Path("roadmap.md"))

    milestone = roadmap.milestones[0]
    section = milestone.sections[0]
    issue = section.issues[0]

    mapping = map_issue(issue, milestone, section)

    print(f"Number: {mapping.number}")
    print(f"Title: {mapping.title}")
    print(f"Work steps: {len(mapping.work_steps)}")

    print(build_issue_body(mapping))


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
                    )
                )

            if use_features:
                for feature in section.features:
                    mappings.append(
                        map_feature_issue(
                            feature,
                            milestone,
                            section,
                        )
                    )

    return mappings
