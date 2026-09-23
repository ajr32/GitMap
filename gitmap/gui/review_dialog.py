import copy
from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QLabel, QListWidget, QPushButton, QTreeWidget

from gitmap.gui.roadmap_tree import populate_roadmap_tree


def load_review_dialog(before_roadmap, after_roadmap):
    """Load the Roadmap Review window."""

    ui_path = Path(__file__).with_name("changes_screen.ui")

    ui_file = QFile(str(ui_path))
    ui_file.open(QFile.OpenModeFlag.ReadOnly)

    loader = QUiLoader()
    dialog = loader.load(ui_file)

    # TEST
    for tree in dialog.findChildren(QTreeWidget):
        print("TREE:", tree.objectName())

    ui_file.close()

    # Find Review Changes widgets.
    before_tree = dialog.findChild(QTreeWidget, "Changes_Before")
    after_tree = dialog.findChild(QTreeWidget, "Changes_after")
    changes_list = dialog.findChild(QListWidget, "changes_list")
    no_changes_label = dialog.findChild(QLabel, "no_changes_label")

    # Find filter buttons.
    filter_buttons = {
        "all": dialog.findChild(QPushButton, "button_changes"),
        "added": dialog.findChild(QPushButton, "button_add"),
        "removed": dialog.findChild(QPushButton, "button_removed"),
        "renumbered": dialog.findChild(QPushButton, "button_renumber"),
        "retitled": dialog.findChild(QPushButton, "button_retitled"),
        "hierarchy": dialog.findChild(QPushButton, "button_hierarchy"),
        "unchanged": dialog.findChild(QPushButton, "button_unchanged"),
    }

    # Hide the tree headers.
    before_tree.setHeaderHidden(True)
    after_tree.setHeaderHidden(True)

    # Always populate the Before tree.
    populate_roadmap_tree(before_tree, before_roadmap)

    # Compare copies so the editor-only is_modified flag
    # does not count as an actual roadmap change.
    before_compare = copy.deepcopy(before_roadmap)
    after_compare = copy.deepcopy(after_roadmap)

    before_compare.is_modified = False
    after_compare.is_modified = False

    # Show the centered "No Changes" message only when
    # the two roadmaps are otherwise identical.
    if before_compare == after_compare:
        after_tree.clear()
        no_changes_label.show()
        no_changes_label.raise_()
    else:
        no_changes_label.hide()
        populate_roadmap_tree(after_tree, after_roadmap)

    def select_filter(selected_name):
        """Select one Review Changes filter button."""

        for name, button in filter_buttons.items():
            if button is None:  # TEST
                print(f"MISSING FILTER BUTTON: {name}")
                continue

            is_selected = name == selected_name
            button.setChecked(is_selected)

            if is_selected:
                button.setStyleSheet("""
                    QPushButton {
                        background-color: gold;
                        color: black;
                        font-weight: bold;
                    }
                """)
            else:
                button.setStyleSheet("""
                    QPushButton {
                        background-color: white;
                        color: black;
                        font-weight: normal;
                    }
                """)

    for name, button in filter_buttons.items():
        button.clicked.connect(
            lambda checked=False, filter_name=name: select_filter(filter_name)
        )

    # All Changes is the default filter.
    select_filter("all")

    return dialog
