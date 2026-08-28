from gitmap.roadmap_numbering import (
    choose_numbering_mode,
    choose_starting_series,
    explain_roadmap_numbering,
    generate_milestone_number,
)

def ask_project_name():
    """Ask the user to enter a project name."""

    while True:
        name = input("Project name: ").strip()

        if name:
            return name

        print("Project name cannot be blank.")


def ask_project_overview():
    """Ask the user to enter a project overview"""
    return collect_multiline("Project sub-title/overview:")


def start_new_roadmap():
    """Start an interactive roadmap-building session."""

    explain_roadmap_numbering()
    numbering_mode = choose_numbering_mode()

    starting_series = None

    if numbering_mode == "automatic":
        starting_series = choose_starting_series()

    project_name = ask_project_name()
    project_overview = ask_project_overview()

    return {
        "name": project_name,
        "overview": project_overview,
        "numbering_mode": numbering_mode,
        "starting_series": starting_series,
        "milestones": collect_milestones(
            numbering_mode,
            starting_series,
        ),
    }


def collect_milestones(numbering_mode, starting_series=None):
    """Guide the user through defining the project milestones."""

    milestones = []

    while True:
        if numbering_mode == "automatic":
            title = input(
                "Milestone title (or press Enter when finished): "
            ).strip()

            if not title:
                break

            number = generate_milestone_number(
                starting_series,
                len(milestones) + 1,
            )

            print(f"Milestone number: {number}")

        else:
            number = input(
                "Milestone number (or press Enter when finished): "
            ).strip()

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

def choose_numbering_mode():
    """Ask the user how roadmap items should be numbered."""

    print()
    print("Choose Numbering Mode")
    print("---------------------")
    print("1. Automatic numbering")
    print("2. Manual numbering")

    while True:
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            return "automatic"

        if choice == "2":
            return "manual"

        print("Please choose 1 or 2.")

def collect_pasted_requirements():
    """Collect multiple requirements from pasted multiline text."""

    text = collect_multiline("Paste requirements:")

    return [line.strip() for line in text.splitlines() if line.strip()]
