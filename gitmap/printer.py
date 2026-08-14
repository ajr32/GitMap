"""Display GitMap roadmap data."""

from gitmap.models import Roadmap

def _print_issue(issue) -> None:
    """Print an issue and its details."""

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
        print(f"[ ] {sub_issue.number} {sub_issue.title}")
        
def print_roadmap(roadmap: Roadmap) -> None:
    """Print a roadmap in a readable hierarchy."""

    print(f"Title: {roadmap.name}")

    if roadmap.overview:
        print()
        print(f"Sub-Title: {roadmap.overview}")

    for milestone in roadmap.milestones:
        print()
        print(f"# {milestone.number} {milestone.title}")
        
        for issue in milestone.issues:
            _print_issue(issue)
        
        for section in milestone.sections:
            print()
            print(f"## {section.number} {section.title}")

            if section.description:
                print()
                print(section.description)

            for feature in section.features:
                print()
                print(f"### {feature.number} {feature.title}")

                if feature.description:
                    print()
                    print(feature.description)

                for issue in feature.issues:
                    _print_issue(issue)

            for issue in section.issues:
                _print_issue(issue)

