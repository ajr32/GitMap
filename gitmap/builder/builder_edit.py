from gitmap.roadmap_preparation import collect_multiline, collect_requirements


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
