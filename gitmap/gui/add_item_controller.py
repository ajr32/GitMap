# =============================================================================
# GITMAP ADD ITEM CONTROLLER
# =============================================================================
# Owns the Editor's Add workflow. app.py supplies the active Editor/Preview
# objects and keeps the main-window/editor lifecycle wiring.
# =============================================================================

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QPushButton, QTreeWidgetItem

from gitmap.models import Feature, Issue, Milestone, Section
from gitmap.roadmap_numbering import generate_issue_number


# =============================================================================
# PART A — VALID ADD TYPES
# =============================================================================
def get_valid_add_types(model, roadmap):
    """Return the item types that may be added from the selected model."""

    if isinstance(model, Issue):
        return ["Issue", "Requirement", "Work Step"]

    if isinstance(model, Feature):
        return ["Feature", "Issue"]

    if isinstance(model, Section):
        choices = ["Section"]

        if roadmap.use_features:
            choices.append("Feature")

        if roadmap.allow_issues_under_sections:
            choices.append("Issue")

        return choices

    if isinstance(model, Milestone):
        choices = ["Milestone"]

        if roadmap.use_sections:
            choices.append("Section")

        if not roadmap.use_sections:
            choices.append("Issue")

        return choices

    return []


# =============================================================================
# PART B — SIBLING POSITION CHOICE
# =============================================================================
def show_sibling_position_choices(dialog, item_type):
    """Change the Add popup from item-type choices to Before / After."""

    for option in dialog.add_options:
        option.setAutoExclusive(False)

    for option in dialog.add_options:
        option.setChecked(False)

    dialog.add_options[0].setText("Before")
    dialog.add_options[1].setText("After")

    for option in dialog.add_options:
        option.setAutoExclusive(True)

    dialog.add_question_label.setText(
        f"Add {item_type} before or after this {item_type}?"
    )

    dialog.add_options[0].show()
    dialog.add_options[1].show()
    dialog.add_options[2].hide()
    dialog.add_options[3].hide()


# =============================================================================
# PART C — ADD DRAFT STATE
# =============================================================================
def _disconnect_placeholder_title_signal(item_editor_window):
    """Disconnect the active draft placeholder title callback, if any."""

    callback = getattr(item_editor_window, "add_placeholder_title_callback", None)

    if callback is not None:
        try:
            item_editor_window.item_title.textChanged.disconnect(callback)
        except (RuntimeError, TypeError):
            pass

    item_editor_window.add_placeholder_title_callback = None


def never_mind_add(
    item_editor_window,
    never_mind_button,
    set_add_draft_actions_visible,
    preview_text,
    context_tree,
):
    """Abandon only the current Add draft."""

    # Save the model, not the QTreeWidgetItem. Refreshes/removals can delete
    # QTreeWidgetItems even though Python still has a reference to them.
    reference_model = getattr(item_editor_window, "add_reference_model", None)

    _disconnect_placeholder_title_signal(item_editor_window)

    placeholder = getattr(item_editor_window, "add_placeholder", None)

    if placeholder is not None:
        try:
            parent_item = placeholder.parent()

            if parent_item is not None:
                parent_item.removeChild(placeholder)
            else:
                # A Milestone draft can be a top-level Preview item.
                placeholder_index = preview_text.indexOfTopLevelItem(placeholder)

                if placeholder_index >= 0:
                    preview_text.takeTopLevelItem(placeholder_index)

        except RuntimeError:
            # The tree may already have been refreshed and deleted the item.
            pass

    item_editor_window.add_mode = False
    item_editor_window.add_question_stage = None
    item_editor_window.add_selected_type = None
    item_editor_window.add_selected_position = None
    item_editor_window.add_new_model = None
    item_editor_window.add_placeholder = None
    item_editor_window.add_parent_model = None
    item_editor_window.add_siblings = None
    item_editor_window.add_insert_index = None
    item_editor_window.add_reference = None

    never_mind_button.hide()
    set_add_draft_actions_visible(True)

    # Re-find the current tree item by its surviving model object instead of
    # selecting a possibly deleted QTreeWidgetItem.
    if reference_model is not None and hasattr(item_editor_window, "select_preview_model"):
        item_editor_window.select_preview_model(reference_model)

    context_tree.clear()


