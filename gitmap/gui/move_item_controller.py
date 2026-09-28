"""Backend helpers for moving roadmap items in the GitMap GUI."""

from dataclasses import dataclass

from gitmap.models import Feature, Issue, Milestone, Roadmap, Section
from gitmap.roadmap_numbering import (
    collect_numbering_changes,
    remember_original_numbers,
    renumber_siblings,
)


@dataclass
class MoveLocation:
    """Describe the list that currently contains a roadmap item."""

    parent: object
    attribute: str
    items: list
    index: int


@dataclass
class MoveDestination:
    """Describe a legal destination list for a roadmap item."""

    parent: object
    attribute: str
    items: list

    @property
    def label(self):
        parent_title = getattr(self.parent, "title", None)

        if isinstance(self.parent, Roadmap):
            return self.parent.name

        parent_number = getattr(self.parent, "number", "")
        if parent_number and parent_title:
            return f"{parent_number} {parent_title}"

        return parent_title or type(self.parent).__name__


def _walk_containers(roadmap):
    """Yield every parent/list pair that can contain movable roadmap items."""

    yield roadmap, "milestones", roadmap.milestones

    for milestone in roadmap.milestones:
        yield milestone, "sections", milestone.sections
        yield milestone, "issues", milestone.issues

        for section in milestone.sections:
            yield section, "features", section.features
            yield section, "issues", section.issues

            for feature in section.features:
                yield feature, "issues", feature.issues

                for issue in feature.issues:
                    yield issue, "work_steps", issue.work_steps

            for issue in section.issues:
                yield issue, "work_steps", issue.work_steps

        for issue in milestone.issues:
            yield issue, "work_steps", issue.work_steps


def find_move_location(roadmap, target):
    """Return the current parent/list/index for target, or None if not found."""

    for parent, attribute, items in _walk_containers(roadmap):
        for index, item in enumerate(items):
            if item is target:
                return MoveLocation(
                    parent=parent,
                    attribute=attribute,
                    items=items,
                    index=index,
                )

    return None


def get_move_destinations(roadmap, target):
    """Return legal destination containers for target."""

    destinations = []

    for parent, attribute, items in _walk_containers(roadmap):
        if _can_move_to(roadmap, target, parent, attribute):
            destinations.append(
                MoveDestination(
                    parent=parent,
                    attribute=attribute,
                    items=items,
                )
            )

    return destinations


def _can_move_to(roadmap, target, parent, attribute):
    """Return True when target may legally be placed in this container."""

    if isinstance(target, Milestone):
        return isinstance(parent, Roadmap) and attribute == "milestones"

    if isinstance(target, Section):
        return (
            roadmap.use_sections
            and isinstance(parent, Milestone)
            and attribute == "sections"
        )

    if isinstance(target, Feature):
        return (
            roadmap.use_features
            and isinstance(parent, Section)
            and attribute == "features"
        )

    if isinstance(target, Issue):
        # Work Steps are represented by Issue objects too. A populated
        # work_step_marker distinguishes them from normal roadmap Issues.
        if getattr(target, "work_step_marker", ""):
            return isinstance(parent, Issue) and attribute == "work_steps"

        if isinstance(parent, Milestone):
            return not roadmap.use_sections and attribute == "issues"

        if isinstance(parent, Section):
            return roadmap.allow_issues_under_sections and attribute == "issues"

        if isinstance(parent, Feature):
            return roadmap.allow_issues_under_features and attribute == "issues"

    return False


def get_position_choices(destination, target):
    """Return friendly insertion choices for a destination."""

    siblings = [item for item in destination.items if item is not target]

    choices = ["At beginning"]

    for item in siblings:
        number = getattr(item, "number", "")
        title = getattr(item, "title", "")
        label = f"{number} {title}".strip()
        choices.append(f"Before {label}")
        choices.append(f"After {label}")

    choices.append("At end")
    return choices


def position_index_from_choice(destination, target, choice):
    """Translate a friendly position choice into a list insertion index."""

    siblings = [item for item in destination.items if item is not target]

    if choice == "At beginning":
        return 0

    if choice == "At end":
        return len(siblings)

    for index, item in enumerate(siblings):
        number = getattr(item, "number", "")
        title = getattr(item, "title", "")
        label = f"{number} {title}".strip()

        if choice == f"Before {label}":
            return index

        if choice == f"After {label}":
            return index + 1

    raise ValueError(f"Unknown move position: {choice}")


def move_item(roadmap, target, destination, insert_index):
    """Move target and renumber affected roadmap items.

    Returns a list of numbering changes.
    """

    source = find_move_location(roadmap, target)

    if source is None:
        raise ValueError("The selected item could not be found in the roadmap.")

    remember_original_numbers(roadmap.milestones)

    source.items.pop(source.index)

    # If moving inside the same list, insert_index was calculated against the
    # list with target excluded, which now matches the actual list.
    destination.items.insert(insert_index, target)

    _renumber_container(roadmap, source.parent, source.attribute)

    if (
        destination.parent is not source.parent
        or destination.attribute != source.attribute
    ):
        _renumber_container(
            roadmap,
            destination.parent,
            destination.attribute,
        )

    return collect_numbering_changes(roadmap.milestones)


def _renumber_container(roadmap, parent, attribute):
    """Renumber one roadmap container using GitMap's numbering backend."""

    items = getattr(parent, attribute)

    if isinstance(parent, Roadmap) and attribute == "milestones":
        renumber_siblings(
            items,
            str(roadmap.starting_series),
        )
        return

    parent_number = getattr(parent, "number", "")

    if isinstance(parent, Milestone) and attribute == "issues":
        renumber_siblings(
            items,
            parent_number,
            parent_type="milestone_issue",
        )
        return

    if isinstance(parent, Section) and attribute == "issues":
        renumber_siblings(
            items,
            parent_number,
            parent_type="section_issue",
        )
        return

    if isinstance(parent, Issue) and attribute == "work_steps":
        renumber_siblings(
            items,
            parent_number,
            parent_type="work_step",
        )
        return

    renumber_siblings(items, parent_number)
