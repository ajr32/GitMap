def ask_project_name():
    """Ask the user to enter a project name"""
    return input("Project name: ").strip()


def ask_project_overview():
    """Ask the user to enter a project overview"""
    return collect_multiline("Project sub-title/overview:")


def start_new_roadmap():
    """Start an interactive roadmap-building session"""

    project_name = ask_project_name()
    project_overview = ask_project_overview()

    return {
        "name": project_name,
        "overview": project_overview,
        "milestones": collect_milestones(),
    }


def collect_milestones():
    """Guide the user through defining the project milestones."""

    milestones = []

    while True:
        number = input("Milestone number (or press Enter when finished): ").strip()

        if not number:
            break

        title = input("Milestone title: ").strip()

        milestone = {
            "number": number,
            "title": title,
            "issues": [],
            "sections": [],
        }

        collect_milestone_items(milestone)
        milestones.append(milestone)

    return milestones


def collect_milestone_items(milestone):
    """Collect issues and sections for a milestone."""

    print()
    print("Milestone options:")
    print("  (i)ssue   — add an issue directly to this milestone")
    print("  (s)ection — add a section")
    print("  (d)one    — finish this milestone")
    print()

    while True:
        choice = input("[(i)ssue / (s)ection / (d)one]: ").strip().lower()

        if choice in ("i", "issue"):
            milestone["issues"].extend(collect_issues(milestone))

        elif choice in ("s", "section"):
            milestone["sections"].extend(collect_sections(milestone))

        elif choice in ("d", "done"):
            break

        else:
            print("Invalid choice.")


def collect_sections(milestone):
    """Guide the user through defining sections for a milestone."""

    sections = []

    while True:
        number = input(
            f"Section number for {milestone['number']} {milestone['title']} "
            "(or press Enter when finished): "
        ).strip()

        if not number:
            break

        title = input("Section title: ").strip()

        overview = collect_multiline("Section overview:")

        section = {
            "number": number,
            "title": title,
            "overview": overview,
            "milestone": milestone["number"],
            "issues": [],
            "features": [],
        }

        collect_section_items(section)

        sections.append(section)

    return sections


def collect_section_items(section):
    """Collect issues and features for a section."""

    print()
    print("Section options:")
    print("  (i)ssue   — add an issue directly to this section")
    print("  (f)eature — add a feature")
    print("  (d)one    — finish this section")
    print()

    while True:
        choice = input("[(i)ssue / (f)eature / (d)one]: ").strip().lower()

        if choice in ("i", "issue"):
            section["issues"].extend(collect_issues(section))

        elif choice in ("f", "feature"):
            section["features"].extend(collect_features(section))

        elif choice in ("d", "done"):
            break

        else:
            print("Invalid choice.")


def collect_features(section):
    """Collect features for a section."""

    features = []

    while True:
        number = input(
            f"Feature number for {section['title']} (or press Enter when finished): "
        ).strip()

        if not number:
            break

        title = input("Feature title: ").strip()

        description = collect_multiline("Feature description:")

        feature = {
            "number": number,
            "title": title,
            "description": description,
            "section": section["title"],
            "issues": [],
        }

        feature["issues"] = collect_issues(feature)

        features.append(feature)

    return features


def collect_requirements():
    """Collect issue requirements one at a time or from pasted text."""

    requirements = []

    while True:
        requirement = input(
            "Requirement, 'paste', or press Enter when finished: "
        ).strip()

        if not requirement:
            break

        if requirement.lower() == "paste":
            requirements.extend(collect_pasted_requirements())
            continue

        requirements.append(requirement)

    return requirements


