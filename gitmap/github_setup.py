import os
import subprocess
from dataclasses import dataclass
from getpass import getpass

from github import Auth, Github, GithubException


@dataclass
class RepositoryInfo:
    username: str
    repository: str

    @property
    def full_name(self):
        return f"{self.username}/{self.repository}"


def get_github_token():
    """Retrieve the GitHub authentication token."""

    token = os.getenv("GITHUB_TOKEN")

    if not token:
        result = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True,
            text=True,
            check=False,
        )

        if result.returncode == 0:
            token = result.stdout.strip()

    if not token:
        token = getpass("GitHub token: ").strip()

    if not token:
        raise ValueError("GitHub authentication token is required.")

    return token


def verify_repository(info):
    """Verify that GitMap can access the selected GitHub repository."""

    token = get_github_token()
    auth = Auth.Token(token)
    github = Github(auth=auth)

    try:
        repository = github.get_repo(info.full_name)
    except GithubException:
        raise ValueError(
            f"Could not access GitHub repository '{info.full_name}'."
        ) from None

    return repository


def collect_repository_info():
    """Ask the user which GitHub repository GitMap should use."""

    print("\nChoose Repository")
    print("1. Use an existing repository")
    print("2. Create a new repository")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":
        username = input("GitHub username: ").strip()
        repository = input("Repository name: ").strip()

        if "/" in username or "/" in repository:
            raise ValueError(
                "Enter the GitHub username and repository name separately."
            )

        if not username or not repository:
            raise ValueError("GitHub username and repository name are required.")

        return RepositoryInfo(
            username=username,
            repository=repository,
        )

    if choice == "2":
        raise NotImplementedError("Create repository will be implemented in #260.")

    raise ValueError("Choose 1 or 2.")
