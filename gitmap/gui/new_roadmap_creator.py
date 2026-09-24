from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QTreeWidget

from gitmap.gui.item_editor import apply_editor_changes, configure_editor
from gitmap.gui.roadmap_tree import MODEL_ROLE, populate_roadmap_tree
from gitmap.models import Milestone


def load_new_roadmap_creator(roadmap):
    """Load the New Roadmap Creator window."""

    ui_path = Path(__file__).with_name("item_builder.ui")

    ui_file = QFile(str(ui_path))
    ui_file.open(QFile.OpenModeFlag.ReadOnly)

    loader = QUiLoader()
    window = loader.load(ui_file)

    ui_file.close()

    starting_series = roadmap.starting_series

    first_milestone = Milestone(
        number=f"{starting_series}.1",
        title="First Milestone",
    )

    roadmap.milestones.append(first_milestone)

    preview_tree = window.findChild(QTreeWidget, "preview_text")
    populate_roadmap_tree(preview_tree, roadmap)

    def refresh_preview():
        populate_roadmap_tree(preview_tree, roadmap)

    window.refresh_preview = refresh_preview

    edit_button = window.findChild(QPushButton, "edit_button")
    delete_button = window.findChild(QPushButton, "delete_button")
    add_button = window.findChild(QPushButton, "add_button")
    add_milestone_button = window.findChild(QPushButton, "add_milestone")
    save_button = window.findChild(QPushButton, "save_button")
    save_exit_button = window.findChild(QPushButton, "save_exit_button")
    apply_button = window.findChild(QPushButton, "apply_button")
    never_mind_button = window.findChild(QPushButton, "never_mind_button")
    title_field = window.findChild(QLineEdit, "item_title")
    number_field = window.findChild(QLineEdit, "item_number")

    apply_button.clicked.connect(lambda: apply_editor_changes(window))

    editor_tips = window.findChild(QLabel, "editor_tips")

    editor_tips.setText(
        "Hi! I'm Robert, your Roadmap Builder helper.\n\n"
        "No... not Bob like the other guy\n\n"
        "I've created your first milestone "
        "to get us started. "
        "Choose Edit Roadmap to begin "
        "building your roadmap."
    )

    editor_tips.setWordWrap(True)

    apply_button.hide()
    never_mind_button.hide()

    window.edit_mode = False

    def start_edit_mode():
        def preview_selection_changed(current, previous):
            if not window.edit_mode:
                return

            if current is None:
                return

            model = current.data(0, MODEL_ROLE)

            if model is None:
                return

            window.roadmap_object = model

            configure_editor(window, model)

            editor_tips.setText(
                "Milestone selected. Make your changes above, then click Apply."
            )

            title_field.setFocus()
            title_field.selectAll()

        preview_tree.currentItemChanged.connect(preview_selection_changed)

        window.edit_mode = True

        edit_button.hide()
        delete_button.hide()
        add_button.hide()
        add_milestone_button.hide()
        save_button.hide()
        save_exit_button.hide()

        apply_button.show()
        never_mind_button.show()

        editor_tips.setText("Click an item in the Preview that you'd like to edit.")

    edit_button.clicked.connect(start_edit_mode)

    window.roadmap = roadmap
    window.first_milestone = first_milestone

    return window
