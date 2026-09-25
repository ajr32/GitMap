# print("### APP_OLD.PY LOADED ###")  # TEST
#
# # =============================================================================
# # GITMAP app.py ROAD MAP
# # =============================================================================
# # Use these labels when discussing this file:
# #
# #   Part A  - Imports and shared tree data roles
# #   Part B  - New Roadmap structure questionnaire
# #   Part C  - Application startup / shared state
# #   Part D  - Main Window roadmap tree setup
# #   Part E  - Open an existing roadmap
# #   Part F  - Main Window tree selection
# #   Part G  - Open/setup Roadmap Editor
# #   Part H  - Enter Add mode
# #   Part I  - Show Add popup
# #   Part J  - Editor Preview + Zoom widget setup
# #   Part K  - Refresh Editor Preview
# #   Part L  - Editor Preview selection router
# #   Part M  - Build Zoom
# #   Part N  - Load selection into editor fields
# #   Part O  - Main Window double-click behavior
# #   Part P  - Main Window button wiring
# #   Part Q  - Create a new unsaved Roadmap model
# #   Part R  - Show Main Window / Qt event loop
# #   Part S  - Python module entry point
# #
# # Example directions can now be:
# #   "Go to Part H, then H1."
# #   "The Add bug is in Part G2/H."
# #
# # These comments are navigation/documentation only. They do not intentionally
# # change GitMap behavior.
# # =============================================================================
# # ============================================================
# # MAIN GITMAP WINDOW
# # Loads the GitMap interface created in Qt Designer.
# # ============================================================
# # =============================================================================
# # PART A — IMPORTS AND SHARED TREE DATA ROLES
# # =============================================================================
# # Imports used by the main GitMap GUI.
# #
# # The MODEL_ROLE / DETAIL_ROLE / DETAIL_KIND_ROLE constants below are the
# # hidden data slots attached to QTreeWidgetItems. They let a visible tree row
# # point back to the real Roadmap/Milestone/Section/Feature/Issue object, or to
# # a Requirement / Work Step detail.
# #
# # When debugging "I clicked X but GitMap edited Y", Part A's roles are one of
# # the first things to remember.
# # =============================================================================
# import copy
# import sys
# import traceback
# from pathlib import Path
#
# from PySide6.QtCore import QFile, Qt
# from PySide6.QtGui import QBrush, QColor
# from PySide6.QtUiTools import QUiLoader
# from PySide6.QtWidgets import (
#     QAbstractItemView,
#     QApplication,
#     QFileDialog,
#     QMessageBox,
#     QPushButton,
#     QTextEdit,
#     QTreeWidget,
#     QTreeWidgetItem,
# )
#
# from gitmap.gui.add_item_controller import (
#     continue_add_item,
#     finish_add,
#     never_mind_add,
#     show_add_type_choices,
#     start_add_mode,
# )
# from gitmap.gui.add_item_dialog import load_add_item_dialog
# from gitmap.gui.cancel_changes import cancel_changes
# from gitmap.gui.item_editor import (
#     configure_editor,
#     get_item_type,
#     load_item_editor,
# )
# from gitmap.gui.new_roadmap_creator import load_new_roadmap_creator
# from gitmap.gui.remove_item_controller import (
#     remove_selected_item,
# )
# from gitmap.gui.review_dialog import load_review_dialog
# from gitmap.gui.roadmap_structure import infer_roadmap_structure
# from gitmap.gui.roadmap_tree import (
#     flatten_tree,
#     populate_roadmap_tree,
# )
# from gitmap.gui.structure_questions import QUESTIONS
# from gitmap.models import Roadmap
# from gitmap.parser import parse_roadmap
#
# MODEL_ROLE = Qt.ItemDataRole.UserRole
# DETAIL_ROLE = Qt.ItemDataRole.UserRole + 1
# DETAIL_KIND_ROLE = Qt.ItemDataRole.UserRole + 2
#
#
# # =============================================================================
# # PART B — NEW ROADMAP STRUCTURE DIALOG
# # =============================================================================
# # Everything in this function controls the questionnaire shown when creating
# # a NEW roadmap.
# #
# # It does NOT create the Roadmap model itself. It gathers answers and leaves
# # them on `dialog.answers`. Part K later uses those answers to build the model.
# #
# # Nested helpers in this part:
# #   validate_configuration() - rejects impossible combinations.
# #   update_details()          - records the selected radio-button answer and
# #                               updates the explanation/example.
# #   show_question()           - redraws the dialog for a particular question.
# #   question_applies()        - decides which conditional questions to skip.
# #   go_forward()              - saves special values and advances.
# #   go_back()                 - returns to the previous applicable question.
# #
# # FUTURE REFACTOR:
# # This whole Part B is a natural controller to move out of app.py later.
# # =============================================================================
# def load_structure_dialog():
#     """Load the new-roadmap structure dialog."""
#
#     ui_path = Path(__file__).with_name("structure_dialog.ui")
#
#     ui_file = QFile(str(ui_path))
#     ui_file.open(QFile.OpenModeFlag.ReadOnly)
#
#     loader = QUiLoader()
#     dialog = loader.load(ui_file)
#     current_question = 0
#     question = QUESTIONS[current_question]
#
#     dialog.starting_series_number.hide()
#     dialog.project_name.hide()
#
#     answers = {}
#
#     dialog.answers = answers
#
#     dialog.structure_subject.setText(question["subject"])
#     dialog.structure_subject.adjustSize()
#     dialog.structure_question.setPlainText(question["question"])
#
#     buttons = [
#         dialog.Button1,
#         dialog.Button2,
#         dialog.Button3,
#         dialog.Button4,
#     ]
#
#     for index, button in enumerate(buttons):
#         if index < len(question["options"]):
#             button.setText(question["options"][index]["text"])
#             button.show()
#         else:
#             button.hide()
#
#     def validate_configuration():
#         if answers.get("use_features") and not answers.get("use_sections"):
#             return False
#
#         if answers.get("allow_issues_under_sections") and not answers.get(
#             "use_sections"
#         ):
#             return False
#
#         if answers.get("allow_issues_under_features") and not answers.get(
#             "use_features"
#         ):
#             return False
#
#         return True
#
#     def update_details():
#         for index, button in enumerate(buttons):
#             if button.isChecked() and index < len(question["options"]):
#                 option = question["options"][index]
#
#                 answers[question["id"]] = option["value"]
#
#                 if question["id"] == "structure":
#                     structure = option["value"]
#
#                     answers["use_sections"] = structure in (
#                         "sections",
#                         "sections_and_features",
#                     )
#
#                     answers["use_features"] = structure == "sections_and_features"
#
#                     if not answers["use_sections"]:
#                         answers["allow_issues_under_sections"] = False
#
#                     if not answers["use_features"]:
#                         answers["allow_issues_under_features"] = False
#
#                 if question["id"] == "section_tracking":
#                     answers["allow_issues_under_sections"] = option["value"] in (
#                         "issues",
#                         "issues_and_labels",
#                     )
#
#                 if question["id"] == "starting_point":
#                     dialog.starting_series_number.setVisible(
#                         option["value"] == "re-production"
#                     )
#
#                 if question["id"] == "feature_tracking":
#                     answers["allow_issues_under_features"] = option["value"] in (
#                         "issues",
#                         "issues_and_labels",
#                     )
#
#                 dialog.structure_status.setText(
#                     "  |  ".join(f"{key}: {value}" for key, value in answers.items())
#                 )
#
#                 dialog.structure_example.setPlainText(option["example"])
#                 dialog.structure_explain.setPlainText(option["explanation"])
#                 break
#
#     def show_question(index):
#         nonlocal question
#         question = QUESTIONS[index]
#         dialog.project_name.setVisible(question["id"] == "project_name")
#         dialog.starting_series_number.setVisible(False)
#
#         answers.pop(question["id"], None)
#
#         dialog.structure_subject.setText(question["subject"])
#         dialog.structure_subject.adjustSize()
#
#         dialog.structure_question.setPlainText(question["question"])
#
#         dialog.structure_example.clear()
#         dialog.structure_explain.clear()
#
#         for button in buttons:
#             button.setAutoExclusive(False)
#             button.setChecked(False)
#             button.setAutoExclusive(True)
#
#         for button_index, button in enumerate(buttons):
#             if button_index < len(question["options"]):
#                 button.setText(question["options"][button_index]["text"])
#                 button.show()
#             else:
#                 button.hide()
#
#     def question_applies(question_id):
#         if question_id == "starting_point":
#             return answers.get("numbering") == "automatic"
#
#         if question_id == "section_tracking":
#             return answers.get("use_sections", False)
#
#         if question_id == "feature_tracking":
#             return answers.get("use_features", False)
#
#         if question_id == "hierarchy":
#             issue_values = ("issues", "issues_and_labels")
#
#             return (
#                 answers.get("section_tracking") in issue_values
#                 or answers.get("feature_tracking") in issue_values
#             )
#
#         return True
#
#     def go_forward():
#         nonlocal current_question
#
#         if question["id"] == "starting_point":
#             if answers.get("starting_point") == "pre-production":
#                 answers["starting_series"] = 0
#             elif answers.get("starting_point") == "production":
#                 answers["starting_series"] = 1
#             elif answers.get("starting_point") == "re-production":
#                 answers["starting_series"] = dialog.starting_series_number.value()
#
#         if question["id"] == "project_name":
#             name = dialog.project_name.text().strip()
#
#             if not name:
#                 return
#
#             answers["project_name"] = name
#
#         if question["id"] not in answers:
#             return
#
#         current_question += 1
#
#         while current_question < len(QUESTIONS):
#             next_question = QUESTIONS[current_question]
#
#             if question_applies(next_question["id"]):
#                 break
#
#             current_question += 1
#
#         if current_question < len(QUESTIONS):
#             show_question(current_question)
#         else:
#             if validate_configuration():
#                 print("Configuration complete:", answers)
#                 dialog.accept()
#             else:
#                 print("Invalid configuration:", answers)
#
#     def go_back():
#         nonlocal current_question
#
#         current_question -= 1
#
#         while current_question >= 0:
#             previous_question = QUESTIONS[current_question]
#
#             if question_applies(previous_question["id"]):
#                 break
#
#             current_question -= 1
#
#         if current_question >= 0:
#             show_question(current_question)
#
#     for button in buttons:
#         button.toggled.connect(update_details)
#
#     dialog.button_forward.clicked.connect(go_forward)
#     dialog.button_back.clicked.connect(go_back)
#
#     ui_file.close()
#
#     return dialog
#
#
# # =============================================================================
# # PART C — APPLICATION STARTUP AND MAIN-WINDOW STATE
# # =============================================================================
# # Starts QApplication, handles the two developer/test command-line shortcuts,
# # creates the state variables for the currently active roadmap, and loads the
# # main_window.ui file.
# #
# # Important state owned here:
# #   active_roadmap_path      - path for an opened roadmap; None for unsaved.
# #   active_roadmap           - the actual Roadmap model currently in memory.
# #   roadmap_is_active        - whether a roadmap is currently active.
# #   selected_roadmap_object  - model object selected in the MAIN window tree.
# #   item_editor_window       - currently opened roadmap Editor window.
# #
# # NOTE:
# # The Main Window selection is not supposed to decide which object the Editor
# # initially edits. "Edit Roadmap" opens the active roadmap Editor.
# # =============================================================================
# def main():
#     """Launch the GitMap desktop application."""
#
#     app = QApplication(sys.argv)
#
#     if "--structure-dialog" in sys.argv:
#         dialog = load_structure_dialog()
#         dialog.exec()
#         return
#
#     if "--item-editor" in sys.argv:
#         editor = load_item_editor()
#         editor.exec()
#         return
#
#     active_roadmap_path = None
#     active_roadmap = None
#     sync_baseline_roadmap = None
#     roadmap_is_active = False
#     selected_roadmap_object = None
#     item_editor_window = None
#     review_window = None
#     new_roadmap_creator_window = None
#
#     ui_path = Path(__file__).with_name("main_window.ui")
#
#     ui_file = QFile(str(ui_path))
#     ui_file.open(QFile.OpenModeFlag.ReadOnly)
#
#     loader = QUiLoader()
#     window = loader.load(ui_file)
#
#     # =========================================================================
#     # PART D — MAIN WINDOW ROADMAP TREE
#     # =========================================================================
#     # Finds and configures the tree on the MAIN GitMap window.
#     #
#     # This is different from `preview_text`, which is the tree inside the
#     # Editor. Both trees are rendered by populate_roadmap_tree().
#     # =========================================================================
#     # Finds the roadmap display created in Qt Designer.
#     roadmap_tree = window.findChild(QTreeWidget, "roadmap_Tree")
#     roadmap_tree.setHeaderHidden(True)
#     roadmap_tree.setStyleSheet("""
#         QTreeWidget {
#             background-color: black;
#             color: black;
#         }
#     """)
#     roadmap_name = window.findChild(QTextEdit, "textEdit")
#     roadmap_name.setReadOnly(True)
#
#     # =========================================================================
#     # PART E — OPEN AN EXISTING ROADMAP
#     # =========================================================================
#     # open_roadmap() handles:
#     #   1. File picker
#     #   2. Markdown parsing
#     #   3. Inferring structural settings for older/existing roadmaps
#     #   4. Updating the Main Window title/tree
#     #   5. Enabling Edit Roadmap
#     #
#     # infer_roadmap_structure() is important because an existing Markdown file
#     # does not necessarily contain the answers from Part B.
#     # =========================================================================
#     # Lets the user choose an existing GitMap Markdown roadmap.
#
#     def open_roadmap():
#         nonlocal \
#             active_roadmap_path, \
#             active_roadmap, \
#             sync_baseline_roadmap, \
#             roadmap_is_active
#         roadmap_path, _ = QFileDialog.getOpenFileName(
#             window,
#             "Open Roadmap",
#             "",
#             "Markdown Roadmaps (*.md);;All Files (*.*)",
#         )
#
#         if not roadmap_path:
#             return
#
#         print(f"Selected roadmap: {roadmap_path}")
#
#         try:
#             roadmap = parse_roadmap(roadmap_path)
#             infer_roadmap_structure(roadmap)
#
#         except (OSError, UnicodeError) as error:
#             print(f"Failed to open roadmap: {roadmap_path}")
#             print(f"Error: {error}")
#             traceback.print_exc()
#
#             QMessageBox.critical(
#                 window,
#                 "Unable to Open Roadmap",
#                 f"GitMap could not open the selected roadmap.\n\n"
#                 f"File: {roadmap_path}\n\n"
#                 f"Error: {error}",
#             )
#
#             return
#
#         active_roadmap_path = roadmap_path
#         active_roadmap = roadmap
#
#         # Keep an untouched copy of the roadmap as it existed when opened.
#         # Later, Sync will be the only operation that replaces this baseline.
#         sync_baseline_roadmap = copy.deepcopy(roadmap)
#
#         roadmap_name.setText(roadmap.name)
#         print(vars(roadmap))
#
#         populate_roadmap_tree(roadmap_tree, roadmap)
#
#         roadmap_is_active = True
#         edit_roadmap_button.show()
#         review_button.show()
#         cancel_button.show()
#
#     # =========================================================================
#     # PART F — MAIN WINDOW TREE SELECTION
#     # =========================================================================
#     # Stores the model object attached to the selected MAIN-window tree row.
#     #
#     # This is intentionally small. Most editing selection behavior happens in
#     # Part H inside the Editor Preview.
#     # =========================================================================
#     def selection_changed(item, previous_item):
#         nonlocal selected_roadmap_object
#
#         model = item.data(0, MODEL_ROLE)
#         selected_roadmap_object = model
#
#         # edit_roadmap_button.setEnabled(model is not None)
#
#     roadmap_tree.currentItemChanged.connect(selection_changed)
#
#     # # =========================================================================
#     # # PART G — OPEN AND SET UP THE ROADMAP EDITOR
#     # # =========================================================================
#     # # This is currently the largest GUI-controller section in app.py.
#     # #
#     # # It:
#     # #   * loads item_editor.ui
#     # #   * attaches the active Roadmap
#     # #   * creates the Add popup
#     # #   * wires the Add button
#     # #   * finds the Editor Preview and Zoom trees
#     # #   * renders the Preview
#     # #   * defines Preview-selection behavior (Part H below)
#     # #
#     # # FUTURE REFACTOR:
#     # # Add workflow behavior now lives in add_item_controller.py. Part G keeps
#     # # only the Editor-specific wiring and Preview/Zoom lifecycle.
#     # # =========================================================================
#     # # -------------------------------------------------------------------------
#     # # PART G' — REMOVE ITEM CONTROLLER
#     # # -------------------------------------------------------------------------
#     #
#     # def open_selected_item_editor():
#     #     nonlocal item_editor_window
#     #
#     #     selected_detail = None
#     #
#     #     item_editor_window = load_item_editor()
#     #     item_editor_window.roadmap_detail = selected_detail
#     #
#     #     if selected_detail is not None:
#     #         print("EDITOR DETAIL:", selected_detail.title)
#     #
#     #     item_type = get_item_type(selected_roadmap_object)
#     #
#     #     item_editor_window.roadmap = active_roadmap
#     #
#     #     item_editor_window.add_item_dialog = load_add_item_dialog()
#     #     add_button = item_editor_window.findChild(QPushButton, "add_button")
#     #     delete_button = item_editor_window.findChild(QPushButton, "delete_button")
#     #     save_button = item_editor_window.findChild(QPushButton, "save_button")
#     #     save_exit_button = item_editor_window.findChild(QPushButton, "save_exit_button")
#     #
#     #     def set_add_draft_actions_visible(visible):
#     #         add_button.setVisible(visible)
#     #         delete_button.setVisible(visible)
#     #         save_button.setVisible(visible)
#     #         save_exit_button.setVisible(visible)
#     #
#     #     add_continue_button = item_editor_window.add_item_dialog.add_continue_button
#     #     never_mind_button = item_editor_window.findChild(
#     #         QPushButton, "never_mind_button"
#     #     )
#     #     never_mind_button.hide()
#     #     set_add_draft_actions_visible(True)
#     #
#     #     delete_button.clicked.connect(lambda: remove_selected_item(item_editor_window))
#     #
#     #     def abandon_add_draft():
#     #         never_mind_add(
#     #             item_editor_window,
#     #             never_mind_button,
#     #             set_add_draft_actions_visible,
#     #             preview_text,
#     #             context_tree,
#     #         )
#     #
#     #     never_mind_button.clicked.connect(abandon_add_draft)
#     #
#     #     def finish_current_add():
#     #         finish_add(
#     #             item_editor_window,
#     #             never_mind_button,
#     #             set_add_draft_actions_visible,
#     #         )
#     #
#     #     item_editor_window.finish_add = finish_current_add
#     #     item_editor_window.add_mode = False
#     #
#     #     def continue_current_add():
#     #         continue_add_item(
#     #             item_editor_window,
#     #             never_mind_button,
#     #             set_add_draft_actions_visible,
#     #             preview_text,
#     #             MODEL_ROLE,
#     #             get_item_type,
#     #         )
#     #
#     #     add_continue_button.clicked.connect(continue_current_add)
#     #
#     #     # ---------------------------------------------------------------------
#     #     # PART H — ENTER ADD MODE
#     #     # ---------------------------------------------------------------------
#     #     def start_current_add_mode():
#     #         start_add_mode(item_editor_window, preview_text)
#     #
#     #     add_button.clicked.connect(start_current_add_mode)
#     #
#     #     # ---------------------------------------------------------------------
#     #     # PART I — ADD POPUP
#     #     # ---------------------------------------------------------------------
#     #     # Popup behavior now lives in add_item_controller.py.
#     #
#     #     # ---------------------------------------------------------------------
#     #     # PART J — EDITOR PREVIEW AND ZOOM WIDGET SETUP
#     #     # ---------------------------------------------------------------------
#     #     # `preview_text` = full clickable roadmap tree on the LEFT of Editor.
#     #     # `context_tree` = read-only-ish "Zoom" neighborhood on bottom-right.
#     #     #
#     #     # Do not confuse `preview_text` with the Main Window `roadmap_tree`.
#     #     # ---------------------------------------------------------------------
#     #     preview_text = item_editor_window.findChild(QTreeWidget, "preview_text")
#     #     preview_text.setHeaderHidden(True)
#     #     preview_text.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
#     #
#     #     context_tree = item_editor_window.findChild(QTreeWidget, "context_tree")
#     #     context_tree.clear()
#     #
#     #     populate_roadmap_tree(preview_text, active_roadmap)
#     #
#     #     # ---------------------------------------------------------------------
#     #     # PART K — REFRESH EDITOR PREVIEW
#     #     # ---------------------------------------------------------------------
#     #     # item_editor.py calls editor.refresh_preview() after Apply changes the
#     #     # in-memory model. This callback redraws the Editor Preview from that
#     #     # model.
#     #     # ---------------------------------------------------------------------
#     #     def select_preview_model(target_model):
#     #         for item in flatten_tree(preview_text):
#     #             if item.data(0, MODEL_ROLE) is target_model:
#     #                 preview_text.setCurrentItem(item)
#     #                 return
#     #
#     #     item_editor_window.select_preview_model = select_preview_model
#     #
#     #     def refresh_editor_preview():
#     #         populate_roadmap_tree(preview_text, active_roadmap)
#     #         populate_roadmap_tree(roadmap_tree, active_roadmap)
#     #
#     #     item_editor_window.refresh_preview = refresh_editor_preview
#     #
#     #     # =====================================================================
#     #     # PART L — EDITOR PREVIEW SELECTION ROUTER
#     #     # =====================================================================
#     #     # This function is the central "what happens when I click Preview?"
#     #     # router. There are TWO modes:
#     #     #
#     #     # NORMAL MODE:
#     #     #   * highlights the selected Preview row
#     #     #   * rebuilds Zoom using nearby structural rows
#     #     #   * stores the selected model/detail on the Editor
#     #     #   * calls configure_editor() to display editable fields
#     #     #
#     #     # ADD MODE:
#     #     #   * stores the clicked row as the Add reference
#     #     #   * decides which child/sibling types are structurally legal
#     #     #   * fills the Add popup radio buttons
#     #     #   * RETURNS EARLY, so normal Zoom/editor selection code does not run
#     #     #
#     #     # That early return is especially relevant to the parked
#     #     # "Cancel Add -> Zoom stops" bug: if add_mode remains True after Cancel,
#     #     # every future Preview click keeps taking the Add branch.
#     #     #
#     #     # STRUCTURE RULES CURRENTLY USED:
#     #     #   Issue     -> Issue / Requirement / Work Step
#     #     #   Feature   -> Feature / Issue
#     #     #   Section   -> Section + optional Feature/Issue according to Roadmap
#     #     #   Milestone -> Milestone + Section, OR Issue when sections aren't used
#     #     #
#     #     # SKIPPED 0.7 DEPENDENCY TO REMEMBER:
#     #     # Structural add/move/renumber behavior must use the existing 0.7
#     #     # numbering/structure backend rather than inventing a GUI-only system.
#     #     # =====================================================================
#     #     def preview_selection_changed(current, previous):
#     #         if previous is not None:
#     #             previous.setBackground(0, QBrush())
#     #
#     #         if current is not None:
#     #             current.setBackground(0, QColor("#3A4A5A"))
#     #
#     #             model = current.data(0, MODEL_ROLE)
#     #             detail = current.data(0, DETAIL_ROLE)
#     #             detail_kind = current.data(0, DETAIL_KIND_ROLE)
#     #
#     #             if item_editor_window.add_mode:
#     #                 item_editor_window.add_reference = current
#     #                 item_editor_window.add_reference_model = model
#     #                 item_editor_window.add_reference_detail = detail
#     #                 item_editor_window.add_reference_detail_kind = detail_kind
#     #
#     #                 show_add_type_choices(
#     #                     item_editor_window,
#     #                     model,
#     #                     active_roadmap,
#     #                     get_item_type,
#     #                 )
#     #
#     #                 return
#     #
#     #             # -------------------------------------------------------------
#     #             # PART M — BUILD THE ZOOM VIEW
#     #             # -------------------------------------------------------------
#     #             # flatten_tree() returns structural Preview rows in visible
#     #             # traversal order while ignoring Description/Requirement/
#     #             # Work-Step detail rows. We then show roughly +/- 4 neighbors.
#     #             # -------------------------------------------------------------
#     #             items = flatten_tree(preview_text)
#     #
#     #             if current in items:
#     #                 current_index = items.index(current)
#     #
#     #                 context_tree.clear()
#     #
#     #                 start = max(0, current_index - 4)
#     #                 end = min(len(items), current_index + 5)
#     #
#     #                 for item in items[start:end]:
#     #                     zoom_item = QTreeWidgetItem([item.text(0)])
#     #
#     #                     if item is current:
#     #                         zoom_item.setBackground(0, QColor("#3A4A5A"))
#     #
#     #                     context_tree.addTopLevelItem(zoom_item)
#     #
#     #             # -------------------------------------------------------------
#     #             # PART N — LOAD THE SELECTED OBJECT INTO THE EDITOR
#     #             # -------------------------------------------------------------
#     #             # `model` is the parent GitMap model object.
#     #             # `detail` is an exact Requirement/WorkStep when applicable.
#     #             # `detail_kind` tells configure_editor() which detail row was
#     #             # actually clicked.
#     #             # -------------------------------------------------------------
#     #             if model is not None:
#     #                 item_editor_window.roadmap_object = model
#     #                 item_editor_window.roadmap_detail = detail
#     #
#     #                 configure_editor(
#     #                     item_editor_window,
#     #                     model,
#     #                     detail,
#     #                     detail_kind,
#     #                 )
#     #
#     #     preview_text.currentItemChanged.connect(preview_selection_changed)
#     #
#     #     item_editor_window.show()
#
#     # =========================================================================
#     # PART O — MAIN WINDOW DOUBLE-CLICK
#     # =========================================================================
#     # Legacy/convenience route that opens the Editor from a model-backed row in
#     # the Main Window tree. Root rows with no MODEL_ROLE are ignored.
#     # =========================================================================
#     def roadmap_item_double_clicked(item, column):
#         model = item.data(0, MODEL_ROLE)
#
#         if model is None:
#             return
#
#         open_selected_item_editor()
#
#     roadmap_tree.itemDoubleClicked.connect(roadmap_item_double_clicked)
#     roadmap_tree.setExpandsOnDoubleClick(False)
#
#     # =========================================================================
#     # PART P — MAIN WINDOW BUTTON WIRING
#     # =========================================================================
#     # Connects the Main Window's Open / New / Edit buttons to the controller
#     # functions in this file.
#     # =========================================================================
#     # Connects the Designer button to the roadmap file picker.
#
#     def open_review_window():
#         nonlocal review_window
#
#         review_window = load_review_dialog(
#             sync_baseline_roadmap,
#             active_roadmap,
#         )
#         review_window.show()
#
#     open_roadmap_button = window.findChild(QPushButton, "Open_Roadmap")
#
#     open_roadmap_button.clicked.connect(open_roadmap)
#
#     new_roadmap_button = window.findChild(QPushButton, "New_Roadmap")
#     edit_roadmap_button = window.findChild(QPushButton, "edit_roadmap_button")
#     # review_button = window.findChild(QPushButton, "review_button")
#     cancel_button = window.findChild(QPushButton, "cancel_button")
#
#     edit_roadmap_button.hide()
#     review_button.hide()
#     cancel_button.hide()
#
#     edit_roadmap_button.clicked.connect(open_selected_item_editor)
#     review_button.clicked.connect(open_review_window)
#
#     # def cancel_pending_changes():
#     #     nonlocal active_roadmap
#     #
#     #     print("CANCEL BUTTON CLICKED")  # TEST
#     #
#     #     restored_roadmap = cancel_changes(
#     #         window,
#     #         sync_baseline_roadmap,
#     #     )
#     #
#     #     if restored_roadmap is None:
#     #         return
#     #
#     #     active_roadmap = restored_roadmap
#     #     populate_roadmap_tree(roadmap_tree, active_roadmap)
#     #
#     # cancel_button.clicked.connect(cancel_pending_changes)
#
#     # =========================================================================
#     # PART Q — CREATE A NEW UNSAVED ROADMAP MODEL
#     # =========================================================================
#     # Runs Part B, then converts its answers into a Roadmap object in memory.
#     #
#     # Important:
#     #   * active_roadmap_path stays None because nothing has been saved yet.
#     #   * no fake root/content is created merely to make the tree look filled.
#     #   * numbering_mode / starting_series / structure flags are copied onto
#     #     the model here.
#     #   * hierarchy "labeling" maps to backend value "type_prefix".
#     #   * GitHub representation answers are normalized to issue/label/both.
#     #
#     # This is the handoff point from "questionnaire answers" to real model.
#     # =========================================================================
#     def create_new_roadmap():
#         nonlocal \
#             active_roadmap_path, \
#             active_roadmap, \
#             roadmap_is_active, \
#             new_roadmap_creator_window
#
#         structure_dialog = load_structure_dialog()
#
#         result = structure_dialog.exec()
#
#         if not result:
#             return
#
#         active_roadmap_path = None
#
#         answers = structure_dialog.answers
#
#         active_roadmap = Roadmap(
#             name=answers["project_name"],
#         )
#         active_roadmap.numbering_mode = answers["numbering"]
#         active_roadmap.starting_series = str(answers.get("starting_series", 0))
#         active_roadmap.use_sections = answers["use_sections"]
#         active_roadmap.use_features = answers["use_features"]
#         active_roadmap.allow_issues_under_sections = answers[
#             "allow_issues_under_sections"
#         ]
#         active_roadmap.allow_issues_under_features = answers[
#             "allow_issues_under_features"
#         ]
#
#         if answers.get("hierarchy") == "labeling":
#             active_roadmap.hierarchy_issue_title_style = "type_prefix"
#         else:
#             active_roadmap.hierarchy_issue_title_style = "plain"
#
#         representation_values = {
#             "issues": "issue",
#             "labeling": "label",
#             "issues_and_labels": "both",
#             "blank": None,
#         }
#         active_roadmap.github_representation = {
#             "section": representation_values.get(answers.get("section_tracking")),
#             "feature": representation_values.get(answers.get("feature_tracking")),
#         }
#         roadmap_name.setText(active_roadmap.name)
#         roadmap_is_active = True
#
#         new_roadmap_creator_window = load_new_roadmap_creator(active_roadmap)
#         new_roadmap_creator_window.show()
#
#     new_roadmap_button.clicked.connect(create_new_roadmap)
#
#     # =========================================================================
#     # PART R — SHOW MAIN WINDOW AND ENTER QT EVENT LOOP
#     # =========================================================================
#     # At this point all Main Window widgets and signals are wired.
#     # =========================================================================
#     ui_file.close()
#
#     window.show()
#
#     sys.exit(app.exec())
#
#
# # =============================================================================
# # PART S — MODULE ENTRY POINT
# # =============================================================================
# # Allows this file to be launched directly with:
# #     python app.py
# #
# # Developer shortcuts handled in Part C:
# #     python app.py --structure-dialog
# #     python app.py --item-editor
# # =============================================================================
# # ============================================================
#
# if __name__ == "__main__":
#     main()
