import copy
from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QLabel, QListWidget, QPushButton, QTreeWidget

from gitmap.gui.roadmap_tree import populate_roadmap_tree
from gitmap.gui.sync_plan import compare_roadmaps


def load_review_dialog(before_roadmap, after_roadmap):
    """Load the Roadmap Review window."""

    ui_path = Path(__file__).with_name("changes_screen.ui")

    ui_file = QFile(str(ui_path))
    ui_file.open(QFile.OpenModeFlag.ReadOnly)

    loader = QUiLoader()
    dialog = loader.load(ui_file)


    ui_file.close()

    # Find Review Changes widgets.
    before_tree = dialog.findChild(QTreeWidget, "Changes_Before")
    after_tree = dialog.findChild(QTreeWidget, "Changes_after")
    changes_list = dialog.findChild(QListWidget, "changes_list")
    no_changes_label = dialog.findChild(QLabel, "no_changes_label")
    changes_list_stats = dialog.findChild(QListWidget, "changes_list_stats")
    changes_detail_label = dialog.findChild(QLabel, "changes_detail_label")

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

    comparison = compare_roadmaps(
        before_roadmap,
        after_roadmap,
    )

    before_items = comparison["before_items"]
    after_items = comparison["after_items"]

    added_ids = comparison["added"]
    removed_ids = comparison["removed"]
    renumbered_ids = comparison["renumbered"]
    retitled_ids = comparison["retitled"]
    hierarchy_ids = comparison["hierarchy"]
    unchanged_ids = comparison["unchanged"]


    # Set up change statistics.
    stat_rows = {
        "added": 0,
        "removed": 1,
        "renumbered": 2,
        "retitled": 3,
        "hierarchy": 4,
        "unchanged": 5,
    }

    changes_list_stats.addItems(
        [
            f"Added: {len(added_ids)}",
            f"Removed: {len(removed_ids)}",
            f"Renumbered: {len(renumbered_ids)}",
            f"Retitled: {len(retitled_ids)}",
            f"Hierarchy Changes: {len(hierarchy_ids)}",
            f"Unchanged: {len(unchanged_ids)}",
        ]
    )

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

        # Highlight the matching statistics row.
        changes_list_stats.clearSelection()

        if selected_name != "all":
            changes_list_stats.setCurrentRow(stat_rows[selected_name])

        # Update the change details.
        changes_list.clear()

        if selected_name == "all":
            changes_detail_label.clear()

        if selected_name == "added":
            added_items = [after_items[item_id] for item_id in added_ids]

            issue_count = sum(1 for item in added_items if item["type"] == "issue")
            feature_count = sum(1 for item in added_items if item["type"] == "feature")
            section_count = sum(1 for item in added_items if item["type"] == "section")

            breakdown = []

            if section_count:
                breakdown.append(
                    f"{section_count} section{'s' if section_count != 1 else ''}"
                )

            if feature_count:
                breakdown.append(
                    f"{feature_count} feature{'s' if feature_count != 1 else ''}"
                )

            if issue_count:
                breakdown.append(
                    f"{issue_count} issue{'s' if issue_count != 1 else ''}"
                )

            changes_detail_label.setText(
                f"Added: {len(added_items)} ({', '.join(breakdown)})"
            )

            for item in added_items:
                changes_list.addItem(f"{item['number']}  {item['title']}")

        elif selected_name == "removed":
            removed_items = [before_items[item_id] for item_id in removed_ids]

            issue_count = sum(1 for item in removed_items if item["type"] == "issue")

            feature_count = sum(
                1 for item in removed_items if item["type"] == "feature"
            )

            section_count = sum(
                1 for item in removed_items if item["type"] == "section"
            )

            breakdown = []

            if section_count:
                breakdown.append(
                    f"{section_count} section{'s' if section_count != 1 else ''}"
                )

            if feature_count:
                breakdown.append(
                    f"{feature_count} feature{'s' if feature_count != 1 else ''}"
                )

            if issue_count:
                breakdown.append(
                    f"{issue_count} issue{'s' if issue_count != 1 else ''}"
                )

            changes_detail_label.setText(
                f"Removed: {len(removed_items)} ({', '.join(breakdown)})"
            )

            for item in sorted(
                removed_items,
                key=lambda value: value["number"],
            ):
                changes_list.addItem(f"{item['number']}  {item['title']}")

        elif selected_name == "renumbered":
            renumbered_items = [
                (before_items[item_id], after_items[item_id])
                for item_id in renumbered_ids
            ]

            changes_detail_label.setText(f"Renumbered: {len(renumbered_items)}")

            for before_item, after_item in sorted(
                renumbered_items,
                key=lambda pair: pair[1]["number"],
            ):
                changes_list.addItem(
                    f"{before_item['number']} → {after_item['number']}  "
                    f"{after_item['title']}"
                )

        elif selected_name == "hierarchy":
            hierarchy_items = [after_items[item_id] for item_id in hierarchy_ids]

            changes_detail_label.setText(f"Hierarchy Changes: {len(hierarchy_items)}")

            for item in sorted(
                hierarchy_items,
                key=lambda value: value["number"],
            ):
                changes_list.addItem(f"{item['number']}  {item['title']}")

        elif selected_name == "retitled":
            retitled_items = [
                (before_items[item_id], after_items[item_id])
                for item_id in retitled_ids
            ]

            issue_count = sum(
                1
                for before_item, after_item in retitled_items
                if after_item["type"] == "issue"
            )
            feature_count = sum(
                1
                for before_item, after_item in retitled_items
                if after_item["type"] == "feature"
            )
            section_count = sum(
                1
                for before_item, after_item in retitled_items
                if after_item["type"] == "section"
            )

            breakdown = []

            if section_count:
                breakdown.append(
                    f"{section_count} section{'s' if section_count != 1 else ''}"
                )

            if feature_count:
                breakdown.append(
                    f"{feature_count} feature{'s' if feature_count != 1 else ''}"
                )

            if issue_count:
                breakdown.append(
                    f"{issue_count} issue{'s' if issue_count != 1 else ''}"
                )

            changes_detail_label.setText(
                f"Retitled: {len(retitled_items)} ({', '.join(breakdown)})"
            )

            for before_item, after_item in retitled_items:
                changes_list.addItem(
                    f"{after_item['number']}  "
                    f"{before_item['title']} → {after_item['title']}"
                )

        elif selected_name == "unchanged":
            unchanged_items = [after_items[item_id] for item_id in unchanged_ids]

            issue_count = sum(1 for item in unchanged_items if item["type"] == "issue")
            feature_count = sum(
                1 for item in unchanged_items if item["type"] == "feature"
            )
            section_count = sum(
                1 for item in unchanged_items if item["type"] == "section"
            )

            breakdown = []

            if section_count:
                breakdown.append(
                    f"{section_count} section{'s' if section_count != 1 else ''}"
                )

            if feature_count:
                breakdown.append(
                    f"{feature_count} feature{'s' if feature_count != 1 else ''}"
                )

            if issue_count:
                breakdown.append(
                    f"{issue_count} issue{'s' if issue_count != 1 else ''}"
                )

            changes_detail_label.setText(
                f"Unchanged: {len(unchanged_items)} ({', '.join(breakdown)})"
            )

            for item in unchanged_items:
                changes_list.addItem(f"{item['number']}  {item['title']}")
                changes_list.addItem(f"{item['number']}  {item['title']}")

    for name, button in filter_buttons.items():
        button.clicked.connect(
            lambda checked=False, filter_name=name: select_filter(filter_name)
        )

    # All Changes is the default filter.
    select_filter("all")

    return dialog