def collect_issues(parent):
    """Guide the user through defining issues for a section."""

    issues = []

    while True:
        number = input(
            f"Issue number for {parent['title']} (or press Enter when finished): "
        ).strip()

        if not number:
            break

        title = input("Issue title: ").strip()

        description = collect_multiline("Issue description:")

        issue = {
            "number": number,
            "title": title,
            "description": description,
            "requirements": [],
            "parent": parent["title"],
            "work_steps": [],
        }

        print()
        print("Issue options:")
        print()
        print(
            "  (r)equirement — something that must be true or completed for this issue"
        )
        print("  (w)ork step   — a smaller piece of work inside this issue")
        print("  (d)one        — finish this issue and move on to the next issue")
        print()

        while True:
            choice = input("[(r)equirement / (w)ork step / (d)one]: ").strip().lower()

            if choice in ("r", "requirement"):
                issue["requirements"].extend(collect_requirements())

            elif choice in ("w", "work", "work step"):
                work_step = collect_work_step(issue)

                if work_step:
                    issue["work_steps"].append(work_step)

            elif choice in ("d", "done"):
                break

            else:
                print("Invalid choice.")

        issues.append(issue)

    return issues


def collect_work_step(issue):
    """Collect one work step for an issue."""

    number = input("Work step number: ").strip()

    if not number:
        return None

    title = input("Work step title: ").strip()
    description = collect_multiline("Work step description:")
    requirements = collect_requirements()
    work_steps = []

    while True:
        choice = input("Add a nested work step? [(y)es or (n)o: ").strip().lower()

        if choice in ("y", "yes"):
            nested_work_step = collect_work_step(
                {
                    "title": title,
                }
            )

            if nested_work_step:
                work_steps.append(nested_work_step)

        elif choice in ("n", "no"):
            break

        else:
            print("Invalid choice.")

    return {
        "number": number,
        "title": title,
        "description": description,
        "requirements": requirements,
        "parent": issue["title"],
        "work_steps": work_steps,
    }


def collect_multiline(prompt):
    """Collect multiline text until the user enters a blank line."""

    print(prompt)
    print("(Press Enter on a blank line when finished.)")

    lines = []

    while True:
        line = input()

        if not line:
            break

        lines.append(line)

    return "\n".join(lines)


def collect_pasted_requirements():
    """Collect multiple requirements from pasted multiline text."""

    text = collect_multiline("Paste requirements:")

    return [line.strip() for line in text.splitlines() if line.strip()]


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


def rename_item(roadmap):
    """Choose which type of roadmap item to rename."""

    print()
    print("Rename:")
    print("  (m)ilestone")
    print("  (f)eature")
    print("  (s)ection")
    print("  (i)ssue")
    print("  (w)ork step")
    print("  (b)ack")
    print()

    choice = input("Choose an item type: ").strip().lower()

    if choice in ("m", "milestone"):
        rename_milestone(roadmap)

    elif choice in ("f", "feature"):
        rename_feature(roadmap)

    elif choice in ("s", "section"):
        rename_section(roadmap)

    elif choice in ("i", "issue"):
        rename_issue(roadmap)

    elif choice in ("w", "work", "work step"):
        rename_work_step(roadmap)

    elif choice in ("b", "back"):
        return

    else:
        print("Invalid choice.")


def rename_milestone(roadmap):
    """Rename a milestone."""

    print()
    print("Milestones:")

    for milestone in roadmap["milestones"]:
        print(f"  • {milestone['number']} {milestone['title']}")

    number = input("Milestone number to rename: ").strip()

    for milestone in roadmap["milestones"]:
        if milestone["number"] == number:
            new_title = input("New milestone title: ").strip()

            if new_title:
                milestone["title"] = new_title

            return

    print("Milestone not found.")


def rename_section(roadmap):
    """Rename a section."""

    print()
    print("Sections:")

    sections = []

    for milestone in roadmap["milestones"]:
        for section in milestone["sections"]:
            sections.append(section)
            print(f"  • {section['number']} {section['title']}")

    number = input("Section number to rename: ").strip()

    for section in sections:
        if section["number"] == number:
            new_title = input("New section title: ").strip()

            if new_title:
                section["title"] = new_title

            return

    print("Section not found.")


