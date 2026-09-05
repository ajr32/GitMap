import argparse
import subprocess
from pathlib import Path

from github import Auth, Github
from rich.console import Console

from gitmap.builder.builder import (
    render_roadmap_markdown,
    review_roadmap,
    roadmap_to_builder_dict,
)
from gitmap.github_mapping import (
    assign_missing_gitmap_ids,
    summarize_roadmap_differences,
)
from gitmap.github_setup import (
    collect_repository_info,
    get_github_token,
    verify_repository,
)
from gitmap.mapping_mod.mapping_issues import (
    SynchronizationError,
    apply_roadmap_label_to_existing_issues,
    collect_hierarchy_issue_mappings,
    get_existing_issues,
    get_gitmap_id_from_github_issue,
    sync_issues,
    sync_removed_issues,
    sync_sub_issue_relationships,
)
from gitmap.mapping_mod.mapping_labels import sync_labels
from gitmap.mapping_mod.mapping_lock import acquire_sync_lock, release_sync_lock
from gitmap.mapping_mod.mapping_validation import (
    validate_synchronization_plan,
    verify_synchronization_results,
)
from gitmap.parser import (
    parse_roadmap,
    parse_roadmap_text,
    write_github_representation_to_roadmap,
    write_gitmap_ids_to_roadmap,
    write_hierarchy_issue_title_style_to_roadmap,
)
from gitmap.roadmap_creation import start_new_roadmap
from gitmap.roadmap_menus import (
    choose_github_representation,
    choose_hierarchy_issue_title_style,
)
from gitmap.validators import validate_roadmap

console = Console()


def choose_startup_workflow():
    """Ask what the user wants GitMap to do."""

    print()
    print("What would you like to do?")
    print("--------------------------")
    print()
    print("Roadmap creation")
    print("----------------")
    print("1. Need to create repository and then create a roadmap")
    print("2. Repository made, but need to create roadmap")
    print("3. Repository made, initial upload/sync of roadmap")
    print()
    print("Roadmap maintenance")
    print("----------------")
    print("4. Check my roadmap for problems")
    print("5. Preview my roadmap in the terminal")
    print("6. -- Coming soon -- ")
    print("7. Repository made, just making a few updates to the roadmap")
    print()
    print("8. Exit GitMap")

    while True:
        choice = input("\nChoose an option: ").strip()

        if choice in ("1", "2", "3", "4", "5", "6", "7", "8"):
            return choice

        print("Please choose 1, 2, 3, 4, 5, 6, 7 or 8.")


def run_new_roadmap():
    """Run the new roadmap workflow."""
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


def choose_roadmap_path():
    """Ask for the roadmap filename."""

    name = input("Roadmap name: ").strip()

    if not name.lower().endswith(".md"):
        name += ".md"

    return Path(name)


def ensure_gitmap_ids(roadmap_path, roadmap, reserved_ids=None):
    """Ensure all roadmap items have permanent GitMap IDs."""

    assigned_ids = assign_missing_gitmap_ids(
        roadmap,
        reserved_ids=reserved_ids,
    )
    if assigned_ids:
        write_gitmap_ids_to_roadmap(roadmap_path, roadmap)

        print()
        print(f"Assigned permanent GitMap IDs to {len(assigned_ids)} roadmap items.")
        print(f"Updated: {roadmap_path.resolve()}")

    return roadmap


def detect_roadmap_structure(roadmap):
    """Detect which hierarchy levels an existing roadmap uses."""

    has_sections = False
    has_features = False

    for milestone in roadmap.milestones:
        if milestone.sections:
            has_sections = True

        for section in milestone.sections:
            if section.features:
                has_features = True

    if has_features:
        return "sections_and_features"

    if has_sections:
        return "sections"

    return "neither"


def run_check(roadmap_path):
    """Check an existing roadmap for problems."""

    roadmap_path = Path(roadmap_path)

    if not roadmap_path.exists():
        print(f"Roadmap not found: {roadmap_path}")
        return

    roadmap = parse_roadmap(roadmap_path)
    roadmap = ensure_gitmap_ids(roadmap_path, roadmap)

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
        print(f"Features: {feature_count}")
        print(f"Issues: {issue_count}")
        print("✓ Roadmap check passed")
        print("✓ Ready to sync")


