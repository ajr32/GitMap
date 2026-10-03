from pathlib import Path
import json
import urllib.error
import urllib.request

from PySide6.QtCore import QFile, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QLineEdit, QMessageBox

from gitmap.gui.application.ui_loader import load_ui
from gitmap.settings import (
    load_github_token,
    load_github_username,
    save_github_settings,
)

GITHUB_API_VERSION = "2026-03-10"


def load_settings_dialog():
    """Load and configure the Settings dialog."""

    dialog = load_ui("settings_dialog.ui",__file__)

    # -------------------------------------------------------------------------
    # Load Saved Settings
    # -------------------------------------------------------------------------

    dialog.github_username.setText(load_github_username())

    dialog.github_token.setText(load_github_token())

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
        username = dialog.github_username.text().strip()
        token = dialog.github_token.text().strip()

        if not username:
            dialog.connection_status.setText(
                "Enter your GitHub username"
            )
            return

        if not token:
            dialog.connection_status.setText(
                "Enter your Personal Access Token"
            )
            return

        dialog.connection_status.setText(
            "Testing connection..."
        )

        request = urllib.request.Request(
            "https://api.github.com/user",
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {token}",
                "X-GitHub-Api-Version": GITHUB_API_VERSION,
                "User-Agent": "GitMap",
            },
        )

        try:
            with urllib.request.urlopen(
                request,
                timeout=10,
            ) as response:
                data = json.loads(
                    response.read().decode("utf-8")
                )

        except urllib.error.HTTPError as error:
            if error.code == 401:
                dialog.connection_status.setText(
                    "Invalid token"
                )
            elif error.code == 403:
                dialog.connection_status.setText(
                    "GitHub denied access"
                )
            else:
                dialog.connection_status.setText(
                    f"GitHub error: {error.code}"
                )

            return

        except urllib.error.URLError:
            dialog.connection_status.setText(
                "Unable to reach GitHub"
            )
            return

        except TimeoutError:
            dialog.connection_status.setText(
                "GitHub connection timed out"
            )
            return

        authenticated_username = data.get("login", "")

        if authenticated_username.lower() != username.lower():
            dialog.connection_status.setText(
                f"Token belongs to {authenticated_username}"
            )

            QMessageBox.warning(
                dialog,
                "GitHub Account Mismatch",
                (
                    "The Personal Access Token is valid, "
                    "but it belongs to a different GitHub account.\n\n"
                    f"Entered username: {username}\n"
                    f"Token account: {authenticated_username}"
                ),
            )

            return

        dialog.connection_status.setText(
            f"Connected as {authenticated_username}"
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
        username = dialog.github_username.text().strip()
        token = dialog.github_token.text().strip()

        if not username:
            QMessageBox.warning(
                dialog,
                "GitHub Username Required",
                "Enter your GitHub username before saving.",
            )
            return

        if not token:
            QMessageBox.warning(
                dialog,
                "GitHub Token Required",
                "Enter your GitHub Personal Access Token before saving.",
            )
            return

        try:
            save_github_settings(
                username,
                token,
            )
        except Exception as error:
            QMessageBox.critical(
                dialog,
                "Unable to Save Settings",
                f"GitMap could not save the settings.\n\n{error}",
            )
            return

        dialog.accept()

    dialog.save_button.clicked.connect(
        save_settings
    )

    return dialog