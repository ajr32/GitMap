from PySide6.QtWidgets import QLabel, QPushButton, QRadioButton

from gitmap.gui.application.ui_loader import load_ui


def load_add_item_dialog():
    dialog = load_ui("add_item_dialog.ui",__file__)

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
