"""Tests for GitMap data models."""

from gitmap.models import Issue, Milestone, Requirement, Roadmap, Section


def test_create_roadmap():
    """A roadmap can contain milestones, Sections, issues, and requirements."""

    requirement = Requirement(text="Create the GitMap package.")

    issue = Issue(
        number="0.1.1",
        title="Create Python Project",
        requirements=[requirement],
    )

    section = Section(
        title="Project Setup",
        issues=[issue],
    )

    milestone = Milestone(
        number="0.1",
        title="Foundations",
        sections=[section],
    )

    roadmap = Roadmap(
        name="GitMap",
        overview="Turn a roadmap into a structured GitHub project.",
        milestones=[milestone],
    )

    assert roadmap.name == "GitMap"
    assert roadmap.milestones[0].title == "Foundations"
    assert roadmap.milestones[0].sections[0].title == "Project Setup"
    assert roadmap.milestones[0].sections[0].issues[0].number == "0.1.1"
    assert (
        roadmap.milestones[0].sections[0].issues[0].requirements[0].text
        == "Create the GitMap package."
    )


def test_issue_can_have_sub_issues():
    """An issue can contain another issue as a sub-issue."""

    child = Issue(
        number="0.2.5.1",
        title="Parse Nested Issue",
    )

    parent = Issue(
        number="0.2.5",
        title="Parse Sub-Issues",
        sub_issues=[child],
    )

    assert parent.sub_issues[0].number == "0.2.5.1"
    assert parent.sub_issues[0].title == "Parse Nested Issue"
