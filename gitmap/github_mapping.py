from dataclasses import dataclass

from github import Github, GithubException

DEFAULT_LABEL_COLOR = "0366d6"
FIRST_GITMAP_ID = "goredsox"


def get_github_client(token):
    """Create an authenticated GitHub client."""

    return Github(token)


@dataclass
class MilestoneMapping:
    number: str
    title: str


@dataclass
class LabelMapping:
    name: str


@dataclass
class IssueMapping:
    number: str
    title: str
    description: str
    requirements: list
    milestone: str
    labels: list
    work_steps: list
    gitmap_id: str = ""


@dataclass
class WorkStepMapping:
    marker: str
    title: str
    description: str
    requirements: list
    parent_number: str
    milestone: str
    labels: list

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

        letters[left] = (
            "a"
            if letters[left] == "z"
            else chr(ord(letters[left]) + 1)
        )

        letters[right] = (
            "z"
            if letters[right] == "a"
            else chr(ord(letters[right]) - 1)
        )

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
    """Assign permanent GitMap IDs to roadmap issues that do not have one."""

    issues = [
        issue
        for issue, _, _, _ in iter_roadmap_issues(roadmap)
    ]

    existing_ids = [
        issue.gitmap_id
        for issue in issues
        if issue.gitmap_id
    ]

    if existing_ids:
        next_id = increment_gitmap_id(existing_ids[-1])
    else:
        next_id = FIRST_GITMAP_ID

    assigned = []

    for issue in issues:
        if issue.gitmap_id:
            continue

        issue.gitmap_id = next_id
        assigned.append(issue)

        next_id = increment_gitmap_id(next_id)

    all_ids = [issue.gitmap_id for issue in issues if issue.gitmap_id]

    if len(all_ids) != len(set(all_ids)):
        raise ValueError("Duplicate GitMap IDs detected.")

    return assigned

def map_issue_labels(issue):
    """Map labels defined on a roadmap issue to GitHub labels."""

    labels = getattr(issue, "labels", [])

    return [LabelMapping(name=label) for label in labels]


def map_section_label(section):
    """Map a roadmap section to its GitHub label."""

    title = section.title.removesuffix(" (DONE)")

    return LabelMapping(
        name=title,
    )


def map_feature_label(feature):
    """Map a roadmap feature to its GitHub label."""

    title = feature.title.removesuffix(" (DONE)")

    return LabelMapping(
        name=title,
    )


def find_existing_label(mapping, existing_labels):
    """Find an existing GitHub label with the same name."""

    for label in existing_labels:
        if label.name.casefold() == mapping.name.casefold():
            return label

    return None


def resolve_label(mapping, existing_labels):
    """Determine whether a label already exists or needs to be created."""

    existing = find_existing_label(mapping, existing_labels)

    if existing:
        return existing

    return mapping


def map_milestone(milestone):
    """Map a roadmap milestone to its GitHub representation."""
    title = milestone.title.removesuffix(" (DONE)")

    return MilestoneMapping(
        number=milestone.number,
        title=f"{milestone.number} {title}",
    )


def find_existing_milestone(mapping, existing_milestones):
    """Find an existing GitHub milestone, including a renumbered milestone."""

    # First try the exact title.
    for milestone in existing_milestones:
        existing_title = milestone.title.removesuffix(" (DONE)")

        if existing_title == mapping.title:
            return milestone

    # Then try matching without the milestone number.
    mapping_parts = mapping.title.split(maxsplit=1)

    if len(mapping_parts) != 2:
        return None

    mapping_name = mapping_parts[1]

    for milestone in existing_milestones:
        existing_title = milestone.title.removesuffix(" (DONE)")
        existing_parts = existing_title.split(maxsplit=1)

        if len(existing_parts) != 2:
            continue

        existing_name = existing_parts[1]

        if existing_name == mapping_name:
            return milestone

    return None


def resolve_milestone(mapping, existing_milestones):
    """Determine whether a milestone already exists or needs to be created."""

    existing = find_existing_milestone(mapping, existing_milestones)

    if existing:
        return existing

    return mapping


def get_existing_milestones(repository):
    """Retrieve existing milestones from a GitHub repository"""

    return list(repository.get_milestones())


def create_missing_milestones(repository, mappings):
    """Create missing milestones and update renumbered milestones."""

    existing_milestones = get_existing_milestones(repository)
    milestones = list(existing_milestones)

    for mapping in mappings:
        existing = find_existing_milestone(mapping, milestones)

        if existing:
            existing_title = existing.title.removesuffix(" (DONE)")

            if existing_title != mapping.title:
                existing.edit(title=mapping.title)

            continue

        milestone = repository.create_milestone(
            title=mapping.title,
        )
        milestones.append(milestone)

    return milestones


