"""Tests for GitMap roadmap parsing."""

from pathlib import Path

from gitmap.parser import parse_roadmap, parse_roadmap_text


def test_parse_roadmap_title():
    """The Title field becomes the roadmap name."""

    text = """Title: Simple Project

Sub-Title: A small example project.
"""

    roadmap = parse_roadmap_text(text)

    assert roadmap.name == "Simple Project"


def test_parse_roadmap_subtitle():
    """The Sub-Title field becomes the roadmap overview."""

    text = """Title: Simple Project

Sub-Title: A small example project.
"""

    roadmap = parse_roadmap_text(text)

    assert roadmap.overview == "A small example project."


def test_parse_milestone():
    """A level-one heading becomes a milestone."""

    text = """Title: Simple Project

# 0.1 Foundations
"""

    roadmap = parse_roadmap_text(text)

    assert len(roadmap.milestones) == 1

    milestone = roadmap.milestones[0]

    assert milestone.number == "0.1"
    assert milestone.title == "Foundations"


def test_parse_section():
    """A level-two heading becomes a section."""

    text = """Title: Simple Project

# 0.1 Foundations

## 0.1.1 Project Setup
"""

    roadmap = parse_roadmap_text(text)

    section = roadmap.milestones[0].sections[0]

    assert section.number == "0.1.1"
    assert section.title == "Project Setup"


def test_parse_issue():
    """A level-four heading becomes an issue."""

    text = """Title: Simple Project

# 0.1 Foundations

## 0.1.1 Project Setup

#### 0.1.1.0.1 Create Project
"""

    roadmap = parse_roadmap_text(text)

    issue = roadmap.milestones[0].sections[0].issues[0]

    assert issue.number == "0.1.1.0.1"
    assert issue.title == "Create Project"

def test_parse_feature():
    """A level-three heading becomes a feature within a section."""

    text = """Title: Simple Project

# 0.1 Foundations

## 0.1.1 Project Setup

### 0.1.1.1 Authentication
"""

    roadmap = parse_roadmap_text(text)

    feature = roadmap.milestones[0].sections[0].features[0]

    assert feature.number == "0.1.1.1"
    assert feature.title == "Authentication"

def test_parse_issue_under_feature():
    """An issue can belong to a feature."""

    text = """Title: Simple Project

# 0.1 Foundations

## 0.1.1 Project Setup

### 0.1.1.1 Authentication

#### 0.1.1.1.1 Create Login
"""

    roadmap = parse_roadmap_text(text)

    feature = roadmap.milestones[0].sections[0].features[0]
    issue = feature.issues[0]

    assert issue.number == "0.1.1.1.1"
    assert issue.title == "Create Login"

def test_parse_issue_under_milestone():
    """An issue can belong directly to a milestone."""

    text = """Title: Simple Project

# 0.1 Foundations

#### 0.1.0.0.1 Create Project
"""

    roadmap = parse_roadmap_text(text)

    milestone = roadmap.milestones[0]
    issue = milestone.issues[0]

    assert issue.number == "0.1.0.0.1"
    assert issue.title == "Create Project"

def test_parse_sub_issues():
    """Checkbox items become sub-issues of the current issue."""

    text = """Title: Simple Project

# 0.1 Foundations

## 0.1.1 Project Setup

#### 0.1.1.0.1 Create Project

[ ] (a) Create the package
[ ] (b) Create the tests
"""

    roadmap = parse_roadmap_text(text)

    issue = roadmap.milestones[0].sections[0].issues[0]

    assert len(issue.sub_issues) == 2

    assert issue.sub_issues[0].number == "(a)"
    assert issue.sub_issues[0].title == "Create the package"

    assert issue.sub_issues[1].number == "(b)"
    assert issue.sub_issues[1].title == "Create the tests"

def test_parse_requirements():
    """Requirements become Requirement objects on an issue."""

    text = """Title: Simple Project

# 0.1 Foundations

## 0.1.1 Project Setup

#### 0.1.1.0.1 Create Project

Create the project.

**Requirements:**
- Create the package.
- Create the tests.
"""

    roadmap = parse_roadmap_text(text)

    issue = roadmap.milestones[0].sections[0].issues[0]

    assert len(issue.requirements) == 2
    assert issue.requirements[0].text == "Create the package."
    assert issue.requirements[1].text == "Create the tests."

