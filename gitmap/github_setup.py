from dataclasses import dataclass
import os
from github import Github

@dataclass
class RepositoryInfo:
    username: str
    repository: str

    @property
    def full_name(self):
        return f"{self.username}/{self.repository}"

def get_github_token():
    """Retrieve the GitHub authentication token from the environment."""

    token = os.getenv("GITHUB_TOKEN")

    if not token:
        raise ValueError("GitHub authentication token is not configured.")

    return token

def verify_repository(info):
    """Verify that GitMap can access the selected GitHub repository."""

    token = get_github_token()
    github = Github(token)

    repository = github.get_repo(info.full_name)

    return repository

def collect_repository_info():
    """Ask the user which GitHub repository GitMap should use."""

    username = input("GitHub username: ").strip()
    repository = input("Repository name: ").strip()


    if "/" in username or "/" in repository:
        raise ValueError("Enter the GitHub username and repository name separately.")
    if not username or not repository:
        raise ValueError("Github username and repository name are required.")

    return RepositoryInfo(
        username=username,
        repository=repository,
    )