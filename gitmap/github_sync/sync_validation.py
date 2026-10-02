import time

from gitmap.github_mapping import normalize_work_step_checkboxes
from gitmap.github_sync.github_representation import map_issue, map_milestone
from gitmap.github_sync.issue_sync import (
    build_issue_body,
)
from gitmap.github_sync.issue_lookup import get_existing_issues, get_gitmap_id_from_github_issue, \
    find_existing_issue_by_gitmap_id
from gitmap.github_sync.hierarchy_sync import build_hierarchy_issue_body
from gitmap.roadmap.traversal import iter_roadmap_issues


def validate_synchronization_plan(plan, roadmap, existing_issues):
    """Validate the exact synchronization plan before GitHub is mutated."""

    conflicts = []

    # Validate permanent IDs across every roadmap item represented by the plan.
    planned_items = (
        list(plan.added_issues)
        + list(plan.changed_issues)
        + list(plan.added_hierarchy)
        + list(plan.changed_hierarchy)
    )

    planned_by_id = {}

    for item in planned_items:
        gitmap_id = getattr(item, "gitmap_id", None)

        if not gitmap_id:
            number = getattr(item, "number", "unknown")
            conflicts.append(
                f"Planned roadmap item {number} has no permanent GitMap-ID"
            )
            continue

        planned_by_id.setdefault(gitmap_id, []).append(item)

    for gitmap_id, items in planned_by_id.items():
        if len(items) > 1:
            numbers = ", ".join(
                str(getattr(item, "number", "unknown")) for item in items
            )
            conflicts.append(
                f"GitMap-ID {gitmap_id} appears more than once in the sync plan: "
                f"{numbers}"
            )

    # Also validate the complete desired roadmap. A duplicate outside the changed
    # subset can still make the planned GitHub mutation ambiguous.
    roadmap_by_id = {}

    for issue, _, _, _ in iter_roadmap_issues(roadmap):
        if not issue.gitmap_id:
            continue

        roadmap_by_id.setdefault(issue.gitmap_id, []).append(issue)

    for hierarchy_item in _iter_hierarchy_items(roadmap):
        gitmap_id = getattr(hierarchy_item, "gitmap_id", None)
        if gitmap_id:
            roadmap_by_id.setdefault(gitmap_id, []).append(hierarchy_item)

    for gitmap_id, items in roadmap_by_id.items():
        if len(items) > 1:
            numbers = ", ".join(
                str(getattr(item, "number", "unknown")) for item in items
            )
            conflicts.append(f"Duplicate GitMap-ID {gitmap_id}: {numbers}")

    # Check duplicate GitMap IDs on GitHub.
    github_by_id = {}

    for github_issue in existing_issues:
        gitmap_id = get_gitmap_id_from_github_issue(github_issue)

        if not gitmap_id:
            continue

        github_by_id.setdefault(gitmap_id, []).append(github_issue)

    for gitmap_id, issues in github_by_id.items():
        if len(issues) > 1:
            numbers = ", ".join(f"#{issue.number}" for issue in issues)
            conflicts.append(
                f"GitMap-ID {gitmap_id} matches multiple GitHub issues: {numbers}"
            )

    # Validate hierarchy mappings that will actually execute.
    hierarchy_mappings = (
        list(plan.added_hierarchy_mappings)
        + list(plan.changed_hierarchy_mappings)
    )

    mapping_by_id = {}

    for mapping in hierarchy_mappings:
        gitmap_id = getattr(mapping, "gitmap_id", None)

        if not gitmap_id:
            title = getattr(mapping, "title", "unknown hierarchy item")
            conflicts.append(
                f"Planned hierarchy mapping '{title}' has no permanent GitMap-ID"
            )
            continue

        mapping_by_id.setdefault(gitmap_id, []).append(mapping)

    for gitmap_id, mappings in mapping_by_id.items():
        if len(mappings) > 1:
            titles = ", ".join(
                str(getattr(mapping, "title", "unknown")) for mapping in mappings
            )
            conflicts.append(
                f"GitMap-ID {gitmap_id} appears in multiple hierarchy mappings: "
                f"{titles}"
            )

    # Relationship work must reference permanent IDs. These fields are empty until
    # relationship planning is populated, but validation is ready for that data.
    for relationship_name in (
        "relationship_additions",
        "relationship_removals",
        "relationship_reparents",
    ):
        for relationship in getattr(plan, relationship_name, []):
            conflicts.extend(
                _validate_relationship_operation(relationship_name, relationship)
            )

    # Preserve the legacy ambiguity checks until remote planning fully replaces
    # number-based fallback matching.
    github_by_number = {}

    for github_issue in existing_issues:
        body = github_issue.body or ""

        for line in body.splitlines():
            if line.startswith("GitMap:"):
                number = line.removeprefix("GitMap:").strip()
                github_by_number.setdefault(number, []).append(github_issue)
                break

    for issue in list(plan.added_issues) + list(plan.changed_issues):
        mapping = _find_issue_mapping(roadmap, issue)

        if mapping is None:
            conflicts.append(
                f"Unable to build GitHub mapping for planned roadmap item "
                f"{getattr(issue, 'number', 'unknown')}"
            )
            continue

        permanent_match = find_existing_issue_by_gitmap_id(
            mapping,
            existing_issues,
        )

        if permanent_match is not None:
            continue

        matches = github_by_number.get(issue.number, [])

        if len(matches) > 1:
            github_numbers = ", ".join(f"#{match.number}" for match in matches)
            conflicts.append(
                f"Roadmap item {issue.number} matches multiple GitHub issues: "
                f"{github_numbers}"
            )

    # Check for ambiguous milestone mappings.
    milestone_by_name = {}

    for milestone in roadmap.milestones:
        mapping = map_milestone(milestone)
        parts = mapping.title.split(maxsplit=1)

        if len(parts) != 2:
            continue

        name = parts[1].casefold()
        milestone_by_name.setdefault(name, []).append(mapping)

    for mappings in milestone_by_name.values():
        if len(mappings) > 1:
            titles = ", ".join(mapping.title for mapping in mappings)
            conflicts.append(
                f"Multiple roadmap milestones could map to the same GitHub "
                f"milestone: {titles}"
            )

    return conflicts


