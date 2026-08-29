import argparse
from pathlib import Path

from rich.console import Console

from gitmap.builder.builder import (
    render_roadmap_markdown,
    review_roadmap,
)
from gitmap.github_mapping import (
    assign_missing_gitmap_ids,
    summarize_roadmap_differences,
)
from gitmap.mapping_mod.mapping_lock import acquire_sync_lock, release_sync_lock
from gitmap.mapping_mod.mapping_validation import validate_synchronization_plan, verify_synchronization_results
from gitmap.mapping_mod.mapping_issues import get_existing_issues
from gitmap.mapping_mod.issues import sync_issues, sync_removed_issues, SynchronizationError
from gitmap.github_setup import collect_repository_info, verify_repository
from gitmap.parser import parse_roadmap, parse_roadmap_text, write_gitmap_ids_to_roadmap
from gitmap.roadmap_creation import start_new_roadmap
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

        while True:
            roadmap = review_roadmap(roadmap)

            roadmap_text = render_roadmap_markdown(roadmap)
            parsed_roadmap = parse_roadmap_text(roadmap_text)

            errors = validate_roadmap(parsed_roadmap)

            if not errors:
                print()
                print("Roadmap validation passed.")
                break

            print()
            print("Roadmap validation failed:")

            for error in errors:
                print(f"  • {error}")

            print()
            print("Return to review to fix these problems.")

        roadmap_path = Path("roadmap.md")
        roadmap_path.write_text(
            render_roadmap_markdown(roadmap),
            encoding="utf-8",
        )

        print()
        print(f"Roadmap saved to: {roadmap_path.resolve()}")

    if args.command == "sync":
        roadmap_path = Path(args.roadmap)

        if not roadmap_path.exists():
            print(f"Roadmap not found: {roadmap_path}")
            return

        roadmap = parse_roadmap(roadmap_path)

        assigned_ids = assign_missing_gitmap_ids(roadmap)

        if assigned_ids:
            write_gitmap_ids_to_roadmap(roadmap_path, roadmap)

            print()
            print(
                f"Assigned permanent GitMap IDs to {len(assigned_ids)} roadmap items."
            )
            print(f"Updated: {roadmap_path.resolve()}")

        info = collect_repository_info()
        repository = verify_repository(info)

        existing_issues = get_existing_issues(repository)

        conflicts = validate_synchronization_plan(
            roadmap,
            existing_issues,
        )

        if conflicts:
            print()
            print("Synchronization conflicts detected")
            print("----------------------------------")

            for conflict in conflicts:
                print(f"• {conflict}")

            print()
            print("Synchronization cancelled. Resolve the conflicts and try again.")
            return

        differences = summarize_roadmap_differences(
            roadmap,
            existing_issues,
        )

        print()
        print("Roadmap Update Preview")
        print("----------------------")

        print(f"Added: {len(differences['new'])}")
        print(f"Changed: {len(differences['changed'])}")

        if differences["renumbered"]:
            print(f"  Renumbered: {len(differences['renumbered'])}")

        print(f"Unchanged: {len(differences['matching'])}")
        print(f"Removed: {len(differences['removed'])}")

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

                renumbered_by_id = {
                    issue.gitmap_id: (old_number, new_number)
                    for issue, old_number, new_number in differences["renumbered"]
                }

                for issue in differences["changed"]:
                    renumbering = renumbered_by_id.get(issue.gitmap_id)

                    if renumbering:
                        old_number, new_number = renumbering

                        print(f"  • {old_number} -> {new_number} {issue.title}")

                    else:
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
                issues_to_sync = differences["new"] + differences["changed"]

                total_changes = len(issues_to_sync) + len(differences["removed"])

                if total_changes == 0:
                    print()

                    print("Nothing to synchronize.")

                    break

                repository_name = repository.full_name

                acquired, lock = acquire_sync_lock(repository_name)

                if not acquired:
                    print()
                    print("Synchronization blocked.")
                    print("------------------------")
                    print(
                        f"A synchronization is already running for {repository_name}."
                    )
                    print(f"Process ID: {lock['pid']}")
                    print()
                    print(
                        "Wait for the active synchronization to finish and try again."
                    )
                    return

                print()

                print(f"Synchronizing {total_changes} changes...")

                print()

                try:
                    results = sync_issues(
                        repository,
                        roadmap,
                        issues_to_sync,
                        progress_start=0,
                        progress_total=total_changes,
                    )

                    removed_results = sync_removed_issues(
                        differences["removed"],
                        progress_start=len(results),
                        progress_total=total_changes,
                    )

                    verification = verify_synchronization_results(
                        repository,
                        roadmap,
                        differences,
                    )

                except SynchronizationError as error:
                    print()
                    print("Synchronization stopped.")
                    print("------------------------")
                    print(f"Completed: {error.completed}")
                    print("Failed: 1")
                    print(f"Remaining: {error.remaining}")
                    print()
                    print("Failed operation:")
                    print(f"  {error.failed.number} {error.failed.title}")
                    print()
                    print(f"Reason: {error.original_error}")
                    print()
                    print("No further changes were attempted.")
                    print("Fix the problem and run sync again.")
                    return

                finally:
                    release_sync_lock()

                verification_failed = (
                    verification["missing_created"]
                    or verification["incorrect_updates"]
                    or verification["identity_failures"]
                    or verification["duplicate_ids"]
                )

                if verification_failed:
                    print()
                    print("Synchronization verification failed.")
                    print("------------------------------------")

                    if verification["missing_created"]:
                        print()
                        print("Expected creations not found:")

                        for issue in verification["missing_created"]:
                            print(f"  • {issue.number} {issue.title}")

                    if verification["incorrect_updates"]:
                        print()
                        print("Updates that do not match the roadmap:")

                        for issue, reason in verification["incorrect_updates"]:
                            print(f"  • {issue.number} {issue.title}: {reason}")

                    if verification["identity_failures"]:
                        print()
                        print("Identity verification failures:")

                        for issue, reason in verification["identity_failures"]:
                            print(f"  • {issue.number} {issue.title}: {reason}")

                    if verification["duplicate_ids"]:
                        print()
                        print("Duplicate GitMap identifiers:")

                        for gitmap_id, github_issues in verification["duplicate_ids"]:
                            issue_numbers = ", ".join(
                                f"#{issue.number}" for issue in github_issues
                            )

                            print(f"  • {gitmap_id}: {issue_numbers}")

                    print()
                    print("GitHub does not match the synchronization plan.")
                    print("Review the differences before synchronizing again.")
                    return

                print()

                print("Synchronization complete.")

                print(f"Synchronized {len(results)} issues.")

                print(f"Closed {len(removed_results)} removed issues.")

                break

            else:
                print("Invalid choice.")
                print()


if __name__ == "__main__":
    main()