def run_preview(roadmap_path):
    """Preview an existing roadmap in the terminal."""

    roadmap_path = Path(roadmap_path)

    if not roadmap_path.exists():
        print(f"Roadmap not found: {roadmap_path}")
        return

    roadmap = parse_roadmap(roadmap_path)
    roadmap = ensure_gitmap_ids(roadmap_path, roadmap)

    console.print()
    console.print("[bold]GitMap Roadmap Preview[/bold]")
    console.print("=" * 22)
    console.print()
    console.print(f"[bold]{roadmap.name}[/bold]")

    section_count = 0
    feature_count = 0
    issue_count = 0
    work_step_count = 0

    for milestone in roadmap.milestones:
        console.print()
        console.print(f"[bold cyan]{milestone.number}  {milestone.title}[/bold cyan]")
        console.print("[cyan]" + "─" * 40 + "[/cyan]")

        for section in milestone.sections:
            section_count += 1

            console.print()
            console.print(f"  [bold yellow]{section.title}[/bold yellow]")

            for feature in section.features:
                feature_count += 1
                console.print()
                console.print(f"    [bold]{feature.number}  {feature.title}[/bold]")

                for issue in feature.issues:
                    issue_count += 1
                    console.print(f"      [white]{issue.number}  {issue.title}[/white]")

                    for work_step in issue.work_steps:
                        work_step_count += 1
                        console.print(
                            f"        [dim]{work_step.number}  {work_step.title}[/dim]"
                        )

            for issue in section.issues:
                issue_count += 1
                console.print(f"    [white]{issue.number}  {issue.title}[/white]")

                for work_step in issue.work_steps:
                    work_step_count += 1
                    console.print(
                        f"      [dim]{work_step.number}  {work_step.title}[/dim]"
                    )

    console.print()
    console.print("─" * 60)
    console.print(
        f" · "
        f"[bold]{len(roadmap.milestones)}[/bold] milestones · "
        f"[bold]{section_count}[/bold] sections · "
        f"[bold]{feature_count}[/bold] features · "
        f"[bold]{issue_count}[/bold] issues · "
        # f"[bold]{work_step_count}[/bold] sub-issues"
    )
    console.print("─" * 60)
    console.print("[dim green]Preview only — no GitHub changes made.[/dim green]")
    console.print()


def detect_repository():
    """Detect the GitHub repository from the current local repository."""

    result = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        return None

    remote_url = result.stdout.strip()

    if remote_url.endswith(".git"):
        remote_url = remote_url[:-4]

    if "github.com/" not in remote_url:
        return None

    return remote_url.split("github.com/", 1)[1]


