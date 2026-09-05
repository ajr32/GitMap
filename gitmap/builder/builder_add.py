import copy

from gitmap.roadmap_numbering import (
    generate_milestone_number,
    next_feature_number,
    next_issue_number,
    next_section_number,
    next_sibling_index, choose_insert_position, renumber_siblings, remember_original_numbers,collect_numbering_changes, preview_numbering_changes
)
from gitmap.roadmap_preparation import (
    collect_multiline,
    collect_requirements,
    collect_work_step,
)


def add_item(roadmap, numbering_mode="manual"):
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
        add_milestone(roadmap, numbering_mode)

    elif choice in ("s", "section"):
        add_section(roadmap, numbering_mode)

    elif choice in ("f", "feature"):
        add_feature(roadmap, numbering_mode)

    elif choice in ("i", "issue"):
        add_issue(roadmap, numbering_mode)

    elif choice in ("w", "work", "work step"):
        add_work_step(roadmap, numbering_mode)

    elif choice in ("b", "back"):
        return

    else:
        print("Invalid choice.")


def add_milestone(roadmap, numbering_mode="manual"):
    """Add a milestone to the roadmap."""

    if numbering_mode == "automatic":
        number = None
    else:
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

    if numbering_mode == "automatic":
        original_milestones = copy.deepcopy(roadmap["milestones"])

        remember_original_numbers(roadmap["milestones"])
        position = choose_insert_position(
            roadmap["milestones"]
        )

        roadmap["milestones"].insert(
            position,
            milestone,
        )

        starting_series = roadmap["starting_series"]

        for index, item in enumerate(
            roadmap["milestones"],
            start=1,
        ):
            item["number"] = generate_milestone_number(
                starting_series,
                index,
            )

            renumber_siblings(
                item["sections"],
                item["number"],
            )

            renumber_siblings(
                item["issues"],
                f"{item['number']}.0.0",
            )

        changes = collect_numbering_changes(roadmap["milestones"])

        if not preview_numbering_changes(changes):
            roadmap["milestones"].clear()
            roadmap["milestones"].extend(original_milestones)

            print("Numbering changes cancelled.")
            return
        print(f"Milestone number: {milestone['number']}")
    else:
        roadmap["milestones"].append(milestone)


def add_section(roadmap, numbering_mode="manual"):
    """Add a section to a milestone."""

    print()
    print("Milestones:")

    for milestone in roadmap["milestones"]:
        print(f"  • {milestone['number']} {milestone['title']}")

    milestone_number = input("Milestone number: ").strip()

    for milestone in roadmap["milestones"]:
        if milestone["number"] == milestone_number:

            if numbering_mode == "automatic":
                number = None
            else:
                number = input("Section number: ").strip()
                if not number:
                    return

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

            if numbering_mode == "automatic":
                original_sections = copy.deepcopy(milestone["sections"])
                remember_original_numbers(milestone["sections"])
                
                position = choose_insert_position(
                    milestone["sections"]
                )

                milestone["sections"].insert(
                    position,
                    section,
                )

                renumber_siblings(
                    milestone["sections"],
                    milestone["number"],
                )

                changes = collect_numbering_changes(milestone["sections"])

                if not preview_numbering_changes(changes):
                    milestone["sections"].clear()
                    milestone["sections"].extend(original_sections)

                    print("Numbering changes cancelled.")
                    return

                print(f"Section number: {section['number']}")
            else:
                milestone["sections"].append(section)

            return

    print("Milestone not found.")


def add_feature(roadmap, numbering_mode="manual"):
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

            if numbering_mode == "automatic":
                number = None
            else:
                number = input("Feature number: ").strip()
                if not number:
                    return

            title = input("Feature title: ").strip()
            description = collect_multiline("Feature description:")

            feature = {
                "number": number,
                "title": title,
                "description": description,
                "section": section["title"],
                "issues": [],
            }

            if numbering_mode == "automatic":
                original_features = copy.deepcopy(section["features"])

                remember_original_numbers(section["features"])
                position = choose_insert_position(
                    section["features"]
                )

                section["features"].insert(
                    position,
                    feature,
                )

                renumber_siblings(
                    section["features"],
                    section["number"],
                )

                changes = collect_numbering_changes(section["features"])

                if not preview_numbering_changes(changes):
                    section["features"].clear()
                    section["features"].extend(original_features)

                    print("Numbering changes cancelled.")
                    return

                print(f"Feature number: {feature['number']}")
            else:
                section["features"].append(feature)

            return

    print("Section not found.")


def add_issue(roadmap, numbering_mode="manual"):
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

            if numbering_mode == "automatic":
                number = None
            else:
                number = input("Issue number: ").strip()
                if not number:
                    return

            title = input("Issue title: ").strip()
            description = collect_multiline("Issue description:")

            issue = {
                "number": number,
                "title": title,
                "type": "issue",
                "description": description,
                "requirements": collect_requirements(),
                "parent": parent["title"],
                "work_steps": [],
            }

            if numbering_mode == "automatic":
                original_issues = copy.deepcopy(parent["issues"])

                remember_original_numbers(parent["issues"])
                position = choose_insert_position(
                    parent["issues"]
                )

                parent["issues"].insert(
                    position,
                    issue,
                )

                if parent["type"] == "section":
                    renumber_siblings(
                        parent["issues"],
                        parent["number"],
                        parent_type="section_issue",
                    )
                else:
                    renumber_siblings(
                        parent["issues"],
                        parent["number"],
                    )

                changes = collect_numbering_changes(parent["issues"])

                if not preview_numbering_changes(changes):
                    parent["issues"].clear()
                    parent["issues"].extend(original_issues)

                    print("Numbering changes cancelled.")
                    return

                print(f"Issue number: {issue['number']}")
            else:
                parent["issues"].append(issue)

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
                if numbering_mode == "automatic":
                    original_work_steps = copy.deepcopy(parent["work_steps"])

                    remember_original_numbers(parent["work_steps"])
                    position = choose_insert_position(parent["work_steps"])

                    parent["work_steps"].insert(
                        position,
                        work_step,
                    )

                    renumber_siblings(
                        parent["work_steps"],
                        parent["number"],
                        parent_type="work_step",
                    )
                    changes = collect_numbering_changes(parent["work_steps"])

                    if not preview_numbering_changes(changes):
                        parent["work_steps"].clear()
                        parent["work_steps"].extend(original_work_steps)

                        print("Numbering changes cancelled.")
                        return

                    print(f"Work step number: {work_step['number']}")
                else:
                    parent["work_steps"].append(work_step)

            return

    print("Parent not found.")
