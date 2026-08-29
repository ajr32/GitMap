from gitmap.builder.builder_add import add_item
from gitmap.builder.builder_delete import delete_item
from gitmap.builder.builder_edit import edit_item
from gitmap.builder.builder_rename import rename_item


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

    if roadmap["overview"]:
        lines.append(f"Sub-Title: {roadmap['overview']}")

    for milestone in roadmap["milestones"]:
        lines.append("")
        lines.append(f"# {milestone['number']} {milestone['title']}")

        for issue in milestone["issues"]:
            lines.append("")
            lines.append(f"#### {issue['number']} {issue['title']}")

            if issue["description"]:
                lines.append("")
                lines.append(issue["description"])

            if issue["requirements"]:
                lines.append("")
                lines.append("**Requirements:**")

                for requirement in issue["requirements"]:
                    lines.append(f"- {requirement}")

            if issue["work_steps"]:
                lines.append("")
                lines.append("**Work Steps:**")

                render_work_steps(lines, issue["work_steps"])

        for section in milestone["sections"]:
            lines.append("")
            lines.append(f"## {section['number']} {section['title']}")

            if section["overview"]:
                lines.append("")
                lines.append(section["overview"])

            for feature in section["features"]:
                lines.append("")
                lines.append(f"### {feature['number']} {feature['title']}")

                if feature["description"]:
                    lines.append("")
                    lines.append(feature["description"])

                for issue in feature["issues"]:
                    lines.append("")
                    lines.append(f"#### {issue['number']} {issue['title']}")

                    if issue["description"]:
                        lines.append("")
                        lines.append(issue["description"])

                    if issue["requirements"]:
                        lines.append("")
                        lines.append("**Requirements:**")

                        for requirement in issue["requirements"]:
                            lines.append(f"- {requirement}")

                    if issue["work_steps"]:
                        lines.append("")
                        lines.append("**Work Steps:**")

                        render_work_steps(lines, issue["work_steps"])

                for issue in section["issues"]:
                    lines.append("")
                    lines.append(f"#### {issue['number']} {issue['title']}")

                    if issue["description"]:
                        lines.append("")
                        lines.append(issue["description"])

                    if issue["requirements"]:
                        lines.append("")
                        lines.append("**Requirements:**")

                        for requirement in issue["requirements"]:
                            lines.append(f"- {requirement}")

                    if issue["work_steps"]:
                        lines.append("")
                        lines.append("**Work Steps:**")

                        render_work_steps(lines, issue["work_steps"])

    return "\n".join(lines)


def review_roadmap(roadmap):
    """Allow the user to review and revise the roadmap before saving."""

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
            add_item(roadmap)

        elif choice in ("d", "delete", "remove"):
            delete_item(roadmap)

        else:
            print("Invalid choice.")


