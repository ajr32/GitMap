# =============================================================================
# GITMAP roadmap_tree.py ROAD MAP
# =============================================================================
# Stable navigation labels:
#
#   Part A   - Imports and hidden tree data roles
#   Part B   - Render one Issue and its detail rows
#     B1     - Issue row
#     B2     - Description row
#     B3     - Temporary/debug output
#     B4     - Requirement rows
#     B5     - Work Step rows
#   Part C   - Render a complete Roadmap tree
#     C1     - Roadmap root
#     C2     - Milestones
#     C3     - Sections and Section-level Issues
#     C4     - Features and Feature-level Issues
#   Part D   - Flatten structural rows for the Zoom view
#
# Existing Part labels are STABLE. Insertions should use C5, B4A, etc.
# Do not reletter existing Parts unless we explicitly refactor navigation.
#
# THIS FILE'S JOB:
# Convert the in-memory GitMap model into QTreeWidgetItems. Both the Main
# Window roadmap tree and the Editor Preview can use the same renderer.
#
# IMPORTANT:
# The visible text is only presentation. MODEL_ROLE / DETAIL_ROLE /
# DETAIL_KIND_ROLE preserve the connection from each tree row back to the
# exact model object that row represents.
# =============================================================================

# =============================================================================
# PART A — IMPORTS AND HIDDEN TREE DATA ROLES
# =============================================================================
# Qt provides the tree rows, fonts/colors, and custom ItemDataRole slots.
#
# MODEL_ROLE:
#   The parent GitMap model object represented by a row.
#
# DETAIL_ROLE:
#   The exact child detail object, currently Requirement or Work Step.
#
# DETAIL_KIND_ROLE:
#   A small string describing which kind of detail row was clicked:
#   "description", "requirement", or "work_step".
#
# These roles are critical to Editor selection behavior.
# =============================================================================
from PySide6.QtCore import QFile, Qt
from PySide6.QtGui import QBrush, QColor, QFont
from PySide6.QtWidgets import QTreeWidgetItem

MODEL_ROLE = Qt.ItemDataRole.UserRole
DETAIL_ROLE = Qt.ItemDataRole.UserRole + 1
DETAIL_KIND_ROLE = Qt.ItemDataRole.UserRole + 2


