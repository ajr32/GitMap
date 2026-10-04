"""Common graphical error reporting for GitMap."""

import logging
import traceback

from PySide6.QtWidgets import QMessageBox


logger = logging.getLogger(__name__)


def show_error(
    parent,
    title,
    message,
    *,
    error=None,
    diagnostic=None,
):
    """Show a friendly GUI error while preserving developer diagnostics.

    Args:
        parent: Parent Qt widget for the message box.
        title: Short title shown in the message box.
        message: User-facing explanation of what went wrong.
        error: Optional exception associated with the failure.
        diagnostic: Optional additional technical context.
    """

    details = []

    if diagnostic:
        details.append(str(diagnostic))

    if error is not None:
        details.append(f"{type(error).__name__}: {error}")

        # Keep the full traceback in normal diagnostic output/logging.
        logger.exception("%s: %s", title, message, exc_info=error)

        # logger.exception() is only useful when logging is configured, so
        # preserve the existing development-friendly console traceback too.
        traceback.print_exception(type(error), error, error.__traceback__)
    elif diagnostic:
        logger.error("%s: %s\n%s", title, message, diagnostic)

    box = QMessageBox(parent)
    box.setIcon(QMessageBox.Icon.Critical)
    box.setWindowTitle(title)
    box.setText(message)

    if details:
        box.setDetailedText("\n\n".join(details))

    box.exec()
