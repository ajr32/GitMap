import argparse
from pathlib import Path

from gitmap.parser import parse_roadmap
from gitmap.validators import validate_roadmap
from rich.console import Console

console = Console()


def main():
    """Run the gitmap command-line interface."""
    parser = argparse.ArgumentParser(
        prog="gitmap",
        description="Create a project roadmap and turn it into a structured GitHub project.",
    )

    subparsers = parser.add_subparsers(dest="command")

    sync_parser = subparsers.add_parser(
        "sync",
        help="Sync a roadmap with Github.",
    )
    sync_parser.add_argument(
        "roadmap",
        help="Path to roadmap file.",
    )

    preview_parser = subparsers.add_parser(
        "preview",
        help="Preview a roadmap before syncing.",
    )

    preview_parser.add_argument(
        "roadmap",
        help="Path to roadmap file.",
    )

    check_parser = subparsers.add_parser(
        "check",
        help="Check a roadmap for problems.",
    )

    check_parser.add_argument(
        "roadmap",
        help="Path to roadmap file.",
    )

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    if args.command == "check":
        roadmap_path = Path(args.roadmap)

        if not roadmap_path.exists():
            print(f"Roadmap not found: {roadmap_path}")
            return

        roadmap = parse_roadmap(roadmap_path)
        errors = validate_roadmap(roadmap)

        issue_count = 0
        section_count = 0
        feature_count = 0

        for milestone in roadmap.milestones:
            issue_count += len(milestone.issues)
            section_count += len(milestone.sections)

            for section in milestone.sections:
                issue_count += len(section.issues)
                feature_count += len(section.features)

                for feature in section.features:
                    issue_count += len(feature.issues)

        if errors:
            print("Roadmap check failed:")
            for error in errors:
                print(f"  ✗ {error}")
        else:
            print("GitMap Roadmap Check")
            print("--------------------")
            print(f"Project: {roadmap.name}")
            print(f"Milestones: {len(roadmap.milestones)}")
            print(f"Sections: {section_count}")
            print(f"Issues: {issue_count}")
            print("✓ Roadmap check passed")
            print("✓ Ready to sync")

    if args.command == "preview":
        roadmap_path = Path(args.roadmap)

        if not roadmap_path.exists():
            print(f"Roadmap not found: {roadmap_path}")
            return

        roadmap = parse_roadmap(roadmap_path)

        console.print()
        console.print("[bold]GitMap Roadmap Preview[/bold]")
        console.print("=" * 22)
        console.print()
        console.print(f"[bold]{roadmap.name}[/bold]")

        section_count = 0
        issue_count = 0

        for milestone in roadmap.milestones:
            console.print()
            console.print(
                f"[bold cyan]{milestone.number}  {milestone.title}[/bold cyan]"
            )
            console.print("[cyan]" + "─" * 40 + "[/cyan]")

            for section in milestone.sections:
                section_count += 1

                console.print()
                console.print(f"  [bold yellow]{section.title}[/bold yellow]")

                for issue in section.issues:
                    issue_count += 1
                    console.print(f"    [white]{issue.number}  {issue.title}[/white]")

                    for sub_issue in issue.sub_issues:
                        issue_count += 1
                        console.print(
                            f"      [dim]{sub_issue.number}  {sub_issue.title}[/dim]"
                        )

        console.print()
        console.print("─" * 40)
        console.print(
            f"[bold]{len(roadmap.milestones)}[/bold] milestones · "
            f"[bold]{section_count}[/bold] sections · "
            f"[bold]{issue_count}[/bold] issues"
        )
        console.print("[dim green]Preview only — no GitHub changes made.[/dim green]")
        console.print()

    if args.command == "sync":
        roadmap_path = Path(args.roadmap)
        if not roadmap_path.exists():
            print(f"Roadmap not found: {roadmap_path}")
            return
        roadmap = parse_roadmap(roadmap_path)

        print(f"Roadmap: {roadmap.name}")
        print(f"Milestones: {len(roadmap.milestones)}")

        for milestone in roadmap.milestones:
            print(f"  {milestone.number} {milestone.title}")

            for section in milestone.sections:
                print(f"    Section: {section.title}")

                for issue in section.issues:
                    print(f"      {issue.number} {issue.title}")

                    for sub_issue in issue.sub_issues:
                        print(f"        {sub_issue.number} {sub_issue.title}")

if __name__ == "__main__":
    main()
