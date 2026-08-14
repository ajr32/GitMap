"""Tests for GitMap roadmap printing."""

from gitmap.parser import parse_roadmap
from gitmap.printer import print_roadmap


def test_print_roadmap(capsys):
    """The printer outputs the roadmap hierarchy."""

    roadmap = parse_roadmap("tests/fixtures/full_project.md")

    print_roadmap(roadmap)

    output = capsys.readouterr().out

    assert "Title: Full Project" in output
    assert "# 0.1 Foundations" in output
    assert "## 0.1.1 Project Setup" in output
    assert "### 0.1.2.1 Documentation" in output
    assert "#### 0.1.1.0.1 Create Project" in output
    assert "[ ] (a) Create the package" in output