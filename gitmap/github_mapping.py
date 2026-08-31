import re

from github import Github

from gitmap.mapping_mod.mapping import (
    LabelMapping,
    MilestoneMapping,
    map_issue,
)
from gitmap.mapping_mod.mapping_issues import (
    build_issue_body,
    detect_changed_hierarchy_issues,
    find_existing_issue,
    find_existing_issue_by_gitmap_id,
    get_gitmap_id_from_github_issue,
)
from gitmap.mapping_mod.mapping_labels import (
    find_existing_label,
    get_existing_labels,
)
from gitmap.mapping_mod.mapping_milestones import (
    find_existing_milestone,
    get_existing_milestones,
)
from gitmap.mapping_mod.mapping_state import iter_roadmap_issues

DEFAULT_LABEL_COLOR = "0366d6"
FIRST_GITMAP_ID = "goredsox"


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


def normalize_work_step_checkboxes(body: str) -> str:
    """Ignore GitHub checkbox completion state when comparing issue bodies."""

    return re.sub(
        r"^- \[[xX ]\]",
        "- [ ]",
        body,
        flags=re.MULTILINE,
    )


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

        existing_body = normalize_work_step_checkboxes(existing.body or "")
        expected_body = normalize_work_step_checkboxes(expected_body)

        if existing_body.strip() != expected_body.strip():
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
        existing_body = normalize_work_step_checkboxes(existing.body or "")
        expected_body = normalize_work_step_checkboxes(expected_body)

        if (
            existing.title == mapping.title
            and existing_body.strip() == expected_body.strip()
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
