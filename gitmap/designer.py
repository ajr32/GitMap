"""Interactive roadmap designer for GitMap."""

from gitmap.models import Milestone, Roadmap


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

    return roadmap