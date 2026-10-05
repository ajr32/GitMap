"""Common graphical error reporting for GitMap."""

from PySide6.QtWidgets import QMessageBox

from gitmap.gui.shared.error_log import log_error, log_exception


def show_error(
    parent,
    title,
    message,
    *,
    error=None,
    diagnostic=None,
):
    """Show a friendly GUI error while preserving developer diagnostics."""
    if error is not None:
        log_exception(title, error, diagnostic=diagnostic)
    elif diagnostic:
        log_error(title, diagnostic=diagnostic)

    details = []

    if diagnostic:
        details.append(str(diagnostic))

    if error is not None:
        details.append(f"{type(error).__name__}: {error}")

    box = QMessageBox(parent)
    box.setIcon(QMessageBox.Icon.Critical)
    box.setWindowTitle(title)
    box.setText(message)

    if details:
        box.setDetailedText("\n\n".join(details))

    box.exec()
