import os
import time
from dataclasses import dataclass
from pathlib import Path

from github import Github

from gitmap.mapping_mod.mapping import MilestoneMapping, LabelMapping, map_milestone, map_issue
from gitmap.mapping_mod.mapping_labels import find_existing_label, get_existing_labels, sync_labels
from gitmap.mapping_mod.mapping_milestones import find_existing_milestone, get_existing_milestones, sync_milestones

DEFAULT_LABEL_COLOR = "0366d6"
FIRST_GITMAP_ID = "goredsox"
SYNC_LOCK_PATH = Path(".gitmap-sync.lock")


def get_github_client(token):
    """Create an authenticated GitHub client."""

    return Github(token)


@dataclass
class SynchronizationError(Exception):
    """Raised when synchronization stops after a GitHub operation fails."""

    def __init__(
        self,
        message,
        completed,
        failed,
        remaining,
        original_error,
    ):
        super().__init__(message)

        self.completed = completed
        self.failed = failed
        self.remaining = remaining
        self.original_error = original_error


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


def assign_missing_gitmap_ids(roadmap) -> list:
    """Assign unique permanent GitMap IDs to roadmap issues."""

    issues = [
        issue
        for issue, _, _, _ in iter_roadmap_issues(roadmap)
    ]

    existing_ids = {
        issue.gitmap_id
        for issue in issues
        if issue.gitmap_id
    }

    # Existing duplicates are an error; do not make the situation worse.
    if len(existing_ids) != sum(
        1 for issue in issues if issue.gitmap_id
    ):
        raise ValueError("Duplicate GitMap IDs detected.")

    next_id = FIRST_GITMAP_ID
    assigned = []

    for issue in issues:
        if issue.gitmap_id:
            continue

        while next_id in existing_ids:
            next_id = increment_gitmap_id(next_id)

        issue.gitmap_id = next_id
        existing_ids.add(next_id)
        assigned.append(issue)

        next_id = increment_gitmap_id(next_id)

    return assigned


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


def get_existing_issues(repository):
    """Retrieve GitMap-managed issues from a GitHub repository."""

    return [
        issue
        for issue in repository.get_issues(state="all")
        if is_gitmap_managed_issue(issue)
    ]


def get_gitmap_id_from_github_issue(issue) -> str:
    """Return the permanent GitMap ID stored in a GitHub issue body."""

    body = issue.body or ""

    for line in body.splitlines():
        if line.startswith("GitMap-ID:"):
            return line.removeprefix("GitMap-ID:").strip()

    return ""


def find_existing_issue_by_gitmap_id(mapping, existing_issues):
    """Find an existing GitHub issue by permanent GitMap ID."""

    if not mapping.gitmap_id:
        return None

    for issue in existing_issues:
        if get_gitmap_id_from_github_issue(issue) == mapping.gitmap_id:
            return issue

    return None


def find_existing_issue(mapping, existing_issues):
    """Find an existing GitHub issue by permanent ID or roadmap number."""

    existing = find_existing_issue_by_gitmap_id(
        mapping,
        existing_issues,
    )

    if existing is not None:
        return existing

    # Backward-compatible fallback for roadmaps that have not
    # yet been migrated to permanent GitMap IDs.
    marker = f"GitMap: {mapping.number}"

    for issue in existing_issues:
        if marker in (issue.body or ""):
            return issue

    return None


def build_issue_body(mapping):
    """Build the GitHub issue body from a roadmap issue mapping."""

    body = mapping.description.strip()

    if mapping.work_steps:
        body += "\n\n**Work Steps:**\n"

        for work_step in mapping.work_steps:
            body += f"- [ ] {work_step.title}\n"

    if mapping.requirements:
        body += "\n\n**End Goal:**\n"

        for requirement in mapping.requirements:
            body += f"- {requirement.text}\n"

    if mapping.gitmap_id:
        body += f"\nGitMap-ID: {mapping.gitmap_id}"

    body += f"\nGitMap: {mapping.number}"

    return body


def create_issue(repository, mapping, milestone, labels):
    """Create a GitHub issue from an issue mapping."""

    return repository.create_issue(
        title=mapping.title,
        body=build_issue_body(mapping),
        milestone=milestone,
        labels=labels,
    )


def sync_issue(repository, mapping):
    """Create or update an issue from a roadmap mapping."""

    existing_issues = get_existing_issues(repository)
    existing = find_existing_issue(mapping, existing_issues)

    milestone, labels = resolve_issue_targets(
        repository,
        mapping,
    )

    if existing:
        existing.edit(
            title=mapping.title,
            body=build_issue_body(mapping),
            milestone=milestone,
            labels=[label.name for label in labels],
        )
        return existing, False

    issue = create_issue(
        repository,
        mapping,
        milestone,
        labels,
    )

    return issue, True


