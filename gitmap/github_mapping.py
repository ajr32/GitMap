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

    return MilestoneMapping(
        number=milestone.number,
        title=milestone.title,
    )

def find_existing_milestone(mapping, existing_milestones):
    """Find an existing GitHub milestone with the same title."""

    for milestone in existing_milestones:
        if milestone.title == mapping.title:
            return milestone

    return None

def resolve_milestone(mapping, existing_milestones):
    """Determine whether a milestone already exists or needs to be created."""

    existing = find_existing_milestone(mapping, existing_milestones)

    if existing:
        return existing

    return mapping

def map_issue(issue, milestone, section):
    """Map a roadmap issue to its GitHub representation."""

    return IssueMapping(
        number=issue.number,
        title=issue.title,
        description=issue.description,
        requirements=issue.requirements,
        milestone=milestone.title,
        labels=[section.title],
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

