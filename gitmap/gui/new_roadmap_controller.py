from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from gitmap.gui.structure_questions import QUESTIONS
from gitmap.models import Roadmap


def load_structure_dialog():
    """Load and configure the New Roadmap questionnaire."""

    ui_path = Path(__file__).with_name("structure_dialog.ui")

    ui_file = QFile(str(ui_path))
    ui_file.open(QFile.OpenModeFlag.ReadOnly)

    loader = QUiLoader()
    dialog = loader.load(ui_file)
    ui_file.close()

    current_question = 0
    question = QUESTIONS[current_question]

    dialog.starting_series_number.hide()
    dialog.project_name.hide()

    answers = {}
    dialog.answers = answers

    buttons = [
        dialog.Button1,
        dialog.Button2,
        dialog.Button3,
        dialog.Button4,
    ]

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
            if not button.isChecked():
                continue

            if index >= len(question["options"]):
                continue

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

            if question["id"] == "feature_tracking":
                answers["allow_issues_under_features"] = option["value"] in (
                    "issues",
                    "issues_and_labels",
                )

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
            issue_values = (
                "issues",
                "issues_and_labels",
            )

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
            return

        if validate_configuration():
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

    show_question(0)

    return dialog


def build_roadmap_from_answers(answers):
    """Create a new unsaved Roadmap from questionnaire answers."""

    roadmap = Roadmap(
        name=answers["project_name"],
    )

    roadmap.numbering_mode = answers["numbering"]
    roadmap.starting_series = str(answers.get("starting_series", 0))

    roadmap.use_sections = answers["use_sections"]
    roadmap.use_features = answers["use_features"]

    roadmap.allow_issues_under_sections = answers.get(
        "allow_issues_under_sections",
        False,
    )

    roadmap.allow_issues_under_features = answers.get(
        "allow_issues_under_features",
        False,
    )

    if answers.get("hierarchy") == "labeling":
        roadmap.hierarchy_issue_title_style = "type_prefix"
    else:
        roadmap.hierarchy_issue_title_style = "plain"

    representation_values = {
        "issues": "issue",
        "labeling": "label",
        "issues_and_labels": "both",
        "blank": None,
    }

    roadmap.github_representation = {
        "section": representation_values.get(answers.get("section_tracking")),
        "feature": representation_values.get(answers.get("feature_tracking")),
    }

    return roadmap