def sync_issues(
    repository,
    roadmap,
    issues_to_sync=None,
    progress_start=0,
    progress_total=None,
):
    """Synchronize changed roadmap issues with GitHub."""

    sync_milestones(repository, roadmap)
    sync_labels(repository, roadmap)

    if issues_to_sync is not None:
        issues_to_sync = {id(issue) for issue in issues_to_sync}

    if progress_total is None:
        progress_total = len(issues_to_sync) if issues_to_sync is not None else 0

    progress = progress_start
    results = []

    for milestone in roadmap.milestones:
        for issue in milestone.issues:
            if issues_to_sync is not None and id(issue) not in issues_to_sync:
                continue

            progress += 1
            print(
                f"[{progress}/{progress_total}] Processing {issue.number} {issue.title}"
            )

            mapping = map_issue(issue, milestone)
            try:
                result, created = sync_issue(repository, mapping)
                results.append((result, created))

            except Exception as error:
                remaining = progress_total - progress

                raise SynchronizationError(
                    message=f"Failed to synchronize {issue.number} {issue.title}",
                    completed=len(results),
                    failed=issue,
                    remaining=remaining,
                    original_error=error,
                ) from error

            except Exception as error:
                remaining = progress_total - progress

                raise SynchronizationError(
                    message=f"Failed to synchronize {issue.number} {issue.title}",
                    completed=len(results),
                    failed=issue,
                    remaining=remaining,
                    original_error=error,
                ) from error

        for section in milestone.sections:
            for issue in section.issues:
                if issues_to_sync is not None and id(issue) not in issues_to_sync:
                    continue

                progress += 1
                print(
                    f"[{progress}/{progress_total}] "
                    f"Processing {issue.number} {issue.title}"
                )

                mapping = map_issue(issue, milestone, section)
                try:
                    result, created = sync_issue(repository, mapping)
                    results.append((result, created))

                except Exception as error:
                    remaining = progress_total - progress

                    raise SynchronizationError(
                        message=f"Failed to synchronize {issue.number} {issue.title}",
                        completed=len(results),
                        failed=issue,
                        remaining=remaining,
                        original_error=error,
                    ) from error

            for feature in section.features:
                for issue in feature.issues:
                    if issues_to_sync is not None and id(issue) not in issues_to_sync:
                        continue

                    progress += 1
                    print(
                        f"[{progress}/{progress_total}] "
                        f"Processing {issue.number} {issue.title}"
                    )

                    mapping = map_issue(
                        issue,
                        milestone,
                        section,
                        feature,
                    )
                    try:
                        result, created = sync_issue(repository, mapping)
                        results.append((result, created))

                    except Exception as error:
                        remaining = progress_total - progress

                        raise SynchronizationError(
                            message=f"Failed to synchronize {issue.number} {issue.title}",
                            completed=len(results),
                            failed=issue,
                            remaining=remaining,
                            original_error=error,
                        ) from error

    return results


def sync_removed_issues(
    removed_issues,
    progress_start=0,
    progress_total=None,
):
    """Close GitHub issues that were removed from the roadmap."""

    if progress_total is None:
        progress_total = progress_start + len(removed_issues)

    progress = progress_start
    results = []

    for issue in removed_issues:
        if issue.state != "open":
            continue

        progress += 1

        print(
            f"[{progress}/{progress_total}] "
            f"Closing removed issue #{issue.number} {issue.title}"
        )

        try:
            issue.edit(state="closed")
            results.append(issue)

        except Exception as error:
            remaining = progress_total - progress

            raise SynchronizationError(
                message=f"Failed to close removed issue #{issue.number}",
                completed=progress - 1,
                failed=issue,
                remaining=remaining,
                original_error=error,
            ) from error

    return results


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

    affected_issues = differences["new"] + differences["changed"]

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

    for issue in differences["changed"]:
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


def resolve_issue_targets(repository, mapping):
    """Resolve the GitHub milestone and labels for an issue."""

    milestones = get_existing_milestones(repository)
    labels = get_existing_labels(repository)

    milestone_mapping = MilestoneMapping(
        number=mapping.number,
        title=mapping.milestone,
    )

    milestone = find_existing_milestone(
        milestone_mapping,
        milestones,
    )

    issue_labels = []

    for label_name in mapping.labels:
        label_mapping = LabelMapping(name=label_name)
        label = find_existing_label(label_mapping, labels)

        if label:
            issue_labels.append(label)

    return milestone, issue_labels


def preserve_issue_numbers(matches):
    """Return GitMap issue numbers mapped to GitHub issue numbers."""
    return {
        roadmap_number: github_issue.number
        for roadmap_number, github_issue in matches.items()
    }


