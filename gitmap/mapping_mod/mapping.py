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


def map_milestone(milestone):
    """Map a roadmap milestone to its GitHub representation."""
    title = milestone.title.removesuffix(" (DONE)")

    return MilestoneMapping(
        number=milestone.number,
        title=f"{milestone.number} {title}",
    )


def map_issue(issue, milestone, section=None, feature=None):
    """Map a roadmap issue to its GitHub representation."""

    labels = []

    if section is not None:
        labels.append(section.title.removesuffix(" (DONE)"))

    if feature is not None:
        labels.append(feature.title.removesuffix(" (DONE)"))

    return IssueMapping(
        number=issue.number,
        title=f"{issue.number} {issue.title.removesuffix(' (DONE)')}",
        description=issue.description,
        requirements=issue.requirements,
        milestone=f"{milestone.number} {milestone.title.removesuffix(' (DONE)')}",
        labels=labels,
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