def run_sync(roadmap_path):
    """Run the roadmap synchronization workflow."""

    roadmap_path = Path(roadmap_path)

    if not roadmap_path.exists():
        print(f"Roadmap not found: {roadmap_path}")
        return

    roadmap = parse_roadmap(roadmap_path)
    # roadmap = ensure_gitmap_ids(roadmap_path, roadmap)

    errors = validate_roadmap(roadmap)

    if errors:
        print()
        print("Roadmap validation failed:")

        for error in errors:
            print(f"  • {error}")

        print()
        print("Fix these problems before performing the initial sync.")
        return

    repository_name = detect_repository()

    if repository_name:
        print(f"Detected repository: {repository_name}")

        use_detected = input("Use this repository? (y/n): ").strip().lower()

        if use_detected != "y":
            repository_name = input("GitHub repository (owner/name): ").strip()
    else:
        repository_name = input("GitHub repository (owner/name): ").strip()

    if not repository_name:
        print("No GitHub repository selected.")
        return

    print(f"Repository: {repository_name}")
    token = get_github_token()
    auth = Auth.Token(token)
    github = Github(auth=auth)
    repository = github.get_repo(repository_name)
    existing_issues = get_existing_issues(repository)

    reserved_ids = {
        get_gitmap_id_from_github_issue(issue)
        for issue in existing_issues
        if get_gitmap_id_from_github_issue(issue)
    }

    roadmap = ensure_gitmap_ids(
        roadmap_path,
        roadmap,
        reserved_ids=reserved_ids,
    )

    roadmap_structure = detect_roadmap_structure(roadmap)

    github_representation = choose_github_representation(roadmap_structure)

    hierarchy_issue_title_style = None

    if github_representation["section"] in ("issue", "both") or github_representation[
        "feature"
    ] in ("issue", "both"):
        hierarchy_issue_title_style = choose_hierarchy_issue_title_style()

    roadmap.github_representation = github_representation
    roadmap.hierarchy_issue_title_style = hierarchy_issue_title_style

    write_github_representation_to_roadmap(
        roadmap_path,
        roadmap,
    )

    if hierarchy_issue_title_style:
        write_hierarchy_issue_title_style_to_roadmap(
            roadmap_path,
            hierarchy_issue_title_style,
        )

    preview_choice = (
        input("\nWould you like to preview the roadmap before synchronization? (y/n): ")
        .strip()
        .lower()
    )

    if preview_choice in ("y", "yes"):
        run_preview(roadmap_path)

    issue_count = 0

    for milestone in roadmap.milestones:
        issue_count += len(milestone.issues)

        for section in milestone.sections:
            issue_count += len(section.issues)

            for feature in section.features:
                issue_count += len(feature.issues)

    section_issue_count = 0
    feature_issue_count = 0

    if github_representation["section"] in ("issue", "both"):
        section_issue_count = sum(
            len(milestone.sections) for milestone in roadmap.milestones
        )

    if github_representation["feature"] in ("issue", "both"):
        feature_issue_count = sum(
            len(section.features)
            for milestone in roadmap.milestones
            for section in milestone.sections
        )

    print()
    print("Initial Synchronization Summary")
    print("-------------------------------")
    print(f"Repository: {repository_name}")
    print(f"Roadmap: {roadmap.name}")
    print()
    print(f"Roadmap Issues: {issue_count}")
    print(f"Section Issues: {section_issue_count}")
    print(f"Feature Issues: {feature_issue_count}")
    print()
    print(
        f"Total GitHub Issues: {issue_count + section_issue_count + feature_issue_count}"
    )

    print()

    confirm = input("Create these GitHub Issues? (y/n): ").strip().lower()

    if confirm not in ("y", "yes"):
        print("Initial synchronization cancelled.")
        return False

    if confirm in ("y", "yes"):
        print("Initial synchronization approved.")

        issues_to_sync = []

        for milestone in roadmap.milestones:
            issues_to_sync.extend(milestone.issues)

            for section in milestone.sections:
                issues_to_sync.extend(section.issues)

                for feature in section.features:
                    issues_to_sync.extend(feature.issues)

        hierarchy_mappings_to_sync = collect_hierarchy_issue_mappings(roadmap)

        print()
        print(f"Normal Issues ready: {len(issues_to_sync)}")
        print(f"Hierarchy Issues ready: {len(hierarchy_mappings_to_sync)}")

        total_to_sync = len(issues_to_sync) + len(hierarchy_mappings_to_sync)

        print(f"Total ready to synchronize: {total_to_sync}")

        results = sync_issues(
            repository,
            roadmap,
            issues_to_sync=issues_to_sync,
            hierarchy_mappings_to_sync=hierarchy_mappings_to_sync,
            hierarchy_expected_operation="create",
            progress_start=0,
            progress_total=total_to_sync,
        )

        print()
        print(f"Initial synchronization complete. {len(results)} Issues synchronized.")
        return True


def run_roadmap_edit(roadmap_path):
    """Edit an existing roadmap and save the changes."""

    roadmap_path = Path(roadmap_path)

    if not roadmap_path.exists():
        print(f"Roadmap not found: {roadmap_path}")
        return False

    roadmap = parse_roadmap(roadmap_path)
    builder_roadmap = roadmap_to_builder_dict(roadmap)
    builder_roadmap = review_roadmap(builder_roadmap)


    roadmap_text = render_roadmap_markdown(builder_roadmap)

    roadmap_path.write_text(
        roadmap_text,
        encoding="utf-8",
    )

    print()
    print(f"Roadmap saved: {roadmap_path}")
    return True


