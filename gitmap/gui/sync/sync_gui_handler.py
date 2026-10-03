from PySide6.QtCore import QObject, Slot
from PySide6.QtWidgets import QMessageBox

from gitmap.gui.dialogs.removal_confirmation import confirm_sync_removals
from gitmap.gui.sync.sync_progress_dialog import (
    fail_current_sync_stage,
    finish_sync_progress,
    update_sync_progress,
)


class SyncGuiHandler(QObject):
    """
    Handle worker signals on the GUI thread.

    Background synchronization workers should emit data only.
    All interaction with Qt widgets and dialogs happens here.
    """

    def __init__(
        self,
        parent,
        progress_dialog,
        preparation_complete_callback=None,
    ):
        super().__init__(parent)

        self.parent_widget = parent
        self.progress_dialog = progress_dialog
        self.preparation_complete_callback = preparation_complete_callback
        self.completed_preparation = None

    @Slot(object, object)
    def update_progress(self, event, history):
        """Display a worker progress event."""
        update_sync_progress(
            self.progress_dialog,
            event,
            history,
        )

    @Slot(str)
    def preparation_failed(self, message):
	    """Handle failure while preparing synchronization."""

	    fail_current_sync_stage(self.progress_dialog)

	    finish_sync_progress(
		    self.progress_dialog,
		    "Synchronization preparation failed.",
		    successful=False,
	    )

	    QMessageBox.critical(
		    self.parent_widget,
		    "GitHub Sync Failed",
		    message,
	    )

    @Slot(object)
    def validation_failed(self, conflicts):
        """Display synchronization-plan validation problems."""
        finish_sync_progress(
            self.progress_dialog,
            "Synchronization validation failed.",
        )

        QMessageBox.critical(
            self.parent_widget,
            "GitHub Sync Validation Failed",
            "GitMap found problems that must be fixed before "
            "synchronization can continue:\n\n"
            + "\n".join(f"• {conflict}" for conflict in conflicts),
        )

    @Slot(object)
    def preparation_complete(self, preparation):
        """Handle a successfully prepared synchronization."""
        removed_items = (
            preparation.removed_github_issues
            + preparation.removed_github_hierarchy
        )

        if removed_items:
            confirmed = confirm_sync_removals(
                self.parent_widget,
                preparation.removed_github_issues,
                preparation.removed_github_hierarchy,
            )

            if not confirmed:
                finish_sync_progress(
                    self.progress_dialog,
                    "Synchronization cancelled.",
                )
                return

        self.completed_preparation = preparation

    @Slot(str)
    def sync_finished(self, repository_full_name):
	    """Handle successful synchronization."""

	    finish_sync_progress(
		    self.progress_dialog,
		    f"Synchronization complete: {repository_full_name}",
	    )

	    # Keep the completed progress dialog visible until the user closes it.
	    self.progress_dialog.raise_()
	    self.progress_dialog.activateWindow()

    @Slot(str)
    def sync_failed(self, message):
	    """Handle failure during synchronization."""

	    fail_current_sync_stage(self.progress_dialog)

	    finish_sync_progress(
		    self.progress_dialog,
		    "Synchronization failed.",
		    successful=False,
	    )

	    QMessageBox.critical(
		    self.parent_widget,
		    "GitHub Sync Failed",
		    message,
	    )