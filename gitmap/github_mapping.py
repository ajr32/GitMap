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
    sub_issues: list

@dataclass
class SubIssueMapping:
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

    return [
        LabelMapping(name=label)
        for label in labels
    ]

def map_section_label(section):
    """Map a roadmap section to its GitHub label."""

    title = section.title.removesuffix(" (DONE)")

    return LabelMapping(
        name=title,
    )

def find_existing_label(mapping, existing_labels):
    """Find an existing GitHub label with the same name."""

    for label in existing_labels:
        if label.name.casefold() == mapping.name.casefold():            return label

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

    mappings = [
        map_milestone(milestone)
        for milestone in roadmap.milestones
    ]

    return create_missing_milestones(repository, mappings)

def map_issue(issue, milestone, section):
    """Map a roadmap issue to its GitHub representation."""

    return IssueMapping(
        number=issue.number,
        title=issue.title.removesuffix(" (DONE)"),
        description=issue.description,
        requirements=issue.requirements,
        milestone=milestone.title.removesuffix(" (DONE)"),
        labels=[section.title.removesuffix(" (DONE)")],
        sub_issues=issue.sub_issues,
    )

def map_sub_issue(sub_issue, parent_issue, milestone, section):
    """Map a roadmap sub-issue to its GitHub representation."""

    return SubIssueMapping(
        marker=sub_issue.number,
        title=sub_issue.title,
        description=sub_issue.description,
        requirements=sub_issue.requirements,
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

    return [
        resolve_label(mapping, existing_labels)
        for mapping in mappings
    ]

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
    """Retrieve existing issues from a GitHub repository."""

    return list(repository.get_issues(state="all"))

def find_existing_issue(mapping, existing_issues):
    """Find an existing GitHub issue by GitMap roadmap number."""

    marker = f"GitMap: {mapping.number}"

    for issue in existing_issues:
        if marker in issue.body:
            return issue

    return None

def build_issue_body(mapping):
    """Build the GitHub issue body from a roadmap issue mapping."""

    body = mapping.description.strip()

    if mapping.requirements:
        body += "\n\nEnd Goal:\n"

        for requirement in mapping.requirements:
            body += f"- {requirement.text}\n"

    if mapping.sub_issues:
        body += "\n\nSub-Issues:\n"

        for sub_issue in mapping.sub_issues:
            title = sub_issue.title.removesuffix(" (DONE)")
            checkbox = "[x]" if sub_issue.title.endswith(" (DONE)") else "[ ]"
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

    if existing:
        existing.edit(body=build_issue_body(mapping))
        return existing, False

    milestone, labels = resolve_issue_targets(
        repository,
        mapping,
    )

    issue = create_issue(
        repository,
        mapping,
        milestone,
        labels,
    )

    return issue, True

def sync_issues(repository, roadmap):
    """Synchronize all roadmap issues with GitHub."""

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

def read_existing_labels(repo):
    """Return the existing GitHub labels by name."""
    labels = {}

    for label in repo.get_labels():
        labels[label.name] = label

    return labels



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
    print(f"Sub-issues: {len(mapping.sub_issues)}")

    print(build_issue_body(mapping))