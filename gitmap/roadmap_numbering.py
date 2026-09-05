def generate_milestone_number(starting_series, sibling_index):
    """Generate a milestone number."""

    return f"{starting_series}.{sibling_index}"

def generate_section_number(milestone_number, sibling_index):
    """Generate a section number beneath a milestone."""
    return f"{milestone_number}.{sibling_index}"


def generate_feature_number(section_number, sibling_index):
    """Generate a feature number beneath a section."""
    return f"{section_number}.{sibling_index}"

def generate_issue_number(parent_number, parent_type, sibling_index):
    """Generate an issue number while preserving hierarchy slots."""

    if parent_type == "milestone":
        return f"{parent_number}.0.0.{sibling_index}"

    if parent_type == "section":
        return f"{parent_number}.0.{sibling_index}"

    if parent_type == "feature":
        return f"{parent_number}.{sibling_index}"

    raise ValueError(f"Cannot create an issue beneath {parent_type}.")

def generate_work_step_number(sibling_index):
    """Generate a letter-based work step number."""

    if sibling_index < 1:
        raise ValueError("Work step index must be at least 1.")

    letters = ""
    number = sibling_index

    while number:
        number -= 1
        letters = chr(ord("a") + number % 26) + letters
        number //= 26

    return f"({letters})"

def next_section_number(milestone):
    """Return the next Section number."""

    sibling_index = next_sibling_index(milestone.get("sections", []))

    return generate_section_number(
        milestone["number"],
        sibling_index,
    )


def next_feature_number(section):
    """Return the next Feature number."""

    sibling_index = next_sibling_index(section.get("features", []))

    return generate_feature_number(
        section["number"],
        sibling_index,
    )


def next_issue_number(parent, parent_type):
    """Return the next Issue number."""

    sibling_index = next_sibling_index(parent.get("issues", []))

    return generate_issue_number(
        parent["number"],
        parent_type,
        sibling_index,
    )



def next_work_step_number(parent):
    """Return the parent Issue number for a Work Step."""

    return parent["number"]

def remember_next_section_number(milestone):
    """Remember the next automatic Section number for an existing milestone."""

    milestone["_next_section_number"] = len(milestone.get("sections", [])) + 1

def remember_next_feature_number(section):
    """Remember the next automatic Feature number for an existing section."""

    section["_next_feature_number"] = len(section.get("features", [])) + 1

def remember_next_issue_number(parent):
    """Remember the next automatic Issue number for an existing parent."""

    parent["_next_issue_number"] = len(parent.get("issues", [])) + 1

def remember_next_work_step_number(issue):
    """Remember the next automatic Work Step number for an existing issue."""

    issue["_next_work_step_number"] = len(issue.get("work_steps", [])) + 1

def next_sibling_index(items):
    """Return the next sibling index based on the last existing number."""

    if not items:
        return 1

    last_number = items[-1]["number"]
    last_part = int(last_number.split(".")[-1])

    return last_part + 1

def remember_numbering_state(roadmap):
    """Restore automatic numbering state for an existing roadmap."""

    for milestone in roadmap.get("milestones", []):
        remember_next_section_number(milestone)
        remember_next_issue_number(milestone)

        for section in milestone.get("sections", []):
            remember_next_feature_number(section)
            remember_next_issue_number(section)

            for feature in section.get("features", []):
                remember_next_issue_number(feature)

                for issue in feature.get("issues", []):
                    remember_next_work_step_number(issue)

            for issue in section.get("issues", []):
                remember_next_work_step_number(issue)

        for issue in milestone.get("issues", []):
            remember_next_work_step_number(issue)

def renumber_siblings(items, parent_number, parent_type=None):
    """Renumber siblings while preserving GitMap hierarchy numbering."""

    for index, item in enumerate(items, start=1):

        if parent_type == "section_issue":
            item["number"] = f"{parent_number}.0.{index}"

        elif parent_type == "work_step":
            item["number"] = parent_number
            item["work_step_marker"] = generate_work_step_number(index)
            
        else:
            item["number"] = f"{parent_number}.{index}"

        if item.get("type") == "section":
            renumber_siblings(
                item.get("issues", []),
                item["number"],
                parent_type="section_issue",
            )

            renumber_siblings(
                item.get("features", []),
                item["number"],
            )

        elif item.get("type") == "feature":
            renumber_siblings(
                item.get("issues", []),
                item["number"],
            )

        elif item.get("type") == "issue":
            renumber_siblings(
                item.get("work_steps", []),
                item["number"],
                parent_type="work_step",
            )

        elif item.get("type") == "work_step":
            renumber_siblings(
                item.get("work_steps", []),
                item["number"],
                parent_type="work_step",
            )

def collect_numbering_changes(items):
    """Collect all roadmap items whose numbers changed."""

    changes = []

    for item in items:
        old_number = item.get("_original_number")
        new_number = item.get("number")

        if old_number and old_number != new_number:
            changes.append(
                {
                    "title": item.get("title", ""),
                    "old_number": old_number,
                    "new_number": new_number,
                }
            )

        for child_key in (
            "sections",
            "features",
            "issues",
            "work_steps",
        ):
            changes.extend(
                collect_numbering_changes(
                    item.get(child_key, [])
                )
            )

    return changes

def remember_original_numbers(items):
    """Remember roadmap numbers before automatic renumbering."""

    for item in items:
        item["_original_number"] = item.get("number")

        remember_original_numbers(
            item.get("sections", [])
        )

        remember_original_numbers(
            item.get("features", [])
        )

        remember_original_numbers(
            item.get("issues", [])
        )

        remember_original_numbers(
            item.get("work_steps", [])
        )

def choose_insert_position(items):
    """Choose where a new automatically numbered item should be inserted."""

    if not items:
        return 0

    print()
    print("Where should this item be placed?")
    print("1. At the end")
    print("2. Before an existing item")
    print("3. After an existing item")

    choice = input("Choose an option: ").strip()

    if choice == "2":
        print()
        print("Choose the item to insert before:")

        for index, item in enumerate(items, start=1):
            print(f"{index}. {item['number']} {item['title']}")

        selection = input("Choose an item: ").strip()

        for position, item in enumerate(items):
            if selection == str(position + 1) or selection == item["number"]:
                return position

    if choice == "3":
        print()
        print("Choose the item to insert after:")

        for index, item in enumerate(items, start=1):
            print(f"{index}. {item['number']} {item['title']}")

        selection = input("Choose an item: ").strip()

        for position, item in enumerate(items):
            if selection == str(position + 1) or selection == item["number"]:
                return position + 1

    return len(items)

def preview_numbering_changes(changes):
    """Show automatic numbering changes and ask for approval."""

    if not changes:
        return True

    print()
    print("Numbering changes:")
    print()

    for change in changes:
        print(f"{change['title']}")
        print(
            f"  {change['old_number']} "
            f"→ {change['new_number']}"
        )

    print()

    choice = input(
        "Apply these numbering changes? (y/n): "
    ).strip().lower()

    return choice in ("y", "yes")