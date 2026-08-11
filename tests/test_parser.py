"""Tests for GitMap roadmap parsing."""

from gitmap.parser import parse_roadmap_text


def test_parse_roadmap_name():
    """The roadmap project name is read from the main heading."""

    text = """# GitMap Roadmap

GitMap turns a project roadmap into a structured GitHub project.
"""

    roadmap = parse_roadmap_text(text)

    assert roadmap.name == "GitMap"


def test_parse_roadmap_overview():
    """Text below the main heading becomes the roadmap overview."""

    text = """# GitMap Roadmap

GitMap turns a project roadmap into a structured GitHub project.

## 0.1 Foundations
"""

    roadmap = parse_roadmap_text(text)

    assert (
        roadmap.overview
        == "GitMap turns a project roadmap into a structured GitHub project."
    )

def test_parse_milestones():
    """Milestone headings become Milestone objects."""

    text = """# GitMap Roadmap

Project overview.

## 0.1 Foundations

## 0.2 Roadmap Parser
"""

    roadmap = parse_roadmap_text(text)

    assert len(roadmap.milestones) == 2

    assert roadmap.milestones[0].number == "0.1"
    assert roadmap.milestones[0].title == "Foundations"

    assert roadmap.milestones[1].number == "0.2"
    assert roadmap.milestones[1].title == "Roadmap Parser"