def rename_feature(roadmap):
    """Rename a feature."""

    print()
    print("Features:")

    features = []

    for milestone in roadmap["milestones"]:
        for section in milestone["sections"]:
            for feature in section["features"]:
                features.append(feature)
                print(f"  • {feature['number']} {feature['title']}")

    number = input("Feature number to rename: ").strip()

    for feature in features:
        if feature["number"] == number:
            new_title = input("New feature title: ").strip()

            if new_title:
                feature["title"] = new_title

            return

    print("Feature not found.")


def rename_issue(roadmap):
    """Rename an issue."""

    print()
    print("Issues:")

    issues = []

    for milestone in roadmap["milestones"]:
        issues.extend(milestone["issues"])

        for section in milestone["sections"]:
            issues.extend(section["issues"])

            for feature in section["features"]:
                issues.extend(feature["issues"])

    for issue in issues:
        print(f"  • {issue['number']} {issue['title']}")

    number = input("Issue number to rename: ").strip()

    for issue in issues:
        if issue["number"] == number:
            new_title = input("New issue title: ").strip()

            if new_title:
                issue["title"] = new_title

            return

    print("Issue not found.")


def rename_work_step(roadmap):
    """Rename a work step, including nested work steps."""

    print()
    print("Work Steps:")

    work_steps = []

    def collect_nested(steps):
        for step in steps:
            work_steps.append(step)
            collect_nested(step.get("work_steps", []))

    for milestone in roadmap["milestones"]:
        for issue in milestone["issues"]:
            collect_nested(issue["work_steps"])

        for section in milestone["sections"]:
            for issue in section["issues"]:
                collect_nested(issue["work_steps"])

            for feature in section["features"]:
                for issue in feature["issues"]:
                    collect_nested(issue["work_steps"])

    for work_step in work_steps:
        print(f"  • {work_step['number']} {work_step['title']}")

    number = input("Work step number to rename: ").strip()

    for work_step in work_steps:
        if work_step["number"] == number:
            new_title = input("New work step title: ").strip()

            if new_title:
                work_step["title"] = new_title

            return

    print("Work step not found.")


def edit_item(roadmap):
    """Choose which type of roadmap item to edit."""

    print()
    print("Edit:")
    print("  (m)ilestone")
    print("  (s)ection")
    print("  (f)eature")
    print("  (i)ssue")
    print("  (w)ork step")
    print("  (b)ack")
    print()

    choice = input("Choose an item type: ").strip().lower()

    if choice in ("m", "milestone"):
        edit_milestone(roadmap)

    elif choice in ("s", "section"):
        edit_section(roadmap)

    elif choice in ("f", "feature"):
        edit_feature(roadmap)

    elif choice in ("i", "issue"):
        edit_issue(roadmap)

    elif choice in ("w", "work", "work step"):
        edit_work_step(roadmap)

    elif choice in ("b", "back"):
        return

    else:
        print("Invalid choice.")


def edit_milestone(roadmap):
    """Edit a milestone description or requirements."""

    print("Milestones can only be renamed.")


def edit_section(roadmap):
    """Edit a section overview."""

    sections = []

    for milestone in roadmap["milestones"]:
        sections.extend(milestone["sections"])

    for section in sections:
        print(f"  • {section['number']} {section['title']}")

    number = input("Section number to edit: ").strip()

    for section in sections:
        if section["number"] == number:
            section["overview"] = collect_multiline("New section overview:")
            return

    print("Section not found.")


def edit_feature(roadmap):
    """Edit a feature description."""

    features = []

    for milestone in roadmap["milestones"]:
        for section in milestone["sections"]:
            features.extend(section["features"])

    for feature in features:
        print(f"  • {feature['number']} {feature['title']}")

    number = input("Feature number to edit: ").strip()

    for feature in features:
        if feature["number"] == number:
            feature["description"] = collect_multiline("New feature description:")
            return

    print("Feature not found.")


