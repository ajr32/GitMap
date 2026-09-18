# =============================================================================
# GITMAP item_editor.py ROAD MAP
# =============================================================================
# Stable navigation labels for this file:
#
#   Part A  - Imports / dependencies
#   Part B  - Apply edits back to the in-memory model
#     B1    - Read editor fields and validate title
#     B2    - Apply Requirement changes
#     B3    - Apply Work Step changes
#     B4    - Apply Issue description
#     B5    - Mark roadmap modified and refresh Preview
#   Part C  - Load and wire the Item Editor UI
#   Part D  - Determine GitMap item type
#   Part E  - Configure Editor for the selected item
#     E1    - Find fields and establish common state
#     E2    - Milestone layout
#     E3    - Section layout
#     E4    - Feature layout
#     E5    - Issue layout and exact-detail handling
#
# Existing Part letters are STABLE. If we insert code later, use subdivisions
# such as B2A, E6, etc. Do not reletter existing Parts unless we explicitly
# decide to refactor this navigation scheme.
# =============================================================================

# ruff: noqa: SIM114
# =============================================================================
# PART A — IMPORTS / DEPENDENCIES
# =============================================================================
# Qt classes here load the Designer .ui file and access its labels, line edits,
# text boxes, message boxes, and buttons.
#
# GitMap model classes are used both for type detection and to decide which
# fields make sense for the selected roadmap object.
# =============================================================================
from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
)

from gitmap.models import Requirement, Feature, Issue, Milestone, Section
from gitmap.roadmap_numbering import renumber_siblings


# =============================================================================
# PART B — APPLY EDITOR CHANGES TO THE IN-MEMORY MODEL
# =============================================================================
# Called when the user presses Apply.
#
# This function does NOT save Markdown to disk. It changes the model object
# currently attached to the Editor. Part B5 then marks the Roadmap modified
# and asks the Editor Preview to redraw.
#
# `editor.roadmap_object` is the selected Milestone/Section/Feature/Issue.
# `editor.roadmap_detail` is an exact Requirement or Work Step when one of
# those detail rows was selected.
# =============================================================================
def apply_editor_changes(editor):
    if getattr(editor, "add_selected_type", None) == "Requirement":
        parent_issue = editor.add_parent_model

        requirement_text = editor.item_require.toPlainText().strip()

        if not requirement_text:
            QMessageBox.warning(
                editor,
                "Invalid Requirement",
                "Requirement cannot be blank.",
            )
            return

        new_requirement = Requirement(text=requirement_text)
        parent_issue.requirements.append(new_requirement)

        editor.roadmap.is_modified = True

        if hasattr(editor, "refresh_preview"):
            editor.refresh_preview()

        if hasattr(editor, "finish_add"):
            editor.finish_add()

        editor.add_selected_type = None

        return

    if getattr(editor, "add_selected_type", None) == "Work Step":
        parent_issue = editor.add_parent_model

        work_step_text = editor.item_work_step.toPlainText().strip()

        if not work_step_text:
            QMessageBox.warning(
                editor,
                "Invalid Work Step",
                "Work Step cannot be blank.",
            )
            return

        new_work_step = Issue(
            number=parent_issue.number,
            title=work_step_text,
        )

        parent_issue.work_steps.append(new_work_step)

        renumber_siblings(
            parent_issue.work_steps,
            parent_issue.number,
            parent_type="work_step",
        )

        editor.roadmap.is_modified = True

        if hasattr(editor, "refresh_preview"):
            editor.refresh_preview()

        if hasattr(editor, "finish_add"):
            editor.finish_add()

        editor.add_selected_type = None

        return

    if getattr(editor, "add_new_model", None) is not None:
        new_model = editor.add_new_model

        title_field = editor.findChild(QLineEdit, "item_title")
        new_title = title_field.text().strip()

        if not new_title:
            QMessageBox.warning(
                editor,
                "Invalid Title",
                "Title cannot be blank.",
            )
            return

        new_model.title = new_title
        if isinstance(new_model, Issue):
            description_field = editor.findChild(QPlainTextEdit, "item_description")
            new_model.description = description_field.toPlainText()
        number_field = editor.findChild(QLineEdit, "item_number")
        new_model.number = number_field.text()
        siblings = editor.add_siblings
        insert_index = editor.add_insert_index

        siblings.insert(insert_index, new_model)
        renumber_siblings(
            siblings,
            editor.add_parent_model.number,
        )

        if hasattr(editor, "refresh_preview"):
            editor.refresh_preview()

        if hasattr(editor, "roadmap"):
            editor.roadmap.is_modified = True

        if hasattr(editor, "select_preview_model"):
            editor.select_preview_model(new_model)

        editor.add_new_model = None
        editor.add_placeholder = None
        if hasattr(editor, "finish_add"):
            editor.finish_add()
        return

    roadmap_object = editor.roadmap_object
    roadmap_detail = getattr(editor, "roadmap_detail", None)

    print(
        "APPLYING DETAIL:",
        getattr(roadmap_detail, "text", None),
    )

    # -------------------------------------------------------------------------
    # PART B1 — READ FIELDS / VALIDATE TITLE
    # -------------------------------------------------------------------------
    # Every structural GitMap item has a title, so blank titles are rejected.
    # Description/Requirement/Work-Step text may follow different rules.
    # -------------------------------------------------------------------------
    title_field = editor.findChild(QLineEdit, "item_title")
    new_title = title_field.text().strip()

    if not new_title:
        QMessageBox.warning(
            editor,
            "Invalid Title",
            "Title cannot be blank.",
        )
        return

    description_field = editor.findChild(QPlainTextEdit, "item_description")

    requirement_field = editor.findChild(QPlainTextEdit, "item_require")

    work_step_field = editor.findChild(QPlainTextEdit, "item_work_step")

    roadmap_object.title = new_title

    # -------------------------------------------------------------------------
    # PART B2 — APPLY REQUIREMENT TEXT
    # -------------------------------------------------------------------------
    # Requirement objects expose `.text`. If the selected detail has that
    # attribute, copy the Requirement text box back into that exact object.
    # -------------------------------------------------------------------------
    if roadmap_detail is not None and hasattr(roadmap_detail, "text"):
        roadmap_detail.text = requirement_field.toPlainText()

    # -------------------------------------------------------------------------
    # PART B3 — APPLY WORK STEP TEXT
    # -------------------------------------------------------------------------
    # Work Steps expose `work_step_marker` and store their editable wording in
    # `.title`. If the marker somehow appears in the text box, strip it before
    # storing the title so the marker isn't duplicated.
    #
    # FUTURE WORK:
    # Adding/removing Work Steps and marker renumbering are separate features.
    # When implemented, use the existing 0.7 numbering backend rather than
    # creating a second GUI-only numbering system.
    # -------------------------------------------------------------------------
    if roadmap_detail is not None and hasattr(roadmap_detail, "work_step_marker"):
        work_step_text = work_step_field.toPlainText()

        marker = roadmap_detail.work_step_marker

        if work_step_text.startswith(marker):
            work_step_text = work_step_text[len(marker) :].strip()

        roadmap_detail.title = work_step_text

    # -------------------------------------------------------------------------
    # PART B4 — APPLY ISSUE DESCRIPTION
    # -------------------------------------------------------------------------
    # Only Issues currently have the editable Description field.
    # -------------------------------------------------------------------------
    if isinstance(roadmap_object, Issue):
        roadmap_object.description = description_field.toPlainText()

    # -------------------------------------------------------------------------
    # PART B5 — MARK MODIFIED / REFRESH PREVIEW
    # -------------------------------------------------------------------------
    # Apply changes only the in-memory model. `is_modified` records that the
    # roadmap has unsaved changes.
    #
    # `refresh_preview` is attached by app.py (Part G4 there). Keeping this as
    # a callback avoids item_editor.py needing to know how the Preview tree is
    # built.
    # -------------------------------------------------------------------------
    if hasattr(editor, "roadmap"):
        editor.roadmap.is_modified = True

    if hasattr(editor, "refresh_preview"):
        editor.refresh_preview()


