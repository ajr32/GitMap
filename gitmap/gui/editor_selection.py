from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import QTreeWidgetItem

from gitmap.gui.add_item_controller import show_add_type_choices
from gitmap.gui.item_editor import configure_editor, get_item_type
from gitmap.gui.roadmap_tree import flatten_tree, populate_roadmap_tree

MODEL_ROLE = Qt.ItemDataRole.UserRole
DETAIL_ROLE = Qt.ItemDataRole.UserRole + 1
DETAIL_KIND_ROLE = Qt.ItemDataRole.UserRole + 2

def setup_editor_selection(
    editor,
    roadmap,
    preview_tree,
    context_tree,
    main_roadmap_tree=None,
):

    # ---------------------------------------------------------------------
    # PART K — REFRESH EDITOR PREVIEW
    # ---------------------------------------------------------------------
    # item_editor.py calls editor.refresh_preview() after Apply changes the
    # in-memory model. This callback redraws the Editor Preview from that
    # model.
    # ---------------------------------------------------------------------
    def select_preview_model(target_model):
        for item in flatten_tree(preview_tree):
            if item.data(0, MODEL_ROLE) is target_model:
                preview_tree.setCurrentItem(item)
                return

    editor.select_preview_model = select_preview_model

    def refresh_editor_preview():
        populate_roadmap_tree(preview_tree, roadmap)

        if main_roadmap_tree is not None:
            populate_roadmap_tree(main_roadmap_tree, roadmap)

    editor.refresh_preview = refresh_editor_preview

    # =====================================================================
    # PART L — EDITOR PREVIEW SELECTION ROUTER
    # =====================================================================
    # This function is the central "what happens when I click Preview?"
    # router. There are TWO modes:
    #
    # NORMAL MODE:
    #   * highlights the selected Preview row
    #   * rebuilds Zoom using nearby structural rows
    #   * stores the selected model/detail on the Editor
    #   * calls configure_editor() to display editable fields
    #
    # ADD MODE:
    #   * stores the clicked row as the Add reference
    #   * decides which child/sibling types are structurally legal
    #   * fills the Add popup radio buttons
    #   * RETURNS EARLY, so normal Zoom/editor selection code does not run
    #
    # That early return is especially relevant to the parked
    # "Cancel Add -> Zoom stops" bug: if add_mode remains True after Cancel,
    # every future Preview click keeps taking the Add branch.
    #
    # STRUCTURE RULES CURRENTLY USED:
    #   Issue     -> Issue / Requirement / Work Step
    #   Feature   -> Feature / Issue
    #   Section   -> Section + optional Feature/Issue according to Roadmap
    #   Milestone -> Milestone + Section, OR Issue when sections aren't used
    #
    # SKIPPED 0.7 DEPENDENCY TO REMEMBER:
    # Structural add/move/renumber behavior must use the existing 0.7
    # numbering/structure backend rather than inventing a GUI-only system.
    # =====================================================================
    def preview_selection_changed(current, previous):
        if previous is not None:
            previous.setBackground(0, QBrush())

        if current is None:
            return

        current.setBackground(0, QColor("#3A4A5A"))

        model = current.data(0, MODEL_ROLE)
        detail = current.data(0, DETAIL_ROLE)
        detail_kind = current.data(0, DETAIL_KIND_ROLE)

        if editor.add_mode:
            editor.add_reference = current
            editor.add_reference_model = model
            editor.add_reference_detail = detail
            editor.add_reference_detail_kind = detail_kind

            show_add_type_choices(
                editor,
                model,
                roadmap,
                get_item_type,
            )
            return

        items = flatten_tree(preview_tree)
        zoom_anchor = current

        if detail_kind is not None:
            for item in items:
                if item.data(0, MODEL_ROLE) is model:
                    zoom_anchor = item
                    break

        if zoom_anchor in items:
            current_index = items.index(zoom_anchor)
            context_tree.clear()

            start = max(0, current_index - 4)
            end = min(len(items), current_index + 5)

            for item in items[start:end]:
                zoom_item = QTreeWidgetItem([item.text(0)])

                if item is zoom_anchor:
                    zoom_item.setBackground(0, QColor("#3A4A5A"))

                context_tree.addTopLevelItem(zoom_item)

        if model is not None:
            editor.roadmap_object = model
            editor.roadmap_detail = detail

            configure_editor(
                editor,
                model,
                detail,
                detail_kind,
            )

    preview_tree.currentItemChanged.connect(preview_selection_changed)