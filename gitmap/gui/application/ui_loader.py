from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


def find_ui_file(filename: str, calling_file: str | Path) -> Path:
    """Find a UI file in the local folder, user_interfaces folder, or project."""

    calling_path = Path(calling_file).resolve()
    local_folder = calling_path.parent

    # 1. Same folder as the calling Python file
    candidate = local_folder / filename
    if candidate.is_file():
        return candidate

    # Find the GitMap package directory.
    package_root = Path(__file__).resolve().parent.parent

    # 2. Central user_interfaces folder
    ui_folder = package_root / "gui" / "user_interfaces"
    candidate = ui_folder / filename
    if candidate.is_file():
        return candidate

    # 3. Entire GitMap package/project
    matches = list(package_root.rglob(filename))

    if len(matches) == 1:
        return matches[0]

    if len(matches) > 1:
        locations = "\n".join(str(path) for path in matches)

        raise RuntimeError(
            f"Multiple UI files named {filename!r} were found:\n{locations}"
        )

    raise FileNotFoundError(
        f"Unable to find UI file: {filename}"
    )


def load_ui(filename: str, calling_file: str | Path):
    """Find and load a Qt Designer UI file."""

    ui_path = find_ui_file(filename, calling_file)

    ui_file = QFile(str(ui_path))

    if not ui_file.open(QFile.ReadOnly):
        raise RuntimeError(
            f"Unable to open UI file: {ui_path}"
        )

    try:
        loader = QUiLoader()
        widget = loader.load(ui_file)
    finally:
        ui_file.close()

    if widget is None:
        raise RuntimeError(
            f"Unable to load UI file: {ui_path}"
        )

    return widget