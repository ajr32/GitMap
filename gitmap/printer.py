"""Display GitMap roadmap data."""

from gitmap.models import Roadmap


def print_roadmap(roadmap: Roadmap) -> None:
    """Print a roadmap in a readable hierarchy."""

    print(f"# {roadmap.name}")

    if roadmap.overview:
        print()
        print(roadmap.overview)

    for milestone in roadmap.milestones:
        print()
        print(f"## {milestone.number} {milestone.title}")

        for Section in milestone.Sections:
            print()
            print(f"### {Section.title}")

            if Section.description:
                print()
                print(Section.description)

            for issue in Section.issues:
                print()
                print(f"#### {issue.number} {issue.title}")

                if issue.description:
                    print()
                    print(issue.description)

                for requirement in issue.requirements:
                    print()
                    print(f"- {requirement.text}")

                for sub_issue in issue.sub_issues:
                    print()
                    print(f"##### {sub_issue.number} {sub_issue.title}")