def edit_issue(roadmap):
    """Edit an issue description or requirements."""

    issues = []

    for milestone in roadmap["milestones"]:
        issues.extend(milestone["issues"])

        for section in milestone["sections"]:
            issues.extend(section["issues"])

            for feature in section["features"]:
                issues.extend(feature["issues"])

    for issue in issues:
        print(f"  • {issue['number']} {issue['title']}")

    number = input("Issue number to edit: ").strip()

    for issue in issues:
        if issue["number"] == number:
            print()
            print("Edit:")
            print("  (d)escription")
            print("  (r)equirements")
            print("  (b)ack")

            choice = input("Choose what to edit: ").strip().lower()

            if choice in ("d", "description"):
                issue["description"] = collect_multiline("New issue description:")

            elif choice in ("r", "requirements"):
                issue["requirements"] = collect_requirements()

            return

    print("Issue not found.")


def edit_work_step(roadmap):
    """Edit a work step description or requirements."""

    work_steps = []

    def collect_nested(steps):
        for step in steps:
            work_steps.append(step)
            collect_nested(step.get("work_steps", []))

    for milestone in roadmap["milestones"]:
        for issue in milestone["issues"]:
            collect_nested(issue["work_steps"])

        for section in milestone["sections"]:
            for issue in section["issues"]:
                collect_nested(issue["work_steps"])

            for feature in section["features"]:
                for issue in feature["issues"]:
                    collect_nested(issue["work_steps"])

    for work_step in work_steps:
        print(f"  • {work_step['number']} {work_step['title']}")

    number = input("Work step number to edit: ").strip()

    for work_step in work_steps:
        if work_step["number"] == number:
            print()
            print("Edit:")
            print("  (d)escription")
            print("  (r)equirements")
            print("  (b)ack")

            choice = input("Choose what to edit: ").strip().lower()

            if choice in ("d", "description"):
                work_step["description"] = collect_multiline(
                    "New work step description:"
                )

            elif choice in ("r", "requirements"):
                work_step["requirements"] = collect_requirements()

            return

    print("Work step not found.")


def add_item(roadmap):
    """Choose which type of roadmap item to add."""

    print()
    print("Add:")
    print("  (m)ilestone")
    print("  (s)ection")
    print("  (f)eature")
    print("  (i)ssue")
    print("  (w)ork step")
    print("  (b)ack")
    print()

    choice = input("Choose an item type: ").strip().lower()

    if choice in ("m", "milestone"):
        add_milestone(roadmap)

    elif choice in ("s", "section"):
        add_section(roadmap)

    elif choice in ("f", "feature"):
        add_feature(roadmap)

    elif choice in ("i", "issue"):
        add_issue(roadmap)

    elif choice in ("w", "work", "work step"):
        add_work_step(roadmap)

    elif choice in ("b", "back"):
        return

    else:
        print("Invalid choice.")


def add_milestone(roadmap):
    """Add a milestone to the roadmap."""

    number = input("Milestone number: ").strip()

    if not number:
        return

    title = input("Milestone title: ").strip()

    milestone = {
        "number": number,
        "title": title,
        "issues": [],
        "sections": [],
    }

    roadmap["milestones"].append(milestone)


def add_section(roadmap):
    """Add a section to a milestone."""

    print()
    print("Milestones:")

    for milestone in roadmap["milestones"]:
        print(f"  • {milestone['number']} {milestone['title']}")

    milestone_number = input("Milestone number: ").strip()

    for milestone in roadmap["milestones"]:
        if milestone["number"] == milestone_number:
            number = input("Section number: ").strip()

            if not number:
                return

            title = input("Section title: ").strip()
            overview = collect_multiline("Section overview:")

            milestone["sections"].append(
                {
                    "number": number,
                    "title": title,
                    "overview": overview,
                    "milestone": milestone["number"],
                    "issues": [],
                    "features": [],
                }
            )

            return

    print("Milestone not found.")


