"""Compare desired GitMap issue state with existing GitHub issue state."""

from gitmap.github_sync.issues.hierarchy_sync import (
    build_hierarchy_issue_body,
)
from gitmap.github_sync.issues.issue_sync import (
    build_issue_body,
    preserve_work_step_checkboxes,
)


def _label_names(github_issue):
    """Return normalized label names from an existing GitHub issue."""

    return {label.name.casefold() for label in github_issue.labels}


def _milestone_title(github_issue):
    """Return the milestone title from an existing GitHub issue."""

    milestone = getattr(github_issue, "milestone", None)

    if milestone is None:
        return None

    return milestone.title


def issue_has_changes(mapping, existing):
    """Return True when a normal GitHub issue differs from its GitMap mapping."""

    expected_body = build_issue_body(mapping)

    expected_body = preserve_work_step_checkboxes(
        existing.body or "",
        expected_body,
    )

    if existing.title != mapping.title:
        return True

    if (existing.body or "").strip() != expected_body.strip():
        return True

    if _milestone_title(existing) != mapping.milestone:
        return True

    expected_labels = {label.casefold() for label in mapping.labels}

    if _label_names(existing) != expected_labels:
        return True

    return False


def hierarchy_issue_has_changes(mapping, existing, roadmap):
    """Return True when a hierarchy issue differs from its GitMap mapping."""

    expected_body = build_hierarchy_issue_body(mapping)

    if existing.title != mapping.title:
        return True

    if (existing.body or "").strip() != expected_body.strip():
        return True

    if _milestone_title(existing) != mapping.milestone:
        return True

    expected_labels = {f"GitMap: {roadmap.name}".casefold()}

    if _label_names(existing) != expected_labels:
        return True

    return False
