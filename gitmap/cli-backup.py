import argparse
from pathlib import Path
from gitmap.parser import find_headings, find_issues, find_milestones, read_roadmap

def main():
    """Run the gitmap command-line interface."""
    parser = argparse.ArgumentParser(
        prog='gitmap',
        description="Turn a project roadmap into Github issues.",
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

    if args.command == "sync":
        roadmap_path = Path(args.roadmap)
        if not roadmap_path.exists():
            print(f"Roadmap not found: {roadmap_path}")
            return
        roadmap_text =  read_roadmap(roadmap_path)
        headings = find_headings(roadmap_text)
        milestones = find_milestones(roadmap_text)
        print(f"Found {len(milestones)} milestones.")
        issues = find_issues(roadmap_text)
        print(f"Found {len(issues)} issues.")
        print(f"Found {len(headings)} headings.")
        print(f"Read {len(roadmap_text)} characters")
        print(f"Roadmap: {roadmap_path}")
if __name__ == "__main__":
    main()