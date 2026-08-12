"""Tests for the GitHub client."""

from gitmap.github import GitHubClient


def test_repository_name():
    """The client builds the expected repository name."""

    client = GitHubClient(
        username="example-user",
        repository="gitmap",
    )

    assert client.repository_name() == "example-user/gitmap"