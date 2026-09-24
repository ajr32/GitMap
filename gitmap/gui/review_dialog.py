import copy
from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QLabel, QListWidget, QPushButton, QTreeWidget

from gitmap.gui.roadmap_tree import populate_roadmap_tree


def collect_roadmap_items(roadmap):
    """Collect GitMap-managed roadmap items for change comparison."""

    items = {}

    for milestone in roadmap.milestones:
        for section in milestone.sections:
            if section.gitmap_id:
                items[section.gitmap_id] = {
                    "type": "section",
                    "number": section.number,
                    "title": section.title,
                }

            for feature in section.features:
                if feature.gitmap_id:
                    items[feature.gitmap_id] = {
                        "type": "feature",
                        "number": feature.number,
                        "title": feature.title,
                    }

                for issue in feature.issues:
                    item_id = issue.gitmap_id or f"new:{issue.number}"

                    items[item_id] = {
                        "type": "issue",
                        "number": issue.number,
                        "title": issue.title,
                    }

            for issue in section.issues:
                item_id = issue.gitmap_id or f"new:{issue.number}"

                items[item_id] = {
                    "type": "issue",
                    "number": issue.number,
                    "title": issue.title,
                }

        for issue in milestone.issues:
            item_id = issue.gitmap_id or f"new:{issue.number}"

            items[item_id] = {
                "type": "issue",
                "number": issue.number,
                "title": issue.title,
            }

    return items


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

        # TEST
    before_items = collect_roadmap_items(before_roadmap)
    after_items = collect_roadmap_items(after_roadmap)

    # TEST
    added_ids = set(after_items) - set(before_items)
    removed_ids = set(before_items) - set(after_items)

    # TEST
    before_items = collect_roadmap_items(before_roadmap)
    after_items = collect_roadmap_items(after_roadmap)

    # TEST
    added_ids = set(after_items) - set(before_items)
    removed_ids = set(before_items) - set(after_items)

    common_ids = set(before_items) & set(after_items)

    retitled_ids = {
        item_id
        for item_id in common_ids
        if before_items[item_id]["title"] != after_items[item_id]["title"]
    }

    unchanged_ids = {
        item_id
        for item_id in common_ids
        if before_items[item_id]["number"] == after_items[item_id]["number"]
        and before_items[item_id]["title"] == after_items[item_id]["title"]
    }

    for item_id in common_ids:  # TEST
        if before_items[item_id]["title"] != after_items[item_id]["title"]:
            print(
                "TITLE CHANGE:",
                repr(before_items[item_id]["title"]),
                "->",
                repr(after_items[item_id]["title"]),
                "ID:",
                item_id,
            )

    renumbered_ids = {
        item_id
        for item_id in common_ids
        if before_items[item_id]["number"] != after_items[item_id]["number"]
    }

    print("ADDED:", len(added_ids))
    print("REMOVED:", len(removed_ids))
    print("RENUMBERED:", len(renumbered_ids))

    print("BEFORE ITEMS:", len(before_items))
    print("AFTER ITEMS:", len(after_items))
    print("ADDED:", len(added_ids))
    print("REMOVED:", len(removed_ids))

    print("BEFORE ITEMS:", len(before_items))
    print("AFTER ITEMS:", len(after_items))

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
            "Renumbered: N/A",
            f"Retitled: {len(retitled_ids)}",
            "Hierarchy Changes: N/A",
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

        elif selected_name == "retitled":
            retitled_items = [
                (before_items[item_id], after_items[item_id])
                for item_id in retitled_ids
            ]

            issue_count = sum(
                1 for before_item, after_item in retitled_items
                if after_item["type"] == "issue"
            )
            feature_count = sum(
                1 for before_item, after_item in retitled_items
                if after_item["type"] == "feature"
            )
            section_count = sum(
                1 for before_item, after_item in retitled_items
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
                    f'{after_item["number"]}  '
                    f'{before_item["title"]} → {after_item["title"]}'
                )

        elif selected_name == "unchanged":
            unchanged_items = [
                after_items[item_id]
                for item_id in unchanged_ids
            ]

            issue_count = sum(
                1 for item in unchanged_items if item["type"] == "issue"
            )
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
                changes_list.addItem(
                    f'{item["number"]}  {item["title"]}'
                )

    for name, button in filter_buttons.items():
        button.clicked.connect(
            lambda checked=False, filter_name=name: select_filter(filter_name)
        )

    # All Changes is the default filter.
    select_filter("all")

    return dialog
