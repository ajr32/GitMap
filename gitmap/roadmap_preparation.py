from gitmap.roadmap_numbering import generate_milestone_number, next_section_number, next_feature_number, \
    next_issue_number, next_work_step_number


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


def collect_milestones(
    numbering_mode,
    starting_series=None,
    roadmap_structure="sections_and_features",
):
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
            "type": "milestone",
            "issues": [],
            "sections": [],
        }

        milestones.append(milestone)

    return milestones


# def collect_milestone_items(
#     milestone,
#     numbering_mode,
#     roadmap_structure,
# ):
#     """Collect items for a milestone based on the chosen roadmap structure."""
#
#     print()
#     print("Milestone options:")
#     print("  (i)ssue   — add an issue directly to this milestone")
#
#     if roadmap_structure != "neither":
#         print("  (s)ection — add a section")
#
#     print("  (d)one    — finish this milestone")
#     print()
#
#     while True:
#         if roadmap_structure == "neither":
#             prompt = "[(i)ssue / (d)one]: "
#         else:
#             prompt = "[(i)ssue / (s)ection / (d)one]: "
#
#         choice = input(prompt).strip().lower()
#
#         if choice in ("i", "issue"):
#             milestone["issues"].extend(
#                 collect_issues(milestone, numbering_mode)
#             )
#
#         elif (
#             choice in ("s", "section")
#             and roadmap_structure != "neither"
#         ):
#             milestone["sections"].extend(
#                 collect_sections(
#                     milestone,
#                     numbering_mode,
#                     roadmap_structure,
#                 )
#             )
#
#         elif choice in ("d", "done"):
#             break
#
#         else:
#             print("Please choose one of the available options.")
#

def collect_sections(
    milestone,
    numbering_mode,
    roadmap_structure,
):
    """Guide the user through defining sections for a milestone."""

    sections = []

    while True:
        if numbering_mode == "automatic":
            title = input(
                f"Section title for {milestone['number']} {milestone['title']} "
                "(or press Enter when finished): "
            ).strip()

            if not title:
                break

            number = next_section_number(milestone)
            print(f"Section number: {number}")

        else:
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
            "type": "section",
            "overview": overview,
            "milestone": milestone["number"],
            "issues": [],
            "features": [],
        }


        sections.append(section)

    return sections


# def collect_section_items(
#     section,
#     numbering_mode,
#     roadmap_structure,
# ):
#     """Collect items for a section based on the chosen roadmap structure."""
#
#     print()
#     print("Section options:")
#     print("  (i)ssue   — add an issue directly to this section")
#
#     if roadmap_structure == "sections_and_features":
#         print("  (f)eature — add a feature")
#
#     print("  (d)one    — finish this section")
#     print()
#
#     while True:
#         if roadmap_structure == "sections_and_features":
#             prompt = "[(i)ssue / (f)eature / (d)one]: "
#         else:
#             prompt = "[(i)ssue / (d)one]: "
#
#         choice = input(prompt).strip().lower()
#
#         if choice in ("i", "issue"):
#             section["issues"].extend(
#                 collect_issues(section, numbering_mode)
#             )
#
#         elif (
#             choice in ("f", "feature")
#             and roadmap_structure == "sections_and_features"
#         ):
#             section["features"].extend(
#                 collect_features(section, numbering_mode)
#             )
#
#         elif choice in ("d", "done"):
#             break
#
#         else:
#             print("Please choose one of the available options.")


def collect_features(section, numbering_mode):
    """Collect features for a section."""

    features = []

    while True:
        if numbering_mode == "automatic":
            title = input(
                f"Feature title for {section['number']} {section['title']} "
                "(or press Enter when finished): "
            ).strip()

            if not title:
                break

            number = next_feature_number(section)
            print(f"Feature number: {number}")

        else:
            number = input(
                f"Feature number for {section['title']} "
                "(or press Enter when finished): "
            ).strip()

            if not number:
                break

            title = input("Feature title: ").strip()

        description = collect_multiline("Feature description:")

        feature = {
            "number": number,
            "title": title,
            "type": "feature",
            "description": description,
            "section": section["title"],
            "issues": [],
        }

        features.append(feature)

    return features

def collect_issues(parent, numbering_mode):
    """Guide the user through defining issues for a parent."""

    issues = []

    while True:
        if numbering_mode == "automatic":
            title = input(
                f"Issue title for {parent['number']} {parent['title']} "
                "(or press Enter when finished): "
            ).strip()

            if not title:
                break

            number = next_issue_number(
                parent,
                parent["type"],
            )

            print(f"Issue number: {number}")

        else:
            number = input(
                f"Issue number for {parent['title']} "
                "(or press Enter when finished): "
            ).strip()

            if not number:
                break

            title = input("Issue title: ").strip()

        description = collect_multiline("Issue description:")

        issue = {
            "number": number,
            "title": title,
            "type": "issue",
            "description": description,
            "requirements": [],
            "parent": parent["title"],
            "work_steps": [],
        }

        collect_issue_details(issue, numbering_mode)

        issues.append(issue)

    return issues

def collect_issue_details(issue, numbering_mode):
    """Collect requirements and work steps for an existing issue."""

    print()
    print(f"Issue: {issue['number']} {issue['title']}")
    print()
    print("Issue options:")
    print(
        "  (r)equirement — something that must be true or completed for this issue"
    )
    print("  (w)ork step   — a smaller piece of work inside this issue")
    print("  (d)one        — finish this issue and move on to the next issue")
    print()

    while True:
        choice = input(
            "[(r)equirement / (w)ork step / (d)one]: "
        ).strip().lower()

        if choice in ("r", "requirement"):
            issue["requirements"].extend(
                collect_requirements()
            )

        elif choice in ("w", "work", "work step"):
            work_step = collect_work_step(
                issue,
                numbering_mode,
            )

            if work_step:
                issue["work_steps"].append(work_step)

        elif choice in ("d", "done"):
            break

        else:
            print("Invalid choice.")

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




def collect_work_step(issue, numbering_mode):
    """Collect one work step for an issue."""

    if numbering_mode == "automatic":
        title = input("Work step title: ").strip()

        if not title:
            return None

        number = next_work_step_number(issue)
        print(f"Work step number: {number}")

    else:
        number = input("Work step number: ").strip()

        if not number:
            return None

        title = input("Work step title: ").strip()

    description = collect_multiline("Work step description:")
    requirements = []

    return {
        "number": number,
        "title": title,
        "type": "work_step",
        "description": description,
        "requirements": requirements,
        "parent": issue["title"],
        "work_steps": [],
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
