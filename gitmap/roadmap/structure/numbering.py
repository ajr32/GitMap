from gitmap.roadmap.model.models import Feature, Issue, Milestone, Section


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


def get_numbering_value(item, name, default=None):
    """Read a numbering value from either a dict or model object."""

    if isinstance(item, dict):
        return item.get(name, default)

    if name == "type":
        if isinstance(item, Milestone):
            return "milestone"
        if isinstance(item, Section):
            return "section"
        if isinstance(item, Feature):
            return "feature"
        if isinstance(item, Issue):
            return "issue"

    return getattr(item, name, default)


def set_numbering_value(item, name, value):
    """Write a numbering value to either a dict or model object."""

    if isinstance(item, dict):
        item[name] = value
    else:
        setattr(item, name, value)


def renumber_siblings(items, parent_number, parent_type=None):
    """Renumber siblings while preserving GitMap hierarchy numbering.

    Section renumbering recursively updates its direct Issues, Features, and
    the Issues beneath those Features. This is the backend used by GUI
    insertion; the GUI must not create a second numbering system.
    """

    for index, item in enumerate(items, start=1):
        if parent_type == "milestone_issue":
            new_number = generate_issue_number(
                parent_number,
                "milestone",
                index,
            )
            set_numbering_value(item, "number", new_number)

        elif parent_type == "section_issue":
            new_number = generate_issue_number(
                parent_number,
                "section",
                index,
            )
            set_numbering_value(item, "number", new_number)

        elif parent_type == "work_step":
            set_numbering_value(item, "number", parent_number)
            set_numbering_value(
                item,
                "work_step_marker",
                generate_work_step_number(index),
            )

        else:
            item_type = get_numbering_value(item, "type")

            if item_type == "milestone":
                new_number = generate_milestone_number(
                    parent_number,
                    index,
                )
            elif item_type == "section":
                new_number = generate_section_number(
                    parent_number,
                    index,
                )
            elif item_type == "feature":
                new_number = generate_feature_number(
                    parent_number,
                    index,
                )
            elif item_type == "issue":
                new_number = generate_issue_number(
                    parent_number,
                    "feature",
                    index,
                )
            else:
                new_number = f"{parent_number}.{index}"

            set_numbering_value(item, "number", new_number)

        if get_numbering_value(item, "type") == "milestone":
            renumber_siblings(
                get_numbering_value(item, "sections", []),
                get_numbering_value(item, "number"),
            )

            renumber_siblings(
                get_numbering_value(item, "issues", []),
                get_numbering_value(item, "number"),
                parent_type="milestone_issue",
            )

        elif get_numbering_value(item, "type") == "section":
            renumber_siblings(
                get_numbering_value(item, "issues", []),
                get_numbering_value(item, "number"),
                parent_type="section_issue",
            )

            renumber_siblings(
                get_numbering_value(item, "features", []),
                get_numbering_value(item, "number"),
            )

        elif get_numbering_value(item, "type") == "feature":
            renumber_siblings(
                get_numbering_value(item, "issues", []),
                get_numbering_value(item, "number"),
            )

        elif get_numbering_value(item, "type") == "issue":
            renumber_siblings(
                get_numbering_value(item, "work_steps", []),
                get_numbering_value(item, "number"),
                parent_type="work_step",
            )

        elif get_numbering_value(item, "type") == "work_step":
            renumber_siblings(
                get_numbering_value(item, "work_steps", []),
                get_numbering_value(item, "number"),
                parent_type="work_step",
            )


def collect_numbering_changes(items):
    """Collect all roadmap items whose numbers changed."""

    changes = []

    for item in items:
        old_number = get_numbering_value(
            item,
            "_original_number",
        )
        new_number = get_numbering_value(
            item,
            "number",
        )
        item_type = get_numbering_value(item, "type")

        if item_type == "work_step":
            old_number = None

        if old_number and old_number != new_number:
            changes.append(
                {
                    "title": get_numbering_value(
                        item,
                        "title",
                        "",
                    ),
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
                    get_numbering_value(
                        item,
                        child_key,
                        [],
                    )
                )
            )

    return changes


def remember_original_numbers(items):
    """Remember roadmap numbers before automatic renumbering."""

    for item in items:
        set_numbering_value(
            item,
            "_original_number",
            get_numbering_value(item, "number"),
        )

        for child_key in (
            "sections",
            "features",
            "issues",
            "work_steps",
        ):
            remember_original_numbers(
                get_numbering_value(
                    item,
                    child_key,
                    [],
                )
            )


def restore_original_numbers(items):
    """Restore roadmap numbers remembered before temporary renumbering."""

    for item in items:
        original_number = get_numbering_value(
            item,
            "_original_number",
        )

        if original_number is not None:
            set_numbering_value(
                item,
                "number",
                original_number,
            )

        for child_key in (
            "sections",
            "features",
            "issues",
            "work_steps",
        ):
            restore_original_numbers(
                get_numbering_value(
                    item,
                    child_key,
                    [],
                )
            )
