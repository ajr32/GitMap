from dataclasses import dataclass


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

def find_existing_label(mapping, existing_labels):
    """Find an existing GitHub label with the same name."""

    for label in existing_labels:
        if label.name == mapping.name:
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