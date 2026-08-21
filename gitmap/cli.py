import argparse
from pathlib import Path

from rich.console import Console

from gitmap.builder import review_roadmap, start_new_roadmap
from gitmap.github_mapping import (
    get_existing_issues,
    summarize_roadmap_differences,
    sync_issues,
)
from gitmap.github_setup import collect_repository_info, verify_repository
from gitmap.parser import parse_roadmap
from gitmap.validators import validate_roadmap

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

    subparsers.add_parser(
        "new-roadmap",
        help="Start a new interactive roadmap.",
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
        work_step_count = 0

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

                    for work_step in issue.work_steps:
                        work_step_count += 1
                        console.print(
                            f"      [dim]{work_step.number}  {work_step.title}[/dim]"
                        )

        console.print()
        console.print("─" * 45)
        console.print(
            f" · "
            f"[bold]{len(roadmap.milestones)}[/bold] milestones · "
            f"[bold]{section_count}[/bold] sections · "
            f"[bold]{issue_count}[/bold] issues · "
            # f"[bold]{work_step_count}[/bold] sub-issues"
        )
        console.print("─" * 45)
        console.print("[dim green]Preview only — no GitHub changes made.[/dim green]")
        console.print()

    if args.command == "new-roadmap":
        roadmap = start_new_roadmap()
        roadmap = review_roadmap(roadmap)

    if args.command == "sync":
        roadmap_path = Path(args.roadmap)

        if not roadmap_path.exists():
            print(f"Roadmap not found: {roadmap_path}")
            return

        roadmap = parse_roadmap(roadmap_path)

        info = collect_repository_info()
        repository = verify_repository(info)

        existing_issues = get_existing_issues(repository)
        differences = summarize_roadmap_differences(
            roadmap,
            existing_issues,
        )

        print()
        print("Roadmap Update Preview")
        print("----------------------")

        print(f"New: {len(differences['new'])}")
        for issue in differences["new"]:
            print(f"  + {issue.number} {issue.title}")

        print(f"Changed: {len(differences['changed'])}")

        print(f"Unchanged: {len(differences['matching'])}")

        print(f"Removed: {len(differences['removed'])}")
        for issue in differences["removed"]:
            print(f"  - #{issue.number} {issue.title}")

        print()

        while True:
            confirm = (
                input(
                    "Apply these changes? [(y)es/(n)o] or review [(a)dded, (c)hanged, (u)nchanged or (r)emoved]: "
                )
                .strip()
                .lower()
            )

            if confirm in ("n", "no"):
                print("Synchronization cancelled.")
                return

            elif confirm in ("a", "added", "review added", "list added"):
                print("Issues added:")
                for issue in differences["new"]:
                    print(f"  • {issue.number} {issue.title}")
                print()

            elif confirm in ("c", "changed", "review changed", "list changed"):
                print("Issues changed:")
                for issue in differences["changed"]:
                    print(f"  • {issue.number} {issue.title}")
                print()

            elif confirm in ("u", "unchanged", "review unchanged", "list unchanged"):
                print("Issues unchanged:")
                for issue in differences["matching"]:
                    print(f"  • {issue.number} {issue.title}")
                print()

            elif confirm in ("r", "removed", "review removed", "list removed"):
                print("Issues removed:")
                for issue in differences["removed"]:
                    print(f"  • {issue.number} {issue.title}")
                print()

            elif confirm in ("y", "yes"):
                results = sync_issues(repository, roadmap)

                print()
                print(f"Synchronized {len(results)} issues.")
                break

            else:
                print("Invalid choice.")
                print()


if __name__ == "__main__":
    main()
