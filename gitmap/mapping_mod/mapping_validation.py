import time

from gitmap.mapping_mod.mapping import map_issue, map_milestone
from gitmap.mapping_mod.mapping_issues import (
    build_hierarchy_issue_body,
    build_issue_body,
    find_existing_issue_by_gitmap_id,
    get_existing_issues,
    get_gitmap_id_from_github_issue,
)
from gitmap.mapping_mod.mapping_state import iter_roadmap_issues


def validate_synchronization_plan(roadmap, existing_issues):
    """Validate that roadmap items can be synchronized safely."""

    conflicts = []

    # Check duplicate GitMap IDs in the roadmap.
    roadmap_by_id = {}

    for issue, _, _, _ in iter_roadmap_issues(roadmap):
        if not issue.gitmap_id:
            continue

        roadmap_by_id.setdefault(issue.gitmap_id, []).append(issue)

    for gitmap_id, issues in roadmap_by_id.items():
        if len(issues) > 1:
            numbers = ", ".join(issue.number for issue in issues)

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

    # Check ambiguous legacy GitMap-number matches.
    github_by_number = {}

    for github_issue in existing_issues:
        body = github_issue.body or ""

        for line in body.splitlines():
            if line.startswith("GitMap:"):
                number = line.removeprefix("GitMap:").strip()

                github_by_number.setdefault(
                    number,
                    [],
                ).append(github_issue)

                break

    for issue, milestone, section, feature in iter_roadmap_issues(roadmap):
        mapping = map_issue(
            issue,
            milestone,
            section,
            feature,
        )

        # Permanent identity wins. If the GitMap-ID uniquely
        # identifies an existing issue, legacy number collisions
        # do not make the match ambiguous.
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
                f"Roadmap item {issue.number} matches multiple "
                f"GitHub issues: {github_numbers}"
            )

    # Check for ambiguous milestone mappings.
    milestone_by_name = {}

    for milestone in roadmap.milestones:
        mapping = map_milestone(milestone)
        parts = mapping.title.split(maxsplit=1)

        if len(parts) != 2:
            continue

        name = parts[1].casefold()

        milestone_by_name.setdefault(
            name,
            [],
        ).append(mapping)

    for name, mappings in milestone_by_name.items():
        if len(mappings) > 1:
            titles = ", ".join(mapping.title for mapping in mappings)

            conflicts.append(
                f"Multiple roadmap milestones could map to "
                f"the same GitHub milestone: {titles}"
            )
    return conflicts


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
                mapping = map_issue(
                    candidate,
                    milestone,
                    section,
                    feature,
                )
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

        if (
            existing.title != mapping.title
            or (existing.body or "").strip() != expected_body.strip()
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
                mapping = map_issue(
                    candidate,
                    milestone,
                    section,
                    feature,
                )
                break

        if mapping is None:
            continue

        existing = find_existing_issue_by_gitmap_id(
            mapping,
            existing_issues,
        )

        if existing is None:
            missing_created.append(issue)

    return {
        "existing_issues": existing_issues,
        "missing_created": missing_created,
        "incorrect_updates": incorrect_updates,
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
            or verification["identity_failures"]
            or verification["duplicate_ids"]
        )

        if not failed:
            return verification

        if attempt < max_attempts:
            print(f"Verification incomplete. Retrying ({attempt}/{max_attempts})...")
            time.sleep(attempt)

    return verification
