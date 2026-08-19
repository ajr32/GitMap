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
    """Guide the user through defining the project milestones"""

    milestones = []

    while True:
        number = input("Milestone number: (or press Enter when finished): ").strip()

        if not number:
            break

        title = input("Milestone title: ").strip()

        milestone = {
            "number": number,
            "title": title,
        }

        milestone["sections"] = collect_sections(milestone)

        milestones.append(milestone)

    return milestones

def collect_sections(milestone):
    """Guide the user through defining sections for a milestone."""

    sections = []

    while True:
        title = input(
            f"Section title for {milestone['number']} {milestone['title']} "
            "(or press Enter when finished): "
        ).strip()

        if not title:
            break

        overview = input("Section overview: ").strip()

        section = {
            "title": title,
            "overview": overview,
            "milestone": milestone["number"],
        }

        section["issues"] = collect_issues(section)

        sections.append(section)

    return sections


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


def collect_issues(section):
    """Guide the user through defining issues for a section."""

    issues = []

    while True:
        title = input(
            f"Issue title for {section['title']} "
            "(or press Enter when finished): "
        ).strip()

        if not title:
            break

        description = collect_multiline("Issue description:")
        issue = {
            "title": title,
            "description": description,
            "requirements": [],
            "section": section["title"],
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
                requirement = input("Requirement: ").strip()

                if requirement:
                    issue["requirements"].append(requirement)

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

    title = input("Work step title: ").strip()

    if not title:
        return None

    description = collect_multiline("Work step description:")
    requirements = collect_requirements()

    return {
        "title": title,
        "description": description,
        "requirements": requirements,
        "parent": issue["title"],
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

    return [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

def render_roadmap_markdown(roadmap):
    """Render a completed roadmap as Markdown."""

    lines = []

    lines.append(f"Title: {roadmap['name']}")

    if roadmap["overview"]:
        lines.append(f"Sub-Title: {roadmap['overview']}")

    for milestone in roadmap["milestones"]:
        lines.append("")
        lines.append(f"# {milestone['number']} {milestone['title']}")

        for section in milestone["sections"]:
            lines.append("")
            lines.append(f"## {section['title']}")

            if section["overview"]:
                lines.append("")
                lines.append(section["overview"])

            for issue in section["issues"]:
                lines.append("")
                lines.append(f"#### {issue['title']}")

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

                    for work_step in issue["work_steps"]:
                        lines.append(f"- [ ] {work_step['title']}")

                        if work_step["description"]:
                            lines.append(f"  {work_step['description']}")

                        for requirement in work_step["requirements"]:
                            lines.append(f"  - {requirement}")

    return "\n".join(lines)