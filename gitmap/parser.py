"""Parse GitMap roadmap Markdown files."""

from pathlib import Path

from gitmap.models import Issue, Milestone, Requirement, Roadmap, Section


def parse_roadmap(path: str | Path) -> Roadmap:
    """Read a Markdown roadmap and return a Roadmap object."""

    roadmap_path = Path(path)

    if not roadmap_path.exists():
        raise FileNotFoundError(f"Roadmap file not found: {roadmap_path}")

    text = roadmap_path.read_text(encoding="utf-8")

    return parse_roadmap_text(text)


def parse_roadmap_text(text: str) -> Roadmap:
    """Parse roadmap Markdown text."""

    lines = text.splitlines()

    name = ""
    overview_lines: list[str] = []

    milestones: list[Milestone] = []

    current_milestone: Milestone | None = None

    current_Section: Section | None = None

    current_issue: Issue | None = None

    current_requirements: list[Requirement] = []

    found_title = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("# ") and not found_title:
            name = stripped[2:].strip()

            if name.lower().endswith(" roadmap"):
                name = name[:-8].strip()

            found_title = True
            continue

        if found_title and stripped.startswith("## "):
            milestone_heading = stripped[3:].strip()
            parts = milestone_heading.split(maxsplit=1)

            if len(parts) == 2:
                current_milestone = Milestone(
                    number=parts[0],
                    title=parts[1],
                )
                milestones.append(current_milestone)

            continue

        if found_title and stripped.startswith("### "):
            if current_milestone is not None:
                Section_title = stripped[4:].strip()

                current_Section = Section(title=Section_title)
                current_milestone.Sections.append(current_Section)

            continue

        if found_title and stripped.startswith("#### "):
            if current_Section is not None:
                issue_heading = stripped[5:].strip()
                parts = issue_heading.split(maxsplit=1)

                if len(parts) == 2:
                    current_issue = Issue(
                        number=parts[0],
                        title=parts[1],
                    )
                    current_Section.issues.append(current_issue)

            continue

        if current_issue is not None and stripped.startswith("- "):
            current_requirements.append(Requirement(text=stripped[2:].strip()))
            current_issue.requirements = current_requirements
            continue

        if current_issue is not None and stripped == "**Requirements:**":
            current_requirements = []
            continue
            
        if (
            current_issue is not None
            and stripped
            and not stripped.startswith("#")
            and not stripped.startswith("**")
        ):
            if current_issue.description:
                current_issue.description += "\n"

            current_issue.description += stripped

        if found_title and stripped:
            overview_lines.append(stripped)

    overview = "\n".join(overview_lines)

    return Roadmap(
        name=name,
        overview=overview,
        milestones=milestones,
    )


def read_roadmap(path):
    roadmap_path = Path(path)
    return roadmap_path.read_text(encoding="utf-8")


def find_headings(text):
    """Find Markdown headings in a roadmap."""
    headings = []

    for line in text.splitlines():
        if line.startswith("#"):
            headings.append(line)

    return headings


def find_issues(text):
    """Find issue headings in a roadmap."""
    issues = []

    for line in text.splitlines():
        if line.startswith("#### "):
            issues.append(line[5:])

    return issues

def find_milestones(text):
    """Find milestones headings in a roadmap."""
    milestones = []

    for line in text.splitlines():
        if line.startswith("## "):
            milestones.append(line[3:])

    return milestones