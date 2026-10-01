from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QTreeWidgetItem

from gitmap.gui.editor_controller import open_editor
from gitmap.gui.item_editor import apply_editor_changes
from gitmap.models import Milestone


def load_builder():
    """Load item_builder.ui."""

    ui_path = Path(__file__).with_name("item_builder.ui")

    ui_file = QFile(str(ui_path))
    ui_file.open(QFile.OpenModeFlag.ReadOnly)

    loader = QUiLoader()
    builder = loader.load(ui_file)

    ui_file.close()

    return builder


def open_builder(roadmap, state=None):
    """Open Builder for the first Milestone of a new Roadmap."""

    builder = load_builder()

    builder.roadmap = roadmap
    builder.roadmap_object = None
    builder.roadmap_detail = None

    # -------------------------------------------------------------------------
    # First Milestone draft
    # -------------------------------------------------------------------------

    first_milestone = Milestone(
        number="",
        title="",
    )

    builder.add_mode = False
    builder.add_question_stage = "ready"
    builder.add_selected_type = "Milestone"
    builder.add_selected_position = "child"
    builder.add_parent_model = roadmap
    builder.add_siblings = roadmap.milestones
    builder.add_insert_index = 0
    builder.add_new_model = first_milestone
    builder.add_reference = None
    builder.add_reference_model = None
    builder.add_placeholder = None
    builder.add_placeholder_title_callback = None

    builder.item_type_label.setText("First Milestone")

    # Automatic numbering starts with the series selected
    # in the New Roadmap questionnaire.
    builder.item_number.setText(f"{roadmap.starting_series}.1")

    builder.item_title.clear()
    builder.item_description.clear()
    builder.item_require.clear()
    builder.item_work_step.clear()

    builder.item_description.hide()
    builder.description_label.hide()
    builder.item_require.hide()
    builder.require_label.hide()
    builder.item_work_step.hide()
    builder.work_step_label.hide()

    # -------------------------------------------------------------------------
    # Preview
    # -------------------------------------------------------------------------

    preview_tree = builder.preview_text
    preview_tree.clear()

    placeholder = QTreeWidgetItem(["[First Milestone]"])
    preview_tree.addTopLevelItem(placeholder)
    preview_tree.setCurrentItem(placeholder)

    builder.add_placeholder = placeholder

    def update_placeholder(text):
        if text.strip():
            placeholder.setText(0, f"[{text.strip()}]")
        else:
            placeholder.setText(0, "[First Milestone]")

    builder.add_placeholder_title_callback = update_placeholder
    builder.item_title.textChanged.connect(update_placeholder)

    # -------------------------------------------------------------------------
    # Apply
    # -------------------------------------------------------------------------

    def apply_first_milestone():
        success = apply_editor_changes(builder)

        if not success:
            return

        builder.close()

        editor = open_editor(
            roadmap,
            state,
        )

        # Go directly to the Milestone that Builder just created.
        if roadmap.milestones:
            editor.select_preview_model(roadmap.milestones[0])

        builder.editor_window = editor

    builder.apply_changes = apply_first_milestone
    builder.apply_button.clicked.connect(apply_first_milestone)

    builder.show()

    return builder
