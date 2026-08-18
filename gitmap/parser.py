"""Parse GitMap roadmap Markdown files."""

from pathlib import Path

from gitmap.models import Feature, Issue, Milestone, Requirement, Roadmap, Section


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

    current_section: Section | None = None

    current_feature: Feature | None = None

    current_issue: Issue | None = None

    current_description_target = None

    current_requirements: list[Requirement] = []

    found_title = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("Title:"):
            name = stripped[6:].strip()
            found_title = True
            continue

        if stripped.startswith("Sub-Title:"):
            overview_lines.append(stripped[10:].strip())
            continue

        if stripped.startswith("# ") and not found_title:
            name = stripped[1:].strip()

            if name.lower().endswith(" roadmap"):
                name = name[:-8].strip()

            found_title = True
            continue

        if found_title and stripped.startswith("# "):
            milestone_heading = stripped[2:].strip()
            parts = milestone_heading.split(maxsplit=1)

            if len(parts) == 2:
                current_milestone = Milestone(
                    number=parts[0],
                    title=parts[1],
                )
                current_section = None
                current_feature = None
                current_issue = None
                current_requirements = []
                current_description_target = None
                milestones.append(current_milestone)

            continue

        if found_title and stripped.startswith("## "):
            if current_milestone is not None:
                section_heading = stripped[3:].strip()
                parts = section_heading.split(maxsplit=1)

                if len(parts) == 2:
                    current_section = Section(
                        number=parts[0],
                        title=parts[1],
                    )
                    current_description_target = current_section
                    current_feature = None
                    current_issue = None
                    current_requirements = []
                    current_milestone.sections.append(current_section)

            continue

        if found_title and stripped.startswith("### "):
            if current_section is not None:
                feature_heading = stripped[4:].strip()
                parts = feature_heading.split(maxsplit=1)

                if len(parts) == 2:
                    current_feature = Feature(
                        number=parts[0],
                        title=parts[1],
                    )
                    current_description_target = current_feature
                    current_issue = None
                    current_requirements = []
                    current_section.features.append(current_feature)

            continue

        if found_title and stripped.startswith("#### "):
            issue_heading = stripped[5:].strip()
            parts = issue_heading.split(maxsplit=1)

            if len(parts) == 2:
                current_issue = Issue(
                    number=parts[0],
                    title=parts[1],
                )
                current_description_target = current_issue

                if current_feature is not None:
                    current_feature.issues.append(current_issue)
                elif current_section is not None:
                    current_section.issues.append(current_issue)
                elif current_milestone is not None:
                    current_milestone.issues.append(current_issue)

                current_requirements = []

            continue

        if current_issue is not None and stripped.startswith("##### "):
            work_step_heading = stripped[6:].strip()
            parts = work_step_heading.split(maxsplit=1)

            if len(parts) == 2:
                work_step = Issue(
                    number=parts[0],
                    title=parts[1],
                )
                current_issue.work_steps.append(work_step)

            continue

        if current_issue is not None and stripped.startswith("[ ] "):
            work_step_text = stripped[4:].strip()
            parts = work_step_text.split(maxsplit=1)

            if len(parts) == 2:
                work_step = Issue(
                    number=parts[0],
                    title=parts[1],
                )
                current_issue.work_steps.append(work_step)

            continue

        if current_issue is not None and stripped in (
            "**Requirements:**",
            "**End Goal:**",
        ):
            current_requirements = []
            continue

        if current_issue is not None and stripped.startswith("- "):
            current_requirements.append(Requirement(text=stripped[2:].strip()))
            current_issue.requirements = current_requirements
            continue

        if (
            current_description_target is not None
            and stripped
            and not stripped.startswith("#")
            and not stripped.startswith("**")
        ):
            if current_description_target.description:
                current_description_target.description += "\n"

            current_description_target.description += stripped

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
        if line.startswith("# "):
            milestones.append(line[2:])

    return milestones
