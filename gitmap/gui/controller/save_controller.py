from pathlib import Path

from PySide6.QtWidgets import QFileDialog

from gitmap.gui.shared.error_display import show_error
from gitmap.roadmap.markdown.serializer import render_roadmap_markdown


def save_roadmap(window, state, save_as=False):
    """Save the active roadmap to its Markdown file."""

    if state.active_roadmap is None:
        return False

    path = state.active_roadmap_path

    if save_as or path is None:
        path, _ = QFileDialog.getSaveFileName(
            window,
            "Save Roadmap As" if save_as else "Save Roadmap",
            f"{state.active_roadmap.name}.md",
            "Markdown Files (*.md)",
        )

        if not path:
            return False

        if not path.lower().endswith(".md"):
            path += ".md"

    try:
        markdown = render_roadmap_markdown(state.active_roadmap)

        Path(path).write_text(
            markdown + "\n",
            encoding="utf-8",
        )

    except (OSError, ValueError, TypeError) as error:
        show_error(
            window,
            "Save Failed",
            "GitMap could not save the roadmap.",
            error=error,
            diagnostic=f"File: {path}",
        )
        return False

    state.active_roadmap_path = str(path)
    state.active_roadmap.is_modified = False

    return True
