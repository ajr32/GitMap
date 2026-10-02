"""Interactive roadmap designer for GitMap."""

from gitmap.models import Milestone, Roadmap, Section


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
            section_title = input("Section title (blank when finished): ").strip()
            section_description = input("Section description: ").strip()

            if not section_title:
                break

            roadmap.milestones[-1].sections.append(
                Section(
                    title=section_title,
                    description=section_description,
                )
            )

    return roadmap
