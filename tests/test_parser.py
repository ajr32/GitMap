"""Tests for GitMap roadmap parsing."""

from gitmap.parser import parse_roadmap, parse_roadmap_text

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


def test_parse_epics():
    """Epic headings become Epic objects within their milestone."""

    text = """# GitMap Roadmap

Project overview.

## 0.1 Foundations

### Project Setup

**Type:** Epic

### Roadmap Format

**Type:** Epic
"""

    roadmap = parse_roadmap_text(text)

    milestone = roadmap.milestones[0]

    assert len(milestone.epics) == 2
    assert milestone.epics[0].title == "Project Setup"
    assert milestone.epics[1].title == "Roadmap Format"


def test_parse_issues():
    """Issue headings become Issue objects within their epic."""

    text = """# GitMap Roadmap

Project overview.

## 0.1 Foundations

### Project Setup

**Type:** Epic

#### 0.1.1 Create Python Project

Create the basic Python project structure.

#### 0.1.2 Install Dependencies

Set up development dependencies.
"""

    roadmap = parse_roadmap_text(text)

    issues = roadmap.milestones[0].epics[0].issues

    assert len(issues) == 2
    assert issues[0].number == "0.1.1"
    assert issues[0].title == "Create Python Project"
    assert issues[1].number == "0.1.2"
    assert issues[1].title == "Install Dependencies"


def test_parse_issue_description():
    """Text beneath an issue heading becomes its description."""

    text = """# GitMap Roadmap

## 0.1 Foundations

### Project Setup

**Type:** Epic

#### 0.1.1 Create Python Project

Create the basic Python project structure for GitMap.
"""

    roadmap = parse_roadmap_text(text)

    issue = roadmap.milestones[0].epics[0].issues[0]

    assert issue.description == (
        "Create the basic Python project structure for GitMap."
    )

def test_parse_requirements():
    """Requirements become Requirement objects on an issue."""

    text = """# GitMap Roadmap

Project overview.

## 0.1 Foundations

### Project Setup

#### 0.1.1 Create Project

Create the project.

**Requirements:**
- Create the package.
- Create the tests.
"""

    roadmap = parse_roadmap_text(text)

    issue = roadmap.milestones[0].epics[0].issues[0]

    assert len(issue.requirements) == 2
    assert issue.requirements[0].text == "Create the package."
    assert issue.requirements[1].text == "Create the tests."

from pathlib import Path


def test_parse_full_fixture():
    """The full roadmap fixture parses into the expected hierarchy."""

    path = Path("tests/fixtures/full_project.md")

    roadmap = parse_roadmap(path)

    assert roadmap.name == "Full Project"
    assert len(roadmap.milestones) == 2

    foundations = roadmap.milestones[0]

    assert foundations.number == "0.1"
    assert foundations.title == "Foundations"
    assert len(foundations.epics) == 2

    project_setup = foundations.epics[0]

    assert project_setup.title == "Project Setup"
    assert len(project_setup.issues) == 2

    issue = project_setup.issues[0]

    assert issue.number == "0.1.1"
    assert issue.title == "Create Project"
    assert issue.description == "Create the project structure."
    assert [item.text for item in issue.requirements] == [
        "Create the package.",
        "Create the tests.",
    ]