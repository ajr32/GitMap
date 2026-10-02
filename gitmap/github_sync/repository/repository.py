from dataclasses import dataclass

from github import Auth, Github, GithubException

from gitmap.settings import load_github_token


@dataclass
class RepositoryInfo:
    username: str
    repository: str

    @property
    def full_name(self):
        return f"{self.username}/{self.repository}"


def get_github_token():
    """Retrieve the GitHub authentication token from GitMap settings."""

    token = load_github_token()

    if not token:
        raise ValueError(
            "GitHub authentication token is not configured. "
            "Open Settings and add a GitHub token."
        )

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


def create_repository(repository_name):
    """Create a new repository for the authenticated GitHub user."""

    if not repository_name:
        raise ValueError("Repository name is required.")

    token = get_github_token()
    auth = Auth.Token(token)
    github = Github(auth=auth)

    try:
        user = github.get_user()

        repository = user.create_repo(
            repository_name,
            private=False,
        )

    except GithubException as error:
        if error.status == 422:
            raise ValueError(
                f"Repository '{repository_name}' already exists "
                "or the repository name is invalid."
            ) from None

        if error.status == 403:
            raise ValueError(
                "GitHub denied permission to create the repository. "
                "Check that the token has Administration: "
                "Read and write permission."
            ) from None

        raise ValueError(
            f"GitHub could not create repository '{repository_name}'."
        ) from None

    return repository