def main():
    """Run the gitmap command-line interface."""
    parser = argparse.ArgumentParser(
        prog="gitmap",
        description="Create a project roadmap and turn it into a structured GitHub project.",
    )

    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser(
        "sync",
        help="Sync a roadmap with Github.",
    ).add_argument(
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

    subparsers.add_parser(
        "initial-sync",
        help="Perform the first synchronization of the roadmap with Github.",
    ).add_argument(
        "roadmap",
        help="Path to roadmap file.",
    )

    args = parser.parse_args()
    workflow = None

    if args.command is None:
        while True:
            workflow = choose_startup_workflow()
            command = args.command or workflow

            command_aliases = {
                "roadmap": "new-roadmap",
                "new": "new-roadmap",
                "new roadmap": "new-roadmap",
                "2": "new-roadmap",
                "initial": "initial-sync",
                "initial sync": "initial-sync",
                "3": "initial-sync",
                "4": "check",
                "5": "preview",
                "8": "exit",
                "quit": "exit",
                "fuck it": "exit",
                "fuck this": "exit",
                "screw this": "exit",
                "let me out": "exit",
                # "6": "configure-sync",
                "7": "update-sync",
            }

            if command is not None:
                command = command_aliases.get(command, command)

            if workflow == "1":
                print("Coming soon.")
                continue

            if command == "new-roadmap":
                run_new_roadmap()
                continue

            if command == "initial-sync":
                roadmap_path = choose_roadmap_path()

                completed = run_sync(roadmap_path)

                if completed:
                    return

                continue

            if command == "preview":
                roadmap_path = choose_roadmap_path()
                run_preview(roadmap_path)
                continue

            if command == "check":
                roadmap_path = choose_roadmap_path()
                run_check(roadmap_path)
                continue

            # if command == "configure-sync":
            #     roadmap_path = choose_roadmap_path()
            #     roadmap = parse_roadmap(roadmap_path)
            #     roadmap_structure = detect_roadmap_structure(roadmap)
            #     github_representation = choose_github_representation(roadmap_structure)
            #     roadmap.github_representation = github_representation
            #     hierarchy_issue_title_style = None
            #     builder_roadmap = roadmap_to_builder_dict(roadmap)
            #     builder_roadmap = review_roadmap(builder_roadmap)
            #     roadmap_text = render_roadmap_markdown(builder_roadmap)
            #     roadmap_path.write_text(
            #         roadmap_text,
            #         encoding="utf-8",
            #     )
            #     roadmap = parse_roadmap(roadmap_path)
            #     errors = validate_roadmap(roadmap)
            #     if errors:
            #         print()
            #         print("Roadmap validation failed:")
            #
            #         for error in errors:
            #             print(f"  • {error}")
            #
            #         continue
            #
            #         print()
            #         print("Roadmap validation passed.")
            #
            #     if github_representation["section"] in (
            #             "issue",
            #             "both",
            #     ) or github_representation["feature"] in ("issue", "both"):
            #         hierarchy_issue_title_style = choose_hierarchy_issue_title_style()
            #     roadmap.hierarchy_issue_title_style = hierarchy_issue_title_style
            #     write_github_representation_to_roadmap(
            #         roadmap_path,
            #         roadmap,
            #     )
            #
            #     if hierarchy_issue_title_style:
            #         write_hierarchy_issue_title_style_to_roadmap(
            #             roadmap_path,
            #             hierarchy_issue_title_style,
            #         )
            #     run_update_sync(roadmap_path)
            #     continue

            if command == "update-sync":
                roadmap_path = choose_roadmap_path()
                # run_roadmap_edit(roadmap_path)
                if run_roadmap_edit(roadmap_path):
                    run_update_sync(roadmap_path)

                continue

            if command == "exit":
                print()
                print("Goodbye!")
                return

    if args.command == "initial-sync":
        run_sync(Path(args.roadmap))
        return

    if args.command == "check":
        run_check(Path(args.roadmap))
        return

    if args.command == "preview":
        run_preview(Path(args.roadmap))
        return

    if args.command == "new-roadmap":
        run_new_roadmap()


def run_update_sync(roadmap_path):
    """Run the normal roadmap update synchronization workflow."""

    roadmap_path = Path(roadmap_path)

    if not roadmap_path.exists():
        print(f"Roadmap not found: {roadmap_path}")
        return

    roadmap = parse_roadmap(roadmap_path)
    assigned_ids = assign_missing_gitmap_ids(roadmap)

    if assigned_ids:
        write_gitmap_ids_to_roadmap(roadmap_path, roadmap)

        print()
        print(f"Assigned permanent GitMap IDs to {len(assigned_ids)} roadmap items.")
        print(f"Updated: {roadmap_path.resolve()}")

    info = collect_repository_info()
    repository = verify_repository(info)

    existing_issues = get_existing_issues(
        repository,
        roadmap=roadmap,
    )

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

    if roadmap.hierarchy_issue_title_style:
        print(
            f"Hierarchy Issue Title Style: "
            f"{roadmap.hierarchy_issue_title_style.replace('_', ' ').title()}"
        )

    print()

    print(f"Added: {len(differences['new'])}")
    print(f"Changed: {len(differences['changed'])}")

    if differences["renumbered"]:
        print(f"  Renumbered: {len(differences['renumbered'])}")

    if differences["hierarchy_changed"]:
        print(f"Hierarchy changed: {len(differences['hierarchy_changed'])}")

    print(f"Unchanged: {len(differences['matching'])}")
    print(f"Removed: {len(differences['removed'])}")

    print()

    while True:
        confirm = (
            input(
                "Apply these changes? [(y)es/(n)o] or review [(a)dded, (c)hanged, (h)ierarchy, (u)nchanged or (r)emoved]: "
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

            for change in differences["changed"]:
                issue = change["issue"]
                changes = change["changes"]

                renumbering = renumbered_by_id.get(issue.gitmap_id)

                if renumbering:
                    old_number, new_number = renumbering
                    print(f"  • {old_number} -> {new_number} {issue.title}")
                else:
                    print(f"  • {issue.number} {issue.title}")

                print(f"    Changes: {', '.join(changes)}")

        elif confirm in ("h", "hierarchy", "review hierarchy", "list hierarchy"):
            print("Hierarchy issues changed:")

            for change in differences["hierarchy_changed"]:
                mapping = change["mapping"]
                changes = change["changes"]

                print(f"  • {mapping.title}")
                print(f"    Changes: {', '.join(changes)}")

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
            issues_to_sync = differences["new"] + [
                change["issue"] for change in differences["changed"]
            ]

            hierarchy_mappings_to_sync = [
                change["mapping"] for change in differences["hierarchy_changed"]
            ]

            total_changes = (
                len(issues_to_sync)
                + len(hierarchy_mappings_to_sync)
                + len(differences["removed"])
            )

            if total_changes == 0:
                print()
                print("No Issue changes to synchronize.")

                sync_labels(
                    repository,
                    roadmap,
                )

                apply_roadmap_label_to_existing_issues(
                    repository,
                    roadmap,
                )

                sync_sub_issue_relationships(
                    repository,
                    roadmap,
                )

                break

            repository_name = repository.full_name

            acquired, lock = acquire_sync_lock(repository_name)

            if not acquired:
                print()
                print("Synchronization blocked.")
                print("------------------------")
                print(f"A synchronization is already running for {repository_name}.")
                print(f"Process ID: {lock['pid']}")
                print()
                print("Wait for the active synchronization to finish and try again.")
                return

            print()

            print(f"Synchronizing {total_changes} changes...")

            print()

            try:
                results = sync_issues(
                    repository,
                    roadmap,
                    issues_to_sync,
                    hierarchy_mappings_to_sync=hierarchy_mappings_to_sync,
                    update_issues=[
                        change["issue"] for change in differences["changed"]
                    ],
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
                or verification["incorrect_closures"]
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

                if verification["incorrect_closures"]:
                    print()
                    print("Closures that do not match the approved plan:")

                    for issue, reason in verification["incorrect_closures"]:
                        print(f"  • #{issue.number} {issue.title}: {reason}")

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
