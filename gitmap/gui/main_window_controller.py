import copy
import traceback

from PySide6.QtWidgets import (
    QFileDialog,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QTreeWidget,
)

from gitmap.gui.editor_controller import open_editor
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

    def roadmap_selection_changed():
        selected_items = roadmap_tree.selectedItems()

        if not selected_items:
            state.selected_roadmap_object = None
            return

        selected_item = selected_items[0]
        state.selected_roadmap_object = selected_item.data(0, MODEL_ROLE)

    roadmap_tree.itemSelectionChanged.connect(roadmap_selection_changed)

    open_button = window.findChild(QPushButton, "Open_Roadmap")
    edit_button = window.findChild(QPushButton, "edit_roadmap_button")
    edit_button.hide()

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

    open_button.clicked.connect(open_roadmap)

    def open_active_editor():
        if not state.roadmap_is_active:
            return

        state.item_editor_window = open_editor(state.active_roadmap)

    edit_button.clicked.connect(open_active_editor)