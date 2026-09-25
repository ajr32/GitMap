import sys
from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from gitmap.gui.main_window_controller import setup_main_window

def load_main_window():
    ui_path = Path(__file__).with_name("main_window.ui")

    ui_file = QFile(str(ui_path))
    ui_file.open(QFile.OpenModeFlag.ReadOnly)

    loader = QUiLoader()
    window = loader.load(ui_file)

    ui_file.close()

    return window


def main():
    app = QApplication(sys.argv)

    main_window = load_main_window()
    setup_main_window(main_window)
    main_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()