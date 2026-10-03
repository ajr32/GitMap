from gitmap.gui.application.ui_loader import load_ui


STAGES = [
    ("repository", "Repository"),
    ("inspection", "Inspection"),
    ("planning", "Planning"),
    ("milestones", "Milestones"),
    ("labels", "Labels"),
    ("removals", "Removals"),
    ("normal_issues", "Issues"),
    ("hierarchy", "Hierarchy"),
    ("relationships", "Relationships"),
]


def load_sync_progress_dialog():
    """Load and configure the GitHub synchronization progress dialog."""

    dialog = load_ui("sync_progress_dialog.ui", __file__)

    dialog.sync_stage_progress = {}
    
    dialog.close_button.clicked.connect(dialog.accept)

    dialog.sync_stage_states = {}
    dialog.sync_activity_count = 0
    dialog.sync_current_stage = None

    _initialize_stage_list(dialog)

    return dialog


def _initialize_stage_list(dialog):
    """Create the high-level synchronization stage checklist."""

    dialog.stages_list.clear()

    # hierarchy_create and hierarchy_update are displayed as one GUI stage.
    displayed = set()

    for stage, label in STAGES:
        display_stage = _display_stage(stage)

        if display_stage in displayed:
            continue

        displayed.add(display_stage)

        dialog.sync_stage_states[display_stage] = "waiting"
        dialog.stages_list.addItem(f"○ {label}")


def _display_stage(stage):
    """Map worker stages onto the stages displayed in the GUI."""

    if stage in ("hierarchy_create", "hierarchy_update"):
        return "hierarchy"

    return stage


def _stage_label(stage):
    """Return the user-facing name for a synchronization stage."""

    labels = {
        "repository": "Repository",
        "inspection": "Inspection",
        "planning": "Planning",
        "milestones": "Milestones",
        "labels": "Labels",
        "removals": "Removals",
        "normal_issues": "Issues",
        "hierarchy": "Hierarchy",
        "relationships": "Relationships",
    }

    return labels.get(stage, stage.replace("_", " ").title())


def _set_stage_state(dialog, stage, state):
    """Set one displayed stage to waiting, active, complete, or failed."""

    stage = _display_stage(stage)

    if stage not in dialog.sync_stage_states:
        return

    dialog.sync_stage_states[stage] = state

    symbols = {
        "waiting": "○",
        "active": "→",
        "complete": "✓",
        "failed": "✗",
    }

    row = 0
    displayed = set()

    for configured_stage, _label in STAGES:
        display_stage = _display_stage(configured_stage)

        if display_stage in displayed:
            continue

        displayed.add(display_stage)

        if display_stage == stage:
            item = dialog.stages_list.item(row)

            if item is not None:
                text = f"{symbols[state]} {_stage_label(stage)}"

                stage_progress = getattr(
                    dialog,
                    "sync_stage_progress",
                    {},
                ).get(stage)

                if stage_progress is not None:
                    current, total = stage_progress
                    text += f"    {current} / {total}"

                item.setText(text)

            return

        row += 1


def _activate_stage(dialog, stage):
    """Mark a newly reported stage as active."""

    stage = _display_stage(stage)
    previous = dialog.sync_current_stage

    if previous is not None and previous != stage:
        if dialog.sync_stage_states.get(previous) == "active":
            _set_stage_state(
                dialog,
                previous,
                "complete",
            )

    _set_stage_state(
        dialog,
        stage,
        "active",
    )

    dialog.sync_current_stage = stage


def _append_activity(dialog, history):
    """Append only activity entries not already displayed."""

    if history is None:
        return

    history = list(history)

    # The old reporter currently keeps only a short rolling history.
    # For Pass 1, append whatever new tail entries it supplies.
    if not history:
        return

    latest = history[-1]

    count = dialog.activity_list.count()

    if count > 0:
        previous = dialog.activity_list.item(count - 1)

        if previous is not None and previous.text() == latest:
            return

    dialog.activity_list.addItem(latest)
    dialog.activity_list.scrollToBottom()


def update_sync_progress(dialog, event, history):
    """Update the synchronization progress dialog from a progress event."""

    _activate_stage(
        dialog,
        event.stage,
    )
    if event.stage_total is not None:
        display_stage = _display_stage(event.stage)

        dialog.sync_stage_progress[display_stage] = (
            event.stage_current,
            event.stage_total,
        )

        state = "active"

        if event.stage_total == 0:
            state = "complete"
        elif event.stage_current >= event.stage_total:
            state = "complete"

        _set_stage_state(
            dialog,
            display_stage,
            state,
        )
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
        dialog.stage_progress.setRange(
            0,
            event.stage_total,
        )

        dialog.stage_progress.setValue(
            event.stage_current,
        )

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

    # ----- Activity -----

    _append_activity(
        dialog,
        history,
    )


def fail_current_sync_stage(dialog):
    """Mark the currently active synchronization stage as failed."""

    stage = dialog.sync_current_stage

    if stage is None:
        return

    _set_stage_state(
        dialog,
        stage,
        "failed",
    )


def finish_sync_progress(
    dialog,
    message="Synchronization complete.",
    successful=True,
):
    """Mark the synchronization progress dialog as finished."""

    dialog.status_label.setText(message)

    current_stage = dialog.sync_current_stage

    if current_stage is not None:
        if successful:
            _set_stage_state(
                dialog,
                current_stage,
                "complete",
            )
        else:
            _set_stage_state(
                dialog,
                current_stage,
                "failed",
            )

    if successful:
        if dialog.stage_progress.maximum() > 0:
            dialog.stage_progress.setValue(
                dialog.stage_progress.maximum()
            )

        dialog.overall_progress.setRange(0, 100)
        dialog.overall_progress.setValue(100)
        dialog.overall_progress.setFormat("%p%")

    dialog.close_button.setEnabled(True)