# =============================================================================
# PART B — RENDER ONE ISSUE AND ITS DETAIL ROWS
# =============================================================================
# Adds one Issue underneath the supplied parent tree item, then adds the
# Issue's Description, Requirements, and Work Steps as child rows.
#
# `parent_item` may currently be a Section or Feature tree row.
# =============================================================================
def add_issue_to_tree(parent_item, issue):
    """Add an issue and its contents to the roadmap tree."""

    # -------------------------------------------------------------------------
    # PART B1 — ISSUE ROW
    # -------------------------------------------------------------------------
    # The Issue row itself stores the exact Issue model in MODEL_ROLE.
    # -------------------------------------------------------------------------
    issue_item = QTreeWidgetItem([f"{issue.number} {issue.title}"])
    issue_item.setData(0, MODEL_ROLE, issue)
    parent_item.addChild(issue_item)

    issue_item.setForeground(0, QColor("#FFFFFF"))

    # -------------------------------------------------------------------------
    # PART B2 — DESCRIPTION ROW
    # -------------------------------------------------------------------------
    # Description is shown as gray italic text beneath its Issue.
    #
    # It points MODEL_ROLE back to the Issue and uses DETAIL_KIND_ROLE to say
    # "description". There is no separate Description model object, so it does
    # not need DETAIL_ROLE.
    # -------------------------------------------------------------------------
    if issue.description:
        description_item = QTreeWidgetItem([issue.description])
        description_item.setData(0, MODEL_ROLE, issue)
        description_item.setData(0, DETAIL_KIND_ROLE, "description")

        description_font = QFont()
        description_font.setItalic(True)
        # description_font.setPointSize(description_font.pointSize() - 1)

        description_item.setFont(0, description_font)
        description_item.setForeground(0, QColor("#808080"))

        issue_item.addChild(description_item)

    # -------------------------------------------------------------------------
    # PART B3 — TEMPORARY / DEBUG OUTPUT
    # -------------------------------------------------------------------------
    # These prints were useful while verifying parser -> model -> tree mapping.
    # They are noisy during normal use and are a cleanup candidate later.
    # They intentionally remain here for now so this documentation pass does
    # not change behavior.
    # -------------------------------------------------------------------------
    print("\nISSUE:", issue.number, issue.title)

    print("  DESCRIPTION:", repr(issue.description))
    for requirement in issue.requirements:
        print("  REQUIREMENT:", repr(requirement.text))

    for work_step in issue.work_steps:
        print("  WORK STEP:", repr(work_step.title))

    # -------------------------------------------------------------------------
    # PART B4 — REQUIREMENT ROWS
    # -------------------------------------------------------------------------
    # Each Requirement row:
    #   * displays a bullet + cleaned Requirement text
    #   * stores the parent Issue in MODEL_ROLE
    #   * stores the exact Requirement object in DETAIL_ROLE
    #   * stores "requirement" in DETAIL_KIND_ROLE
    #
    # Legacy Markdown checkbox prefixes are stripped for display only.
    # -------------------------------------------------------------------------
    for requirement in issue.requirements:
        requirement_text = requirement.text

        if requirement_text.strip() == issue.description.strip():
            continue

        # Remove legacy Markdown checkbox syntax.
        for prefix in (
            "- [ ] ",
            "* [ ] ",
            "[ ] ",
            "- [x] ",
            "* [x] ",
            "[x] ",
            "- [X] ",
            "* [X] ",
            "[X] ",
        ):
            if requirement_text.startswith(prefix):
                requirement_text = requirement_text[len(prefix) :]
                break

        requirement_item = QTreeWidgetItem([f"• {requirement_text}"])
        requirement_item.setData(0, MODEL_ROLE, issue)
        requirement_item.setData(0, DETAIL_ROLE, requirement)
        requirement_item.setData(0, DETAIL_KIND_ROLE, "requirement")

        requirement_item.setForeground(0, QColor("#B08CC6"))

        issue_item.addChild(requirement_item)

    # -------------------------------------------------------------------------
    # PART B5 — WORK STEP ROWS
    # -------------------------------------------------------------------------
    # Each Work Step row displays its marker and title, and preserves both the
    # parent Issue and exact Work Step object in the hidden data roles.
    #
    # Future Add/Delete/Renumber Work-Step behavior should use the existing
    # 0.7 numbering backend rather than inventing separate GUI numbering.
    # -------------------------------------------------------------------------
    for work_step in issue.work_steps:
        work_step_item = QTreeWidgetItem(
            [f"{work_step.work_step_marker} {work_step.title}"]
        )
        work_step_item.setData(0, MODEL_ROLE, issue)
        work_step_item.setData(0, DETAIL_ROLE, work_step)
        work_step_item.setData(0, DETAIL_KIND_ROLE, "work_step")

        work_step_item.setForeground(0, QColor("#4F8A5B"))

        issue_item.addChild(work_step_item)


