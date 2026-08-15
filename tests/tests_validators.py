"""Tests for GitMap roadmap validation."""

from gitmap.parser import parse_roadmap_text
from gitmap.validators import validate_roadmap
from gitmap.models import Feature, Issue, Milestone, Roadmap, Section


def test_valid_roadmap_has_no_errors():
    """A valid roadmap produces no validation errors."""

    text = """Title: Simple Project

# 0.1 Foundations

## 0.1.1 Project Setup

### 0.1.1.1 Authentication

#### 0.1.1.1.1 Create Login

Create the login system.

[ ] (a) Create the form
[ ] (b) Add validation

**Requirements:**
- Use the existing authentication system.
"""

    roadmap = parse_roadmap_text(text)

    errors = validate_roadmap(roadmap)

    assert errors == []


def test_blank_issue_title_is_invalid():
    """An issue with a blank title produces a validation error."""

    issue = Issue(
        number="0.1.1.0.1",
        title="",
    )

    milestone = Milestone(
        number="0.1",
        title="Foundations",
        issues=[issue],
    )

    roadmap = Roadmap(
        name="Simple Project",
        overview="",
        milestones=[milestone],
    )

    errors = validate_roadmap(roadmap)

    assert len(errors) == 1
    assert "blank title" in str(errors[0])


def test_blank_feature_title_is_invalid():
    """A feature with a blank title produces a validation error."""

    from gitmap.models import Feature, Section

    feature = Feature(
        number="0.1.1.1",
        title="",
    )

    section = Section(
        number="0.1.1",
        title="Project Setup",
        features=[feature],
    )

    milestone = Milestone(
        number="0.1",
        title="Foundations",
        sections=[section],
    )

    roadmap = Roadmap(
        name="Simple Project",
        overview="",
        milestones=[milestone],
    )

    errors = validate_roadmap(roadmap)

    assert len(errors) == 1
    assert "blank title" in str(errors[0])


def test_duplicate_milestone_number_is_invalid():
    """Duplicate milestone numbers produce a validation error."""

    milestone_one = Milestone(
        number="0.1",
        title="Foundations",
    )

    milestone_two = Milestone(
        number="0.1",
        title="More Foundations",
    )

    roadmap = Roadmap(
        name="Simple Project",
        overview="",
        milestones=[milestone_one, milestone_two],
    )

    errors = validate_roadmap(roadmap)

    assert len(errors) == 1
    assert "Duplicate number: 0.1" in str(errors[0])


def test_duplicate_issue_number_is_invalid():
    """Duplicate issue numbers produce a validation error."""

    issue_one = Issue(
        number="0.1.1.0.1",
        title="First Issue",
    )

    issue_two = Issue(
        number="0.1.1.0.1",
        title="Second Issue",
    )

    milestone = Milestone(
        number="0.1",
        title="Foundations",
        issues=[issue_one, issue_two],
    )

    roadmap = Roadmap(
        name="Simple Project",
        overview="",
        milestones=[milestone],
    )

    errors = validate_roadmap(roadmap)
    assert len(errors) == 1
    assert "Duplicate number: 0.1.1.0.1" in str(errors[0])