def add_feature(roadmap):
    """Add a feature to a section."""

    sections = []

    print()
    print("Sections:")

    for milestone in roadmap["milestones"]:
        for section in milestone["sections"]:
            sections.append(section)
            print(f"  • {section['number']} {section['title']}")

    section_number = input("Section number: ").strip()

    for section in sections:
        if section["number"] == section_number:
            number = input("Feature number: ").strip()

            if not number:
                return

            title = input("Feature title: ").strip()
            description = collect_multiline("Feature description:")

            section["features"].append(
                {
                    "number": number,
                    "title": title,
                    "description": description,
                    "section": section["title"],
                    "issues": [],
                }
            )

            return

    print("Section not found.")


def add_issue(roadmap):
    """Add an issue to a milestone, section, or feature."""

    parents = []

    print()
    print("Possible parents:")

    for milestone in roadmap["milestones"]:
        parents.append(milestone)
        print(f"  • {milestone['number']} {milestone['title']}")

        for section in milestone["sections"]:
            parents.append(section)
            print(f"  • {section['number']} {section['title']}")

            for feature in section["features"]:
                parents.append(feature)
                print(f"  • {feature['number']} {feature['title']}")

    parent_number = input("Parent number: ").strip()

    for parent in parents:
        if parent["number"] == parent_number:
            number = input("Issue number: ").strip()

            if not number:
                return

            title = input("Issue title: ").strip()
            description = collect_multiline("Issue description:")

            parent["issues"].append(
                {
                    "number": number,
                    "title": title,
                    "description": description,
                    "requirements": collect_requirements(),
                    "parent": parent["title"],
                    "work_steps": [],
                }
            )

            return

    print("Parent not found.")


def add_work_step(roadmap):
    """Add a work step to an issue or another work step."""

    parents = []

    def collect_work_step_parents(work_steps):
        for work_step in work_steps:
            parents.append(work_step)
            collect_work_step_parents(work_step.get("work_steps", []))

    print()
    print("Possible parents:")

    for milestone in roadmap["milestones"]:
        for issue in milestone["issues"]:
            parents.append(issue)
            collect_work_step_parents(issue["work_steps"])

        for section in milestone["sections"]:
            for issue in section["issues"]:
                parents.append(issue)
                collect_work_step_parents(issue["work_steps"])

            for feature in section["features"]:
                for issue in feature["issues"]:
                    parents.append(issue)
                    collect_work_step_parents(issue["work_steps"])

    for parent in parents:
        print(f"  • {parent['number']} {parent['title']}")

    parent_number = input("Parent number: ").strip()

    for parent in parents:
        if parent["number"] == parent_number:
            work_step = collect_work_step(parent)

            if work_step:
                parent["work_steps"].append(work_step)

            return

    print("Parent not found.")

def delete_item(roadmap):
    """Choose which type of roadmap item to delete."""

    print()
    print("Delete:")
    print("  (m)ilestone")
    print("  (s)ection")
    print("  (f)eature")
    print("  (i)ssue")
    print("  (w)ork step")
    print("  (b)ack")
    print()

    choice = input("Choose an item type: ").strip().lower()

    if choice in ("m", "milestone"):
        delete_milestone(roadmap)

    elif choice in ("s", "section"):
        delete_section(roadmap)

    elif choice in ("f", "feature"):
        delete_feature(roadmap)

    elif choice in ("i", "issue"):
        delete_issue(roadmap)

    elif choice in ("w", "work", "work step"):
        delete_work_step(roadmap)

    elif choice in ("b", "back"):
        return

    else:
        print("Invalid choice.")

