import argparse
from pathlib import Path

from gitmap.parser import parse_roadmap


def main():
    """Run the gitmap command-line interface."""
    parser = argparse.ArgumentParser(
        prog="gitmap",
        description="Create a project roadmap and turn it into a structured GitHub project.",
    )

    subparsers = parser.add_subparsers(dest="command")

    sync_paser = subparsers.add_parser(
        "sync",
        help="Sync a roadmap with Github.",
    )

    sync_paser.add_argument(
        "roadmap",
        help="Path to roadmap file.",
    )
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

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

            for Section in milestone.Sections:
                print(f"    Section: {Section.title}")

                for issue in Section.issues:
                    print(f"      {issue.number} {issue.title}")


if __name__ == "__main__":
    main()