def test_parse_issue_description():
    """Text beneath an issue heading becomes its description."""

    text = """Title: Simple Project

# 0.1 Foundations

## 0.1.1 Project Setup

#### 0.1.1.0.1 Create Project

Create the project structure.
"""

    roadmap = parse_roadmap_text(text)

    issue = roadmap.milestones[0].sections[0].issues[0]

    assert issue.description == "Create the project structure."

def test_parse_section_description():
    """Text beneath a section heading becomes its description."""

    text = """Title: Simple Project

# 0.1 Foundations

## 0.1.1 Project Setup

Set up the basic project.
"""

    roadmap = parse_roadmap_text(text)

    section = roadmap.milestones[0].sections[0]

    assert section.description == "Set up the basic project."

def test_parse_feature_description():
    """Text beneath a feature heading becomes its description."""

    text = """Title: Simple Project

# 0.1 Foundations

## 0.1.1 Project Setup

### 0.1.1.1 Authentication

Handle user authentication.
"""

    roadmap = parse_roadmap_text(text)

    feature = roadmap.milestones[0].sections[0].features[0]

    assert feature.description == "Handle user authentication."

def test_parse_full_fixture():
    """The full roadmap fixture parses into the expected hierarchy."""

    path = Path(__file__).parent / "fixtures" / "full_project.md"

    roadmap = parse_roadmap(path)

    # Root
    assert roadmap.name == "Full Project"

    # Level 1 — Milestones
    assert len(roadmap.milestones) == 2

    foundations = roadmap.milestones[0]

    assert foundations.number == "0.1"
    assert foundations.title == "Foundations"

    # Level 2 — Sections
    assert len(foundations.sections) == 2

    project_setup = foundations.sections[0]

    assert project_setup.number == "0.1.1"
    assert project_setup.title == "Project Setup"
    assert project_setup.description == "Set up the basic project."

    # Section → Issue (Feature skipped)
    assert len(project_setup.issues) == 2

    issue = project_setup.issues[0]

    assert issue.number == "0.1.1.0.1"
    assert issue.title == "Create Project"
    assert issue.description == "Create the project structure."

    # Sub-issues
    assert len(issue.sub_issues) == 2
    assert issue.sub_issues[0].number == "(a)"
    assert issue.sub_issues[0].title == "Create the package"
    assert issue.sub_issues[1].number == "(b)"
    assert issue.sub_issues[1].title == "Create the tests"

    # Requirements
    assert [item.text for item in issue.requirements] == [
        "Create the package.",
        "Create the tests.",
    ]

    # Second Section
    documentation = foundations.sections[1]

    assert documentation.number == "0.1.2"
    assert documentation.title == "Documentation"

    # Section → Feature → Issue
    assert len(documentation.features) == 1

    feature = documentation.features[0]

    assert feature.number == "0.1.2.1"
    assert feature.title == "Documentation"
    assert feature.description == "Write the README."

    assert len(feature.issues) == 1

    feature_issue = feature.issues[0]

    assert feature_issue.number == "0.1.2.1.1"
    assert feature_issue.title == "Write README"

    # Second Milestone
    release = roadmap.milestones[1]

    assert release.number == "0.2"
    assert release.title == "Release"

    assert len(release.sections) == 1

    preparation = release.sections[0]

    assert preparation.number == "0.2.1"
    assert preparation.title == "Preparation"

    assert len(preparation.features) == 1

    feature = preparation.features[0]

    assert feature.number == "0.2.1.1"
    assert feature.title == "Testing"

    assert len(feature.issues) == 1

    issue = feature.issues[0]

    assert issue.number == "0.2.1.1.1"
    assert issue.title == "Run Tests"

def test_feature_without_section_is_ignored():
    """A feature cannot exist without a section."""

    text = """Title: Simple Project

# 0.1 Foundations

### 0.1.1.1 Authentication
"""

    roadmap = parse_roadmap_text(text)

    milestone = roadmap.milestones[0]

    assert len(milestone.sections) == 0
    assert len(milestone.issues) == 0

def test_section_without_feature_is_valid():
    """A section can contain issues without a feature."""

    text = """Title: Simple Project

# 0.1 Foundations

## 0.1.1 Project Setup

#### 0.1.1.0.1 Create Project
"""

    roadmap = parse_roadmap_text(text)

    section = roadmap.milestones[0].sections[0]

    assert section.number == "0.1.1"
    assert len(section.features) == 0
    assert len(section.issues) == 1