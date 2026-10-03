from gitmap.github_sync.issues.github_representation import map_milestone


def find_existing_milestone(mapping, existing_milestones):
    """Find an existing GitHub milestone, including a renumbered milestone."""

    for milestone in existing_milestones:
        existing_title = milestone.title.removesuffix(" (DONE)")

        if existing_title == mapping.title:
            return milestone

    mapping_parts = mapping.title.split(maxsplit=1)

    if len(mapping_parts) != 2:
        return None

    mapping_name = mapping_parts[1]

    for milestone in existing_milestones:
        existing_title = milestone.title.removesuffix(" (DONE)")
        existing_parts = existing_title.split(maxsplit=1)

        if len(existing_parts) != 2:
            continue

        existing_name = existing_parts[1]

        if existing_name == mapping_name:
            return milestone

    return None


def resolve_milestone(mapping, existing_milestones):
    """Determine whether a milestone already exists or needs to be created."""

    existing = find_existing_milestone(
        mapping,
        existing_milestones,
    )

    if existing:
        return existing

    return mapping


def get_existing_milestones(repository):
    """Retrieve existing milestones from a GitHub repository."""

    return list(repository.get_milestones())


def create_missing_milestones(
    repository,
    mappings,
    progress_callback=None,
):
    """Create missing milestones and update renumbered milestones."""

    existing_milestones = get_existing_milestones(repository)
    milestones = list(existing_milestones)

    total = len(mappings)

    for current, mapping in enumerate(mappings, start=1):
        existing = find_existing_milestone(
            mapping,
            milestones,
        )

        if existing:
            existing_title = existing.title.removesuffix(" (DONE)")

            if existing_title != mapping.title:
                message = f"Updating milestone: {mapping.title}"
                existing.edit(title=mapping.title)
            else:
                message = f"Milestone unchanged: {mapping.title}"

        else:
            message = f"Creating milestone: {mapping.title}"

            milestone = repository.create_milestone(
                title=mapping.title,
            )

            milestones.append(milestone)

        if progress_callback is not None:
            progress_callback(
                "Milestones",
                current,
                total,
                message,
            )

    return milestones


def sync_milestones(
    repository,
    roadmap,
    progress_callback=None,
):
    """Create any missing milestones for a roadmap."""

    mappings = [
        map_milestone(milestone)
        for milestone in roadmap.milestones
    ]

    return create_missing_milestones(
        repository,
        mappings,
        progress_callback=progress_callback,
    )