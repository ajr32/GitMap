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