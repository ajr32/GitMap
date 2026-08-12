"""Tests for the GitHub client."""

from gitmap.github import GitHubClient


def test_repository_name():
    """The client builds the expected repository name."""

    client = GitHubClient(
        username="example-user",
        repository="gitmap",
    )

    assert client.repository_name() == "example-user/gitmap"

def test_client_is_authenticated_with_token():
    """A client with a token reports authenticated."""

    client = GitHubClient(
        username="example-user",
        repository="gitmap",
        token="test-token",
    )

    assert client.is_authenticated()


def test_client_is_not_authenticated_without_token():
    """A client without a token reports unauthenticated."""

    client = GitHubClient(
        username="example-user",
        repository="gitmap",
    )

    assert not client.is_authenticated()