from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView, QPushButton, QTreeWidget

from gitmap.gui.add_item_controller import (
    continue_add_item,
    finish_add,
    never_mind_add,
    start_add_milestone,
    start_add_mode,
)
from gitmap.gui.add_item_dialog import load_add_item_dialog
from gitmap.gui.editor_mode import set_editor_mode
from gitmap.gui.editor_selection import setup_editor_selection
from gitmap.gui.item_editor import (
    apply_editor_changes,
    get_item_type,
    load_item_editor,
)
from gitmap.gui.remove_item_controller import remove_selected_item
from gitmap.gui.roadmap_tree import populate_roadmap_tree

MODEL_ROLE = Qt.ItemDataRole.UserRole


def open_editor(roadmap):
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
    add_milestone_button = editor.findChild(
        QPushButton,
        "add_milestone",
    )
    edit_button = editor.findChild(QPushButton, "edit_button")
    delete_button = editor.findChild(QPushButton, "delete_button")
    never_mind_button = editor.findChild(
        QPushButton,
        "never_mind_button",
    )

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
    # ADD MILESTONE
    # =========================================================================
    def start_current_add_milestone():
        start_add_milestone(
            editor,
            preview_tree,
        )

    add_milestone_button.clicked.connect(start_current_add_milestone)

    # =========================================================================
    # OPEN
    # =========================================================================
    editor.show()

    return editor
