from PySide6.QtCore import QObject, Signal

from gitmap.github_sync.issues.hierarchy_sync import collect_hierarchy_issue_mappings
from gitmap.github_sync.issues.issue_sync import sync_issues
from gitmap.github_sync.issues.relationship_sync import (
    count_desired_relationships,
    sync_sub_issue_relationships,
)
from gitmap.github_sync.issues.removed_issue_sync import sync_removed_issues
from gitmap.github_sync.metadata.label_sync import collect_label_mappings, sync_labels
from gitmap.github_sync.metadata.milestone_sync import sync_milestones
from gitmap.github_sync.sync_progress import SyncProgressReporter
from gitmap.github_sync.sync_results import SyncResultCollector
from gitmap.roadmap.model.traversal import iter_roadmap_issues


class SyncWorker(QObject):
    """Execute a prepared GitHub synchronization outside the GUI thread."""

    progress = Signal(object, object)
    results_ready = Signal(str, str)
    finished = Signal(str)
    failed = Signal(str)

    def __init__(
        self,
        repository,
        roadmap,
        plan,
        removed_github_issues,
        removed_github_hierarchy,
        log_directory,
    ):
        super().__init__()
        self.repository = repository
        self.roadmap = roadmap
        self.plan = plan
        self.removed_github_issues = removed_github_issues
        self.removed_github_hierarchy = removed_github_hierarchy
        self.log_directory = log_directory

        self.results = SyncResultCollector(
            roadmap_name=roadmap.name,
            repository_name=repository.full_name,
        )

        self.relationship_count = count_desired_relationships(roadmap)
        self.all_normal_issues = [
            issue
            for issue, _milestone, _section, _feature
            in iter_roadmap_issues(roadmap)
        ]
        self.all_hierarchy_mappings = collect_hierarchy_issue_mappings(roadmap)
        self.label_count = len(collect_label_mappings(roadmap))
        self.milestone_count = len(roadmap.milestones)
        self.removal_count = len(
            removed_github_issues + removed_github_hierarchy
        )

        base_total = (
            self.milestone_count
            + self.label_count
            + self.removal_count
            + len(self.all_normal_issues)
            + len(self.all_hierarchy_mappings)
            + self.relationship_count
        )

        self.reporter = SyncProgressReporter(
            overall_total=base_total,
            callback=self._report_progress,
        )

    def _report_progress(self, event, history):
        self.progress.emit(event, history)

    def _emit_results(self):
        """Save and expose the structured synchronization results."""
        try:
            path = self.results.save(self.log_directory)
            log_path = str(path)
        except Exception as error:
            self.results.failed("Log", "Save synchronization log", str(error))
            log_path = ""

        self.results_ready.emit(self.results.render(), log_path)

    def run(self):
        try:
            self._execute()
        except Exception as error:
            # Individual operations record their own failures where possible.
            # This entry guarantees that every terminal worker failure is visible.
            self.results.failed("Synchronization", "Synchronization stopped", str(error))
            self._emit_results()
            self.failed.emit(str(error))
            return

        self._emit_results()
        self.finished.emit(self.repository.full_name)

    def _execute(self):
        self._sync_milestones()
        self._sync_labels()
        self._sync_removals()
        self._sync_normal_issues()
        self._sync_hierarchy()
        self._sync_relationships()

    def _sync_milestones(self):
        total = self.milestone_count
        if total == 0:
            self.reporter.report("milestones", 0, 0, "No milestones to synchronize.")
            return

        self.reporter.report("milestones", 0, total, "Synchronizing milestones...")
        sync_milestones(
            self.repository,
            self.roadmap,
            progress_callback=self._milestone_progress,
            result_collector=self.results,
        )

    def _sync_labels(self):
        total = self.label_count
        if total == 0:
            self.reporter.report("labels", 0, 0, "No labels to synchronize.")
            return

        self.reporter.report("labels", 0, total, "Synchronizing labels...")
        sync_labels(
            self.repository,
            self.roadmap,
            progress_callback=self._label_progress,
            result_collector=self.results,
        )

    def _sync_removals(self):
        removed = self.removed_github_issues + self.removed_github_hierarchy
        total = len(removed)
        if total == 0:
            self.reporter.report("removals", 0, 0, "No removed items to synchronize.")
            return

        self.reporter.report("removals", 0, total, "Synchronizing removed items...")
        sync_removed_issues(
            removed,
            progress_total=total,
            progress_callback=self._removal_progress,
            result_collector=self.results,
        )

    def _sync_normal_issues(self):
        total = len(self.all_normal_issues)
        if total == 0:
            self.reporter.report("normal_issues", 0, 0, "No GitHub issues to synchronize.")
            return

        self.reporter.report("normal_issues", 0, total, "Checking GitHub issues...")

        added_ids = {id(issue) for issue in self.plan["added_issues"]}
        changed_ids = {id(issue) for issue in self.plan["changed_issues"]}
        issues_to_sync = self.plan["added_issues"] + self.plan["changed_issues"]
        sync_ids = added_ids | changed_ids
        current = 0

        for issue in self.all_normal_issues:
            if id(issue) in sync_ids:
                continue
            current += 1
            description = f"{issue.number} {issue.title}"
            self.results.skipped("Issue", description, "Unchanged")
            self.reporter.report(
                "normal_issues",
                current,
                total,
                f"Issue unchanged: {description}",
            )

        if not issues_to_sync:
            return

        self._normal_issue_offset = current
        sync_issues(
            self.repository,
            self.roadmap,
            issues_to_sync=issues_to_sync,
            update_issues=self.plan["changed_issues"],
            progress_total=len(issues_to_sync),
            progress_callback=self._normal_issue_progress,
            result_collector=self.results,
        )

    def _sync_hierarchy(self):
        total = len(self.all_hierarchy_mappings)
        if total == 0:
            self.reporter.report("hierarchy", 0, 0, "No hierarchy items to synchronize.")
            return

        self.reporter.report("hierarchy", 0, total, "Checking hierarchy items...")
        added = self.plan["added_hierarchy_mappings"]
        changed = self.plan["changed_hierarchy_mappings"]
        changed_ids = {
            mapping.gitmap_id
            for mapping in added + changed
            if mapping.gitmap_id
        }
        current = 0

        for mapping in self.all_hierarchy_mappings:
            if mapping.gitmap_id in changed_ids:
                continue
            current += 1
            description = f"{mapping.number} {mapping.title}"
            self.results.skipped("Hierarchy Issue", description, "Unchanged")
            self.reporter.report(
                "hierarchy",
                current,
                total,
                f"Hierarchy unchanged: {description}",
            )

        self._hierarchy_offset = current

        if added:
            self._hierarchy_phase_offset = self._hierarchy_offset
            sync_issues(
                self.repository,
                self.roadmap,
                issues_to_sync=[],
                hierarchy_mappings_to_sync=added,
                hierarchy_expected_operation="create",
                progress_total=len(added),
                progress_callback=self._hierarchy_progress,
                result_collector=self.results,
            )
            self._hierarchy_offset += len(added)

        if changed:
            self._hierarchy_phase_offset = self._hierarchy_offset
            sync_issues(
                self.repository,
                self.roadmap,
                issues_to_sync=[],
                hierarchy_mappings_to_sync=changed,
                hierarchy_expected_operation="update",
                progress_total=len(changed),
                progress_callback=self._hierarchy_progress,
                result_collector=self.results,
            )

    def _sync_relationships(self):
        total = self.relationship_count
        if total == 0:
            self.reporter.report("relationships", 0, 0, "No relationships to synchronize.")
            return

        self.reporter.report("relationships", 0, total, "Checking GitHub relationships...")
        sync_sub_issue_relationships(
            self.repository,
            self.roadmap,
            progress_callback=self._relationship_progress,
            result_collector=self.results,
        )

    def _milestone_progress(self, _stage, current, total, message):
        self.reporter.report("milestones", current, total, message)

    def _label_progress(self, _stage, current, total, message):
        self.reporter.report("labels", current, total, message)

    def _removal_progress(self, _stage, current, total, message):
        self.reporter.report("removals", current, total, message)

    def _normal_issue_progress(self, _stage, current, _total, message):
        self.reporter.report(
            "normal_issues",
            self._normal_issue_offset + current,
            len(self.all_normal_issues),
            message,
        )

    def _hierarchy_progress(self, _stage, current, _total, message):
        self.reporter.report(
            "hierarchy",
            self._hierarchy_phase_offset + current,
            len(self.all_hierarchy_mappings),
            message,
        )

    def _relationship_progress(self, _stage, current, total, message):
        self.reporter.report("relationships", current, total, message)
