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
