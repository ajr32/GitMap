"""Tests for the GitMap roadmap printer."""

from gitmap.models import Epic, Issue, Milestone, Roadmap
from gitmap.printer import print_roadmap


def test_print_roadmap(capsys):
    """A roadmap is printed in the expected hierarchy."""

    roadmap = Roadmap(
        name="GitMap",
        overview="A roadmap tool.",
        milestones=[
            Milestone(
                number="0.1",
                title="Foundations",
                epics=[
                    Epic(
                        title="Project Setup",
                        issues=[
                            Issue(
                                number="0.1.1",
                                title="Create Python Project",
                                description="Create the project.",
                            )
                        ],
                    )
                ],
            )
        ],
    )

    print_roadmap(roadmap)

    output = capsys.readouterr().out

    assert "# GitMap" in output
    assert "A roadmap tool." in output
    assert "## 0.1 Foundations" in output
    assert "### Project Setup" in output
    assert "#### 0.1.1 Create Python Project" in output
    assert "Create the project." in output
