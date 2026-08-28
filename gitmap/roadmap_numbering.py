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


def generate_child_number(parent_number, sibling_index):
    """Generate a hierarchical number beneath a parent."""

    return f"{parent_number}.{sibling_index}"


def generate_milestone_number(starting_series, sibling_index):
    """Generate a milestone number."""

    return f"{starting_series}.{sibling_index}"


def generate_work_step_number(sibling_index):
    """Generate a letter-based work step number."""

    if sibling_index < 1:
        raise ValueError("Work step index must be at least 1.")

    letters = ""
    number = sibling_index

    while number:
        number -= 1
        letters = chr(ord("a") + number % 26) + letters
        number //= 26

    return f"({letters})"