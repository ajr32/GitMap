from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QInputDialog,
    QMessageBox,
    QPushButton,
    QTreeWidget,
)

from gitmap.gui.controller.add_item_controller import (
    continue_add_item,
    finish_add,
    never_mind_add,
    start_add_mode,
)
from gitmap.gui.controller.move_item_controller import (
    get_move_destinations,
    get_position_choices,
    move_item,
    position_index_from_choice,
)
from gitmap.gui.controller.remove_item_controller import remove_selected_item
from gitmap.gui.controller.save_controller import save_roadmap
from gitmap.gui.editor.add_item_dialog import load_add_item_dialog
from gitmap.gui.editor.editor_mode import set_editor_mode
from gitmap.gui.editor.editor_selection import setup_editor_selection
from gitmap.gui.editor.item_editor import (
    apply_editor_changes,
    get_item_type,
    load_item_editor,
)
from gitmap.gui.review.review_dialog import load_review_dialog
from gitmap.gui.shared.roadmap_tree import populate_roadmap_tree
from gitmap.gui.sync.sync_controller import run_github_sync

MODEL_ROLE = Qt.ItemDataRole.UserRole


def open_editor(
    roadmap,
    state=None,
    refresh_main_window=None,
):
    """Open the normal GitMap Editor for a Roadmap."""

    editor = load_item_editor()

    editor.roadmap = roadmap
    editor.roadmap_detail = None
    editor.add_mode = False

    # =========================================================================
    # PREVIEW / ZOOM
    # =========================================================================
    preview_tree = editor.findChild(QTreeWidget, "preview_text")
    preview_tree.setHeaderHidden(True)
    preview_tree.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

    populate_roadmap_tree(preview_tree, roadmap)

    def refresh_preview():
        populate_roadmap_tree(preview_tree, roadmap)

    editor.refresh_preview = refresh_preview

    context_tree = editor.findChild(QTreeWidget, "context_tree")
    context_tree.clear()

    # =========================================================================
    # EDITOR MODE
    # =========================================================================
    set_editor_mode(editor, "normal")

    def apply_current_changes():
        success = apply_editor_changes(editor)

        if success:
            set_editor_mode(editor, "normal")

        return success

    editor.apply_changes = apply_current_changes

    # =========================================================================
    # PREVIEW SELECTION
    # =========================================================================
    setup_editor_selection(
        editor,
        roadmap,
        preview_tree,
        context_tree,
    )

    # =========================================================================
    # ADD DIALOG
    # =========================================================================
    editor.add_item_dialog = load_add_item_dialog()
    add_continue_button = editor.add_item_dialog.add_continue_button

    # =========================================================================
    # BUTTONS
    # =========================================================================
    add_button = editor.findChild(QPushButton, "add_button")
    edit_button = editor.findChild(QPushButton, "edit_button")
    delete_button = editor.findChild(QPushButton, "delete_button")
    move_button = editor.findChild(QPushButton, "move_button")
    never_mind_button = editor.findChild(
        QPushButton,
        "never_mind_button",
    )
    save_button = editor.findChild(QPushButton, "save_button")
    save_exit_button = editor.findChild(QPushButton, "save_exit_button")
    review_button = editor.findChild(QPushButton, "review_button")
    sync_button = editor.findChild(QPushButton, "sync_button")

    # =========================================================================
    # DELETE
    # =========================================================================
    delete_button.clicked.connect(lambda: remove_selected_item(editor))

    # =========================================================================
    # NEVER MIND
    # =========================================================================
    def never_mind_current_action():
        if editor.add_selected_type is not None or editor.add_placeholder is not None:
            never_mind_add(
                editor,
                preview_tree,
                context_tree,
            )
            return

        set_editor_mode(editor, "normal")

    never_mind_button.clicked.connect(never_mind_current_action)

    # =========================================================================
    # FINISH ADD
    # =========================================================================
    def finish_current_add():
        finish_add(editor)

    editor.finish_add = finish_current_add

    # =========================================================================
    # CONTINUE ADD
    # =========================================================================
    def continue_current_add():
        continue_add_item(
            editor,
            preview_tree,
            MODEL_ROLE,
            get_item_type,
        )

    add_continue_button.clicked.connect(continue_current_add)

    # =========================================================================
    # EDIT
    # =========================================================================
    def start_edit_mode():
        if editor.roadmap_object is None:
            return

        set_editor_mode(editor, "edit")

    edit_button.clicked.connect(start_edit_mode)

    # =========================================================================
    # ADD
    # =========================================================================
    def start_current_add_mode():
        start_add_mode(
            editor,
            preview_tree,
        )

    add_button.clicked.connect(start_current_add_mode)

    # =========================================================================
    # MOVE
    # =========================================================================
    def start_move_mode():
        target = editor.roadmap_object

        if target is None:
            QMessageBox.information(
                editor,
                "Move Item",
                "Select an item to move first.",
            )
            return

        destinations = get_move_destinations(roadmap, target)

        if not destinations:
            QMessageBox.information(
                editor,
                "Move Item",
                "There are no valid destinations for this item.",
            )
            return

        labels = [destination.label for destination in destinations]

        selected_label, accepted = QInputDialog.getItem(
            editor,
            "Move Item",
            "Move to:",
            labels,
            0,
            False,
        )

        if not accepted:
            return

        selected_index = labels.index(selected_label)
        destination = destinations[selected_index]

        position_choices = get_position_choices(
            destination,
            target,
        )

        selected_position, accepted = QInputDialog.getItem(
            editor,
            "Move Item",
            "Place item:",
            position_choices,
            0,
            False,
        )

        if not accepted:
            return

        insert_index = position_index_from_choice(
            destination,
            target,
            selected_position,
        )

        changes = move_item(
            roadmap,
            target,
            destination,
            insert_index,
        )

        roadmap.is_modified = True

        populate_roadmap_tree(preview_tree, roadmap)

        if hasattr(editor, "select_preview_model"):
            editor.select_preview_model(target)

        if changes:
            change_lines = [
                f"{change['old_number']} → {change['new_number']}  {change['title']}"
                for change in changes
            ]

            QMessageBox.information(
                editor,
                "Move Complete",
                "Item moved. Numbering changes:\n\n" + "\n".join(change_lines),
            )
        else:
            QMessageBox.information(
                editor,
                "Move Complete",
                "Item moved.",
            )

    move_button.clicked.connect(start_move_mode)

    # =========================================================================
    # REVIEW
    # =========================================================================
    def review_current_changes():
        if state is None:
            return

        state.review_window = load_review_dialog(
            state.review_baseline_roadmap,
            roadmap,
        )

        state.review_window.show()

    review_button.clicked.connect(review_current_changes)

    # =========================================================================
    # SYNC
    # =========================================================================
    def sync_current_changes():
        if state is None:
            return

        run_github_sync(editor, state)

    sync_button.clicked.connect(sync_current_changes)

    # =========================================================================
    # SAVE
    # =========================================================================
    def save_current_roadmap():
        if state is None:
            return False

        save_as = False

        # If this roadmap already has a file, ask whether to save there
        # or choose a new file.
        if state.active_roadmap_path is not None:
            message_box = QMessageBox(editor)
            message_box.setWindowTitle("Save Roadmap")
            message_box.setText("How would you like to save this roadmap?")

            save_button_choice = message_box.addButton(
                "Save",
                QMessageBox.ButtonRole.AcceptRole,
            )
            save_as_button_choice = message_box.addButton(
                "Save As...",
                QMessageBox.ButtonRole.ActionRole,
            )
            message_box.addButton(
                "Cancel",
                QMessageBox.ButtonRole.RejectRole,
            )

            message_box.exec()

            clicked_button = message_box.clickedButton()

            if clicked_button is save_button_choice:
                save_as = False
            elif clicked_button is save_as_button_choice:
                save_as = True
            else:
                return False

        success = save_roadmap(
            editor,
            state,
            save_as=save_as,
        )

        if success:
            QMessageBox.information(
                editor,
                "Saved",
                "Roadmap saved successfully.",
            )

        return success

    def save_and_exit():
        if not save_current_roadmap():
            return

        if hasattr(state, "refresh_main_roadmap"):
            state.refresh_main_roadmap()

        editor.close()

    save_button.clicked.connect(save_current_roadmap)
    save_exit_button.clicked.connect(save_and_exit)

    # =========================================================================
    # OPEN
    # =========================================================================
    editor.show()

    return editor
