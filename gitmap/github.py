"""GitHub integration for GitMap."""

from dataclasses import dataclass


@dataclass
class GitHubClient:
    """Connect to a GitHub repository."""

    username: str
    repository: str

    def repository_name(self) -> str:
        """Return the full GitHub repository name."""

        return f"{self.username}/{self.repository}"