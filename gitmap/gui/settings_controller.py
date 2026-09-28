from pathlib import Path

from PySide6.QtCore import QFile, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QLineEdit


def load_settings_dialog():
    """Load and configure the Settings dialog."""

    ui_path = Path(__file__).with_name("settings_dialog.ui")

    ui_file = QFile(str(ui_path))

    if not ui_file.open(QFile.ReadOnly):
        raise RuntimeError(
            f"Unable to open settings UI: {ui_path}"
        )

    loader = QUiLoader()
    dialog = loader.load(ui_file)

    ui_file.close()

    if dialog is None:
        raise RuntimeError(
            f"Unable to load settings UI: {ui_path}"
        )

    # -------------------------------------------------------------------------
    # Create GitHub Token
    # -------------------------------------------------------------------------

    def open_github_token_page():
        QDesktopServices.openUrl(
            QUrl(
                "https://github.com/settings/"
                "personal-access-tokens/new"
            )
        )

    dialog.get_token_button.clicked.connect(
        open_github_token_page
    )

    # -------------------------------------------------------------------------
    # Test GitHub Connection
    # -------------------------------------------------------------------------

    def test_connection():
        # Actual GitHub connection testing comes next.
        dialog.connection_status.setText(
            "Testing not connected yet"
        )

    dialog.test_connection_button.clicked.connect(
        test_connection
    )

    # -------------------------------------------------------------------------
    # Show / Hide GitHub Token
    # -------------------------------------------------------------------------

    def toggle_token_visibility(checked):
        if checked:
            dialog.github_token.setEchoMode(
                QLineEdit.EchoMode.Normal
            )
            dialog.show_token_button.setText("Hide")
        else:
            dialog.github_token.setEchoMode(
                QLineEdit.EchoMode.Password
            )
            dialog.show_token_button.setText("Show")

    dialog.show_token_button.toggled.connect(
        toggle_token_visibility
    )

    # -------------------------------------------------------------------------
    # Cancel
    # -------------------------------------------------------------------------

    dialog.cancel_button.clicked.connect(
        dialog.reject
    )

    # -------------------------------------------------------------------------
    # Save
    # -------------------------------------------------------------------------

    def save_settings():
        # Settings persistence will be added later.
        dialog.accept()

    dialog.save_button.clicked.connect(
        save_settings
    )

    return dialog