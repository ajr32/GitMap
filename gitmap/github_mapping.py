from dataclasses import dataclass

from github import Github, GithubException

DEFAULT_LABEL_COLOR = "0366d6"


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


@dataclass
class WorkStepMapping:
    marker: str
    title: str
    description: str
    requirements: list
    parent_number: str
    milestone: str
    labels: list


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
    """Find an existing GitHub milestone with the same title."""

    for milestone in existing_milestones:
        if milestone.title.removesuffix(" (DONE)") == mapping.title:
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
    """Create milestones that do not already exist."""

    existing_milestones = get_existing_milestones(repository)
    milestones = list(existing_milestones)

    for mapping in mappings:
        existing = find_existing_milestone(mapping, milestones)

        if existing:
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


def map_issue(issue, milestone, section):
    """Map a roadmap issue to its GitHub representation."""

    return IssueMapping(
        number=issue.number,
        title=issue.title.removesuffix(" (DONE)"),
        description=issue.description,
        requirements=issue.requirements,
        milestone=f"{milestone.number} {milestone.title.removesuffix(' (DONE)')}",
        labels=[section.title.removesuffix(" (DONE)")],
        work_steps=issue.work_steps,
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
        for section in milestone.sections:
            mappings.append(map_section_label(section))

            for issue in section.issues:
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


def find_existing_issue(mapping, existing_issues):
    """Find an existing GitHub issue by GitMap roadmap number."""

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

    if mapping.work_steps:
        body += "\n\n**Work Steps:**\n"

        for work_step in mapping.work_steps:
            title = work_step.title.removesuffix(" (DONE)")
            checkbox = "[x]" if work_step.title.endswith(" (DONE)") else "[ ]"
            body += f"- {checkbox} {title}\n"

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


def sync_issues(repository, roadmap):
    """Synchronize all roadmap issues with GitHub."""

    sync_milestones(repository, roadmap)
    sync_labels(repository, roadmap)

    results = []

    for milestone in roadmap.milestones:
        for section in milestone.sections:
            for issue in section.issues:
                mapping = map_issue(issue, milestone, section)
                result, created = sync_issue(repository, mapping)

                results.append((result, created))

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

    for milestone in roadmap.milestones:
        for section in milestone.sections:
            for issue in section.issues:
                if issue.number not in matched_numbers:
                    unmatched.append(issue)

    return unmatched


def rebuild_roadmap_state(repository, roadmap):
    """Rebuild GitMap project state from existing GitHub data."""

    existing_issues = get_existing_issues(repository)

    return {
        "milestones": associate_issues_with_milestones(existing_issues),
        "sections": associate_issues_with_sections(existing_issues, roadmap),
        "work_steps": restore_work_step_relationships(existing_issues),
        "unmatched": find_unmatched_roadmap_items(roadmap, existing_issues),
    }


def detect_new_roadmap_items(roadmap, existing_issues):
    """Return roadmap issues that do not yet exist on GitHub."""

    existing_numbers = set()

    for issue in existing_issues:
        body = issue.body or ""

        for line in body.splitlines():
            if line.startswith("GitMap:"):
                existing_numbers.add(line.removeprefix("GitMap:").strip())
                break

    new_items = []

    for milestone in roadmap.milestones:
        for section in milestone.sections:
            for issue in section.issues:
                if issue.number not in existing_numbers:
                    new_items.append(issue)

    return new_items


def detect_changed_roadmap_items(roadmap, existing_issues):
    """Return roadmap issues that differ from their GitHub issues."""

    changed = []

    for milestone in roadmap.milestones:
        for section in milestone.sections:
            for issue in section.issues:
                mapping = map_issue(issue, milestone, section)
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

    for milestone in roadmap.milestones:
        for section in milestone.sections:
            for issue in section.issues:
                mapping = map_issue(issue, milestone, section)
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


def summarize_roadmap_differences(roadmap, existing_issues):
    """Summarize roadmap differences before synchronization."""

    return {
        "new": detect_new_roadmap_items(roadmap, existing_issues),
        "changed": detect_changed_roadmap_items(roadmap, existing_issues),
        "matching": detect_matching_roadmap_items(roadmap, existing_issues),
        "removed": detect_removed_roadmap_items(roadmap, existing_issues),
    }


def detect_removed_roadmap_items(roadmap, existing_issues):
    """Return GitMap-managed GitHub issues no longer present in the roadmap."""

    roadmap_numbers = {
        issue.number
        for milestone in roadmap.milestones
        for section in milestone.sections
        for issue in section.issues
    }

    removed = []

    for issue in existing_issues:
        if not is_gitmap_managed_issue(issue):
            continue

        body = issue.body or ""

        for line in body.splitlines():
            if line.startswith("GitMap:"):
                roadmap_number = line.removeprefix("GitMap:").strip()

                if roadmap_number not in roadmap_numbers:
                    removed.append(issue)

                break

    return removed


def is_gitmap_managed_issue(issue):
    """Return True if the GitHub issue is managed by GitMap."""
    return "GitMap:" in (issue.body or "")


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
