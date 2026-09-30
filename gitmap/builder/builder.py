from gitmap.builder.builder_add import add_item
from gitmap.builder.builder_delete import delete_item
from gitmap.builder.builder_edit import edit_item
from gitmap.builder.builder_rename import rename_item
from gitmap.roadmap_numbering import remember_numbering_state


def render_work_steps(lines, work_steps, depth=0):
    """Render work steps and any nested work steps."""

    indent = "  " * depth

    for work_step in work_steps:
        marker = work_step.work_step_marker or ""

        lines.append(f"{indent}- [ ] {work_step.number} {marker} {work_step.title}")

        if work_step.description:
            lines.append(f"{indent}  {work_step.description}")

        for requirement in work_step.requirements:
            requirement_text = (
                requirement.text if hasattr(requirement, "text") else requirement
            )
            lines.append(f"{indent}  - {requirement_text}")

        render_work_steps(
            lines,
            work_step.work_steps,
            depth + 1,
        )


def render_roadmap_markdown(roadmap):
    """Render a completed Roadmap model as Markdown."""

    lines = []

    lines.append(f"Title: {roadmap.name}")
    lines.append("")

    if roadmap.numbering_mode:
        lines.append(f"Numbering-Mode: {roadmap.numbering_mode}")
        lines.append("")

    if roadmap.starting_series is not None:
        lines.append(f"Starting-Series: {roadmap.starting_series}")
        lines.append("")

    representation = roadmap.github_representation

    if isinstance(representation, dict):
        section_value = representation.get("section") or ""
        feature_value = representation.get("feature") or ""

        lines.append(f"<!-- GitMap-Section-Representation: {section_value} -->")
        lines.append(f"<!-- GitMap-Feature-Representation: {feature_value} -->")
        lines.append("")

    if roadmap.overview:
        lines.append(f"Sub-Title: {roadmap.overview}")

    if roadmap.hierarchy_issue_title_style:
        lines.append("")
        lines.append(
            f"Hierarchy-Issue-Title-Style: {roadmap.hierarchy_issue_title_style}"
        )

    for milestone in roadmap.milestones:
        lines.append("")
        lines.append(f"# {milestone.number} {milestone.title}")

        # Milestone-level issues
        for issue in milestone.issues:
            lines.append("")
            lines.append(f"#### {issue.number} {issue.title}")

            if issue.gitmap_id:
                lines.append(f"<!-- GitMap-ID: {issue.gitmap_id} -->")

            if issue.description:
                lines.append("")
                lines.append(issue.description)

            if issue.requirements:
                lines.append("")
                lines.append("**Requirements:**")

                for requirement in issue.requirements:
                    requirement_text = (
                        requirement.text
                        if hasattr(requirement, "text")
                        else requirement
                    )
                    lines.append(f"- {requirement_text}")

            if issue.work_steps:
                lines.append("")
                lines.append("**Work Steps:**")
                render_work_steps(lines, issue.work_steps)

        # Sections
        for section in milestone.sections:
            lines.append("")
            lines.append(f"## {section.number} {section.title}")

            if section.gitmap_id:
                lines.append(f"<!-- GitMap-ID: {section.gitmap_id} -->")

            # Features
            for feature in section.features:
                lines.append("")
                lines.append(f"### {feature.number} {feature.title}")

                if feature.gitmap_id:
                    lines.append(f"<!-- GitMap-ID: {feature.gitmap_id} -->")

                if feature.description:
                    lines.append("")
                    lines.append(feature.description)

                # Feature-level issues
                for issue in feature.issues:
                    lines.append("")
                    lines.append(f"#### {issue.number} {issue.title}")

                    if issue.gitmap_id:
                        lines.append(f"<!-- GitMap-ID: {issue.gitmap_id} -->")

                    if issue.description:
                        lines.append("")
                        lines.append(issue.description)

                    if issue.requirements:
                        lines.append("")
                        lines.append("**Requirements:**")

                        for requirement in issue.requirements:
                            requirement_text = (
                                requirement.text
                                if hasattr(requirement, "text")
                                else requirement
                            )
                            lines.append(f"- {requirement_text}")

                    if issue.work_steps:
                        lines.append("")
                        lines.append("**Work Steps:**")
                        render_work_steps(lines, issue.work_steps)

            # Section-level issues
            for issue in section.issues:
                lines.append("")
                lines.append(f"#### {issue.number} {issue.title}")

                if issue.gitmap_id:
                    lines.append(f"<!-- GitMap-ID: {issue.gitmap_id} -->")

                if issue.description:
                    lines.append("")
                    lines.append(issue.description)

                if issue.requirements:
                    lines.append("")
                    lines.append("**Requirements:**")

                    for requirement in issue.requirements:
                        requirement_text = (
                            requirement.text
                            if hasattr(requirement, "text")
                            else requirement
                        )
                        lines.append(f"- {requirement_text}")

                if issue.work_steps:
                    lines.append("")
                    lines.append("**Work Steps:**")
                    render_work_steps(lines, issue.work_steps)

    return "\n".join(lines)


def review_roadmap(roadmap):
    """Allow the user to review and revise the roadmap before saving."""

    numbering_mode = roadmap.get("numbering_mode") or "manual"

    remember_numbering_state(roadmap)

    while True:
        print()
        print(render_roadmap_markdown(roadmap))
        print()
        print("Roadmap options:")
        print("  (r)ename an item")
        print("  (e)dit description or requirements")
        print("  (a)dd an item")
        print("  (d)elete an item")
        print("  (f)inished reviewing")
        print()

        choice = input("Choose an option: ").strip().lower()

        if choice in ("f", "finished", "done"):
            return roadmap

        elif choice in ("r", "rename"):
            rename_item(roadmap)

        elif choice in ("e", "edit"):
            edit_item(roadmap)

        elif choice in ("a", "add"):
            add_item(roadmap, numbering_mode)

        elif choice in ("d", "delete", "remove"):
            delete_item(roadmap)

        else:
            print("Invalid choice.")
