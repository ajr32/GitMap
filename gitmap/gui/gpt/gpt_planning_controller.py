"""Standalone PySide6 wizard; can later be launched by GitMap's main window."""
from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtGui import QGuiApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox

from .planning_order import PlanningOrder
from .planning_prompt_builder import build_prompt
from .chatgpt_launcher import open_chatgpt


class GPTPlanningController:
    def __init__(self):
        ui_path = Path(__file__).with_name("gpt_planning_dialog.ui")
        ui_file = QFile(str(ui_path))
        if not ui_file.open(QFile.ReadOnly):
            raise RuntimeError(f"Cannot open {ui_path}")
        try:
            self.dialog = QUiLoader().load(ui_file)
        finally:
            ui_file.close()
        if self.dialog is None:
            raise RuntimeError("Unable to load planning dialog")

        self.pages = self._get("pages")
        self._get("back_button").clicked.connect(self.back)
        self._get("next_button").clicked.connect(self.next)
        self._get("close_button").clicked.connect(self.dialog.reject)
        self._get("autonomy_slider").valueChanged.connect(self.update_autonomy_guide)
        self.update_autonomy_guide(self._get("autonomy_slider").value())
        self._get("copy_button").clicked.connect(self.copy_prompt)
        self._get("suggest_name_checkbox").toggled.connect(self.update_name_visibility)
        self._get("project_name_edit").textChanged.connect(self.refresh_preview)
        self.update_name_visibility()
        self._get("launch_button").clicked.connect(self.launch)
        self._get("save_order_button").clicked.connect(self.save_order)
        self._get("operation_combo").currentIndexChanged.connect(self.update_roadmap_visibility)
        self.update_roadmap_visibility()
        self.update_page()

    def _get(self, name):
        widget = self.dialog.findChild(__import__("PySide6.QtWidgets", fromlist=["QWidget"]).QWidget, name)
        if widget is None:
            raise RuntimeError(f"Missing UI widget: {name}")
        return widget

    def update_autonomy_guide(self, level):
        descriptions = [
            "You make every decision; GPT organizes your instructions.",
            "GPT suggests options, but asks before choosing any.",
            "GPT drafts small pieces and checks with you frequently.",
            "GPT proposes a plan, then asks you to approve each stage.",
            "GPT shares decisions with you and checks major choices.",
            "GPT handles routine choices; you approve the overall direction.",
            "GPT builds most of the roadmap and checks key assumptions.",
            "GPT plans independently, asking only about significant uncertainties.",
            "GPT makes nearly all planning decisions and presents a complete draft for review.",
            "GPT takes the lead from concept to detailed roadmap; you review before GitMap imports anything.",
        ]
        self._get("autonomy_label").setText(f"GPT autonomy: {level} / 10")
        lines = [
            f"{'▶' if i == level else ' '} {i:>2}. {description}"
            for i, description in enumerate(descriptions, 1)
        ]
        guide = self._get("autonomy_guide")
        guide.setPlainText("\n".join(lines))
        # Keep the selected level visible when the text box needs scrolling.
        cursor = guide.textCursor()
        cursor.movePosition(cursor.MoveOperation.Start)
        for _ in range(level - 1):
            cursor.movePosition(cursor.MoveOperation.Down)
        guide.setTextCursor(cursor)
        guide.ensureCursorVisible()

    def update_name_visibility(self, *_):
        suggest = self._get("suggest_name_checkbox").isChecked()
        self._get("project_name_edit").setEnabled(not suggest)
        self.refresh_preview()

    def refresh_preview(self, *_):
        if self.pages.currentIndex() == 2:
            try:
                self._get("prompt_preview").setPlainText(self.get_prompt())
            except (OSError, UnicodeError, ValueError) as error:
                self._get("prompt_preview").setPlainText(str(error))

    def update_roadmap_visibility(self, *_):
        show = self._get("operation_combo").currentIndex() == 1
        self._get("roadmap_label").setVisible(show)
        self._get("roadmap_path_edit").setVisible(show)

    def get_order(self):
        return PlanningOrder(
            project_name=("" if self._get("suggest_name_checkbox").isChecked() else self._get("project_name_edit").text().strip()),
            suggest_name=self._get("suggest_name_checkbox").isChecked(),
            project_description=self._get("description_edit").toPlainText().strip(),
            operation="existing" if self._get("operation_combo").currentIndex() else "new",
            autonomy=self._get("autonomy_slider").value(),
            hierarchy=["recommend", "simple", "full"][self._get("hierarchy_combo").currentIndex()],
            detail=["outline", "detailed", "comprehensive"][self._get("detail_combo").currentIndex()],
            questions=["important", "discuss", "none"][self._get("questions_combo").currentIndex()],
            existing_roadmap_path=self._get("roadmap_path_edit").text().strip(),
        )

    def get_prompt(self):
        order = self.get_order()
        content = ""
        if order.operation == "existing":
            if not order.existing_roadmap_path:
                raise ValueError("Select an existing roadmap file before continuing.")
            path = Path(order.existing_roadmap_path)
            if not path.is_file():
                raise ValueError(f"Roadmap file not found: {path}")
            content = path.read_text(encoding="utf-8")
        return build_prompt(order, content)

    def update_page(self):
        page = self.pages.currentIndex()
        self._get("step_label").setText([
            "Step 1 of 3 — The Big Idea",
            "Step 2 of 3 — Planning Preferences",
            "Step 3 of 3 — Name, Review & Launch",
        ][page])
        self._get("back_button").setEnabled(page > 0)
        self._get("next_button").setVisible(page < 2)
        if page == 2:
            self._get("prompt_preview").setPlainText(self.get_prompt())

    def next(self):
        if self.pages.currentIndex() == 0 and not self.get_order().project_description:
            QMessageBox.information(self.dialog, "Project description", "Please describe your project before continuing.")
            return
        try:
            self.pages.setCurrentIndex(min(2, self.pages.currentIndex() + 1))
            self.update_page()
        except (OSError, UnicodeError, ValueError) as error:
            self.pages.setCurrentIndex(0)
            QMessageBox.warning(self.dialog, "Planning order", str(error))
            self.update_page()

    def back(self):
        self.pages.setCurrentIndex(max(0, self.pages.currentIndex() - 1))
        self.update_page()

    def copy_prompt(self):
        QGuiApplication.clipboard().setText(self.get_prompt())
        QMessageBox.information(self.dialog, "Copied", "Planning order copied to the clipboard.")

    def launch(self):
        QGuiApplication.clipboard().setText(self.get_prompt())
        if not open_chatgpt():
            QMessageBox.warning(self.dialog, "Browser", "Could not open the browser. Visit https://chatgpt.com/ manually. Your order is already copied.")
        else:
            QMessageBox.information(self.dialog, "ChatGPT", "Your planning order is copied. Paste it into the new ChatGPT conversation.")

    def save_order(self):
        path, _ = QFileDialog.getSaveFileName(self.dialog, "Save Planning Order", "planning_order.json", "JSON (*.json)")
        if path:
            try:
                self.get_order().save(path)
            except OSError as error:
                QMessageBox.warning(self.dialog, "Save failed", str(error))

    def run(self):
        return self.dialog.exec()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    controller = GPTPlanningController()
    sys.exit(controller.run())
