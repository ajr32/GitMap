from gitmap.builder.builder_add import add_item
from gitmap.builder.builder_delete import delete_item
from gitmap.builder.builder_edit import edit_item
from gitmap.builder.builder_rename import rename_item
from gitmap.roadmap_numbering import remember_numbering_state


def render_work_steps(lines, work_steps, depth=0):
    """Render work steps and any nested work steps."""

    indent = "  " * depth

    for work_step in work_steps:
        lines.append(f"{indent}- [ ] {work_step['number']} {work_step['title']}")

        if work_step["description"]:
            lines.append(f"{indent}  {work_step['description']}")

        for requirement in work_step["requirements"]:
            lines.append(f"{indent}  - {requirement}")

        render_work_steps(
            lines,
            work_step.get("work_steps", []),
            depth + 1,
        )


def render_roadmap_markdown(roadmap):
    """Render a completed roadmap as Markdown."""

    lines = []

    lines.append(f"Title: {roadmap['name']}")

    if roadmap.get("numbering_mode"):
        lines.append(f"Numbering-Mode: {roadmap['numbering_mode']}")

    if roadmap.get("starting_series") is not None:
        lines.append(f"Starting-Series: {roadmap['starting_series']}")

    if roadmap["overview"]:
        lines.append(f"Sub-Title: {roadmap['overview']}")

    if roadmap.get("hierarchy_issue_title_style"):
        lines.append("")
        lines.append(
            f"Hierarchy-Issue-Title-Style: {roadmap['hierarchy_issue_title_style']}"
        )

    for milestone in roadmap["milestones"]:
        lines.append("")
        lines.append(f"# {milestone['number']} {milestone['title']}")

        # Milestone-level issues
        for issue in milestone["issues"]:
            lines.append("")
            lines.append(f"#### {issue['number']} {issue['title']}")

            if issue.get("gitmap_id"):
                lines.append(f"<!-- GitMap-ID: {issue['gitmap_id']} -->")

            if issue["description"]:
                lines.append("")
                lines.append(issue["description"])

            if issue["requirements"]:
                lines.append("")
                lines.append("**Requirements:**")

                for requirement in issue["requirements"]:
                    lines.append(
                        f"- {requirement.text if hasattr(requirement, 'text') else requirement}"
                    )

            if issue["work_steps"]:
                lines.append("")
                lines.append("**Work Steps:**")
                render_work_steps(lines, issue["work_steps"])

        # Sections
        for section in milestone["sections"]:
            lines.append("")
            lines.append(f"## {section['number']} {section['title']}")

            if section.get("gitmap_id"):
                lines.append(f"<!-- GitMap-ID: {section['gitmap_id']} -->")

            if section["overview"]:
                lines.append("")
                lines.append(section["overview"])

            # Features
            for feature in section["features"]:
                lines.append("")
                lines.append(f"### {feature['number']} {feature['title']}")

                if feature.get("gitmap_id"):
                    lines.append(f"<!-- GitMap-ID: {feature['gitmap_id']} -->")

                if feature["description"]:
                    lines.append("")
                    lines.append(feature["description"])

                # Feature-level issues
                for issue in feature["issues"]:
                    lines.append("")
                    lines.append(f"#### {issue['number']} {issue['title']}")

                    if issue.get("gitmap_id"):
                        lines.append(f"<!-- GitMap-ID: {issue['gitmap_id']} -->")

                    if issue["description"]:
                        lines.append("")
                        lines.append(issue["description"])

                    if issue["requirements"]:
                        lines.append("")
                        lines.append("**Requirements:**")

                        for requirement in issue["requirements"]:
                            lines.append(
                                f"- {requirement.text if hasattr(requirement, 'text') else requirement}"
                            )

                    if issue["work_steps"]:
                        lines.append("")
                        lines.append("**Work Steps:**")
                        render_work_steps(lines, issue["work_steps"])

            # Section-level issues
            for issue in section["issues"]:
                lines.append("")
                lines.append(f"#### {issue['number']} {issue['title']}")

                if issue.get("gitmap_id"):
                    lines.append(f"<!-- GitMap-ID: {issue['gitmap_id']} -->")

                if issue["description"]:
                    lines.append("")
                    lines.append(issue["description"])

                if issue["requirements"]:
                    lines.append("")
                    lines.append("**Requirements:**")

                    for requirement in issue["requirements"]:
                        lines.append(
                            f"- {requirement.text if hasattr(requirement, 'text') else requirement}"
                        )

                if issue["work_steps"]:
                    lines.append("")
                    lines.append("**Work Steps:**")
                    render_work_steps(lines, issue["work_steps"])

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


def work_steps_to_builder_list(work_steps):
    """Convert parsed work steps into builder format."""

    builder_work_steps = []

    for work_step in work_steps:
        builder_work_steps.append(
            {
                "number": work_step.number,
                "title": work_step.title,
                "description": work_step.description,
                "requirements": work_step.requirements,
                "work_steps": work_steps_to_builder_list(work_step.work_steps),
            }
        )
    return builder_work_steps


def requirements_to_builder_list(requirements):
    return [
        requirement.text if hasattr(requirement, "text") else requirement
        for requirement in requirements
    ]


def roadmap_to_builder_dict(roadmap):
    """Convert a parsed roadmap into the builder format."""

    builder_roadmap = {
        "name": roadmap.name,
        "overview": roadmap.overview,
        "numbering_mode": roadmap.numbering_mode,
        "starting_series": roadmap.starting_series,
        "github_representation": roadmap.github_representation,
        "hierarchy_issue_title_style": roadmap.hierarchy_issue_title_style,
        "milestones": [],
    }

    for milestone in roadmap.milestones:
        builder_milestone = {
            "type": "milestone",
            "number": milestone.number,
            "title": milestone.title,
            "issues": [],
            "sections": [],
        }

        for section in milestone.sections:
            builder_section = {
                "type": "section",
                "number": section.number,
                "title": section.title,
                "gitmap_id": section.gitmap_id,
                "overview": "",
                "issues": [],
                "features": [],
            }

            for issue in section.issues:
                builder_section["issues"].append(
                    {
                        "number": issue.number,
                        "title": issue.title,
                        "gitmap_id": issue.gitmap_id,
                        "description": issue.description,
                        "requirements": requirements_to_builder_list(
                            issue.requirements
                        ),
                        "work_steps": work_steps_to_builder_list(issue.work_steps),
                    }
                )

            for feature in section.features:
                builder_feature = {
                    "type": "feature",
                    "number": feature.number,
                    "title": feature.title,
                    "gitmap_id": feature.gitmap_id,
                    "description": feature.description,
                    "issues": [],
                }

                builder_section["features"].append(builder_feature)

                for issue in feature.issues:
                    builder_feature["issues"].append(
                        {
                            "number": issue.number,
                            "title": issue.title,
                            "gitmap_id": issue.gitmap_id,
                            "description": issue.description,
                            "requirements": requirements_to_builder_list(
                                issue.requirements
                            ),
                            "work_steps": work_steps_to_builder_list(issue.work_steps),
                        }
                    )
            builder_milestone["sections"].append(builder_section)

        for issue in milestone.issues:
            builder_milestone["issues"].append(
                {
                    "number": issue.number,
                    "title": issue.title,
                    "gitmap_id": issue.gitmap_id,
                    "description": issue.description,
                    "requirements": requirements_to_builder_list(issue.requirements),
                    "work_steps": work_steps_to_builder_list(issue.work_steps),
                }
            )

        builder_roadmap["milestones"].append(builder_milestone)

    return builder_roadmap