def delete_milestone(roadmap):
    """Delete a milestone from the roadmap."""

    print()
    print("Milestones:")

    for milestone in roadmap["milestones"]:
        print(f"  • {milestone['number']} {milestone['title']}")

    number = input("Milestone number to delete: ").strip()

    for milestone in roadmap["milestones"]:
        if milestone["number"] == number:
            confirm = input(
                f"Delete {milestone['number']} {milestone['title']} "
                "and everything inside it? [(y)es / (n)o]: "
            ).strip().lower()

            if confirm in ("y", "yes"):
                roadmap["milestones"].remove(milestone)
                print("Milestone deleted.")

            return

    print("Milestone not found.")

def delete_section(roadmap):
    """Delete a section from the roadmap."""

    sections = []

    print()
    print("Sections:")

    for milestone in roadmap["milestones"]:
        for section in milestone["sections"]:
            sections.append((milestone, section))
            print(f"  • {section['number']} {section['title']}")

    number = input("Section number to delete: ").strip()

    for milestone, section in sections:
        if section["number"] == number:
            confirm = input(
                f"Delete {section['number']} {section['title']} "
                "and everything inside it? [(y)es / (n)o]: "
            ).strip().lower()

            if confirm in ("y", "yes"):
                milestone["sections"].remove(section)
                print("Section deleted.")

            return

    print("Section not found.")

def delete_feature(roadmap):
    """Delete a feature from the roadmap."""

    features = []

    print()
    print("Features:")

    for milestone in roadmap["milestones"]:
        for section in milestone["sections"]:
            for feature in section["features"]:
                features.append((section, feature))
                print(f"  • {feature['number']} {feature['title']}")

    number = input("Feature number to delete: ").strip()

    for section, feature in features:
        if feature["number"] == number:
            confirm = input(
                f"Delete {feature['number']} {feature['title']} "
                "and everything inside it? [(y)es / (n)o]: "
            ).strip().lower()

            if confirm in ("y", "yes"):
                section["features"].remove(feature)
                print("Feature deleted.")

            return

    print("Feature not found.")

def delete_issue(roadmap):
    """Delete an issue from the roadmap."""

    issues = []

    print()
    print("Issues:")

    for milestone in roadmap["milestones"]:
        for issue in milestone["issues"]:
            issues.append((milestone, issue))
            print(f"  • {issue['number']} {issue['title']}")

        for section in milestone["sections"]:
            for issue in section["issues"]:
                issues.append((section, issue))
                print(f"  • {issue['number']} {issue['title']}")

            for feature in section["features"]:
                for issue in feature["issues"]:
                    issues.append((feature, issue))
                    print(f"  • {issue['number']} {issue['title']}")

    number = input("Issue number to delete: ").strip()

    for parent, issue in issues:
        if issue["number"] == number:
            confirm = input(
                f"Delete {issue['number']} {issue['title']} "
                "and all of its work steps? [(y)es / (n)o]: "
            ).strip().lower()

            if confirm in ("y", "yes"):
                parent["issues"].remove(issue)
                print("Issue deleted.")

            return

    print("Issue not found.")

def delete_work_step(roadmap):
    """Delete a work step, including nested work steps."""

    work_steps = []

    print()
    print("Work Steps:")

    def collect_nested(parent, steps):
        for step in steps:
            work_steps.append((parent, step))
            print(f"  • {step['number']} {step['title']}")
            collect_nested(step, step.get("work_steps", []))

    for milestone in roadmap["milestones"]:
        for issue in milestone["issues"]:
            collect_nested(issue, issue["work_steps"])

        for section in milestone["sections"]:
            for issue in section["issues"]:
                collect_nested(issue, issue["work_steps"])

            for feature in section["features"]:
                for issue in feature["issues"]:
                    collect_nested(issue, issue["work_steps"])

    number = input("Work step number to delete: ").strip()

    for parent, work_step in work_steps:
        if work_step["number"] == number:
            confirm = input(
                f"Delete {work_step['number']} {work_step['title']} "
                "and all nested work steps? [(y)es / (n)o]: "
            ).strip().lower()

            if confirm in ("y", "yes"):
                parent["work_steps"].remove(work_step)
                print("Work step deleted.")

            return

    print("Work step not found.")