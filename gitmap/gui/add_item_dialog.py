from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QLabel, QPushButton, QRadioButton


def load_add_item_dialog():
    ui_path = Path(__file__).with_name("add_item_dialog.ui")

    ui_file = QFile(str(ui_path))
    ui_file.open(QFile.OpenModeFlag.ReadOnly)

    loader = QUiLoader()
    dialog = loader.load(ui_file)

    ui_file.close()

    cancel_button = dialog.findChild(QPushButton, "add_cancel_button")
    # cancel_button.clicked.connect(dialog.close)

    dialog.add_question_label = dialog.findChild(QLabel, "add_question_label")

    dialog.add_options = [
        dialog.findChild(QRadioButton, "add_option_1"),
        dialog.findChild(QRadioButton, "add_option_2"),
        dialog.findChild(QRadioButton, "add_option_3"),
        dialog.findChild(QRadioButton, "add_option_4"),
    ]

    dialog.add_continue_button = dialog.findChild(QPushButton, "add_continue_button")

    return dialog
