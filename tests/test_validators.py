"""Tests for GitMap roadmap validation."""

from gitmap.models import Issue, Milestone, Roadmap, Section
from gitmap.validators import validate_roadmap


def test_valid_roadmap_has_no_errors():
    """A correctly structured roadmap passes validation."""

    roadmap = Roadmap(
        name="GitMap",
        milestones=[
            Milestone(
                number="0.1",
                title="Foundations",
                Sections=[
                    Section(
                        title="Project Setup",
                        issues=[
                            Issue(
                                number="0.1.1",
                                title="Create Python Project",
                            )
                        ],
                    )
                ],
            )
        ],
    )

    errors = validate_roadmap(roadmap)

    assert errors == []


def test_blank_roadmap_name_fails():
    """A roadmap must have a name."""

    roadmap = Roadmap(name="")

    errors = validate_roadmap(roadmap)

    assert len(errors) == 1
    assert str(errors[0]) == "Roadmap name cannot be blank."


def test_blank_issue_title_fails():
    """An issue must have a title."""

    roadmap = Roadmap(
        name="GitMap",
        milestones=[
            Milestone(
                number="0.1",
                title="Foundations",
                Sections=[
                    Section(
                        title="Project Setup",
                        issues=[
                            Issue(
                                number="0.1.1",
                                title="",
                            )
                        ],
                    )
                ],
            )
        ],
    )

    errors = validate_roadmap(roadmap)

    assert len(errors) == 1
    assert str(errors[0]) == "Issue 0.1.1 cannot have a blank title."