def sync_milestones(repository, roadmap):
    """Create any missing milestones for a roadmap."""

    mappings = [map_milestone(milestone) for milestone in roadmap.milestones]

    return create_missing_milestones(repository, mappings)


def map_issue(issue, milestone, section=None, feature=None):
    """Map a roadmap issue to its GitHub representation."""

    labels = []

    if section is not None:
        labels.append(section.title.removesuffix(" (DONE)"))

    if feature is not None:
        labels.append(feature.title.removesuffix(" (DONE)"))

    return IssueMapping(
        number=issue.number,
        title=issue.title.removesuffix(" (DONE)"),
        description=issue.description,
        requirements=issue.requirements,
        milestone=f"{milestone.number} {milestone.title.removesuffix(' (DONE)')}",
        labels=[section.title.removesuffix(" (DONE)")],
        work_steps=issue.work_steps,
        gitmap_id=issue.gitmap_id,
    )


def map_work_step(work_step, parent_issue, milestone, section):
    """Map a roadmap work step to its GitHub representation."""

    return WorkStepMapping(
        marker=work_step.number,
        title=work_step.title,
        description=work_step.description,
        requirements=work_step.requirements,
        parent_number=parent_issue.number,
        milestone=milestone.title,
        labels=[section.title],
    )


def get_existing_labels(repository):
    """Retrieve existing labels from a GitHub repository."""

    return list(repository.get_labels())


def create_missing_labels(repository, mappings):
    """Create missing labels and return all available labels."""

    existing_labels = get_existing_labels(repository)
    labels = list(existing_labels)

    for mapping in mappings:
        existing = find_existing_label(mapping, labels)

        if existing:
            continue

        try:
            label = repository.create_label(
                name=mapping.name,
                color=DEFAULT_LABEL_COLOR,
            )
        except GithubException as error:
            if error.status == 422:
                existing_labels = get_existing_labels(repository)
                label = find_existing_label(mapping, existing_labels)

                if label is None:
                    raise
            else:
                raise

        labels.append(label)

    return labels


def sync_labels(repository, roadmap):
    """Create any missing structural labels for a roadmap."""

    mappings = collect_label_mappings(roadmap)
    return create_missing_labels(repository, mappings)


def collect_label_mappings(roadmap):
    """Collect the labels required by a roadmap."""

    mappings = []

    for milestone in roadmap.milestones:
        for issue in milestone.issues:
            mappings.extend(map_issue_labels(issue))

        for section in milestone.sections:
            mappings.append(map_section_label(section))

            for issue in section.issues:
                mappings.extend(map_issue_labels(issue))

            for feature in section.features:
                mappings.append(map_feature_label(feature))

                for issue in feature.issues:
                    mappings.extend(map_issue_labels(issue))

    return mappings


def prepare_labels(repository, roadmap):
    """Prepare roadmap labels for GitHub synchronization."""

    mappings = collect_label_mappings(roadmap)
    existing_labels = get_existing_labels(repository)

    return [resolve_label(mapping, existing_labels) for mapping in mappings]


def preview_missing_labels(repository, roadmap):
    """Preview labels that would be created without changing GitHub."""

    mappings = collect_label_mappings(roadmap)
    existing_labels = get_existing_labels(repository)

    missing = [
        mapping
        for mapping in mappings
        if not find_existing_label(mapping, existing_labels)
    ]

    for mapping in missing:
        print(f"Would create label: {mapping.name}")

    return missing


def get_existing_issues(repository):
    """Retrieve GitMap-managed issues from a GitHub repository."""

    return [
        issue
        for issue in repository.get_issues(state="all")
        if is_gitmap_managed_issue(issue)
    ]

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

def build_issue_body(mapping):
    """Build the GitHub issue body from a roadmap issue mapping."""

    body = mapping.description.strip()

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

    if issues_to_sync is not None:
        issues_to_sync = {id(issue) for issue in issues_to_sync}

    if progress_total is None:
        progress_total = (
            len(issues_to_sync)
            if issues_to_sync is not None
            else 0
        )

    progress = progress_start
    results = []

    for milestone in roadmap.milestones:
        for issue in milestone.issues:
            if issues_to_sync is not None and id(issue) not in issues_to_sync:
                continue

            progress += 1
            print(
                f"[{progress}/{progress_total}] "
                f"Processing {issue.number} {issue.title}"
            )

            mapping = map_issue(issue, milestone)
            result, created = sync_issue(repository, mapping)
            results.append((result, created))

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
                result, created = sync_issue(repository, mapping)
                results.append((result, created))

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
                    result, created = sync_issue(repository, mapping)
                    results.append((result, created))

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

        issue.edit(state="closed")
        results.append(issue)

    return results

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


