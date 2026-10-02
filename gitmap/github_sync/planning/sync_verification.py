import re
import time

from gitmap.github_sync.issues.github_representation import map_issue
from gitmap.github_sync.issues.hierarchy_sync import build_hierarchy_issue_body
from gitmap.github_sync.issues.issue_lookup import (
    find_existing_issue_by_gitmap_id,
    get_existing_issues,
    get_gitmap_id_from_github_issue,
)
from gitmap.github_sync.issues.issue_sync import build_issue_body
from gitmap.roadmap.model.traversal import iter_roadmap_issues


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


def normalize_work_step_checkboxes(body: str) -> str:
    """Ignore GitHub checkbox completion state when comparing issue bodies."""

    return re.sub(
        r"^- \[[xX ]\]",
        "- [ ]",
        body,
        flags=re.MULTILINE,
    )
