"""Interactive roadmap designer for GitMap."""

from gitmap.models import Epic, Milestone, Roadmap


def create_roadmap() -> Roadmap:
    """Create a roadmap through an interactive session."""

    name = input("What are you building? ").strip()
    overview = input("Give me a short overview: ").strip()

    roadmap = Roadmap(
        name=name,
        overview=overview,
    )

    while True:
        number = input("Milestone number (blank when finished): ").strip()

        if not number:
            break

        title = input("Milestone title: ").strip()

        roadmap.milestones.append(
            Milestone(
                number=number,
                title=title,
            )
        )

        while True:
            epic_title = input("Epic title (blank when finished): ").strip()

            if not epic_title:
                break

            roadmap.milestones[-1].epics.append(Epic(title=epic_title))

    return roadmap