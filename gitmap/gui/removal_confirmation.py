from PySide6.QtWidgets import QMessageBox


def confirm_sync_removals(
    parent,
    removed_issues,
    removed_hierarchy,
):
    """Confirm planned GitHub removals before synchronization."""

    total = len(removed_issues) + len(removed_hierarchy)

    if total == 0:
        return True

    lines = [
        "GitMap will remove the following items from GitHub:",
        "",
    ]

    if removed_issues:
        lines.append(f"Normal Issues: {len(removed_issues)}")

        for item_id in removed_issues:
            lines.append(f"  • {item_id}")

    if removed_hierarchy:
        lines.append("")
        lines.append(f"Hierarchy Issues: {len(removed_hierarchy)}")

        for item_id in removed_hierarchy:
            lines.append(f"  • {item_id}")

    lines.extend(
        [
            "",
            "Continue with synchronization?",
        ]
    )

    result = QMessageBox.warning(
        parent,
        "Confirm GitHub Removals",
        "\n".join(lines),
        QMessageBox.Yes | QMessageBox.No,
        QMessageBox.No,
    )

    return result == QMessageBox.Yes