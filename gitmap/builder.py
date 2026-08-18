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
        requirements = collect_requirements()

        issue = {
            "title": title,
            "description": description,
            "requirements": requirements,
            "section": section["title"],
        }

        issue["work_steps"] = collect_work_steps(issue)

        issues.append(issue)

        return issues

def collect_work_steps(issue):
    """Collect work steps for an issue."""

    work_steps = []

    while True:
        title = input(
            f"Work step for {issue['title']} "
            "(or press Enter when finished): "
        ).strip()

        if not title:
            break

        description = input("Work step description: ").strip()
        requirements = collect_requirements()

        work_steps.append(
            {
                "title": title,
                "description": description,
                "requirements": requirements,
                "parent": issue["title"],
            }
        )

    return work_steps

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