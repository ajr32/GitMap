# ============================================================
# MAIN GITMAP WINDOW
# Loads the GitMap interface created in Qt Designer.
# ============================================================

import sys
import traceback
from pathlib import Path

from PySide6.QtCore import QFile, Qt
from PySide6.QtGui import QBrush, QColor, QFont
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QFileDialog,
    QLineEdit,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QTextEdit,
    QTreeWidget,
    QTreeWidgetItem,
    QTreeWidgetItemIterator,
)

from gitmap.gui.structure_questions import QUESTIONS
from gitmap.models import Roadmap
from gitmap.parser import parse_roadmap

MODEL_ROLE = Qt.ItemDataRole.UserRole


def add_issue_to_tree(parent_item, issue):
    """Add an issue and its contents to the roadmap tree."""

    issue_item = QTreeWidgetItem([f"{issue.number} {issue.title}"])
    issue_item.setData(0, MODEL_ROLE, issue)
    parent_item.addChild(issue_item)

    issue_item.setForeground(0, QColor("#FFFFFF"))

    if issue.description:
        description_item = QTreeWidgetItem([issue.description])

        description_font = QFont()
        description_font.setItalic(True)
        # description_font.setPointSize(description_font.pointSize() - 1)

        description_item.setFont(0, description_font)
        description_item.setForeground(0, QColor("#808080"))

        issue_item.addChild(description_item)

    print("\nISSUE:", issue.number, issue.title)

    print("  DESCRIPTION:", repr(issue.description))
    for requirement in issue.requirements:
        print("  REQUIREMENT:", repr(requirement.text))

    for work_step in issue.work_steps:
        print("  WORK STEP:", repr(work_step.title))

    # --- Requirements ---
    for requirement in issue.requirements:
        requirement_text = requirement.text

        if requirement_text.strip() == issue.description.strip():
            continue

        # Remove legacy Markdown checkbox syntax.
        for prefix in (
            "- [ ] ",
            "* [ ] ",
            "[ ] ",
            "- [x] ",
            "* [x] ",
            "[x] ",
            "- [X] ",
            "* [X] ",
            "[X] ",
        ):
            if requirement_text.startswith(prefix):
                requirement_text = requirement_text[len(prefix) :]
                break

        requirement_item = QTreeWidgetItem([f"• {requirement_text}"])

        requirement_item.setForeground(0, QColor("#B08CC6"))

        issue_item.addChild(requirement_item)

    # --- Work Steps ---
    for work_step in issue.work_steps:
        work_step_item = QTreeWidgetItem(
            [f"{work_step.work_step_marker} {work_step.title}"]
        )

        work_step_item.setForeground(0, QColor("#4F8A5B"))

        issue_item.addChild(work_step_item)


# def load_item_editor():
#     """Load the roadmap item editor."""
#
#     ui_path = Path(__file__).with_name("item_editor.ui")
#
#     ui_file = QFile(str(ui_path))
#     ui_file.open(QFile.OpenModeFlag.ReadOnly)
#
#     loader = QUiLoader()
#     editor = loader.load(ui_file)
#
#     def apply_item():
#         title = editor.findChild(QLineEdit, "item_title")
#         number = editor.findChild(QLineEdit, "item_number")
#         description = editor.findChild(QPlainTextEdit, "item_description")
#         preview = editor.findChild(QPlainTextEdit, "preview_text")
#         print("Title:", title.text())
#         print("Number:", number.text())
#         print("Description:", description.toPlainText())
#         preview.setPlainText(
#             f"{number.text()} {title.text()}\n\n{description.toPlainText()}"
#         )
#
#     apply_button = editor.findChild(QPushButton, "apply_button")
#     apply_button.clicked.connect(apply_item)
#     title = editor.findChild(QLineEdit, "item_title")
#     number = editor.findChild(QLineEdit, "item_number")
#
#     title.returnPressed.connect(apply_button.click)
#     number.returnPressed.connect(apply_button.click)
#
#     ui_file.close()
#     return editor