def preserve_issue_numbers(matches):
    """Return GitMap issue numbers mapped to GitHub issue numbers."""
    return {
        roadmap_number: github_issue.number
        for roadmap_number, github_issue in matches.items()
    }


def associate_issues_with_milestones(existing_issues):
    """Associate GitMap-managed issues with their GitHub milestones."""

    associations = {}

    for issue in existing_issues:
        if not is_gitmap_managed_issue(issue):
            continue

        if issue.milestone is None:
            continue

        marker = "GitMap:"
        body = issue.body or ""

        for line in body.splitlines():
            if line.startswith(marker):
                roadmap_number = line.removeprefix(marker).strip()
                associations[roadmap_number] = issue.milestone
                break

    return associations


def associate_issues_with_sections(existing_issues, roadmap):
    """Associate GitMap-managed issues with their roadmap sections."""

    associations = {}

    section_names = {
        section.title.removesuffix(" (DONE)"): section
        for milestone in roadmap.milestones
        for section in milestone.sections
    }

    for issue in existing_issues:
        if not is_gitmap_managed_issue(issue):
            continue

        for label in issue.labels:
            if label.name in section_names:
                associations[issue.number] = section_names[label.name]
                break

    return associations


def associate_issues_with_features(existing_issues, roadmap):
    """Associate GitMap-managed issues with their roadmap features."""

    associations = {}

    feature_names = {
        feature.title.removesuffix(" (DONE)"): feature
        for milestone in roadmap.milestones
        for section in milestone.sections
        for feature in section.features
    }

    for issue in existing_issues:
        if not is_gitmap_managed_issue(issue):
            continue

        for label in issue.labels:
            if label.name in feature_names:
                associations[issue.number] = feature_names[label.name]
                break

    return associations


def restore_work_step_relationships(existing_issues):
    """Restore work steps from GitMap-managed GitHub issue bodies."""

    relationships = {}

    for issue in existing_issues:
        if not is_gitmap_managed_issue(issue):
            continue

        body = issue.body or ""
        lines = body.splitlines()

        in_work_steps = False
        work_steps = []

        for line in lines:
            if line.strip() == "**Work Steps:**":
                in_work_steps = True
                continue

            if in_work_steps:
                if not line.startswith("- ["):
                    if line.strip():
                        break
                    continue

                work_steps.append(line.strip())

        if work_steps:
            relationships[issue.number] = work_steps

    return relationships


def find_unmatched_roadmap_items(roadmap, existing_issues):
    """Return roadmap issues that cannot be safely matched to GitHub issues."""

    matched_numbers = set()

    for issue in existing_issues:
        if not is_gitmap_managed_issue(issue):
            continue

        body = issue.body or ""

        for line in body.splitlines():
            if line.startswith("GitMap:"):
                roadmap_number = line.removeprefix("GitMap:").strip()
                matched_numbers.add(roadmap_number)
                break

    unmatched = []

    for issue, _, _, _ in iter_roadmap_issues(roadmap):
        if issue.number not in matched_numbers:
            unmatched.append(issue)

    return unmatched


def rebuild_roadmap_state(repository, roadmap):
    """Rebuild GitMap project state from existing GitHub data."""

    existing_issues = get_existing_issues(repository)

    return {
        "milestones": associate_issues_with_milestones(existing_issues),
        "sections": associate_issues_with_sections(existing_issues, roadmap),
        "features": associate_issues_with_features(existing_issues, roadmap),
        "work_steps": restore_work_step_relationships(existing_issues),
        "unmatched": find_unmatched_roadmap_items(roadmap, existing_issues),
    }


def iter_roadmap_issues(roadmap):
    """Yield every roadmap issue with its structural context."""

    for milestone in roadmap.milestones:
        for issue in getattr(milestone, "issues", []):
            yield issue, milestone, None, None

        for section in getattr(milestone, "sections", []):
            for issue in getattr(section, "issues", []):
                yield issue, milestone, section, None

            for feature in getattr(section, "features", []):
                for issue in getattr(feature, "issues", []):
                    yield issue, milestone, section, feature


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

        if (
            existing.title != mapping.title
            or (existing.body or "").strip() != expected_body.strip()
        ):
            changed.append(issue)

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
            renumbered.append(
                (issue, old_number, issue.number)
            )

    return renumbered

def summarize_roadmap_differences(roadmap, existing_issues):
    """Summarize roadmap differences before synchronization."""

    return {
        "new": detect_new_roadmap_items(roadmap, existing_issues),
        "changed": detect_changed_roadmap_items(roadmap, existing_issues),
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


def is_gitmap_managed_issue(issue):
    """Return True if the GitHub issue is managed by GitMap."""

    body = issue.body or ""

    return "GitMap-ID:" in body or "GitMap:" in body


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
