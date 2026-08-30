from gitmap.mapping_mod.mapping import MilestoneMapping
from gitmap.mapping_mod.mapping_milestones import (
    find_existing_milestone,
    get_existing_milestones,
)


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


def is_gitmap_managed_issue(issue):
    """Return True if the GitHub issue is managed by GitMap."""

    body = issue.body or ""

    return "GitMap-ID:" in body or "GitMap:" in body


def build_hierarchy_issue_body(mapping):
    """Build the body for a Section or Feature GitHub Issue."""

    body = mapping.description.strip()

    if mapping.gitmap_id:
        body += f"\n\nGitMap-ID: {mapping.gitmap_id}"

    body += f"\nGitMap: {mapping.number}"
    body += f"\nGitMap-Type: {mapping.hierarchy_type}"

    return body


def create_hierarchy_issue(repository, mapping, milestone):
    """Create a GitHub Issue representing a Section or Feature."""

    return repository.create_issue(
        title=mapping.title,
        body=build_hierarchy_issue_body(mapping),
        milestone=milestone,
    )


def sync_hierarchy_issue(repository, mapping):
    """Create or update a Section or Feature GitHub Issue."""

    existing_issues = get_existing_issues(repository)
    existing = find_existing_issue(mapping, existing_issues)

    milestones = get_existing_milestones(repository)

    milestone_mapping = MilestoneMapping(
        number=mapping.number,
        title=mapping.milestone,
    )

    milestone = find_existing_milestone(
        milestone_mapping,
        milestones,
    )

    if existing:
        existing.edit(
            title=mapping.title,
            body=build_hierarchy_issue_body(mapping),
            milestone=milestone,
        )
        return existing, False

    issue = create_hierarchy_issue(
        repository,
        mapping,
        milestone,
    )

    return issue, True
