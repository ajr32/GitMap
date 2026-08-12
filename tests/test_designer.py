"""Tests for the GitMap roadmap designer."""

from gitmap.designer import create_roadmap


def test_create_roadmap(monkeypatch):
    """The designer collects the project name and overview."""

    answers = iter(
        [
            "GitMap",
            "Turn a roadmap into a structured GitHub project.",
            "0.1",
            "Foundations",
            "",
            "",
        ]
    )

    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    roadmap = create_roadmap()

    assert len(roadmap.milestones) == 1
    assert roadmap.milestones[0].number == "0.1"
    assert roadmap.milestones[0].title == "Foundations"

def test_create_roadmap_with_milestone(monkeypatch):
    """The designer adds a milestone to the roadmap."""

    answers = iter(
        [
            "GitMap",
            "Turn a roadmap into a structured GitHub project.",
            "0.1",
            "Foundations",
            "",
            "",
        ]
    )

    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    roadmap = create_roadmap()

    assert len(roadmap.milestones) == 1
    assert roadmap.milestones[0].number == "0.1"
    assert roadmap.milestones[0].title == "Foundations"

def test_create_roadmap_with_multiple_milestones(monkeypatch):
    """The designer can collect multiple milestones."""

    answers = iter(
        [
            "GitMap",
            "Turn a roadmap into a structured GitHub project.",
            "0.1",
            "Foundations",
            "Project Setup",
            "",
            "0.2",
            "Roadmap Parser",
            "",
            "",
        ]
    )

    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    roadmap = create_roadmap()

    assert len(roadmap.milestones) == 2
    assert roadmap.milestones[0].number == "0.1"
    assert roadmap.milestones[0].title == "Foundations"
    assert roadmap.milestones[1].number == "0.2"
    assert roadmap.milestones[1].title == "Roadmap Parser"