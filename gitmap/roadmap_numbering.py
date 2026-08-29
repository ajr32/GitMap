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
    """Generate the next section number for a milestone."""
    sibling_index = milestone.get("_next_section_number", 1)
    number = generate_section_number(
        milestone["number"],
        sibling_index,
    )
    milestone["_next_section_number"] = sibling_index + 1
    return number


def next_feature_number(section):
    """Generate the next feature number for a section."""
    sibling_index = section.get("_next_feature_number", 1)
    number = generate_feature_number(
        section["number"],
        sibling_index,
    )
    section["_next_feature_number"] = sibling_index + 1
    return number


def next_issue_number(parent, parent_type):
    """Generate the next issue number for a parent."""
    sibling_index = parent.get("_next_issue_number", 1)
    number = generate_issue_number(
        parent["number"],
        parent_type,
        sibling_index,
    )
    parent["_next_issue_number"] = sibling_index + 1
    return number




def next_work_step_number(parent):
    """Return the next letter-based number beneath a work-step parent."""

    child_index = parent.get("_next_work_step_number", 1)
    number = generate_work_step_number(child_index)
    parent["_next_work_step_number"] = child_index + 1

    return number