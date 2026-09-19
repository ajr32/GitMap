# =============================================================================
# GITMAP GUI DIALOGS
# =============================================================================
# Shared confirmation and preview dialogs used by the GitMap desktop GUI.
# Business logic stays outside this file; dialogs only present information
# and return the user's choice.
# =============================================================================

from PySide6.QtWidgets import QMessageBox


# =============================================================================
# PART A — NUMBERING CHANGE PREVIEW
# =============================================================================
def confirm_numbering_changes(parent, changes):
    """Show proposed numbering changes and return True when approved."""

    if not changes:
        return True

    lines = []

    for change in changes:
        title = change["title"]
        old_number = change["old_number"]
        new_number = change["new_number"]

        lines.append(
            f"{old_number} {title}  →  {new_number} {title}"
        )

    message = "\n".join(lines)

    message_box = QMessageBox(parent)

    message_box.setWindowTitle("Numbering Changes")
    message_box.setIcon(QMessageBox.Icon.Question)

    message_box.setText(
        "<b>This particular change would cause the following "
        "items to be renumbered:</b>"
    )

    message_box.setInformativeText(
        f"{message}\n\n"
        "Be sure to click Save or Save &amp; Exit to lock these "
        "changes to your roadmap.\n\n"
        "Apply this change?"
    )

    message_box.setStandardButtons(
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
    )

    message_box.setDefaultButton(QMessageBox.StandardButton.No)

    result = message_box.exec()

    return result == QMessageBox.StandardButton.Yes