from github import GithubException

from gitmap.github_sync.issues.github_representation import (
    map_feature_label,
    map_issue_labels,
    map_roadmap_label,
    map_section_label,
    should_use_feature_label,
    should_use_section_label,
)

DEFAULT_LABEL_COLOR = "0366d6"

GITHUB_LABEL_MAX_LENGTH = 50


def validate_label_mappings(mappings):
    """Return label mappings whose names exceed GitHub's length limit."""
    return [
        mapping for mapping in mappings if len(mapping.name) > GITHUB_LABEL_MAX_LENGTH
    ]


def validate_roadmap_labels(roadmap):
    """Return invalid labels required by a roadmap."""
    return validate_label_mappings(collect_label_mappings(roadmap))


def create_missing_labels(
    repository,
    mappings,
    progress_callback=None,
    result_collector=None,
):
    """Create missing labels and return all available labels."""
    existing_labels = get_existing_labels(repository)
    labels = list(existing_labels)
    total = len(mappings)

    for current, mapping in enumerate(mappings, start=1):
        existing = find_existing_label(mapping, labels)

        if existing:
            message = f"Label unchanged: {mapping.name}"
            if result_collector is not None:
                result_collector.skipped("Label", mapping.name, "Already exists")
        else:
            message = f"Creating label: {mapping.name}"
            try:
                label = repository.create_label(
                    name=mapping.name,
                    color=DEFAULT_LABEL_COLOR,
                )
            except GithubException as error:
                if error.status == 422:
                    existing_labels = get_existing_labels(repository)
                    label = find_existing_label(mapping, existing_labels)
                    if label is None:
                        if result_collector is not None:
                            result_collector.failed("Label", mapping.name, str(error))
                        raise
                    if result_collector is not None:
                        result_collector.skipped(
                            "Label",
                            mapping.name,
                            "Already existed when GitHub was rechecked",
                        )
                else:
                    if result_collector is not None:
                        result_collector.failed("Label", mapping.name, str(error))
                    raise
            else:
                if result_collector is not None:
                    result_collector.created("Label", mapping.name)

            labels.append(label)

        if progress_callback is not None:
            progress_callback("Labels", current, total, message)

    return labels


def find_existing_label(mapping, existing_labels):
    """Find an existing GitHub label with the same name."""
    for label in existing_labels:
        if label.name.casefold() == mapping.name.casefold():
            return label
    return None


def resolve_label(mapping, existing_labels):
    """Determine whether a label already exists or needs to be created."""
    existing = find_existing_label(mapping, existing_labels)
    if existing:
        return existing
    return mapping


def get_existing_labels(repository):
    """Retrieve existing labels from a GitHub repository."""
    return list(repository.get_labels())


def sync_labels(
    repository,
    roadmap,
    progress_callback=None,
    result_collector=None,
):
    """Create any missing structural labels for a roadmap."""
    mappings = collect_label_mappings(roadmap)
    return create_missing_labels(
        repository,
        mappings,
        progress_callback=progress_callback,
        result_collector=result_collector,
    )


def collect_label_mappings(roadmap):
    """Collect the labels required by a roadmap."""
    mappings = [map_roadmap_label(roadmap)]

    for milestone in roadmap.milestones:
        for issue in milestone.issues:
            mappings.extend(map_issue_labels(issue))

        for section in milestone.sections:
            if should_use_section_label(roadmap):
                mappings.append(map_section_label(section))

            for issue in section.issues:
                mappings.extend(map_issue_labels(issue))

            for feature in section.features:
                if should_use_feature_label(roadmap):
                    mappings.append(map_feature_label(feature))

                for issue in feature.issues:
                    mappings.extend(map_issue_labels(issue))

    return mappings


def prepare_labels(repository, roadmap):
    """Prepare roadmap labels for GitHub synchronization."""
    mappings = collect_label_mappings(roadmap)
    existing_labels = get_existing_labels(repository)
    return [resolve_label(mapping, existing_labels) for mapping in mappings]


def preview_missing_labels(repository, roadmap):
    """Preview labels that would be created without changing GitHub."""
    mappings = collect_label_mappings(roadmap)
    existing_labels = get_existing_labels(repository)

    missing = [
        mapping
        for mapping in mappings
        if not find_existing_label(mapping, existing_labels)
    ]

    for mapping in missing:
        print(f"Would create label: {mapping.name}")

    return missing