def associate_issues_with_milestones(existing_issues):
    """Associate GitMap-managed issues with their GitHub milestones."""

    associations = {}

    for issue in existing_issues:
        if not is_gitmap_managed_issue(issue):
            continue

        if issue.milestone is None:
            continue

        marker = "GitMap:"
        body = issue.body or ""

        for line in body.splitlines():
            if line.startswith(marker):
                roadmap_number = line.removeprefix(marker).strip()
                associations[roadmap_number] = issue.milestone
                break

    return associations


def associate_issues_with_sections(existing_issues, roadmap):
    """Associate GitMap-managed issues with their roadmap sections."""

    associations = {}

    section_names = {
        section.title.removesuffix(" (DONE)"): section
        for milestone in roadmap.milestones
        for section in milestone.sections
    }

    for issue in existing_issues:
        if not is_gitmap_managed_issue(issue):
            continue

        for label in issue.labels:
            if label.name in section_names:
                associations[issue.number] = section_names[label.name]
                break

    return associations


def associate_issues_with_features(existing_issues, roadmap):
    """Associate GitMap-managed issues with their roadmap features."""

    associations = {}

    feature_names = {
        feature.title.removesuffix(" (DONE)"): feature
        for milestone in roadmap.milestones
        for section in milestone.sections
        for feature in section.features
    }

    for issue in existing_issues:
        if not is_gitmap_managed_issue(issue):
            continue

        for label in issue.labels:
            if label.name in feature_names:
                associations[issue.number] = feature_names[label.name]
                break

    return associations


def restore_work_step_relationships(existing_issues):
    """Restore work steps from GitMap-managed GitHub issue bodies."""

    relationships = {}

    for issue in existing_issues:
        if not is_gitmap_managed_issue(issue):
            continue

        body = issue.body or ""
        lines = body.splitlines()

        in_work_steps = False
        work_steps = []

        for line in lines:
            if line.strip() == "**Work Steps:**":
                in_work_steps = True
                continue

            if in_work_steps:
                if not line.startswith("- ["):
                    if line.strip():
                        break
                    continue

                work_steps.append(line.strip())

        if work_steps:
            relationships[issue.number] = work_steps

    return relationships


def find_unmatched_roadmap_items(roadmap, existing_issues):
    """Return roadmap issues that cannot be safely matched to GitHub issues."""

    matched_numbers = set()

    for issue in existing_issues:
        if not is_gitmap_managed_issue(issue):
            continue

        body = issue.body or ""

        for line in body.splitlines():
            if line.startswith("GitMap:"):
                roadmap_number = line.removeprefix("GitMap:").strip()
                matched_numbers.add(roadmap_number)
                break

    unmatched = []

    for issue, _, _, _ in iter_roadmap_issues(roadmap):
        if issue.number not in matched_numbers:
            unmatched.append(issue)

    return unmatched


def rebuild_roadmap_state(repository, roadmap):
    """Rebuild GitMap project state from existing GitHub data."""

    existing_issues = get_existing_issues(repository)

    return {
        "milestones": associate_issues_with_milestones(existing_issues),
        "sections": associate_issues_with_sections(existing_issues, roadmap),
        "features": associate_issues_with_features(existing_issues, roadmap),
        "work_steps": restore_work_step_relationships(existing_issues),
        "unmatched": find_unmatched_roadmap_items(roadmap, existing_issues),
    }


def iter_roadmap_issues(roadmap):
    """Yield every roadmap issue with its structural context."""

    for milestone in roadmap.milestones:
        for issue in getattr(milestone, "issues", []):
            yield issue, milestone, None, None

        for section in getattr(milestone, "sections", []):
            for issue in getattr(section, "issues", []):
                yield issue, milestone, section, None

            for feature in getattr(section, "features", []):
                for issue in getattr(feature, "issues", []):
                    yield issue, milestone, section, feature


def detect_new_roadmap_items(roadmap, existing_issues):
    """Return roadmap issues that do not yet exist on GitHub."""

    new_items = []

    for issue, milestone, section, feature in iter_roadmap_issues(roadmap):
        mapping = map_issue(
            issue,
            milestone,
            section,
            feature,
        )

        existing = find_existing_issue(
            mapping,
            existing_issues,
        )

        if existing is None:
            new_items.append(issue)

    return new_items


def detect_changed_roadmap_items(roadmap, existing_issues):
    """Return roadmap issues that differ from their GitHub issues."""

    changed = []

    for issue, milestone, section, feature in iter_roadmap_issues(roadmap):
        mapping = map_issue(
            issue,
            milestone,
            section,
            feature,
        )
        existing = find_existing_issue(mapping, existing_issues)

        if existing is None:
            continue

        expected_body = build_issue_body(mapping)

        if (
            existing.title != mapping.title
            or (existing.body or "").strip() != expected_body.strip()
        ):
            changed.append(issue)

    return changed


