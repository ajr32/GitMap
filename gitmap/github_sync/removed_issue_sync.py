from gitmap.github_sync.issue_sync import SynchronizationError


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
