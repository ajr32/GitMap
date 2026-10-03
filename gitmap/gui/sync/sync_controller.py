from PySide6.QtCore import QThread
from PySide6.QtWidgets import QMessageBox

from gitmap.gui.dialogs.removal_confirmation import confirm_sync_removals
from gitmap.gui.sync.sync_dialog import load_sync_dialog
from gitmap.gui.sync.sync_preparation_worker import SyncPreparationWorker
from gitmap.gui.sync.sync_progress_dialog import finish_sync_progress, load_sync_progress_dialog, update_sync_progress
from gitmap.gui.sync.sync_worker import SyncWorker
from gitmap.settings import load_github_username


def run_github_sync(parent, state):
    """Start GitHub synchronization without blocking the GUI thread."""

    dialog = load_sync_dialog()
    if not dialog.exec():
        return

    repository_name = dialog.repository
    create_new = dialog.create_repository
    username = load_github_username()

    if not username:
        QMessageBox.warning(parent, "GitHub Settings Required", "Open Settings and enter your GitHub username first.")
        return

    progress_dialog = load_sync_progress_dialog()
    progress_dialog.show()

    worker = SyncPreparationWorker(
        repository_name=repository_name,
        create_new=create_new,
        username=username,
        roadmap=state.active_roadmap,
        baseline_roadmap=state.review_baseline_roadmap,
    )
    thread = QThread(parent)
    worker.moveToThread(thread)

    progress_dialog.preparation_thread = thread
    progress_dialog.preparation_worker = worker

    worker.progress.connect(lambda event, history: update_sync_progress(progress_dialog, event, history))

    def preparation_failed(message):
        finish_sync_progress(progress_dialog, "Synchronization preparation failed.")
        QMessageBox.critical(parent, "GitHub Sync Failed", message)

    def validation_failed(conflicts):
        finish_sync_progress(progress_dialog, "Synchronization validation failed.")
        QMessageBox.critical(
            parent,
            "GitHub Sync Validation Failed",
            "GitMap found problems that must be fixed before synchronization can continue:\n\n"
            + "\n".join(f"• {conflict}" for conflict in conflicts),
        )

    def preparation_complete(preparation):
        removed_items = preparation.removed_github_issues + preparation.removed_github_hierarchy
        if removed_items and not confirm_sync_removals(
            parent,
            preparation.removed_github_issues,
            preparation.removed_github_hierarchy,
        ):
            finish_sync_progress(progress_dialog, "Synchronization cancelled.")
            return

        _start_sync_worker(parent, state, progress_dialog, preparation)

    worker.prepared.connect(preparation_complete)
    worker.validation_failed.connect(validation_failed)
    worker.failed.connect(preparation_failed)

    worker.prepared.connect(thread.quit)
    worker.validation_failed.connect(thread.quit)
    worker.failed.connect(thread.quit)

    thread.finished.connect(worker.deleteLater)
    thread.finished.connect(thread.deleteLater)
    thread.started.connect(worker.run)
    thread.start()


def _start_sync_worker(parent, state, progress_dialog, preparation):
    """Start the mutation phase after preparation and confirmation."""

    worker = SyncWorker(
        repository=preparation.repository,
        roadmap=state.active_roadmap,
        plan=preparation.plan,
        removed_github_issues=preparation.removed_github_issues,
        removed_github_hierarchy=preparation.removed_github_hierarchy,
    )
    thread = QThread(parent)
    worker.moveToThread(thread)

    progress_dialog.sync_thread = thread
    progress_dialog.sync_worker = worker

    worker.progress.connect(lambda event, history: update_sync_progress(progress_dialog, event, history))

    def sync_finished(repository_full_name):
        finish_sync_progress(progress_dialog, "Synchronization complete.")
        QMessageBox.information(
            parent,
            "GitHub Sync Complete",
            f"GitMap successfully synchronized with:\n\n{repository_full_name}",
        )

    def sync_failed(message):
        finish_sync_progress(progress_dialog, "Synchronization failed.")
        QMessageBox.critical(parent, "GitHub Sync Failed", message)

    worker.finished.connect(sync_finished)
    worker.failed.connect(sync_failed)
    worker.finished.connect(thread.quit)
    worker.failed.connect(thread.quit)
    thread.finished.connect(worker.deleteLater)
    thread.finished.connect(thread.deleteLater)
    thread.started.connect(worker.run)
    thread.start()
