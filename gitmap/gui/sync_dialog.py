from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMessageBox


def load_sync_dialog():
    """Load the GitHub Sync dialog."""

    ui_path = Path(__file__).with_name("sync_dialog.ui")

    ui_file = QFile(str(ui_path))

    if not ui_file.open(QFile.ReadOnly):
        raise RuntimeError(f"Unable to open Sync UI: {ui_path}")

    loader = QUiLoader()
    dialog = loader.load(ui_file)

    ui_file.close()

    if dialog is None:
        raise RuntimeError(f"Unable to load Sync UI: {ui_path}")

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
