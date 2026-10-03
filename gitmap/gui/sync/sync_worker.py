from PySide6.QtCore import QObject, Signal

from gitmap.github_sync.issues.issue_sync import sync_issues
from gitmap.github_sync.issues.relationship_sync import sync_sub_issue_relationships
from gitmap.github_sync.issues.removed_issue_sync import sync_removed_issues
from gitmap.github_sync.metadata.label_sync import sync_labels
from gitmap.github_sync.metadata.milestone_sync import sync_milestones
from gitmap.github_sync.sync_progress import SyncProgressReporter


class SyncWorker(QObject):
    """Execute a prepared GitHub synchronization outside the GUI thread."""

    progress = Signal(object, object)
    finished = Signal(str)
    failed = Signal(str)

    def __init__(self, repository, roadmap, plan, removed_github_issues, removed_github_hierarchy):
        super().__init__()
        self.repository = repository
        self.roadmap = roadmap
        self.plan = plan
        self.removed_github_issues = removed_github_issues
        self.removed_github_hierarchy = removed_github_hierarchy
        self.reporter = SyncProgressReporter(
            overall_total=plan.total_operations,
            callback=self._report_progress,
        )

    def _report_progress(self, event, history):
        self.progress.emit(event, history)

    def run(self):
        try:
            self._execute()
        except Exception as error:
            self.failed.emit(str(error))
            return
        self.finished.emit(self.repository.full_name)

    def _execute(self):
        removed_ids = self.plan["removed_issues"] + self.plan["removed_hierarchy"]

        self.reporter.report("milestones", 0, None, "Synchronizing milestones...")
        sync_milestones(self.repository, self.roadmap)

        self.reporter.report("labels", 0, None, "Synchronizing labels...")
        sync_labels(self.repository, self.roadmap)

        if removed_ids:
            self.reporter.report("removals", 0, None, "Synchronizing removed items...")
            sync_removed_issues(self.removed_github_issues + self.removed_github_hierarchy)

        issues_to_sync = self.plan["added_issues"] + self.plan["changed_issues"]
        if issues_to_sync:
            self.reporter.report("normal_issues", 0, len(issues_to_sync), "Synchronizing GitHub issues...")
            sync_issues(
                self.repository,
                self.roadmap,
                issues_to_sync=issues_to_sync,
                update_issues=self.plan["changed_issues"],
                progress_total=len(issues_to_sync),
                progress_callback=self._normal_issue_progress,
            )

        if self.plan["added_hierarchy_mappings"]:
            mappings = self.plan["added_hierarchy_mappings"]
            self.reporter.report("hierarchy_create", 0, len(mappings), "Creating GitHub hierarchy items...")
            sync_issues(
                self.repository,
                self.roadmap,
                issues_to_sync=[],
                hierarchy_mappings_to_sync=mappings,
                hierarchy_expected_operation="create",
                progress_total=len(mappings),
                progress_callback=self._hierarchy_create_progress,
            )

        if self.plan["changed_hierarchy_mappings"]:
            mappings = self.plan["changed_hierarchy_mappings"]
            self.reporter.report("hierarchy_update", 0, len(mappings), "Updating GitHub hierarchy items...")
            sync_issues(
                self.repository,
                self.roadmap,
                issues_to_sync=[],
                hierarchy_mappings_to_sync=mappings,
                hierarchy_expected_operation="update",
                progress_total=len(mappings),
                progress_callback=self._hierarchy_update_progress,
            )

        self.reporter.report("relationships", 0, None, "Synchronizing GitHub relationships...")
        sync_sub_issue_relationships(self.repository, self.roadmap)

    def _normal_issue_progress(self, _stage, current, total, message):
        self.reporter.report("normal_issues", current, total, message)

    def _hierarchy_create_progress(self, _stage, current, total, message):
        self.reporter.report("hierarchy_create", current, total, message)

    def _hierarchy_update_progress(self, _stage, current, total, message):
        self.reporter.report("hierarchy_update", current, total, message)