# =============================================================================
# PART C — LOAD AND WIRE THE ITEM EDITOR UI
# =============================================================================
# Loads item_editor.ui from the same directory as this Python file.
#
# Wiring performed here:
#   Apply  -> apply_editor_changes(editor)
#   Cancel -> close the Editor window
#
# app.py performs the roadmap-specific setup after this function returns.
# =============================================================================
def load_item_editor():
    """Load the roadmap Item Editor window."""

    ui_path = Path(__file__).with_name("item_editor.ui")

    ui_file = QFile(str(ui_path))
    ui_file.open(QFile.OpenModeFlag.ReadOnly)

    loader = QUiLoader()
    editor = loader.load(ui_file)

    ui_file.close()

    apply_button = editor.findChild(QPushButton, "apply_button")
    apply_button.clicked.connect(lambda: apply_editor_changes(editor))

    cancel_button = editor.findChild(QPushButton, "cancel_button")
    cancel_button.clicked.connect(editor.close)

    return editor


# =============================================================================
# PART D — DETERMINE THE SELECTED GITMAP ITEM TYPE
# =============================================================================
# Converts the Python model class into the display/type name used by the
# Editor. This keeps isinstance checks out of the UI-label code.
#
# Requirement and Work Step are NOT returned here because those are details
# belonging to an Issue; their exact type is passed separately as detail_kind.
# =============================================================================
def get_item_type(roadmap_object):
    if isinstance(roadmap_object, Milestone):
        return "Milestone"

    if isinstance(roadmap_object, Section):
        return "Section"

    if isinstance(roadmap_object, Feature):
        return "Feature"

    if isinstance(roadmap_object, Issue):
        return "Issue"

    return "Unknown"


