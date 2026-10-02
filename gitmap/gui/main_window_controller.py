import copy
import traceback

from PySide6.QtWidgets import (
    QFileDialog,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QTreeWidget,
)

from gitmap.github_sync.removed_issue_sync import sync_removed_issues
from gitmap.github_sync.label_sync import sync_labels
from gitmap.github_sync.milestone_sync import sync_milestones
from gitmap.github_sync.relationship_sync import sync_sub_issue_relationships
from gitmap.github_sync.issue_sync import (
    sync_issues,
)
from gitmap.github_sync.repository import (
    RepositoryInfo,
    create_repository,
    verify_repository,
)
from gitmap.gui.cancel_changes import cancel_changes
from gitmap.gui.editor_controller import open_editor
from gitmap.gui.new_roadmap_controller import (
    build_roadmap_from_answers,
    load_structure_dialog,
)

from gitmap.github_sync.issue_lookup import (
    find_github_issues_by_gitmap_ids,
    get_existing_issues,
)
from gitmap.gui.removal_confirmation import confirm_sync_removals
from gitmap.gui.review_dialog import load_review_dialog
from gitmap.gui.roadmap_editor_controller import open_builder
from gitmap.gui.roadmap_structure import infer_roadmap_structure
from gitmap.gui.roadmap_tree import MODEL_ROLE, populate_roadmap_tree
from gitmap.gui.settings_controller import load_settings_dialog
from gitmap.gui.sync_dialog import load_sync_dialog
from gitmap.github_sync.sync_plan import (
    build_initial_sync_plan,
    build_sync_plan,
)
from gitmap.github_sync.sync_validation import validate_synchronization_plan
from gitmap.roadmap.parser import parse_roadmap
from gitmap.settings import load_github_username


class MainWindowState:
    """Runtime state for the roadmap currently loaded in GitMap."""

    active_roadmap_path: str | None = None
    active_roadmap: object | None = None
    review_baseline_roadmap: object | None = None

    selected_roadmap_object: object | None = None

    item_editor_window: object | None = None
    review_window: object | None = None
    new_roadmap_creator_window: object | None = None

    @property
    def roadmap_is_active(self):
        return self.active_roadmap is not None