def load_item_editor():
    """Load the roadmap item editor."""

    ui_path = Path(__file__).with_name("item_editor.ui")

    ui_file = QFile(str(ui_path))
    ui_file.open(QFile.OpenModeFlag.ReadOnly)

    loader = QUiLoader()
    editor = loader.load(ui_file)

    preview_text = editor.findChild(QTreeWidget, "preview_text")
    ui_file.close()

    apply_button = editor.findChild(QPushButton, "apply_button")
    apply_button.clicked.connect(
        lambda: print("APPLY MODEL:", type(editor.roadmap_object).__name__)
    )
    cancel_button = editor.findChild(QPushButton, "cancel_button")
    cancel_button.clicked.connect(editor.close)
    return editor


def load_structure_dialog():
    """Load the new-roadmap structure dialog."""

    ui_path = Path(__file__).with_name("structure_dialog.ui")

    ui_file = QFile(str(ui_path))
    ui_file.open(QFile.OpenModeFlag.ReadOnly)

    loader = QUiLoader()
    dialog = loader.load(ui_file)
    current_question = 0
    question = QUESTIONS[current_question]

    dialog.starting_series_number.hide()
    dialog.project_name.hide()

    answers = {}

    dialog.answers = answers

    dialog.structure_subject.setText(question["subject"])
    dialog.structure_subject.adjustSize()
    dialog.structure_question.setPlainText(question["question"])

    buttons = [
        dialog.Button1,
        dialog.Button2,
        dialog.Button3,
        dialog.Button4,
    ]

    for index, button in enumerate(buttons):
        if index < len(question["options"]):
            button.setText(question["options"][index]["text"])
            button.show()
        else:
            button.hide()

    def validate_configuration():
        if answers.get("use_features") and not answers.get("use_sections"):
            return False

        if answers.get("allow_issues_under_sections") and not answers.get(
            "use_sections"
        ):
            return False

        if answers.get("allow_issues_under_features") and not answers.get(
            "use_features"
        ):
            return False

        return True

    def update_details():
        for index, button in enumerate(buttons):
            if button.isChecked() and index < len(question["options"]):
                option = question["options"][index]

                answers[question["id"]] = option["value"]

                if question["id"] == "structure":
                    structure = option["value"]

                    answers["use_sections"] = structure in (
                        "sections",
                        "sections_and_features",
                    )

                    answers["use_features"] = structure == "sections_and_features"

                    if not answers["use_sections"]:
                        answers["allow_issues_under_sections"] = False

                    if not answers["use_features"]:
                        answers["allow_issues_under_features"] = False

                if question["id"] == "section_tracking":
                    answers["allow_issues_under_sections"] = option["value"] in (
                        "issues",
                        "issues_and_labels",
                    )

                if question["id"] == "starting_point":
                    dialog.starting_series_number.setVisible(
                        option["value"] == "re-production"
                    )

                if question["id"] == "feature_tracking":
                    answers["allow_issues_under_features"] = option["value"] in (
                        "issues",
                        "issues_and_labels",
                    )

                dialog.structure_status.setText(
                    "  |  ".join(f"{key}: {value}" for key, value in answers.items())
                )

                dialog.structure_example.setPlainText(option["example"])
                dialog.structure_explain.setPlainText(option["explanation"])
                break

    def show_question(index):
        nonlocal question
        question = QUESTIONS[index]
        dialog.project_name.setVisible(question["id"] == "project_name")
        dialog.starting_series_number.setVisible(False)

        answers.pop(question["id"], None)

        dialog.structure_subject.setText(question["subject"])
        dialog.structure_subject.adjustSize()

        dialog.structure_question.setPlainText(question["question"])

        dialog.structure_example.clear()
        dialog.structure_explain.clear()

        for button in buttons:
            button.setAutoExclusive(False)
            button.setChecked(False)
            button.setAutoExclusive(True)

        for button_index, button in enumerate(buttons):
            if button_index < len(question["options"]):
                button.setText(question["options"][button_index]["text"])
                button.show()
            else:
                button.hide()

    def question_applies(question_id):
        if question_id == "starting_point":
            return answers.get("numbering") == "automatic"

        if question_id == "section_tracking":
            return answers.get("use_sections", False)

        if question_id == "feature_tracking":
            return answers.get("use_features", False)

        if question_id == "hierarchy":
            issue_values = ("issues", "issues_and_labels")

            return (
                answers.get("section_tracking") in issue_values
                or answers.get("feature_tracking") in issue_values
            )

        return True

    def go_forward():
        nonlocal current_question

        if question["id"] == "starting_point":
            if answers.get("starting_point") == "pre-production":
                answers["starting_series"] = 0
            elif answers.get("starting_point") == "production":
                answers["starting_series"] = 1
            elif answers.get("starting_point") == "re-production":
                answers["starting_series"] = dialog.starting_series_number.value()

        if question["id"] == "project_name":
            name = dialog.project_name.text().strip()

            if not name:
                return

            answers["project_name"] = name

        if question["id"] not in answers:
            return

        current_question += 1

        while current_question < len(QUESTIONS):
            next_question = QUESTIONS[current_question]

            if question_applies(next_question["id"]):
                break

            current_question += 1

        if current_question < len(QUESTIONS):
            show_question(current_question)
        else:
            if validate_configuration():
                print("Configuration complete:", answers)
                dialog.accept()
            else:
                print("Invalid configuration:", answers)

    def go_back():
        nonlocal current_question

        current_question -= 1

        while current_question >= 0:
            previous_question = QUESTIONS[current_question]

            if question_applies(previous_question["id"]):
                break

            current_question -= 1

        if current_question >= 0:
            show_question(current_question)

    for button in buttons:
        button.toggled.connect(update_details)

    dialog.button_forward.clicked.connect(go_forward)
    dialog.button_back.clicked.connect(go_back)

    ui_file.close()

    return dialog


