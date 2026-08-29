from gitmap.mapping_mod.mapping_issues import get_existing_issues, is_gitmap_managed_issue


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
