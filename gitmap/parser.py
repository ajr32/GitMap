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


def write_hierarchy_issue_title_style_to_roadmap(
    path,
    hierarchy_issue_title_style,
):
    """Write the hierarchy Issue title style to the roadmap file."""

    roadmap_path = Path(path)
    text = roadmap_path.read_text(encoding="utf-8")

    setting = f"Hierarchy-Issue-Title-Style: {hierarchy_issue_title_style}"

    lines = text.splitlines()

    for index, line in enumerate(lines):
        if line.startswith("Hierarchy-Issue-Title-Style:"):
            lines[index] = setting
            break
    else:
        insert_at = 1
        lines.insert(insert_at, setting)

    roadmap_path.write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )


def write_gitmap_ids_to_roadmap(path: str | Path, roadmap: Roadmap) -> None:
    """Write exactly one permanent GitMap ID for each issue."""

    roadmap_path = Path(path)
    lines = roadmap_path.read_text(encoding="utf-8").splitlines()

    ids_by_number = {}

    for milestone in roadmap.milestones:
        for issue in milestone.issues:
            if issue.gitmap_id:
                ids_by_number[issue.number] = issue.gitmap_id

        for section in milestone.sections:
            if section.gitmap_id:
                ids_by_number[section.number] = section.gitmap_id

            for issue in section.issues:
                if issue.gitmap_id:
                    ids_by_number[issue.number] = issue.gitmap_id

            for feature in section.features:
                if feature.gitmap_id:
                    ids_by_number[feature.number] = feature.gitmap_id

                for issue in feature.issues:
                    if issue.gitmap_id:
                        ids_by_number[issue.number] = issue.gitmap_id

    output = []
    index = 0

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        # Never copy an existing GitMap-ID marker.
        if stripped.startswith("<!-- GitMap-ID:"):
            index += 1
            continue

        output.append(line)

        if stripped.startswith("## ") and not stripped.startswith("### "):
            heading = stripped[3:].strip()
            parts = heading.split(maxsplit=1)

            if parts:
                number = parts[0]
                gitmap_id = ids_by_number.get(number)

                if gitmap_id:
                    output.append(f"<!-- GitMap-ID: {gitmap_id} -->")

        if stripped.startswith("### ") and not stripped.startswith("#### "):
            heading = stripped[4:].strip()
            parts = heading.split(maxsplit=1)

            if parts:
                number = parts[0]
                gitmap_id = ids_by_number.get(number)

                if gitmap_id:
                    output.append(f"<!-- GitMap-ID: {gitmap_id} -->")

        if stripped.startswith("#### "):
            heading = stripped[5:].strip()
            parts = heading.split(maxsplit=1)

            if parts:
                number = parts[0]
                gitmap_id = ids_by_number.get(number)

                if gitmap_id:
                    output.append(f"<!-- GitMap-ID: {gitmap_id} -->")

        index += 1

    roadmap_path.write_text(
        "\n".join(output) + "\n",
        encoding="utf-8",
    )


def write_github_representation_to_roadmap(
    path: str | Path,
    roadmap: Roadmap,
) -> None:
    """Write GitHub hierarchy representation settings to the roadmap."""

    representation = roadmap.github_representation

    if not isinstance(representation, dict):
        return

    roadmap_path = Path(path)
    lines = roadmap_path.read_text(encoding="utf-8").splitlines()

    # Remove existing representation markers so we never duplicate them.
    output = [
        line
        for line in lines
        if not line.strip().startswith(
            (
                "<!-- GitMap-Section-Representation:",
                "<!-- GitMap-Feature-Representation:",
            )
        )
    ]

    section_value = representation.get("section") or ""
    feature_value = representation.get("feature") or ""

    markers = [
        f"<!-- GitMap-Section-Representation: {section_value} -->",
        f"<!-- GitMap-Feature-Representation: {feature_value} -->",
    ]

    # Put the settings near the top of the roadmap.
    insert_at = 0

    for index, line in enumerate(output):
        if line.strip().startswith(("Title:", "# ")):
            insert_at = index + 1
            break

    output[insert_at:insert_at] = [
        "",
        *markers,
    ]

    roadmap_path.write_text(
        "\n".join(output) + "\n",
        encoding="utf-8",
    )


def parse_roadmap_text(text: str) -> Roadmap:
    """Parse roadmap Markdown text."""

    lines = text.splitlines()

    name = ""
    overview_lines: list[str] = []

    milestones: list[Milestone] = []

    github_representation = None

    hierarchy_issue_title_style = None

    numbering_mode = None

    starting_series = None

    current_milestone: Milestone | None = None

    current_section: Section | None = None

    current_feature: Feature | None = None

    current_issue: Issue | None = None

    current_description_target = None

    current_requirements: list[Requirement] = []

    found_title = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("<!-- GitMap-Section-Representation:"):
            value = (
                stripped.removeprefix("<!-- GitMap-Section-Representation:")
                .removesuffix("-->")
                .strip()
            )

            if github_representation is None:
                github_representation = {}

            github_representation["section"] = value or None
            continue

        if stripped.startswith("<!-- GitMap-Feature-Representation:"):
            value = (
                stripped.removeprefix("<!-- GitMap-Feature-Representation:")
                .removesuffix("-->")
                .strip()
            )

            if github_representation is None:
                github_representation = {}

            github_representation["feature"] = value or None
            continue

        if stripped.startswith("Numbering-Mode:"):
            numbering_mode = stripped.removeprefix("Numbering-Mode:").strip()
            continue

        if stripped.startswith("Starting-Series:"):
            starting_series = stripped.removeprefix("Starting-Series:").strip()
            continue

        if stripped.startswith("Hierarchy-Issue-Title-Style:"):
            hierarchy_issue_title_style = stripped.removeprefix(
                "Hierarchy-Issue-Title-Style:"
            ).strip()
            continue

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

        if stripped.startswith("<!-- GitMap-ID:"):
            gitmap_id = (
                stripped.removeprefix("<!-- GitMap-ID:").removesuffix("-->").strip()
            )

            if gitmap_id:
                if current_issue is not None:
                    current_issue.gitmap_id = gitmap_id
                elif current_feature is not None:
                    current_feature.gitmap_id = gitmap_id
                elif current_section is not None:
                    current_section.gitmap_id = gitmap_id

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
        github_representation=github_representation,
        hierarchy_issue_title_style=hierarchy_issue_title_style,
        numbering_mode=numbering_mode,
        starting_series=starting_series,
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