# =============================================================================
# PART C — RENDER A COMPLETE ROADMAP TREE
# =============================================================================
# Clears the supplied QTreeWidget and rebuilds it from the current in-memory
# Roadmap model.
#
# This shared renderer is used for both:
#   * Main Window roadmap tree
#   * Editor Preview tree
#
# It returns the Roadmap root tree item after expanding the tree.
#
# KNOWN STRUCTURAL GAP / SKIPPED 0.7 CONCERN:
# This current implementation renders Issues under Sections and Features, but
# DOES NOT render Issues directly under Milestones. That matters for roadmaps
# configured without Sections. Do not silently work around it elsewhere; fix
# the renderer intentionally when we address that structural case.
# =============================================================================
def populate_roadmap_tree(tree, roadmap):
    tree.clear()

    # -------------------------------------------------------------------------
    # PART C1 — ROADMAP ROOT
    # -------------------------------------------------------------------------
    # Visual root containing the Roadmap name.
    #
    # It intentionally has no MODEL_ROLE, so it is not treated as a normal
    # editable/add-reference model item.
    # -------------------------------------------------------------------------
    test_item = QTreeWidgetItem([roadmap.name])
    tree.addTopLevelItem(test_item)

    # -------------------------------------------------------------------------
    # PART C2 — MILESTONES
    # -------------------------------------------------------------------------
    # Milestones are cyan-ish and bold and store their Milestone model.
    #
    # NOTE: milestone.issues are not currently rendered here. See the known
    # structural gap in the Part C header.
    # -------------------------------------------------------------------------
    for milestone in roadmap.milestones:
        milestone_item = QTreeWidgetItem([f"{milestone.number} {milestone.title}"])
        milestone_item.setData(0, MODEL_ROLE, milestone)
        milestone_font = QFont()
        milestone_font.setBold(True)
        milestone_item.setFont(0, milestone_font)

        milestone_item.setData(
            0,
            Qt.ItemDataRole.ForegroundRole,
            QColor("#008B8B"),
        )

        test_item.addChild(milestone_item)

        # ---------------------------------------------------------------------
        # PART C3 — SECTIONS AND SECTION-LEVEL ISSUES
        # ---------------------------------------------------------------------
        # Sections are gold and bold.
        # Issues attached directly to a Section are rendered before Features.
        # ---------------------------------------------------------------------
        for section in milestone.sections:
            section_item = QTreeWidgetItem([f"{section.number} {section.title}"])
            section_item.setData(0, MODEL_ROLE, section)
            section_font = QFont()
            section_font.setBold(True)
            section_item.setFont(0, section_font)

            section_item.setForeground(0, QColor("#D49A00"))

            milestone_item.addChild(section_item)

            for issue in section.issues:
                add_issue_to_tree(section_item, issue)

            # -----------------------------------------------------------------
            # PART C4 — FEATURES AND FEATURE-LEVEL ISSUES
            # -----------------------------------------------------------------
            # Features are muted red and bold. Issues belonging to a Feature
            # are rendered underneath that Feature using Part B.
            # -----------------------------------------------------------------
            for feature in section.features:
                feature_item = QTreeWidgetItem([f"{feature.number} {feature.title}"])
                feature_item.setData(0, MODEL_ROLE, feature)

                feature_font = QFont()
                feature_font.setBold(True)
                feature_item.setFont(0, feature_font)
                feature_item.setForeground(0, QColor("#C05050"))

                section_item.addChild(feature_item)

                for issue in feature.issues:
                    add_issue_to_tree(feature_item, issue)

    tree.expandAll()
    return test_item


# =============================================================================
# PART D — FLATTEN STRUCTURAL ROWS FOR THE ZOOM VIEW
# =============================================================================
# Converts the hierarchical QTreeWidget into a simple ordered Python list.
#
# Rows with BOTH DETAIL_ROLE and DETAIL_KIND_ROLE empty are considered
# structural rows and are included. Detail rows such as Description,
# Requirement, and Work Step are excluded.
#
# app.py uses this list to find the selected row's nearby neighbors and build
# the small Zoom tree.
#
# NOTE ABOUT CURRENT RECURSION:
# Child traversal is currently inside the `if`. That means a detail row stops
# traversal below itself. Today those detail rows have no structural children,
# so this matches the current tree shape. If detail rows ever gain children,
# revisit this rather than assuming the traversal is general-purpose.
# =============================================================================
def flatten_tree(tree):
    items = []

    def visit(item):
        if item.data(0, DETAIL_ROLE) is None and item.data(0, DETAIL_KIND_ROLE) is None:
            items.append(item)
            for i in range(item.childCount()):
                visit(item.child(i))

    for i in range(tree.topLevelItemCount()):
        visit(tree.topLevelItem(i))

    return items
