import copy

from PySide6.QtWidgets import QMessageBox


def cancel_changes(parent, baseline_roadmap):
    """Confirm cancellation and return the restored roadmap."""

    message_box = QMessageBox(parent)
    message_box.setWindowTitle("Cancel Changes?")
    message_box.setIcon(QMessageBox.Icon.Warning)

    message_box.setText(
        "This will discard all changes made since the roadmap was "
        "opened or last synced."
    )

    message_box.setInformativeText(
        "The original roadmap state will be restored. "
        "This cannot be undone."
    )

    keep_button = message_box.addButton(
        "Keep Changes",
        QMessageBox.ButtonRole.RejectRole,
    )

    cancel_button = message_box.addButton(
        "Remove Changes",
        QMessageBox.ButtonRole.DestructiveRole,
    )

    message_box.setDefaultButton(keep_button)
    message_box.exec()

    if message_box.clickedButton() is not cancel_button:
        return None

    return copy.deepcopy(baseline_roadmap)