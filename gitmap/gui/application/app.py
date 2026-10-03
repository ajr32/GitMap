import sys
from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication

from gitmap.gui.application.ui_loader import load_ui
from gitmap.gui.controller.main_window_controller import setup_main_window


def load_main_window():
    window = load_ui("main_window.ui", __file__)

    return window


def main():
    app = QApplication(sys.argv)

    main_window = load_main_window()
    setup_main_window(main_window)
    main_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()