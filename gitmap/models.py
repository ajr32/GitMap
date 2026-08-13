"""Data models used by GitMap."""

from dataclasses import dataclass, field


@dataclass
class Requirement:
    """A requirement belonging to a roadmap item."""

    text: str


@dataclass
class Issue:
    """A roadmap issue."""

    number: str
    title: str
    description: str = ""
    requirements: list[Requirement] = field(default_factory=list)
    sub_issues: list["Issue"] = field(default_factory=list)


@dataclass
class Feature:
    """A roadmap feature."""

    number: str
    title: str
    description: str = ""
    issues: list[Issue] = field(default_factory=list)


@dataclass
class Section:
    """A collection of related roadmap items."""

    number: str
    title: str
    description: str = ""
    features: list[Feature] = field(default_factory=list)
    issues: list[Issue] = field(default_factory=list)


@dataclass
class Milestone:
    """A roadmap milestone."""

    number: str
    title: str
    sections: list[Section] = field(default_factory=list)
    issues: list[Issue] = field(default_factory=list)


@dataclass
class Roadmap:
    """A complete GitMap roadmap."""

    name: str
    overview: str = ""
    milestones: list[Milestone] = field(default_factory=list)
