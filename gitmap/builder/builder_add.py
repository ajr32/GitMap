from gitmap.roadmap_preparation import collect_multiline, collect_requirements, collect_work_step


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


def add_work_step(roadmap, numbering_mode="manual"):
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
            work_step = collect_work_step(parent, numbering_mode)

            if work_step:
                parent["work_steps"].append(work_step)

            return

    print("Parent not found.")
