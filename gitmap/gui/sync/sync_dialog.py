
from PySide6.QtWidgets import QMessageBox

from gitmap.gui.application.ui_loader import load_ui


def load_sync_dialog():
    """Load the GitHub Sync dialog."""

    dialog = load_ui("sync_dialog.ui", __file__)

    # -------------------------------------------------------------------------
    # Repository Choice
    # -------------------------------------------------------------------------

    def update_repository_mode():
        if dialog.existing_repository.isChecked():
            dialog.repository_status.setText(
                "GitMap will connect to this existing repository."
            )
        else:
            dialog.repository_status.setText(
                "GitMap will create this repository on GitHub."
            )

    dialog.existing_repository.toggled.connect(update_repository_mode)

    dialog.new_repository.toggled.connect(update_repository_mode)

    update_repository_mode()

    # -------------------------------------------------------------------------
    # Cancel
    # -------------------------------------------------------------------------

    dialog.cancel_button.clicked.connect(dialog.reject)

    # -------------------------------------------------------------------------
    # Continue
    # -------------------------------------------------------------------------

    def continue_sync():
        repository = dialog.repository_name.text().strip()

        if not repository:
            QMessageBox.warning(
                dialog,
                "Repository Required",
                "Enter a GitHub repository name.",
            )
            return

        dialog.repository = repository
        dialog.create_repository = dialog.new_repository.isChecked()

        dialog.accept()

    dialog.continue_button.clicked.connect(continue_sync)

    return dialog
