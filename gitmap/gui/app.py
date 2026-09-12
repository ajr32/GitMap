# ============================================================
# MAIN GITMAP WINDOW
# Loads the GitMap interface created in Qt Designer.
# ============================================================

import sys
import traceback
from pathlib import Path

from PySide6.QtCore import QFile, Qt
from PySide6.QtGui import QColor, QFont
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QTreeWidget,
    QTreeWidgetItem,
)
from structure_questions import QUESTIONS

from gitmap.parser import parse_roadmap


def add_issue_to_tree(parent_item, issue):
    """Add an issue and its contents to the roadmap tree."""

    issue_item = QTreeWidgetItem([f"{issue.number} {issue.title}"])
    parent_item.addChild(issue_item)

    print("\nISSUE:", issue.number, issue.title)

    for requirement in issue.requirements:
        print("  REQUIREMENT:", repr(requirement.text))

    for work_step in issue.work_steps:
        print("  WORK STEP:", repr(work_step.title))

    # --- Requirements ---
    for requirement in issue.requirements:
        requirement_text = requirement.text

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

        requirement_item = QTreeWidgetItem([requirement_text])

        issue_item.setForeground(0, QColor("#707070"))

        requirement_font = QFont()
        requirement_font.setItalic(True)
        requirement_item.setFont(0, requirement_font)
        requirement_item.setForeground(0, QColor("#808080"))

        issue_item.addChild(requirement_item)

    # --- Work Steps ---
    for work_step in issue.work_steps:
        work_step_item = QTreeWidgetItem(
            [f"{work_step.work_step_marker} {work_step.title}"]
        )

        work_step_item.setForeground(0, QColor("#4F8A5B"))

        issue_item.addChild(work_step_item)


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

    answers = {}

    dialog.structure_subject.setText(question["subject"])
    dialog.structure_subject.adjustSize()
    dialog.structure_question.setPlainText(question["question"])
    # dialog.structure_question.adjustSize()
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

    def update_details():
        for index, button in enumerate(buttons):
            if button.isChecked() and index < len(question["options"]):
                option = question["options"][index]

                answers[question["id"]] = option["value"]

                if question["id"] == "starting_point":
                    dialog.starting_series_number.setVisible(
                        option["value"] == "re-production"
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
            return answers.get("structure") in ("sections", "sections_and_features")

        if question_id == "feature_tracking":
            return answers.get("structure") == "sections_and_features"

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
            print("Configuration complete:", answers)
            dialog.accept()

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

    active_roadmap_path = None
    active_roadmap = None
    roadmap_is_active = False

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
            background-color: white;
            color: black;
        }
    """)
    roadmap_name = window.findChild(QTextEdit, "textEdit")
    roadmap_name.setReadOnly(True)

    # --- Open Roadmap ---
    # Lets the user choose an existing GitMap Markdown roadmap.
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

        # --- Display Roadmap ---
        # Temporary test to prove we can write to the Designer tree.
        roadmap_tree.clear()

        test_item = QTreeWidgetItem([roadmap.name])
        roadmap_tree.addTopLevelItem(test_item)

        for milestone in roadmap.milestones:
            milestone_item = QTreeWidgetItem([f"{milestone.number} {milestone.title}"])
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

                section_font = QFont()
                section_font.setBold(True)
                section_item.setFont(0, section_font)

                section_item.setForeground(0, QColor("#D49A00"))

                milestone_item.addChild(section_item)

                for feature in section.features:
                    feature_item = QTreeWidgetItem(
                        [f"{feature.number} {feature.title}"]
                    )

                    section_item.addChild(feature_item)

                    feature_font = QFont()
                    feature_font.setBold(True)
                    feature_item.setFont(0, feature_font)

                    for issue in feature.issues:
                        add_issue_to_tree(feature_item, issue)

                    # for issue in feature.issues:
                    #     issue_item = QTreeWidgetItem([f"{issue.number} {issue.title}"])
                    #
                    #     feature_item.addChild(issue_item)
                    #
                    #     # --- Issue Requirements ---
                    #     for requirement in issue.requirements:
                    #         requirement_item = QTreeWidgetItem([requirement.text])
                    #
                    #         issue_item.addChild(requirement_item)
                    #
                    #     # --- Issue Work Steps ---
                    #     for work_step in issue.work_steps:
                    #         work_step_item = QTreeWidgetItem(
                    #             [f"({work_step.work_step_marker}) {work_step.title}"]
                    #         )
                    #
                    #         issue_item.addChild(work_step_item)

                # --- Issues Directly Under Section ---
                for issue in section.issues:
                    add_issue_to_tree(section_item, issue)

            # --- Issues Directly Under Milestone ---
            for issue in milestone.issues:
                add_issue_to_tree(milestone_item, issue)

        roadmap_tree.expandAll()

        test_item.setExpanded(True)

        roadmap_is_active = True

        print(f"Parsed roadmap: {roadmap}")

    # --- Open Roadmap Button ---
    # Connects the Designer button to the roadmap file picker.
    open_roadmap_button = window.findChild(QPushButton, "Open_Roadmap")

    open_roadmap_button.clicked.connect(open_roadmap)

    new_roadmap_button = window.findChild(QPushButton, "New_Roadmap")

    def create_new_roadmap():
        structure_dialog = load_structure_dialog()
        structure_dialog.exec()

    new_roadmap_button.clicked.connect(create_new_roadmap)

    ui_file.close()

    window.show()

    sys.exit(app.exec())


# ============================================================
# MODULE ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
