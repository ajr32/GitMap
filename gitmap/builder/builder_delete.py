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
