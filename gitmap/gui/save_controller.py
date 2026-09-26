import copy
from pathlib import Path

from PySide6.QtWidgets import QFileDialog, QMessageBox

from gitmap.builder.builder import (
    render_roadmap_markdown,
    roadmap_to_builder_dict,
)


def save_roadmap(window, state):
    """Save the active roadmap to its Markdown file."""

    if state.active_roadmap is None:
        return False

    path = state.active_roadmap_path

    if path is None:
        path, _ = QFileDialog.getSaveFileName(
            window,
            "Save Roadmap",
            f"{state.active_roadmap.name}.md",
            "Markdown Files (*.md)",
        )

        if not path:
            return False

        if not path.lower().endswith(".md"):
            path += ".md"

    try:
        builder_roadmap = roadmap_to_builder_dict(state.active_roadmap)

        markdown = render_roadmap_markdown(builder_roadmap)

        Path(path).write_text(
            markdown + "\n",
            encoding="utf-8",
        )

    except (OSError, ValueError, TypeError) as error:
        QMessageBox.critical(
            window,
            "Save Failed",
            f"GitMap could not save the roadmap:\n\n{error}",
        )
        return False

    state.active_roadmap_path = str(path)
    state.sync_baseline_roadmap = copy.deepcopy(state.active_roadmap)

    return True
