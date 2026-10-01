from gitmap.github_sync.repository import RepositoryInfo


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
