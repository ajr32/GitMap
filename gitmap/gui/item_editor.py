# ruff: noqa: SIM114
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

from gitmap.models import Feature, Issue, Milestone, Section


def apply_editor_changes(editor):
    roadmap_object = editor.roadmap_object
    roadmap_detail = getattr(editor, "roadmap_detail", None)

    print(
        "APPLYING DETAIL:",
        getattr(roadmap_detail, "text", None),
    )

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

    if roadmap_detail is not None and hasattr(roadmap_detail, "text"):
        roadmap_detail.text = requirement_field.toPlainText()

        print("AFTER CHANGE:", roadmap_detail.text)
        print("DETAIL OBJECT ID:", id(roadmap_detail))

    if roadmap_detail is not None and hasattr(roadmap_detail, "work_step_marker"):
        work_step_text = work_step_field.toPlainText()

        marker = roadmap_detail.work_step_marker

        if work_step_text.startswith(marker):
            work_step_text = work_step_text[len(marker) :].strip()

        roadmap_detail.title = work_step_text

    if isinstance(roadmap_object, Issue):
        roadmap_object.description = description_field.toPlainText()

    if hasattr(editor, "refresh_preview"):
        editor.refresh_preview()


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


def configure_editor(
    editor,
    roadmap_object,
    selected_detail=None,
    detail_kind=None,
):
    item_type = get_item_type(roadmap_object)

    type_field = editor.findChild(QLabel, "item_type")
    type_field.setText(item_type)

    requirement_field = editor.findChild(QPlainTextEdit, "item_require")
    work_step_field = editor.findChild(QPlainTextEdit, "item_work_step")
    title_field = editor.findChild(QLineEdit, "item_title")
    number_field = editor.findChild(QLineEdit, "item_number")
    number_field.setReadOnly(True)
    description_field = editor.findChild(QPlainTextEdit, "item_description")
    description_label = editor.findChild(QLabel, "description_label")
    require_label = editor.findChild(QLabel, "require_label")
    work_step_label = editor.findChild(QLabel, "work_step_label")

    if item_type == "Milestone":
        description_field.setVisible(False)
        description_label.setVisible(False)

        requirement_field.setVisible(False)
        require_label.setVisible(False)

        work_step_field.setVisible(False)
        work_step_label.setVisible(False)

        title_field.setText(roadmap_object.title)
        number_field.setText(roadmap_object.number)

    elif item_type == "Section":
        description_field.setVisible(False)
        description_label.setVisible(False)

        requirement_field.setVisible(False)
        require_label.setVisible(False)

        work_step_field.setVisible(False)
        work_step_label.setVisible(False)
        title_field.setText(roadmap_object.title)
        number_field.setText(roadmap_object.number)

    elif item_type == "Feature":
        description_field.setVisible(False)
        description_label.setVisible(False)

        requirement_field.setVisible(False)
        require_label.setVisible(False)

        work_step_field.setVisible(False)
        work_step_label.setVisible(False)
        title_field.setText(roadmap_object.title)
        number_field.setText(roadmap_object.number)

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
