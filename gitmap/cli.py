import argparse
from pathlib import Path

from gitmap.parser import parse_roadmap
from gitmap.validators import validate_roadmap


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


if __name__ == "__main__":
    main()
