def get_existing_issues(repository, roadmap=None):
    """Retrieve GitMap-managed issues from a GitHub repository."""

    issues = [
        issue
        for issue in repository.get_issues(state="all")
        if is_gitmap_managed_issue(issue)
    ]

    if roadmap is None:
        return issues

    roadmap_label = f"GitMap: {roadmap.name}"

    return [
        issue
        for issue in issues
        if any(
            label.name.casefold() == roadmap_label.casefold() for label in issue.labels
        )
    ]


def has_existing_gitmap_issues(repository):
    """Return whether the repository already contains synchronized GitMap issues."""

    return bool(get_existing_issues(repository))

def find_github_issues_by_gitmap_ids(existing_issues, gitmap_ids):
    """Find GitMap-managed GitHub Issues by permanent GitMap ID."""

    wanted_ids = set(gitmap_ids)
    matches = []

    for issue in existing_issues:
        gitmap_id = get_gitmap_id_from_github_issue(issue)

        if gitmap_id in wanted_ids:
            matches.append(issue)

    return matches

def get_gitmap_id_from_github_issue(issue) -> str:
    """Return the permanent GitMap ID stored in a GitHub issue body."""

    body = issue.body or ""

    for line in body.splitlines():
        if line.startswith("GitMap-ID:"):
            return line.removeprefix("GitMap-ID:").strip()

    return ""


def find_github_issue_by_gitmap_id(gitmap_id, existing_issues):
    """Find a GitHub Issue by its permanent GitMap ID."""

    if not gitmap_id:
        return None

    for issue in existing_issues:
        if get_gitmap_id_from_github_issue(issue) == gitmap_id:
            return issue

    return None


def find_existing_issue_by_gitmap_id(mapping, existing_issues):
    """Find an existing GitHub issue by permanent GitMap ID."""

    return find_github_issue_by_gitmap_id(
        mapping.gitmap_id,
        existing_issues,
    )


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
        for line in (issue.body or "").splitlines():
            if line.strip() == marker:
                return issue
    return None


def find_all_existing_issue_matches(mapping, existing_issues):
    """Return all GitHub issues that could represent a GitMap mapping."""

    matches = []

    for issue in existing_issues:
        body = issue.body or ""

        gitmap_id = get_gitmap_id_from_github_issue(issue)

        id_matches = mapping.gitmap_id and gitmap_id == mapping.gitmap_id

        number_matches = any(
            line.strip() == f"GitMap: {mapping.number}" for line in body.splitlines()
        )

        if id_matches or number_matches:
            matches.append(issue)

    return matches


def classify_existing_issue(mapping, existing_issues):
    """Classify a GitMap mapping as existing, missing, or conflicting."""

    matches = find_all_existing_issue_matches(
        mapping,
        existing_issues,
    )

    if not matches:
        return "missing", []

    if len(matches) == 1:
        return "existing", matches

    return "conflict", matches


def is_gitmap_managed_issue(issue):
    """Return True if the GitHub issue is managed by GitMap."""

    body = issue.body or ""

    return "GitMap-ID:" in body or "GitMap:" in body

