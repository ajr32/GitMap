"""Parse GitMap roadmap Markdown files."""

from pathlib import Path

from gitmap.models import Milestone, Roadmap

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
                milestones.append(
                    Milestone(
                        number=parts[0],
                        title=parts[1],
                    )
                )

            continue

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