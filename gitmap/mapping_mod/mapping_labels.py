from github import GithubException

from gitmap.mapping_mod.mapping import (
    LabelMapping,
    map_feature_label,
    map_issue_labels,
    map_roadmap_label,
    map_section_label,
    should_use_feature_label,
    should_use_section_label,
)

DEFAULT_LABEL_COLOR = "0366d6"


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


def create_missing_labels(repository, mappings):
    """Create missing labels and return all available labels."""

    existing_labels = get_existing_labels(repository)
    labels = list(existing_labels)

    for mapping in mappings:
        existing = find_existing_label(mapping, labels)

        if existing:
            continue

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
                    raise
            else:
                raise

        labels.append(label)

    return labels


def sync_labels(repository, roadmap):
    """Create any missing structural labels for a roadmap."""

    mappings = collect_label_mappings(roadmap)
    return create_missing_labels(repository, mappings)


def collect_label_mappings(roadmap):
    """Collect the labels required by a roadmap."""

    mappings = [
        map_roadmap_label(roadmap),
    ]

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
