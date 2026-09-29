from pathlib import Path
import json

import keyring


SETTINGS_FILE = Path.home() / ".gitmap" / "settings.json"
KEYRING_SERVICE = "GitMap"


def save_github_settings(username, token):
    """Save GitHub settings."""

    SETTINGS_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    SETTINGS_FILE.write_text(
        json.dumps(
            {
                "github_username": username,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    keyring.set_password(
        KEYRING_SERVICE,
        "github_token",
        token,
    )


def load_github_username():
    """Load the saved GitHub username."""

    if not SETTINGS_FILE.exists():
        return ""

    try:
        data = json.loads(
            SETTINGS_FILE.read_text(
                encoding="utf-8",
            )
        )
    except (OSError, json.JSONDecodeError):
        return ""

    return data.get("github_username", "")


def load_github_token():
    """Load the GitHub token from secure credential storage."""

    return (
        keyring.get_password(
            KEYRING_SERVICE,
            "github_token",
        )
        or ""
    )