def finish_add(item_editor_window, never_mind_button, set_add_draft_actions_visible):
    """Restore normal Editor actions after a successful Add."""

    _disconnect_placeholder_title_signal(item_editor_window)

    never_mind_button.hide()
    set_add_draft_actions_visible(True)
    item_editor_window.add_selected_type = None
    item_editor_window.add_placeholder = None


# =============================================================================
# PART D — ADD POPUP / MODE
# =============================================================================
def open_add_dialog(item_editor_window):
    """Reset, position, and show the Add decision popup."""

    dialog = item_editor_window.add_item_dialog

    cancel_button = dialog.findChild(QPushButton, "add_cancel_button")

    if getattr(item_editor_window, "add_cancel_callback", None) is None:
        def cancel_add_mode():
            item_editor_window.add_mode = False
            dialog.close()

        item_editor_window.add_cancel_callback = cancel_add_mode
        cancel_button.clicked.connect(item_editor_window.add_cancel_callback)

    dialog.add_question_label.setText("Select an item in Preview.")

    for option in dialog.add_options:
        option.hide()

    editor_pos = item_editor_window.pos()
    dialog.move(editor_pos.x() + 470, editor_pos.y())
    dialog.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
    dialog.show()


def start_add_mode(item_editor_window, preview_text):
    """Enter Add mode and wait for a Preview reference selection."""

    item_editor_window.add_mode = True
    item_editor_window.add_question_stage = None
    item_editor_window.add_placeholder_title_callback = None
    item_editor_window.add_item_dialog.add_continue_button.setText("Continue")

    open_add_dialog(item_editor_window)

    current_item = preview_text.currentItem()

    if current_item is not None:
        preview_text.setCurrentItem(None)


# =============================================================================
# PART E — ADD CHOICE PRESENTATION
# =============================================================================
def show_add_type_choices(
    item_editor_window,
    model,
    roadmap,
    get_item_type,
):
    """Populate the Add popup for the selected Preview reference."""

    dialog = item_editor_window.add_item_dialog
    choices = get_valid_add_types(model, roadmap)

    dialog.add_question_label.setText("What would you like to add?")

    for index, option in enumerate(dialog.add_options):
        if index < len(choices):
            option.setText(choices[index])
            option.show()
        else:
            option.hide()

    def add_type_selected(selected_option):
        selected_type = selected_option.text()

        if selected_type in ("Before", "After"):
            item_editor_window.add_selected_position = selected_type
            dialog.add_continue_button.setText("Add")
            return

        reference_type = get_item_type(item_editor_window.add_reference_model)

        if selected_type != reference_type:
            dialog.add_continue_button.setText("Add")
        else:
            dialog.add_continue_button.setText("Continue")

    # Existing behavior intentionally preserved here. Signal cleanup can be a
    # separate tested refactor if it ever causes duplicate callbacks.
    for option in dialog.add_options:
        option.clicked.connect(
            lambda checked=False, button=option: add_type_selected(button)
        )


