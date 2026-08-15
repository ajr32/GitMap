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

        if sub_issue.description:
            print(f"    {sub_issue.description}")

            for requirement in sub_issue.requirements:
                print(f"    - {requirement.text}")
        
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
def _print_preview_issue(issue, indent: str) -> None:
    """Print an issue in the sync preview."""

    print(f"{indent}Issue: {issue.number} {issue.title}")

    for sub_issue in issue.sub_issues:
        print(f"{indent}  Sub-issue: {sub_issue.number} {sub_issue.title}")


def print_sync_preview(roadmap: Roadmap) -> None:
    """Print a preview of what GitMap will sync."""

    print("GitMap Sync Preview")
    print("-------------------")
    print()
    print(f"Project: {roadmap.name}")

    for milestone in roadmap.milestones:
        print()
        print(f"Milestone: {milestone.number} {milestone.title}")

        for issue in milestone.issues:
            _print_preview_issue(issue, "  ")

        for section in milestone.sections:
            print(f"  Section: {section.number} {section.title}")

            for feature in section.features:
                print(f"    Feature: {feature.number} {feature.title}")

                for issue in feature.issues:
                    _print_preview_issue(issue, "      ")

            for issue in section.issues:
                _print_preview_issue(issue, "    ")

    print()
    print("Preview complete.")