def _iter_hierarchy_items(roadmap):
    """Yield Sections and Features from a roadmap."""

    for milestone in roadmap.milestones:
        for section in milestone.sections:
            yield section

            for feature in section.features:
                yield feature


def _find_issue_mapping(roadmap, target_issue):
    """Return the GitHub mapping for a specific roadmap Issue."""

    for issue, milestone, section, feature in iter_roadmap_issues(roadmap):
        if issue is target_issue:
            return map_issue(
                issue,
                milestone,
                section,
                feature,
                roadmap=roadmap,
            )

    return None


def _validate_relationship_operation(operation_name, relationship):
    """Validate permanent identity references in one planned relationship change."""

    conflicts = []

    child_id = _relationship_value(
        relationship,
        "child_gitmap_id",
        "child_id",
    )
    parent_id = _relationship_value(
        relationship,
        "parent_gitmap_id",
        "parent_id",
    )

    if not child_id:
        conflicts.append(
            f"{operation_name} contains a relationship with no child GitMap-ID"
        )

    if operation_name != "relationship_removals" and not parent_id:
        conflicts.append(
            f"{operation_name} contains a relationship with no parent GitMap-ID"
        )

    if child_id and parent_id and child_id == parent_id:
        conflicts.append(
            f"{operation_name} would make GitMap-ID {child_id} its own parent"
        )

    return conflicts


def _relationship_value(relationship, *names):
    """Read a relationship field from either an object or a mapping."""

    for name in names:
        if isinstance(relationship, dict) and name in relationship:
            return relationship[name]

        value = getattr(relationship, name, None)
        if value is not None:
            return value

    return None


