from dataclasses import dataclass

from PySide6.QtCore import QObject, Signal

from gitmap.gui.shared.error_log import log_exception

from gitmap.github_sync.issues.issue_lookup import find_github_issues_by_gitmap_ids, get_existing_issues
from gitmap.github_sync.planning.sync_plan import build_initial_sync_plan, build_sync_plan
from gitmap.github_sync.planning.sync_validation import validate_synchronization_plan
from gitmap.github_sync.repository.repository import RepositoryInfo, create_repository, verify_repository
from gitmap.github_sync.sync_progress import SyncProgressReporter


@dataclass
class SyncPreparation:
    repository: object
    plan: object
    removed_github_issues: list
    removed_github_hierarchy: list


class SyncPreparationWorker(QObject):
    """Prepare a GitHub synchronization without blocking the GUI thread."""

    progress = Signal(object, object)
    prepared = Signal(object)
    validation_failed = Signal(object)
    failed = Signal(str)

    def __init__(self, repository_name, create_new, username, roadmap, baseline_roadmap):
        super().__init__()
        self.repository_name = repository_name
        self.create_new = create_new
        self.username = username
        self.roadmap = roadmap
        self.baseline_roadmap = baseline_roadmap
        self.reporter = SyncProgressReporter(callback=self._report_progress)

    def _report_progress(self, event, history):
        self.progress.emit(event, history)

    def run(self):
        try:
            preparation = self._prepare()
        except Exception as error:
            log_exception(
                "GitHub synchronization preparation failed",
                error,
                diagnostic=f"Repository: {self.repository_name}",
            )
            self.failed.emit(str(error))
            return

        if preparation is not None:
            self.prepared.emit(preparation)

    def _prepare(self):
        if self.create_new:
            self.reporter.report("repository", 0, None, f"Creating GitHub repository {self.repository_name}...")
            repository = create_repository(self.repository_name)
            self.reporter.report("repository", 1, 1, f"Created GitHub repository {repository.full_name}.")
        else:
            self.reporter.report("repository", 0, None, f"Connecting to GitHub repository {self.repository_name}...")
            info = RepositoryInfo(username=self.username, repository=self.repository_name)
            repository = verify_repository(info)
            self.reporter.report("repository", 1, 1, f"Connected to GitHub repository {repository.full_name}.")

        self.reporter.report("inspection", 0, None, "Reading existing GitMap issues from GitHub...")
        existing_issues = get_existing_issues(repository, self.roadmap)
        self.reporter.report("inspection", 1, 1, f"Found {len(existing_issues)} existing GitMap issue(s).")

        self.reporter.report("planning", 0, None, "Building synchronization plan...")
        if not existing_issues:
            plan = build_initial_sync_plan(self.roadmap)
        else:
            plan = build_sync_plan(self.baseline_roadmap, self.roadmap)

        conflicts = validate_synchronization_plan(plan, self.roadmap, existing_issues)
        if conflicts:
            self.validation_failed.emit(conflicts)
            return None

        removed_issue_ids = plan["removed_issues"]
        removed_hierarchy_ids = plan["removed_hierarchy"]

        removed_github_issues = (
            find_github_issues_by_gitmap_ids(existing_issues, removed_issue_ids)
            if removed_issue_ids else []
        )
        removed_github_hierarchy = (
            find_github_issues_by_gitmap_ids(existing_issues, removed_hierarchy_ids)
            if removed_hierarchy_ids else []
        )

        self.reporter.report("planning", 1, 1, "Synchronization plan ready.")
        return SyncPreparation(repository, plan, removed_github_issues, removed_github_hierarchy)
