from gitmap.models import Milestone, Requirement
from gitmap.roadmap_numbering import renumber_siblings
from gitmap.gui.confirmation import confirm_remove_item

# =============================================================================
# GITMAP REMOVE ITEM CONTROLLER
# =============================================================================
# Owns the Item Editor Remove workflow.
#
# Removal applies to:
#   - Milestone
#   - Section
#   - Feature
#   - Issue
#   - Requirement
#   - Work Step
#
# This controller is responsible for determining exactly what the user selected,
# locating that object in the roadmap model, confirming removal, applying any
# required renumbering, and refreshing the Editor Preview.
# =============================================================================


# =============================================================================
# PART A — DETERMINE REMOVE TARGET
# =============================================================================
def get_remove_target(editor):
    """Return the exact model/detail object selected for removal."""

    detail = getattr(editor, "roadmap_detail", None)

    # Requirement and Work Step rows point at their exact detail object.
    if detail is not None:
        return detail

    # Structural rows use the main roadmap object.
    return getattr(editor, "roadmap_object", None)

# =============================================================================
# PART B — DETERMINE STRUCTURAL PARENT AND SIBLING LIST
# =============================================================================
def find_structural_parent(roadmap, target):
    """Find the parent model and sibling list for a structural roadmap item."""

    # Milestones live directly beneath the Roadmap.
    if target in roadmap.milestones:
        return roadmap, roadmap.milestones

    for milestone in roadmap.milestones:

        # Sections live beneath Milestones.
        if target in milestone.sections:
            return milestone, milestone.sections

        # Issues may live directly beneath a Milestone.
        if target in milestone.issues:
            return milestone, milestone.issues

        for section in milestone.sections:

            # Features live beneath Sections.
            if target in section.features:
                return section, section.features

            # Issues may live directly beneath a Section.
            if target in section.issues:
                return section, section.issues

            for feature in section.features:

                # Issues may live beneath Features.
                if target in feature.issues:
                    return feature, feature.issues

    return None, None

# =============================================================================
# PART C — REMOVE STRUCTURAL ITEM
# =============================================================================
def remove_structural_item(editor):
    """Confirm and remove the selected structural roadmap item."""

    target = get_remove_target(editor)

    if target is None:
        return False

    parent, siblings = find_structural_parent(
        editor.roadmap,
        target,
    )

    if siblings is None:
        return False

    item_type = type(target).__name__
    title = getattr(target, "title", "")

    approved = confirm_remove_item(
        editor,
        item_type,
        title,
    )

    if not approved:
        return False

    # Remove the selected object from its actual model list.
    siblings.remove(target)

    # Renumber whatever remains at this level.
    if siblings:
        if isinstance(target, Milestone):
            milestone_series = target.number.rsplit(".", 1)[0]

            renumber_siblings(
                siblings,
                milestone_series,
            )
        else:
            renumber_siblings(
                siblings,
                parent.number,
            )

    editor.roadmap.is_modified = True

    if hasattr(editor, "refresh_preview"):
        editor.refresh_preview()

    return True

# =============================================================================
# PART D — REMOVE REQUIREMENT
# =============================================================================
def remove_requirement(editor):
    """Confirm and remove the selected Requirement."""

    target = get_remove_target(editor)

    if not isinstance(target, Requirement):
        return False

    parent_issue = getattr(editor, "roadmap_object", None)

    if parent_issue is None:
        return False

    if target not in parent_issue.requirements:
        return False

    approved = confirm_remove_item(
        editor,
        "Requirement",
        target.text,
    )

    if not approved:
        return False

    parent_issue.requirements.remove(target)

    editor.roadmap.is_modified = True

    if hasattr(editor, "refresh_preview"):
        editor.refresh_preview()

    return True

# =============================================================================
# PART E — ROUTE REMOVE REQUEST
# =============================================================================
def remove_selected_item(editor):
    """Route Delete to the correct removal handler."""

    target = get_remove_target(editor)

    if target is None:
        return False

    # Requirements have their own removal path.
    if isinstance(target, Requirement):
        return remove_requirement(editor)

    # Milestones, Sections, Features, and normal Issues use the
    # structural removal path.
    return remove_structural_item(editor)

# =============================================================================
# PART E — REMOVE WORK STEP
# =============================================================================
def remove_work_step(editor):
    """Confirm and remove the selected Work Step."""

    work_step = getattr(editor, "roadmap_detail", None)
    parent_issue = getattr(editor, "roadmap_object", None)

    if work_step is None or parent_issue is None:
        return False

    if work_step not in parent_issue.work_steps:
        return False

    approved = confirm_remove_item(
        editor,
        "Work Step",
        work_step.title,
    )

    if not approved:
        return False

    parent_issue.work_steps.remove(work_step)

    # Reassign (a), (b), (c), etc. after removing a Work Step.
    renumber_siblings(
        parent_issue.work_steps,
        parent_issue.number,
        parent_type="work_step",
    )

    editor.roadmap.is_modified = True

    if hasattr(editor, "refresh_preview"):
        editor.refresh_preview()

    return True

# =============================================================================
# PART F — ROUTE REMOVE REQUEST
# =============================================================================
def remove_selected_item(editor):
    """Route Delete to the correct removal handler."""

    target = get_remove_target(editor)

    if target is None:
        return False

    # Requirements are exact detail objects beneath an Issue.
    if isinstance(target, Requirement):
        return remove_requirement(editor)

    # Work Steps are also detail objects, but internally they are Issue objects.
    # Check membership in the selected parent Issue instead of relying on class.
    parent_issue = getattr(editor, "roadmap_object", None)

    if (
        parent_issue is not None
        and target in getattr(parent_issue, "work_steps", [])
    ):
        return remove_work_step(editor)

    # Everything else is one of the structural roadmap items.
    return remove_structural_item(editor)