def setup_main_window(window):
    """Initialize the basic Main Window widgets."""
    roadmap_tree = window.findChild(QTreeWidget, "roadmap_Tree")
    roadmap_tree.setHeaderHidden(True)

    roadmap_tree.setStyleSheet("""
        QTreeWidget {
            background-color: black;
            color: black;
        }
    """)

    roadmap_name = window.findChild(QTextEdit, "textEdit")
    roadmap_name.setReadOnly(True)

    window.gitmap_state = MainWindowState()
    state = window.gitmap_state

    def refresh_main_roadmap():
        if not state.roadmap_is_active:
            return

        roadmap_name.setText(state.active_roadmap.name)

        populate_roadmap_tree(
            roadmap_tree,
            state.active_roadmap,
        )

    state.refresh_main_roadmap = refresh_main_roadmap

    # -------------------------------------------------------------------------
    # Main Window roadmap selection
    # -------------------------------------------------------------------------

    def roadmap_selection_changed():
        selected_items = roadmap_tree.selectedItems()

        if not selected_items:
            state.selected_roadmap_object = None
            return

        selected_item = selected_items[0]
        state.selected_roadmap_object = selected_item.data(0, MODEL_ROLE)

    roadmap_tree.itemSelectionChanged.connect(roadmap_selection_changed)

    # -------------------------------------------------------------------------
    # Main Window buttons
    # -------------------------------------------------------------------------

    new_roadmap_button = window.findChild(QPushButton, "New_Roadmap")
    open_button = window.findChild(QPushButton, "Open_Roadmap")
    edit_button = window.findChild(QPushButton, "edit_roadmap_button")
    review_button = window.findChild(QPushButton, "review_button")
    cancel_button = window.findChild(QPushButton, "cancel_button")
    settings_button = window.findChild(QPushButton, "settings_button")
    sync_to_github_button = window.findChild(QPushButton, "sync_to_github_button")

    edit_button.hide()
    review_button.hide()
    cancel_button.hide()

    # -------------------------------------------------------------------------
    # New Roadmap
    # -------------------------------------------------------------------------

    def create_new_roadmap():
        structure_dialog = load_structure_dialog()

        if not structure_dialog.exec():
            return

        roadmap = build_roadmap_from_answers(structure_dialog.answers)

        state.active_roadmap_path = None
        state.active_roadmap = roadmap
        state.review_baseline_roadmap = copy.deepcopy(roadmap)
        state.selected_roadmap_object = None

        roadmap_name.setText(roadmap.name)
        populate_roadmap_tree(roadmap_tree, roadmap)

        edit_button.show()
        review_button.show()
        cancel_button.show()
        state.new_roadmap_creator_window = open_builder(
            roadmap,
            state,
        )

    new_roadmap_button.clicked.connect(create_new_roadmap)

    # -------------------------------------------------------------------------
    # Open Roadmap
    # -------------------------------------------------------------------------

    def open_roadmap():
        roadmap_path, _ = QFileDialog.getOpenFileName(
            window,
            "Open Roadmap",
            "",
            "Markdown Roadmaps (*.md);;All Files (*.*)",
        )

        if not roadmap_path:
            return

        try:
            roadmap = parse_roadmap(roadmap_path)
            infer_roadmap_structure(roadmap)

        except (OSError, UnicodeError) as error:
            traceback.print_exc()

            QMessageBox.critical(
                window,
                "Unable to Open Roadmap",
                f"GitMap could not open the selected roadmap.\n\n"
                f"File: {roadmap_path}\n\n"
                f"Error: {error}",
            )
            return

        state.active_roadmap_path = roadmap_path
        state.active_roadmap = roadmap

        # Local review baseline: the roadmap as it existed when this editing session began.
        # This is intentionally separate from GitHub remote synchronization state.
        state.review_baseline_roadmap = copy.deepcopy(roadmap)

        roadmap_name.setText(roadmap.name)
        populate_roadmap_tree(roadmap_tree, roadmap)

        edit_button.show()
        review_button.show()
        cancel_button.show()

    open_button.clicked.connect(open_roadmap)

    # -------------------------------------------------------------------------
    # Edit Roadmap
    # -------------------------------------------------------------------------

    def open_active_editor(target_model=None):
        if not state.roadmap_is_active:
            return

        state.item_editor_window = open_editor(
            state.active_roadmap,
            state,
            refresh_main_roadmap,
        )
        if target_model is not None:
            state.item_editor_window.select_preview_model(target_model)

    edit_button.clicked.connect(lambda: open_active_editor())

    # -------------------------------------------------------------------------
    # Main Window double-click
    # -------------------------------------------------------------------------

    def roadmap_item_double_clicked(item, column):
        model = item.data(0, MODEL_ROLE)

        if model is None:
            return

        open_active_editor(model)

    roadmap_tree.itemDoubleClicked.connect(roadmap_item_double_clicked)
    roadmap_tree.setExpandsOnDoubleClick(False)

    # -------------------------------------------------------------------------
    # Review Changes
    # -------------------------------------------------------------------------

    def open_review_window():
        if not state.roadmap_is_active:
            return

        state.review_window = load_review_dialog(
            state.review_baseline_roadmap,
            state.active_roadmap,
        )

        state.review_window.show()

    review_button.clicked.connect(open_review_window)

    # -------------------------------------------------------------------------
    # Cancel Changes
    # -------------------------------------------------------------------------

    def cancel_pending_changes():
        if not state.roadmap_is_active:
            return

        restored_roadmap = cancel_changes(
            window,
            state.review_baseline_roadmap,
        )

        if restored_roadmap is None:
            return

        state.active_roadmap = restored_roadmap
        state.selected_roadmap_object = None

        populate_roadmap_tree(
            roadmap_tree,
            state.active_roadmap,
        )

    cancel_button.clicked.connect(cancel_pending_changes)

    # -------------------------------------------------------------------------
    # Open Settings
    # -------------------------------------------------------------------------

    def open_settings():
        settings_dialog = load_settings_dialog()
        settings_dialog.exec()

    settings_button.clicked.connect(open_settings)

    # -------------------------------------------------------------------------
    # Sync to GitHub
    # -------------------------------------------------------------------------

    def open_github_sync():
        dialog = load_sync_dialog()

        if not dialog.exec():
            return

        repository_name = dialog.repository
        create_new = dialog.create_repository
        username = load_github_username()

        if not username:
            QMessageBox.warning(
                window,
                "GitHub Settings Required",
                "Open Settings and enter your GitHub username first.",
            )
            return

        try:
            if create_new:
                repository = create_repository(repository_name)

            else:
                info = RepositoryInfo(
                    username=username,
                    repository=repository_name,
                )

                repository = verify_repository(info)

        except ValueError as error:
            QMessageBox.critical(
                window,
                "GitHub Repository Error",
                str(error),
            )
            return

        try:
            existing_issues = get_existing_issues(
                repository,
                state.active_roadmap,
            )

            if not existing_issues:
                # First synchronization still gets a complete plan so the exact
                # work that will execute can be validated before any sync mutation.
                plan = build_initial_sync_plan(
                    state.active_roadmap,
                )
            else:
                # Temporary bridge: the sync plan still compares against the
                # local review baseline until remote-state planning replaces it.
                plan = build_sync_plan(
                    state.review_baseline_roadmap,
                    state.active_roadmap,
                )

            conflicts = validate_synchronization_plan(
                plan,
                state.active_roadmap,
                existing_issues,
            )

            if conflicts:
                QMessageBox.critical(
                    window,
                    "GitHub Sync Validation Failed",
                    "GitMap found problems that must be fixed before "
                    "synchronization can continue:\n\n"
                    + "\n".join(f"• {conflict}" for conflict in conflicts),
                )
                return

            removed_issue_ids = plan["removed_issues"]
            removed_hierarchy_ids = plan["removed_hierarchy"]
            removed_ids = removed_issue_ids + removed_hierarchy_ids

            removed_github_issues = []
            removed_github_hierarchy = []

            if removed_ids:
                removed_github_issues = find_github_issues_by_gitmap_ids(
                    existing_issues,
                    removed_issue_ids,
                )
                removed_github_hierarchy = find_github_issues_by_gitmap_ids(
                    existing_issues,
                    removed_hierarchy_ids,
                )

                # Confirmation also happens before mutation. Cancelling here leaves
                # labels, milestones, Issues, and relationships untouched.
                if not confirm_sync_removals(
                    window,
                    removed_github_issues,
                    removed_github_hierarchy,
                ):
                    return

            # Nothing above this point mutates synchronization state. Once
            # validation and confirmation pass, execute the exact prepared plan.
            sync_milestones(repository, state.active_roadmap)
            sync_labels(repository, state.active_roadmap)

            if removed_ids:
                sync_removed_issues(
                    removed_github_issues + removed_github_hierarchy,
                )

            issues_to_sync = plan["added_issues"] + plan["changed_issues"]

            if issues_to_sync:
                sync_issues(
                    repository,
                    state.active_roadmap,
                    issues_to_sync=issues_to_sync,
                    update_issues=plan["changed_issues"],
                )

            if plan["added_hierarchy_mappings"]:
                sync_issues(
                    repository,
                    state.active_roadmap,
                    issues_to_sync=[],
                    hierarchy_mappings_to_sync=plan["added_hierarchy_mappings"],
                    hierarchy_expected_operation="create",
                    progress_total=len(plan["added_hierarchy_mappings"]),
                )

            if plan["changed_hierarchy_mappings"]:
                sync_issues(
                    repository,
                    state.active_roadmap,
                    issues_to_sync=[],
                    hierarchy_mappings_to_sync=plan["changed_hierarchy_mappings"],
                    hierarchy_expected_operation="update",
                    progress_total=len(plan["changed_hierarchy_mappings"]),
                )

            # Relationships remain a final synchronization stage. The structured
            # plan already has relationship fields; a later planning phase can
            # populate them before this executor is converted to consume them.
            sync_sub_issue_relationships(
                repository,
                state.active_roadmap,
            )

        except Exception as error:
            QMessageBox.critical(
                window,
                "GitHub Sync Failed",
                str(error),
            )
            return

        QMessageBox.information(
            window,
            "GitHub Sync Complete",
            (f"GitMap successfully synchronized with:\n\n{repository.full_name}"),
        )

    sync_to_github_button.clicked.connect(open_github_sync)