def detect_matching_roadmap_items(roadmap, existing_issues):
    """Return roadmap issues that already match their GitHub issues."""

    matching = []

    for issue, milestone, section, feature in iter_roadmap_issues(roadmap):
        mapping = map_issue(
            issue,
            milestone,
            section,
            feature,
        )
        existing = find_existing_issue(mapping, existing_issues)

        if existing is None:
            continue

        expected_body = build_issue_body(mapping)

        if (
            existing.title == mapping.title
            and (existing.body or "").strip() == expected_body.strip()
        ):
            matching.append(issue)

    return matching


def detect_renumbered_roadmap_items(roadmap, existing_issues):
    """Return roadmap issues whose GitMap number has changed."""

    renumbered = []

    for issue, milestone, section, feature in iter_roadmap_issues(roadmap):
        if not issue.gitmap_id:
            continue

        mapping = map_issue(
            issue,
            milestone,
            section,
            feature,
        )

        existing = find_existing_issue_by_gitmap_id(
            mapping,
            existing_issues,
        )

        if existing is None:
            continue

        body = existing.body or ""
        old_number = None

        for line in body.splitlines():
            if line.startswith("GitMap:"):
                old_number = line.removeprefix("GitMap:").strip()
                break

        if old_number and old_number != issue.number:
            renumbered.append((issue, old_number, issue.number))

    return renumbered


def summarize_roadmap_differences(roadmap, existing_issues):
    """Summarize roadmap differences before synchronization."""

    return {
        "new": detect_new_roadmap_items(roadmap, existing_issues),
        "changed": detect_changed_roadmap_items(roadmap, existing_issues),
        "renumbered": detect_renumbered_roadmap_items(
            roadmap,
            existing_issues,
        ),
        "matching": detect_matching_roadmap_items(roadmap, existing_issues),
        "removed": detect_removed_roadmap_items(roadmap, existing_issues),
    }


def detect_removed_roadmap_items(roadmap, existing_issues):
    """Return previously tracked GitMap issues removed from the roadmap."""

    roadmap_ids = {
        issue.gitmap_id
        for issue, _, _, _ in iter_roadmap_issues(roadmap)
        if issue.gitmap_id
    }

    removed = []

    for github_issue in existing_issues:
        if github_issue.state != "open":
            continue

        gitmap_id = get_gitmap_id_from_github_issue(github_issue)

        if not gitmap_id:
            continue

        if gitmap_id not in roadmap_ids:
            removed.append(github_issue)

    return removed


def is_gitmap_managed_issue(issue):
    """Return True if the GitHub issue is managed by GitMap."""

    body = issue.body or ""

    return "GitMap-ID:" in body or "GitMap:" in body


def create_sync_lock(repository_name):
    """Create a synchronization lock for the current process."""

    SYNC_LOCK_PATH.write_text(
        f"repository={repository_name}\npid={os.getpid()}\n",
        encoding="utf-8",
    )


def read_sync_lock():
    """Read the current synchronization lock."""

    if not SYNC_LOCK_PATH.exists():
        return None

    values = {}

    for line in SYNC_LOCK_PATH.read_text(encoding="utf-8").splitlines():
        key, _, value = line.partition("=")

        if key and value:
            values[key] = value

    if "repository" not in values or "pid" not in values:
        return None

    try:
        pid = int(values["pid"])
    except ValueError:
        return None

    return {
        "repository": values["repository"],
        "pid": pid,
    }


def is_process_running(pid):
    """Return True if a process with the given PID is still running."""

    try:
        os.kill(pid, 0)
    except OSError:
        return False

    return True


def acquire_sync_lock(repository_name):
    """Acquire the synchronization lock if no active sync owns it."""

    lock = read_sync_lock()

    if lock is not None:
        if lock["repository"] == repository_name and is_process_running(lock["pid"]):
            return False, lock

        # Existing lock is stale.
        SYNC_LOCK_PATH.unlink(missing_ok=True)

    create_sync_lock(repository_name)

    return True, None


def release_sync_lock():
    """Release the synchronization lock."""

    SYNC_LOCK_PATH.unlink(missing_ok=True)


if __name__ == "__main__":
    from pathlib import Path

    from gitmap.parser import parse_roadmap

    roadmap = parse_roadmap(Path("roadmap.md"))

    milestone = roadmap.milestones[0]
    section = milestone.sections[0]
    issue = section.issues[0]

    mapping = map_issue(issue, milestone, section)

    print(f"Number: {mapping.number}")
    print(f"Title: {mapping.title}")
    print(f"Work steps: {len(mapping.work_steps)}")

    print(build_issue_body(mapping))