def verify_synchronization_result_once(
    repository,
    roadmap,
    differences,
):
    """Verify GitHub state after synchronization."""

    # Re-read GitHub after synchronization.
    existing_issues = get_existing_issues(repository)

    missing_created = []

    incorrect_updates = []

    identity_failures = []

    duplicate_ids = []

    incorrect_closures = []

    github_ids = {}

    for github_issue in existing_issues:
        gitmap_id = get_gitmap_id_from_github_issue(github_issue)

        if not gitmap_id:
            continue

        github_ids.setdefault(
            gitmap_id,
            [],
        ).append(github_issue)

    for gitmap_id, github_issues in github_ids.items():
        if len(github_issues) > 1:
            duplicate_ids.append(
                (
                    gitmap_id,
                    github_issues,
                )
            )

    affected_issues = differences["new"] + [
        change["issue"] for change in differences["changed"]
    ]

    for issue in affected_issues:
        if not issue.gitmap_id:
            identity_failures.append((issue, "Roadmap item has no GitMap-ID"))
            continue

        matches = [
            github_issue
            for github_issue in existing_issues
            if get_gitmap_id_from_github_issue(github_issue) == issue.gitmap_id
        ]

        if len(matches) == 0:
            identity_failures.append((issue, "GitMap-ID not found on GitHub"))

        elif len(matches) > 1:
            identity_failures.append(
                (
                    issue,
                    f"GitMap-ID appears on {len(matches)} GitHub issues",
                )
            )

    for change in differences["changed"]:
        issue = change["issue"]
        mapping = None

        for candidate, milestone, section, feature in iter_roadmap_issues(roadmap):
            if candidate is issue:
                mapping = map_issue(issue, milestone, section, feature, roadmap=roadmap)

                break

        if mapping is None:
            continue

        existing = find_existing_issue_by_gitmap_id(
            mapping,
            existing_issues,
        )

        if existing is None:
            incorrect_updates.append((issue, "GitHub issue not found"))
            continue

        expected_body = build_issue_body(mapping)

        existing_body = normalize_work_step_checkboxes(existing.body or "")
        expected_body = normalize_work_step_checkboxes(expected_body)

        if (
            existing.title != mapping.title
            or existing_body.strip() != expected_body.strip()
        ):
            incorrect_updates.append((issue, "GitHub content does not match roadmap"))

    for change in differences.get("hierarchy_changed", []):
        mapping = change["mapping"]

        existing = find_existing_issue_by_gitmap_id(
            mapping,
            existing_issues,
        )

        if existing is None:
            incorrect_updates.append((mapping, "Hierarchy GitHub issue not found"))
            continue

        expected_body = build_hierarchy_issue_body(mapping)

        if (
            existing.title != mapping.title
            or (existing.body or "").strip() != expected_body.strip()
        ):
            incorrect_updates.append(
                (mapping, "Hierarchy GitHub content does not match roadmap")
            )

    for issue in differences["new"]:
        mapping = None

        for candidate, milestone, section, feature in iter_roadmap_issues(roadmap):
            if candidate is issue:
                mapping = map_issue(issue, milestone, section, feature, roadmap=roadmap)

                break

        if mapping is None:
            continue

        existing = find_existing_issue_by_gitmap_id(
            mapping,
            existing_issues,
        )

        if existing is None:
            missing_created.append(issue)

    for github_issue in differences["removed"]:
        refreshed = next(
            (issue for issue in existing_issues if issue.number == github_issue.number),
            None,
        )

        if refreshed is None:
            incorrect_closures.append((github_issue, "GitHub issue not found"))
            continue

        if refreshed.state != "closed":
            incorrect_closures.append((github_issue, "GitHub issue was not closed"))

    return {
        "existing_issues": existing_issues,
        "missing_created": missing_created,
        "incorrect_updates": incorrect_updates,
        "incorrect_closures": incorrect_closures,
        "identity_failures": identity_failures,
        "duplicate_ids": duplicate_ids,
    }


def verify_synchronization_results(
    repository,
    roadmap,
    differences,
    max_attempts=3,
):
    """Verify synchronization, retrying if GitHub state is briefly stale."""

    verification = None

    for attempt in range(1, max_attempts + 1):
        verification = verify_synchronization_result_once(
            repository,
            roadmap,
            differences,
        )

        failed = (
            verification["missing_created"]
            or verification["incorrect_updates"]
            or verification["incorrect_closures"]
            or verification["identity_failures"]
            or verification["duplicate_ids"]
        )

        if not failed:
            return verification

        if attempt < max_attempts:
            print(f"Verification incomplete. Retrying ({attempt}/{max_attempts})...")
            time.sleep(attempt)

    return verification
