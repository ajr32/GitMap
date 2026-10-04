from pathlib import Path

from PySide6.QtCore import QThread
from PySide6.QtWidgets import QMessageBox

from gitmap.gui.sync.sync_dialog import load_sync_dialog
from gitmap.gui.sync.sync_gui_handler import SyncGuiHandler
from gitmap.gui.sync.sync_preparation_worker import SyncPreparationWorker
from gitmap.gui.sync.sync_progress_dialog import load_sync_progress_dialog
from gitmap.gui.sync.sync_worker import SyncWorker
from gitmap.settings import load_github_username


def _sync_log_directory(state):
    """Return the per-roadmap synchronization log directory."""
    if state.active_roadmap_path:
        return Path(state.active_roadmap_path).parent / ".gitmap" / "sync_logs"
    return Path.cwd() / ".gitmap" / "sync_logs"


def run_github_sync(parent, state):
    """Start GitHub synchronization without blocking the GUI thread."""
    dialog = load_sync_dialog()
    if not dialog.exec():
        return

    repository_name = dialog.repository
    create_new = dialog.create_repository
    username = load_github_username()

    if not username:
        QMessageBox.warning(
            parent,
            "GitHub Settings Required",
            "Open Settings and enter your GitHub username first.",
        )
        return

    progress_dialog = load_sync_progress_dialog()
    progress_dialog.show()

    gui_handler = SyncGuiHandler(
        parent=parent,
        progress_dialog=progress_dialog,
        sync_complete_callback=state.refresh_main_roadmap,
    )
    progress_dialog.sync_gui_handler = gui_handler

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

    worker.progress.connect(gui_handler.update_progress)
    worker.prepared.connect(gui_handler.preparation_complete)
    worker.validation_failed.connect(gui_handler.validation_failed)
    worker.failed.connect(gui_handler.preparation_failed)

    worker.prepared.connect(thread.quit)
    worker.validation_failed.connect(thread.quit)
    worker.failed.connect(thread.quit)

    thread.finished.connect(worker.deleteLater)
    thread.finished.connect(thread.deleteLater)

    def start_sync_after_preparation():
        preparation = gui_handler.completed_preparation
        if preparation is None:
            return
        _start_sync_worker(
            parent,
            state,
            progress_dialog,
            gui_handler,
            preparation,
        )

    thread.finished.connect(start_sync_after_preparation)
    thread.started.connect(worker.run)
    thread.start()


def _start_sync_worker(
    parent,
    state,
    progress_dialog,
    gui_handler,
    preparation,
):
    """Start the mutation phase after preparation and confirmation."""
    worker = SyncWorker(
        repository=preparation.repository,
        roadmap=state.active_roadmap,
        plan=preparation.plan,
        removed_github_issues=preparation.removed_github_issues,
        removed_github_hierarchy=preparation.removed_github_hierarchy,
        log_directory=_sync_log_directory(state),
    )

    thread = QThread(parent)
    worker.moveToThread(thread)
    progress_dialog.sync_thread = thread
    progress_dialog.sync_worker = worker

    worker.progress.connect(gui_handler.update_progress)
    worker.results_ready.connect(gui_handler.display_results)
    worker.finished.connect(gui_handler.sync_finished)
    worker.failed.connect(gui_handler.sync_failed)

    worker.finished.connect(thread.quit)
    worker.failed.connect(thread.quit)

    thread.finished.connect(worker.deleteLater)
    thread.finished.connect(thread.deleteLater)
    thread.started.connect(worker.run)
    thread.start()
