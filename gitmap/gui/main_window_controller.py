import copy
import traceback

from PySide6.QtWidgets import (
    QFileDialog,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QTreeWidget,
)

from gitmap.gui.builder_controller import open_builder
from gitmap.gui.cancel_changes import cancel_changes
from gitmap.gui.editor_controller import open_editor
from gitmap.gui.new_roadmap_controller import (
    build_roadmap_from_answers,
    load_structure_dialog,
)
from gitmap.gui.review_dialog import load_review_dialog
from gitmap.gui.roadmap_structure import infer_roadmap_structure
from gitmap.gui.roadmap_tree import MODEL_ROLE, populate_roadmap_tree
from gitmap.parser import parse_roadmap


class MainWindowState:
    """Runtime state for the roadmap currently loaded in GitMap."""

    active_roadmap_path: str | None = None
    active_roadmap: object | None = None
    sync_baseline_roadmap: object | None = None

    selected_roadmap_object: object | None = None

    item_editor_window: object | None = None
    review_window: object | None = None
    new_roadmap_creator_window: object | None = None

    @property
    def roadmap_is_active(self):
        return self.active_roadmap is not None


def setup_main_window(window):
    """Initialize the basic Main Window widgets."""

    roadmap_tree = window.findChild(QTreeWidget, "roadmap_Tree")
    roadmap_tree.setHeaderHidden(True)

    roadmap_tree.setStyleSheet("""
        QTreeWidget {
            background-color: black;
            color: black;
        }
    """)

    roadmap_name = window.findChild(QTextEdit, "textEdit")
    roadmap_name.setReadOnly(True)

    window.gitmap_state = MainWindowState()
    state = window.gitmap_state

    # -------------------------------------------------------------------------
    # Main Window roadmap selection
    # -------------------------------------------------------------------------

    def roadmap_selection_changed():
        selected_items = roadmap_tree.selectedItems()

        if not selected_items:
            state.selected_roadmap_object = None
            return

        selected_item = selected_items[0]
        state.selected_roadmap_object = selected_item.data(0, MODEL_ROLE)

    roadmap_tree.itemSelectionChanged.connect(roadmap_selection_changed)

    # -------------------------------------------------------------------------
    # Main Window buttons
    # -------------------------------------------------------------------------

    new_roadmap_button = window.findChild(QPushButton, "New_Roadmap")
    open_button = window.findChild(QPushButton, "Open_Roadmap")
    edit_button = window.findChild(QPushButton, "edit_roadmap_button")
    review_button = window.findChild(QPushButton, "review_button")
    cancel_button = window.findChild(QPushButton, "cancel_button")

    edit_button.hide()
    review_button.hide()
    cancel_button.hide()

    # -------------------------------------------------------------------------
    # New Roadmap
    # -------------------------------------------------------------------------

    def create_new_roadmap():
        structure_dialog = load_structure_dialog()

        if not structure_dialog.exec():
            return

        roadmap = build_roadmap_from_answers(structure_dialog.answers)

        state.active_roadmap_path = None
        state.active_roadmap = roadmap
        state.sync_baseline_roadmap = copy.deepcopy(roadmap)
        state.selected_roadmap_object = None

        roadmap_name.setText(roadmap.name)
        populate_roadmap_tree(roadmap_tree, roadmap)

        edit_button.show()
        review_button.show()
        cancel_button.show()
        state.new_roadmap_creator_window = open_builder(roadmap)

    new_roadmap_button.clicked.connect(create_new_roadmap)

    # -------------------------------------------------------------------------
    # Open Roadmap
    # -------------------------------------------------------------------------

    def open_roadmap():
        roadmap_path, _ = QFileDialog.getOpenFileName(
            window,
            "Open Roadmap",
            "",
            "Markdown Roadmaps (*.md);;All Files (*.*)",
        )

        if not roadmap_path:
            return

        try:
            roadmap = parse_roadmap(roadmap_path)
            infer_roadmap_structure(roadmap)

        except (OSError, UnicodeError) as error:
            traceback.print_exc()

            QMessageBox.critical(
                window,
                "Unable to Open Roadmap",
                f"GitMap could not open the selected roadmap.\n\n"
                f"File: {roadmap_path}\n\n"
                f"Error: {error}",
            )
            return

        state.active_roadmap_path = roadmap_path
        state.active_roadmap = roadmap

        # Untouched copy of the roadmap as it existed when opened.
        state.sync_baseline_roadmap = copy.deepcopy(roadmap)

        roadmap_name.setText(roadmap.name)
        populate_roadmap_tree(roadmap_tree, roadmap)

        edit_button.show()
        review_button.show()
        cancel_button.show()

    open_button.clicked.connect(open_roadmap)

    # -------------------------------------------------------------------------
    # Edit Roadmap
    # -------------------------------------------------------------------------

    def open_active_editor(target_model=None):
        if not state.roadmap_is_active:
            return

        state.item_editor_window = open_editor(state.active_roadmap)

        if target_model is not None:
            state.item_editor_window.select_preview_model(target_model)

    edit_button.clicked.connect(lambda: open_active_editor())

    # -------------------------------------------------------------------------
    # Main Window double-click
    # -------------------------------------------------------------------------

    def roadmap_item_double_clicked(item, column):
        model = item.data(0, MODEL_ROLE)

        if model is None:
            return

        open_active_editor(model)

    roadmap_tree.itemDoubleClicked.connect(roadmap_item_double_clicked)
    roadmap_tree.setExpandsOnDoubleClick(False)

    # -------------------------------------------------------------------------
    # Review Changes
    # -------------------------------------------------------------------------

    def open_review_window():
        if not state.roadmap_is_active:
            return

        state.review_window = load_review_dialog(
            state.sync_baseline_roadmap,
            state.active_roadmap,
        )

        state.review_window.show()

    review_button.clicked.connect(open_review_window)

    # -------------------------------------------------------------------------
    # Cancel Changes
    # -------------------------------------------------------------------------

    def cancel_pending_changes():
        if not state.roadmap_is_active:
            return

        restored_roadmap = cancel_changes(
            window,
            state.sync_baseline_roadmap,
        )

        if restored_roadmap is None:
            return

        state.active_roadmap = restored_roadmap
        state.selected_roadmap_object = None

        populate_roadmap_tree(
            roadmap_tree,
            state.active_roadmap,
        )

    cancel_button.clicked.connect(cancel_pending_changes)
