from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView, QPushButton, QTreeWidget

from gitmap.gui.add_item_controller import (
    continue_add_item,
    finish_add,
    never_mind_add,
    start_add_mode,
)

from gitmap.gui.item_editor import (
    apply_editor_changes,
    get_item_type,
    load_item_editor,
)
from gitmap.gui.editor_mode import set_editor_mode
from gitmap.gui.add_item_dialog import load_add_item_dialog
from gitmap.gui.editor_selection import setup_editor_selection
from gitmap.gui.remove_item_controller import remove_selected_item
from gitmap.gui.roadmap_tree import populate_roadmap_tree

MODEL_ROLE = Qt.ItemDataRole.UserRole

def open_editor(roadmap):
    """Open the normal GitMap Editor for a Roadmap."""

    editor = load_item_editor()

    editor.roadmap = roadmap
    editor.roadmap_detail = None
    editor.add_mode = False

    preview_tree = editor.findChild(QTreeWidget, "preview_text")
    preview_tree.setHeaderHidden(True)
    preview_tree.setSelectionMode(
        QAbstractItemView.SelectionMode.SingleSelection
    )

    populate_roadmap_tree(preview_tree, roadmap)

    context_tree = editor.findChild(QTreeWidget, "context_tree")
    context_tree.clear()

    set_editor_mode(editor, "normal")

    def apply_current_changes():
        success = apply_editor_changes(editor)

        if success:
            set_editor_mode(editor, "normal")

        return success

    editor.apply_changes = apply_current_changes

    setup_editor_selection(
        editor,
        roadmap,
        preview_tree,
        context_tree,
    )

    # =========================================================================
    # PART G — OPEN AND SET UP THE ROADMAP EDITOR
    # =========================================================================
    # This is currently the largest GUI-controller section in app.py.
    #
    # It:
    #   * loads item_editor.ui
    #   * attaches the active Roadmap
    #   * creates the Add popup
    #   * wires the Add button
    #   * finds the Editor Preview and Zoom trees
    #   * renders the Preview
    #   * defines Preview-selection behavior (Part H below)
    #
    # FUTURE REFACTOR:
    # Add workflow behavior now lives in add_item_controller.py. Part G keeps
    # only the Editor-specific wiring and Preview/Zoom lifecycle.
    # =========================================================================
    # -------------------------------------------------------------------------
    # REMOVE ITEM CONTROLLER
    # -------------------------------------------------------------------------

    editor.add_item_dialog = load_add_item_dialog()
    add_button = editor.findChild(QPushButton, "add_button")
    edit_button = editor.findChild(QPushButton, "edit_button")
    delete_button = editor.findChild(QPushButton, "delete_button")
    save_button = editor.findChild(QPushButton, "save_button")
    save_exit_button = editor.findChild(QPushButton, "save_exit_button")

    def set_add_draft_actions_visible(visible):
        add_button.setVisible(visible)
        delete_button.setVisible(visible)
        save_button.setVisible(visible)
        save_exit_button.setVisible(visible)

    add_continue_button = editor.add_item_dialog.add_continue_button
    never_mind_button = editor.findChild(
        QPushButton, "never_mind_button"
    )
    never_mind_button.hide()
    set_add_draft_actions_visible(True)

    delete_button.clicked.connect(lambda: remove_selected_item(editor))

    def never_mind_current_action():
        if editor.add_mode:
            never_mind_add(
                editor,
                never_mind_button,
                set_add_draft_actions_visible,
                preview_tree,
                context_tree,
            )

        set_editor_mode(editor, "normal")

    never_mind_button.clicked.connect(never_mind_current_action)

    def finish_current_add():
        finish_add(
            editor,
            never_mind_button,
            set_add_draft_actions_visible,
        )

    editor.finish_add = finish_current_add
    editor.add_mode = False

    def continue_current_add():
        continue_add_item(
            editor,
            never_mind_button,
            set_add_draft_actions_visible,
            preview_tree,
            MODEL_ROLE,
            get_item_type,
        )

    add_continue_button.clicked.connect(continue_current_add)

    def start_edit_mode():
        if editor.roadmap_object is None:
            return

        set_editor_mode(editor, "edit")

    edit_button.clicked.connect(start_edit_mode)
    # ---------------------------------------------------------------------
    # PART H — ENTER ADD MODE
    # ---------------------------------------------------------------------
    def start_current_add_mode():
        start_add_mode(editor, preview_tree)

    add_button.clicked.connect(start_current_add_mode)

    editor.show()

    return editor