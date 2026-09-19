from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


def load_review_dialog():
    """Load the Roadmap Review window."""

    ui_path = Path(__file__).with_name("changes_screen.ui")

    ui_file = QFile(str(ui_path))
    ui_file.open(QFile.OpenModeFlag.ReadOnly)

    loader = QUiLoader()
    dialog = loader.load(ui_file)

    ui_file.close()

    return dialog