# =============================================================================
# PART F — CONTINUE / CREATE ADD DRAFT
# =============================================================================
def continue_add_item(
    item_editor_window,
    never_mind_button,
    set_add_draft_actions_visible,
    preview_text,
    model_role,
    get_item_type,
):

    """Advance the Add popup or create the selected in-memory draft."""

    if getattr(item_editor_window, "add_question_stage", None) == "position":
        selected_position = next(
            (
                option
                for option in item_editor_window.add_item_dialog.add_options
                if option.isChecked()
            ),
            None,
        )

        if selected_position is None:
            return

        position = selected_position.text()
        item_editor_window.add_selected_position = position
        item_editor_window.add_question_stage = "ready"

        item_editor_window.item_type_label.setText(
            f"Adding {item_editor_window.add_selected_type}"
        )

        if item_editor_window.add_selected_type in ("Feature", "Section", "Milestone"):
            item_editor_window.item_description.hide()
            item_editor_window.description_label.hide()
            item_editor_window.item_require.hide()
            item_editor_window.require_label.hide()
            item_editor_window.item_work_step.hide()
            item_editor_window.work_step_label.hide()

        never_mind_button.show()
        set_add_draft_actions_visible(False)

        item_editor_window.item_title.clear()
        item_editor_window.item_description.clear()
        item_editor_window.item_require.clear()
        item_editor_window.item_work_step.clear()

        reference_item = item_editor_window.add_reference

        # ---------------------------------------------------------------------
        # PART F1 — RESOLVE SIBLING CONTAINER
        # ---------------------------------------------------------------------
        # Milestones are top-level Preview items. They do not have a model-backed
        # parent item, so use the Roadmap's milestone list directly.
        # ---------------------------------------------------------------------
        if item_editor_window.add_selected_type == "Milestone":
            # Milestones are children of the visible Roadmap root item.
            parent_item = reference_item.parent()
            parent_model = item_editor_window.roadmap
            item_editor_window.add_parent_model = parent_model
            item_editor_window.add_siblings = item_editor_window.roadmap.milestones

        else:
            parent_item = reference_item.parent()
            parent_model = parent_item.data(0, model_role)
            item_editor_window.add_parent_model = parent_model

            if item_editor_window.add_selected_type == "Feature":
                item_editor_window.add_siblings = parent_model.features

            elif item_editor_window.add_selected_type == "Section":
                item_editor_window.add_siblings = parent_model.sections

            else:
                item_editor_window.add_siblings = parent_model.issues

        placeholder = QTreeWidgetItem(
            [f"[New {item_editor_window.add_selected_type}]"]
        )
        item_editor_window.add_placeholder = placeholder

        title_field = item_editor_window.item_title

        def update_add_placeholder_title(text):
            if text.strip():
                placeholder.setText(0, f"[{text.strip()}]")
            else:
                placeholder.setText(
                    0, f"[New {item_editor_window.add_selected_type}]"
                )

        _disconnect_placeholder_title_signal(item_editor_window)
        item_editor_window.add_placeholder_title_callback = update_add_placeholder_title
        title_field.textChanged.connect(
            item_editor_window.add_placeholder_title_callback
        )

        if item_editor_window.add_selected_type in ("Feature", "Section", "Milestone"):
            placeholder.setForeground(0, QColor("#F6DF4F"))
            font = placeholder.font(0)
            font.setBold(True)
            placeholder.setFont(0, font)

        if parent_item is not None:
            reference_index = parent_item.indexOfChild(reference_item)

            if item_editor_window.add_selected_position == "Before":
                insert_index = reference_index
            else:
                insert_index = reference_index + 1

            if item_editor_window.add_selected_type == "Issue":
                new_model = Issue(number="", title="")

            elif item_editor_window.add_selected_type == "Feature":
                new_model = Feature(number="", title="")

            elif item_editor_window.add_selected_type == "Section":
                new_model = Section(number="", title="")

            elif item_editor_window.add_selected_type == "Milestone":
                new_model = Milestone(number="", title="")

            else:
                return

            item_editor_window.add_new_model = new_model
            item_editor_window.add_insert_index = insert_index

            if item_editor_window.add_selected_type == "Milestone":
                reference_number = item_editor_window.add_reference_model.number
                milestone_series, reference_sibling = reference_number.rsplit(".", 1)

                reference_sibling = int(reference_sibling)

                if item_editor_window.add_selected_position == "Before":
                    proposed_sibling = reference_sibling
                else:
                    proposed_sibling = reference_sibling + 1

                proposed_number = f"{milestone_series}.{proposed_sibling}"

            else:
                parent_type = get_item_type(parent_model).lower()

                if item_editor_window.add_selected_type == "Issue":
                    proposed_number = generate_issue_number(
                        parent_model.number,
                        parent_type,
                        insert_index + 1,
                    )
                else:
                    proposed_number = f"{parent_model.number}.{insert_index + 1}"

            item_editor_window.item_number.setText(proposed_number)
            parent_item.insertChild(insert_index, placeholder)
            item_editor_window.add_mode = False
            preview_text.setCurrentItem(placeholder)

            item_editor_window.add_item_dialog.close()
            return

    selected_option = next(
        (
            option
            for option in item_editor_window.add_item_dialog.add_options
            if option.isChecked()
        ),
        None,
    )

    if selected_option is None:
        return

    selected_type = selected_option.text()
    item_editor_window.add_selected_type = selected_type

    reference_model = item_editor_window.add_reference_model
    reference_type = get_item_type(reference_model)

    if selected_type == reference_type:
        show_sibling_position_choices(
            item_editor_window.add_item_dialog,
            selected_type,
        )
        item_editor_window.add_question_stage = "position"
        return

    item_editor_window.add_selected_position = "child"
    item_editor_window.add_parent_model = reference_model
    item_editor_window.add_question_stage = "ready"

    # -------------------------------------------------------------------------
    # PART F2 — CREATE STRUCTURAL CHILD DRAFT
    # -------------------------------------------------------------------------
    # Child additions append beneath the selected parent. Unlike sibling
    # insertion, they do not need a Before / After question.
    # -------------------------------------------------------------------------
    if (
        (selected_type == "Section" and isinstance(reference_model, Milestone))
        or (selected_type == "Feature" and isinstance(reference_model, Section))
        or (
            selected_type == "Issue"
            and isinstance(reference_model, (Milestone, Section, Feature))
        )
    ):
        item_editor_window.item_type_label.setText(f"Adding {selected_type}")
        item_editor_window.add_parent_model = reference_model

        if selected_type == "Section":
            siblings = reference_model.sections
            new_model = Section(number="", title="")
            proposed_number = f"{reference_model.number}.{len(siblings) + 1}"

        elif selected_type == "Feature":
            siblings = reference_model.features
            new_model = Feature(number="", title="")
            proposed_number = f"{reference_model.number}.{len(siblings) + 1}"

        else:
            siblings = reference_model.issues
            new_model = Issue(number="", title="")

            proposed_number = generate_issue_number(
                reference_model.number,
                get_item_type(reference_model).lower(),
                len(siblings) + 1,
            )

        item_editor_window.add_siblings = siblings
        item_editor_window.add_insert_index = len(siblings)
        item_editor_window.add_new_model = new_model

        item_editor_window.item_number.setText(proposed_number)
        item_editor_window.item_title.clear()
        item_editor_window.item_description.clear()

        if selected_type == "Issue":
            item_editor_window.item_description.show()
            item_editor_window.description_label.show()
        else:
            item_editor_window.item_description.hide()
            item_editor_window.description_label.hide()

        item_editor_window.item_require.hide()
        item_editor_window.require_label.hide()
        item_editor_window.item_work_step.hide()
        item_editor_window.work_step_label.hide()

        reference_item = item_editor_window.add_reference

        placeholder = QTreeWidgetItem([f"[New {selected_type}]"])
        item_editor_window.add_placeholder = placeholder

        if selected_type in ("Section", "Feature"):
            placeholder.setForeground(0, QColor("#F6DF4F"))
            font = placeholder.font(0)
            font.setBold(True)
            placeholder.setFont(0, font)

        reference_item.addChild(placeholder)
        reference_item.setExpanded(True)

        def update_child_placeholder_title(text):
            if text.strip():
                placeholder.setText(0, f"[{text.strip()}]")
            else:
                placeholder.setText(0, f"[New {selected_type}]")

        _disconnect_placeholder_title_signal(item_editor_window)
        item_editor_window.add_placeholder_title_callback = (
            update_child_placeholder_title
        )
        item_editor_window.item_title.textChanged.connect(
            item_editor_window.add_placeholder_title_callback
        )

        never_mind_button.show()
        set_add_draft_actions_visible(False)

        item_editor_window.add_mode = False
        preview_text.setCurrentItem(placeholder)

        item_editor_window.add_item_dialog.close()
        return

    if selected_type == "Requirement":
        item_editor_window.item_type_label.setText("Adding Requirement")
        item_editor_window.add_parent_model = reference_model
        item_editor_window.item_require.setVisible(True)
        item_editor_window.require_label.setVisible(True)
        item_editor_window.item_require.clear()
        never_mind_button.show()
        set_add_draft_actions_visible(False)
        item_editor_window.add_item_dialog.close()
        return

    if selected_type == "Work Step":
        item_editor_window.item_type_label.setText("Adding Work Step")
        item_editor_window.add_parent_model = reference_model
        item_editor_window.item_work_step.setVisible(True)
        item_editor_window.work_step_label.setVisible(True)
        item_editor_window.item_work_step.clear()
        never_mind_button.show()
        set_add_draft_actions_visible(False)
        item_editor_window.add_item_dialog.close()
