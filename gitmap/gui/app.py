# ============================================================
# MAIN GITMAP WINDOW
# Loads the GitMap interface created in Qt Designer.
# ============================================================

import sys
from pathlib import Path

from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QPushButton,
    QTreeWidget,
    QTreeWidgetItem,
)

from gitmap.parser import parse_roadmap


def add_issue_to_tree(parent_item, issue):
    """Add an issue and its contents to the roadmap tree."""

    issue_item = QTreeWidgetItem([f"{issue.number} {issue.title}"])
    parent_item.addChild(issue_item)

    # --- Requirements ---
    for requirement in issue.requirements:
        requirement_text = requirement.text

        if requirement_text.startswith("[ ] "):
            requirement_text = requirement_text[4:]

        requirement_item = QTreeWidgetItem([requirement_text])
        requirement_item.setCheckState(0, Qt.CheckState.Unchecked)

        issue_item.addChild(requirement_item)

    # --- Work Steps ---
    for work_step in issue.work_steps:
        work_step_item = QTreeWidgetItem(
            [f"({work_step.work_step_marker}) {work_step.title}"]
        )
        issue_item.addChild(work_step_item)


def main():
    """Launch the GitMap desktop application."""

    app = QApplication(sys.argv)

    ui_path = Path(__file__).with_name("main_window.ui")

    ui_file = QFile(str(ui_path))
    ui_file.open(QFile.OpenModeFlag.ReadOnly)

    loader = QUiLoader()
    window = loader.load(ui_file)

    # --- Roadmap Tree ---
    # Finds the roadmap display created in Qt Designer.
    roadmap_tree = window.findChild(QTreeWidget, "roadmap_Tree")
    roadmap_tree.setHeaderHidden(True)

    # --- Open Roadmap ---
    # Lets the user choose an existing GitMap Markdown roadmap.
    def open_roadmap():
        roadmap_path, _ = QFileDialog.getOpenFileName(
            window,
            "Open Roadmap",
            "",
            "Markdown Roadmaps (*.md);;All Files (*.*)",
        )

        if not roadmap_path:
            return

        print(f"Selected roadmap: {roadmap_path}")

        roadmap = parse_roadmap(roadmap_path)
        print(vars(roadmap))

        # --- Display Roadmap ---
        # Temporary test to prove we can write to the Designer tree.
        roadmap_tree.clear()

        test_item = QTreeWidgetItem([roadmap.name])
        roadmap_tree.addTopLevelItem(test_item)

        for milestone in roadmap.milestones:
            milestone_item = QTreeWidgetItem([f"{milestone.number} {milestone.title}"])

            test_item.addChild(milestone_item)

            for section in milestone.sections:
                section_item = QTreeWidgetItem([f"{section.number} {section.title}"])

                milestone_item.addChild(section_item)

                for feature in section.features:
                    feature_item = QTreeWidgetItem(
                        [f"{feature.number} {feature.title}"]
                    )

                    section_item.addChild(feature_item)

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

        test_item.addChild(milestone_item)
        test_item.setExpanded(True)

        print(f"Parsed roadmap: {roadmap}")

    # --- Open Roadmap Button ---
    # Connects the Designer button to the roadmap file picker.
    open_roadmap_button = window.findChild(QPushButton, "Open_Roadmap")

    open_roadmap_button.clicked.connect(open_roadmap)

    ui_file.close()

    window.show()

    sys.exit(app.exec())


# ============================================================
# MODULE ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
