from gitmap.roadmap.model.traversal import iter_roadmap_issues

DEFAULT_LABEL_COLOR = "0366d6"
FIRST_GITMAP_ID = "goredsox"

def increment_gitmap_id(gitmap_id: str) -> str:
    """Return the next GitMap ID using outside-in paired counting."""

    if len(gitmap_id) != 8 or not gitmap_id.isalpha() or not gitmap_id.islower():
        raise ValueError(f"Invalid GitMap ID: {gitmap_id}")

    letters = list(gitmap_id)

    pairs = [
        (0, 7),  # positions 1 & 8
        (1, 6),  # positions 2 & 7
        (2, 5),  # positions 3 & 6
        (3, 4),  # positions 4 & 5
    ]

    for left, right in pairs:
        # Each pair is one base-26 wheel.
        #
        # Left moves forward.
        # Right moves backward.
        #
        # The right character tells us whether this wheel
        # has completed its 26-position cycle.
        start_right = FIRST_GITMAP_ID[right]

        letters[left] = "a" if letters[left] == "z" else chr(ord(letters[left]) + 1)

        letters[right] = "z" if letters[right] == "a" else chr(ord(letters[right]) - 1)

        # If this pair has NOT returned to its starting
        # right-hand character, this increment is finished.
        if letters[right] != start_right:
            return "".join(letters)

        # This pair completed a full cycle.
        # Restore it and carry into the next pair.
        letters[left] = FIRST_GITMAP_ID[left]
        letters[right] = FIRST_GITMAP_ID[right]

    raise ValueError("GitMap ID space exhausted.")


def assign_missing_gitmap_ids(roadmap, reserved_ids=None) -> list:
    """Assign unique permanent GitMap IDs to roadmap items."""

    if reserved_ids is None:
        reserved_ids = set()
    else:
        reserved_ids = set(reserved_ids)

    items = [issue for issue, _, _, _ in iter_roadmap_issues(roadmap)]

    for milestone in roadmap.milestones:
        for section in milestone.sections:
            items.append(section)

            for feature in section.features:
                items.append(feature)

    roadmap_ids = [item.gitmap_id for item in items if item.gitmap_id]

    # Existing duplicates in the roadmap are an error.
    if len(set(roadmap_ids)) != len(roadmap_ids):
        raise ValueError("Duplicate GitMap IDs detected.")

    existing_ids = set(roadmap_ids)
    existing_ids.update(reserved_ids)

    next_id = FIRST_GITMAP_ID
    assigned = []

    for item in items:
        if item.gitmap_id:
            continue

        while next_id in existing_ids:
            next_id = increment_gitmap_id(next_id)

        item.gitmap_id = next_id
        existing_ids.add(next_id)
        assigned.append(item)

        next_id = increment_gitmap_id(next_id)

    return assigned
