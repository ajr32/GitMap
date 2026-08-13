"""Tests for the GitMap roadmap designer."""

from pathlib import Path

from gitmap.designer import create_roadmap
from gitmap.parser import parse_roadmap


def roadmap_answers(path: str | Path) -> list[str]:
    """Turn a roadmap fixture into designer input."""

    roadmap = parse_roadmap(path)

    answers = [
        roadmap.name,
        roadmap.overview,
    ]

    for milestone in roadmap.milestones:
        answers.extend(
            [
                milestone.number,
                milestone.title,
            ]
        )

        for section in milestone.sections:
            answers.extend(
                [
                    section.title,
                    section.description,
                ]
            )

        answers.append("")

    answers.append("")
    print(answers)
    return answers


def test_create_roadmap(monkeypatch):
    """The designer collects the project name and overview."""
    print(Path(__file__).resolve())
    answers = iter(
        roadmap_answers(Path(__file__).parent / "fixtures" / "simple_project.md")
    )

    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    roadmap = create_roadmap()

    assert len(roadmap.milestones) == 1
    assert roadmap.milestones[0].number == "0.1"
    assert roadmap.milestones[0].title == "Foundations"


def test_create_roadmap_with_milestone(monkeypatch):
    """The designer adds a milestone to the roadmap."""

    answers = iter(
        roadmap_answers(Path(__file__).parent / "fixtures" / "simple_project.md")
    )

    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    roadmap = create_roadmap()

    assert len(roadmap.milestones) == 1
    assert roadmap.milestones[0].number == "0.1"
    assert roadmap.milestones[0].title == "Foundations"


def test_create_roadmap_with_multiple_milestones(monkeypatch):
    """The designer can collect multiple milestones."""

    answers = iter(
        roadmap_answers(Path(__file__).parent / "fixtures" / "full_project.md")
    )

    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    roadmap = create_roadmap()

    assert len(roadmap.milestones) == 2
    assert roadmap.milestones[0].number == "0.1"
    assert roadmap.milestones[0].title == "Foundations"
    assert roadmap.milestones[1].number == "0.2"
    assert roadmap.milestones[1].title == "Roadmap Parser"
