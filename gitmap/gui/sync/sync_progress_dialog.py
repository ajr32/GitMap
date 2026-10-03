from gitmap.gui.application.ui_loader import load_ui


def load_sync_progress_dialog():
    """Load and configure the GitHub synchronization progress dialog."""

    dialog = load_ui("sync_progress_dialog.ui", __file__)

    dialog.close_button.clicked.connect(dialog.accept)

    return dialog


def update_sync_progress(dialog, event, history):
    """Update the synchronization progress dialog from a progress event."""

    # ----- Live status line -----

    if event.stage_total is not None and event.stage_total > 0:
        dialog.status_label.setText(
            f"{event.message} — "
            f"{event.stage_current} of {event.stage_total}"
        )
    else:
        dialog.status_label.setText(event.message)

    # ----- Current stage -----

    if event.stage_total is None:
        dialog.stage_progress.setRange(0, 0)
        dialog.stage_progress.setFormat("")
    else:
        dialog.stage_progress.setRange(0, event.stage_total)
        dialog.stage_progress.setValue(event.stage_current)
        dialog.stage_progress.setFormat("%v / %m")

    # ----- Overall progress -----

    if event.overall_total is None or event.overall_total <= 0:
        dialog.overall_progress.setRange(0, 0)
        dialog.overall_progress.setFormat("")
    else:
        percent = round(
            (event.overall_current / event.overall_total) * 100
        )

        dialog.overall_progress.setRange(0, 100)
        dialog.overall_progress.setValue(percent)
        dialog.overall_progress.setFormat("%p%")

    # ----- Activity history -----

    scrollbar = dialog.activity_list.verticalScrollBar()

    # Remember whether the user was already at the bottom.
    was_at_bottom = scrollbar.value() >= scrollbar.maximum() - 2

    dialog.activity_list.clear()
    dialog.activity_list.addItems(history)

    # Follow new activity only if the user had not deliberately
    # scrolled upward to read older entries.
    if was_at_bottom:
        dialog.activity_list.scrollToBottom()


def finish_sync_progress(dialog, message="Synchronization complete."):
    """Mark the synchronization progress dialog as complete."""

    dialog.status_label.setText(message)

    if dialog.stage_progress.maximum() > 0:
        dialog.stage_progress.setValue(
            dialog.stage_progress.maximum()
        )

    dialog.overall_progress.setRange(0, 100)
    dialog.overall_progress.setValue(100)
    dialog.overall_progress.setFormat("%p%")

    dialog.close_button.setEnabled(True)