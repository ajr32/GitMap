def explain_roadmap_numbering():
    """Explain GitMap's roadmap numbering system."""

    print()
    print("Roadmap Numbering")
    print("-----------------")
    print("Milestones use top-level numbers, such as 0.1.")
    print("Items below a milestone extend their parent's number.")
    print()
    print("Example:")
    print("  0         Development Stage (typically 0)")
    print("  0.1       Milestone")
    print("  0.1.1     Section")
    print("  0.1.1.1   Feature")
    print("  0.1.1.1.1 Issue")
    print()
    print("GitMap can number roadmap items automatically,")
    print("or you can enter numbers manually.")
    print()
    print("Automatic numbering:")
    print("     GitMap assigns the next available number based on the item's parent.")
    print()
    print("Manual numbering:")
    print("     You may enter a number yourself. Child numbers ")
    print("     must extend their parent's number.")
    print()


def choose_numbering_mode():
    """Ask whether GitMap should use automatic or manual numbering."""

    print()
    print("Choose Numbering Mode")
    print("---------------------")
    print("1. Automatic numbering")
    print("2. Manual numbering")

    while True:
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            return "automatic"

        if choice == "2":
            return "manual"

        print("Please choose 1 or 2.")


def choose_starting_series():
    """Ask which version series automatic numbering should use."""

    print()
    print("Choose Starting Series")
    print("----------------------")
    print("1. Pre-production (0.x)")
    print("2. Production (1.x)")
    print("3. Choose another production series (ex. 3.x)")

    while True:
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            return "0"

        if choice == "2":
            return "1"

        if choice == "3":
            while True:
                series = input("Starting series: ").strip()

                if series.isdigit():
                    return series

                print("Enter a positive whole number, such as 2, 10, or 22.")

        print("Please choose 1, 2 or 3.")

RESET = "\033[0m"
BOLD = "\033[1m"
PROJECT_COLOR = "\033[95m"    # Magenta
MILESTONE_COLOR = "\033[94m"  # Blue
SECTION_COLOR = "\033[92m"    # Green
FEATURE_COLOR = "\033[93m"    # Yellow
ISSUE_COLOR = "\033[96m"      # Cyan


def colored(text, color):
    """Return colored terminal text."""
    return f"{color}{text}{RESET}"


def print_columns(left_lines, right_lines, width=52):
    """Print two blocks of text side by side."""

    line_count = max(len(left_lines), len(right_lines))

    for index in range(line_count):
        left = left_lines[index] if index < len(left_lines) else ""
        right = right_lines[index] if index < len(right_lines) else ""

        print(f"{left:<{width}}{right}")


def choose_roadmap_structure():
    """Ask which organizational levels the roadmap should use."""

    print()
    print("Choose Roadmap Structure")
    print("------------------------")
    print()
    print("Think of a roadmap like an address:")
    print()
    print(
        f"{PROJECT_COLOR}World{RESET} -> "
        f"{MILESTONE_COLOR}Country{RESET} -> "
        f"{SECTION_COLOR}State{RESET} -> "
        f"{FEATURE_COLOR}City{RESET}      -> "
        f"{ISSUE_COLOR}Issue{RESET}"
    )

    print(
        f"{PROJECT_COLOR}Project{RESET} -> "
        f"{MILESTONE_COLOR}Milestone{RESET} -> "
        f"{SECTION_COLOR}Section{RESET} -> "
        f"{FEATURE_COLOR}Feature{RESET} -> "
        f"{ISSUE_COLOR}Issue{RESET}"
    )

    print()

    print_columns(
        [
            f"{BOLD}1. Sections only{RESET}",
            "   Adds another level of organization.",
            "   Sections can also be useful as labels",
            "   when synchronized to GitHub.",
            "",
            "",
            (
                f"   {PROJECT_COLOR}Project{RESET} -> "
                f"{MILESTONE_COLOR}Milestone{RESET} -> "
                f"{SECTION_COLOR}Section{RESET} -> "
                f"{ISSUE_COLOR}Issue{RESET}"
            ),
        ],
        [
            f"{BOLD}Example:{RESET}",
            f"{PROJECT_COLOR}Earth{RESET}",
            f"└── {MILESTONE_COLOR}United States{RESET}",
            f"  └── {SECTION_COLOR}Maryland{RESET}",
            f"    ├── {ISSUE_COLOR}Improve Bay water quality{RESET}",
            f"    └── {ISSUE_COLOR}Expand statewide transit{RESET}",
        ],
    )

    print()

    print_columns(
        [
            f"{BOLD}2. Add Features{RESET}",
            "   Adds another level beneath Sections.",
            "   Useful for larger or more detailed",
            "   roadmaps.",
            "",
            (
                f"   {PROJECT_COLOR}Project{RESET} -> "
                f"{MILESTONE_COLOR}Milestone{RESET} -> "
                f"{SECTION_COLOR}Section{RESET} -> "
                f"{FEATURE_COLOR}Feature{RESET} -> "
                f"{ISSUE_COLOR}Issue{RESET}"
            ),
        ],
        [
            f"{BOLD}Example:{RESET}",
            f"{PROJECT_COLOR}Earth{RESET}",
            f"└── {MILESTONE_COLOR}United States{RESET}",
            f"  └── {SECTION_COLOR}Maryland{RESET}",
            f"    └── {FEATURE_COLOR}Baltimore{RESET}",
            f"      └── {ISSUE_COLOR}Improve public transportation{RESET}",
        ],
    )

    print()

    print_columns(
        [
            f"{BOLD}3. Neither{RESET}",
            "   Best for simple roadmaps.",
            "",
            "",
            "",
            (
                f"   {PROJECT_COLOR}Project{RESET} -> "
                f"{MILESTONE_COLOR}Milestone{RESET} -> "
                f"{ISSUE_COLOR}Issue{RESET}"
            ),
        ],
        [
            f"{BOLD}Example:{RESET}",
            f"{PROJECT_COLOR}Earth{RESET}",
            f"└── {MILESTONE_COLOR}United States{RESET}",
            f"  ├── {ISSUE_COLOR}Modernize the electrical grid{RESET}",
            f"  └── {ISSUE_COLOR}Improve interstate rail service{RESET}",
        ],
    )

    while True:
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            return "sections"

        if choice == "2":
            return "sections_and_features"

        if choice == "3":
            return "neither"

        print("Please choose 1, 2, or 3.")