def main():
    """Launch the GitMap desktop application."""

    app = QApplication(sys.argv)

    if "--structure-dialog" in sys.argv:
        dialog = load_structure_dialog()
        dialog.exec()
        return

    if "--item-editor" in sys.argv:
        editor = load_item_editor()
        editor.exec()
        return

    active_roadmap_path = None
    active_roadmap = None
    roadmap_is_active = False
    selected_roadmap_object = None
    item_editor_window = None

    ui_path = Path(__file__).with_name("main_window.ui")

    ui_file = QFile(str(ui_path))
    ui_file.open(QFile.OpenModeFlag.ReadOnly)

    loader = QUiLoader()
    window = loader.load(ui_file)

    # --- Roadmap Tree ---
    # Finds the roadmap display created in Qt Designer.
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

    # --- Open Roadmap ---
    # Lets the user choose an existing GitMap Markdown roadmap.

    def populate_roadmap_tree(tree, roadmap):
        tree.clear()

        test_item = QTreeWidgetItem([roadmap.name])
        tree.addTopLevelItem(test_item)

        for milestone in roadmap.milestones:
            milestone_item = QTreeWidgetItem([f"{milestone.number} {milestone.title}"])
            milestone_item.setData(0, MODEL_ROLE, milestone)
            milestone_font = QFont()
            milestone_font.setBold(True)
            milestone_item.setFont(0, milestone_font)

            milestone_item.setData(
                0,
                Qt.ItemDataRole.ForegroundRole,
                QColor("#008B8B"),
            )

            test_item.addChild(milestone_item)

            for section in milestone.sections:
                section_item = QTreeWidgetItem([f"{section.number} {section.title}"])
                section_item.setData(0, MODEL_ROLE, section)
                section_font = QFont()
                section_font.setBold(True)
                section_item.setFont(0, section_font)

                section_item.setForeground(0, QColor("#D49A00"))

                milestone_item.addChild(section_item)

                for issue in section.issues:
                    add_issue_to_tree(section_item, issue)

                for feature in section.features:
                    feature_item = QTreeWidgetItem(
                        [f"{feature.number} {feature.title}"]
                    )
                    feature_item.setData(0, MODEL_ROLE, feature)

                    feature_font = QFont()
                    feature_font.setBold(True)
                    feature_item.setFont(0, feature_font)
                    feature_item.setForeground(0, QColor("#C05050"))

                    section_item.addChild(feature_item)

                    for issue in feature.issues:
                        add_issue_to_tree(feature_item, issue)

        tree.expandAll()
        return test_item

    def open_roadmap():
        nonlocal active_roadmap_path, active_roadmap, roadmap_is_active

        roadmap_path, _ = QFileDialog.getOpenFileName(
            window,
            "Open Roadmap",
            "",
            "Markdown Roadmaps (*.md);;All Files (*.*)",
        )

        if not roadmap_path:
            return

        print(f"Selected roadmap: {roadmap_path}")

        try:
            roadmap = parse_roadmap(roadmap_path)
        except (OSError, UnicodeError) as error:
            print(f"Failed to open roadmap: {roadmap_path}")
            print(f"Error: {error}")
            traceback.print_exc()

            QMessageBox.critical(
                window,
                "Unable to Open Roadmap",
                f"GitMap could not open the selected roadmap.\n\n"
                f"File: {roadmap_path}\n\n"
                f"Error: {error}",
            )

            return

        active_roadmap_path = roadmap_path
        active_roadmap = roadmap

        roadmap_name.setText(roadmap.name)
        print(vars(roadmap))

        populate_roadmap_tree(roadmap_tree, roadmap)

        roadmap_is_active = True

    def selection_changed(item, previous_item):
        nonlocal selected_roadmap_object

        model = item.data(0, MODEL_ROLE)
        selected_roadmap_object = model

        edit_roadmap_button.setEnabled(model is not None)

    roadmap_tree.currentItemChanged.connect(selection_changed)

    def open_selected_item_editor():
        nonlocal item_editor_window

        if selected_roadmap_object is None:
            return

        item_editor_window = load_item_editor()
        item_editor_window.roadmap_object = selected_roadmap_object
        item_editor_window.roadmap = active_roadmap

        preview_text = item_editor_window.findChild(QTreeWidget, "preview_text")
        preview_text.setHeaderHidden(True)
        preview_text.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        populate_roadmap_tree(preview_text, active_roadmap)

        def preview_selection_changed(current, previous):
            if previous is not None:
                previous.setBackground(0, QBrush())

            if current is not None:
                current.setBackground(0, QColor("#3A4A5A"))

        preview_text.currentItemChanged.connect(preview_selection_changed)

        iterator = QTreeWidgetItemIterator(preview_text)

        while iterator.value():
            item = iterator.value()

            if item.data(0, MODEL_ROLE) is selected_roadmap_object:
                preview_text.setCurrentItem(item)
                break

            iterator += 1

        item_editor_window.show()

    def roadmap_item_double_clicked(item, column):
        model = item.data(0, MODEL_ROLE)

        if model is None:
            return

        open_selected_item_editor()

    roadmap_tree.itemDoubleClicked.connect(roadmap_item_double_clicked)
    roadmap_tree.setExpandsOnDoubleClick(False)

    # --- Open Roadmap Button ---
    # Connects the Designer button to the roadmap file picker.
    open_roadmap_button = window.findChild(QPushButton, "Open_Roadmap")

    open_roadmap_button.clicked.connect(open_roadmap)

    new_roadmap_button = window.findChild(QPushButton, "New_Roadmap")
    edit_roadmap_button = window.findChild(QPushButton, "edit_roadmap_button")
    edit_roadmap_button.setEnabled(False)

    edit_roadmap_button.clicked.connect(open_selected_item_editor)

    def create_new_roadmap():
        nonlocal active_roadmap_path, active_roadmap, roadmap_is_active

        structure_dialog = load_structure_dialog()

        result = structure_dialog.exec()

        if not result:
            return

        active_roadmap_path = None

        answers = structure_dialog.answers

        active_roadmap = Roadmap(
            name=answers["project_name"],
        )
        active_roadmap.numbering_mode = answers["numbering"]
        active_roadmap.starting_series = str(answers.get("starting_series", 0))
        active_roadmap.use_sections = answers["use_sections"]
        active_roadmap.use_features = answers["use_features"]
        active_roadmap.allow_issues_under_sections = answers[
            "allow_issues_under_sections"
        ]
        active_roadmap.allow_issues_under_features = answers[
            "allow_issues_under_features"
        ]

        if answers.get("hierarchy") == "labeling":
            active_roadmap.hierarchy_issue_title_style = "type_prefix"
        else:
            active_roadmap.hierarchy_issue_title_style = "plain"

        representation_values = {
            "issues": "issue",
            "labeling": "label",
            "issues_and_labels": "both",
            "blank": None,
        }
        active_roadmap.github_representation = {
            "section": representation_values.get(answers.get("section_tracking")),
            "feature": representation_values.get(answers.get("feature_tracking")),
        }
        roadmap_name.setText(active_roadmap.name)
        roadmap_is_active = True

    new_roadmap_button.clicked.connect(create_new_roadmap)

    ui_file.close()

    window.show()

    sys.exit(app.exec())


# ============================================================
# MODULE ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