# =============================================================================
# PART E — CONFIGURE EDITOR FOR THE SELECTED ITEM
# =============================================================================
# Called whenever the user selects a model-backed row in the Editor Preview.
#
# Inputs:
#   editor          - loaded Item Editor window
#   roadmap_object  - Milestone / Section / Feature / Issue
#   selected_detail - exact Requirement or Work Step object, when applicable
#   detail_kind     - "requirement", "work_step", "description", or None
#
# Main job:
# Show only the fields that make sense for the selected item and populate them
# from the in-memory model.
# =============================================================================
def configure_editor(
    editor,
    roadmap_object,
    selected_detail=None,
    detail_kind=None,
):
    item_type = get_item_type(roadmap_object)

    # -------------------------------------------------------------------------
    # PART E1 — FIND FIELDS / ESTABLISH COMMON EDITOR STATE
    # -------------------------------------------------------------------------
    # All widgets are looked up by the objectName assigned in Qt Designer.
    #
    # The number field is ALWAYS read-only. Numbers are controlled by roadmap
    # structure/order and the numbering backend, not arbitrary text editing.
    # -------------------------------------------------------------------------
    type_field = editor.findChild(QLabel, "item_type_label")
    type_field.setText(f"Editing {item_type}")

    requirement_field = editor.findChild(QPlainTextEdit, "item_require")
    work_step_field = editor.findChild(QPlainTextEdit, "item_work_step")
    title_field = editor.findChild(QLineEdit, "item_title")
    number_field = editor.findChild(QLineEdit, "item_number")
    number_field.setReadOnly(True)
    description_field = editor.findChild(QPlainTextEdit, "item_description")
    description_label = editor.findChild(QLabel, "description_label")
    require_label = editor.findChild(QLabel, "require_label")
    work_step_label = editor.findChild(QLabel, "work_step_label")

    # -------------------------------------------------------------------------
    # PART E2 — MILESTONE LAYOUT
    # -------------------------------------------------------------------------
    # Milestones currently expose only Title + Number.
    # -------------------------------------------------------------------------
    if item_type == "Milestone":
        description_field.setVisible(False)
        description_label.setVisible(False)

        requirement_field.setVisible(False)
        require_label.setVisible(False)

        work_step_field.setVisible(False)
        work_step_label.setVisible(False)

        title_field.setText(roadmap_object.title)
        number_field.setText(roadmap_object.number)

    # -------------------------------------------------------------------------
    # PART E3 — SECTION LAYOUT
    # -------------------------------------------------------------------------
    # Sections currently expose only Title + Number.
    # -------------------------------------------------------------------------
    elif item_type == "Section":
        description_field.setVisible(False)
        description_label.setVisible(False)

        requirement_field.setVisible(False)
        require_label.setVisible(False)

        work_step_field.setVisible(False)
        work_step_label.setVisible(False)
        title_field.setText(roadmap_object.title)
        number_field.setText(roadmap_object.number)

    # -------------------------------------------------------------------------
    # PART E4 — FEATURE LAYOUT
    # -------------------------------------------------------------------------
    # Features currently expose only Title + Number.
    # -------------------------------------------------------------------------
    elif item_type == "Feature":
        description_field.setVisible(False)
        description_label.setVisible(False)

        requirement_field.setVisible(False)
        require_label.setVisible(False)

        work_step_field.setVisible(False)
        work_step_label.setVisible(False)
        title_field.setText(roadmap_object.title)
        number_field.setText(roadmap_object.number)

    # -------------------------------------------------------------------------
    # PART E5 — ISSUE LAYOUT / EXACT DETAIL HANDLING
    # -------------------------------------------------------------------------
    # Issues always expose Title + Number + Description.
    #
    # Requirement and Work Step fields start hidden. They become visible only
    # when the user clicked that exact detail row in Preview:
    #   detail_kind == "requirement" -> show/populate Requirement field
    #   detail_kind == "work_step"   -> show/populate Work Step field
    #
    # Clearing the hidden detail fields first prevents text from a previously
    # selected detail from leaking into the next selection.
    # -------------------------------------------------------------------------
    elif item_type == "Issue":
        description_field.setVisible(True)
        description_label.setVisible(True)

        requirement_field.setVisible(False)
        require_label.setVisible(False)

        work_step_field.setVisible(False)
        work_step_label.setVisible(False)

        requirement_field.clear()
        work_step_field.clear()

        if detail_kind == "requirement":
            requirement_field.setVisible(True)
            require_label.setVisible(True)

        if detail_kind == "work_step":
            work_step_field.setVisible(True)
            work_step_label.setVisible(True)

        description_field.setEnabled(True)
        requirement_field.setEnabled(True)
        work_step_field.setEnabled(True)
        title_field.setText(roadmap_object.title)
        number_field.setText(roadmap_object.number)
        description_field.setPlainText(roadmap_object.description or "")
        if detail_kind == "requirement" and selected_detail is not None:
            requirement_field.setPlainText(selected_detail.text)
        if detail_kind == "work_step" and selected_detail is not None:
            work_step_field.setPlainText(selected_detail.title)
