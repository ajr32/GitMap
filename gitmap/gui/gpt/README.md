# GitMap GPT Planning Wizard — Skeleton

This is a **standalone prototype**, not yet wired into GitMap's main window.

## Run

1. Install `PySide6` in your PyCharm interpreter (`pip install PySide6`).
2. Open this folder as a project, or add the files to your existing GitMap project.
3. Run `gpt_planning_controller.py`.
4. Complete the three pages, then select **Copy & Open ChatGPT**.
5. Paste the copied planning order into ChatGPT.

## Notes

- Edit `gpt_planning_dialog.ui` in Qt Designer.
- `planning_order.py` and `planning_prompt_builder.py` have no Qt dependency.
- The prototype reads the existing roadmap file only when you choose **Existing roadmap**. That file's entire contents are included in the copied prompt; consider privacy and message-length limits before sending it to ChatGPT.
- No API key, paid service, or automatic transfer to ChatGPT is required.
- The **Save Order** button saves settings as JSON, not a roadmap.
- Future GitMap integration should reuse its existing parser, validator, ID assignment, and sync workflows. This prototype deliberately does not implement them.
- The generated prompt references the maintained roadmap format specification; attach that specification and validated examples to ChatGPT once #232/#233 are finalized.


## Updated naming workflow

Project name is now requested on the final page, after the description and planning preferences. The **Let GPT suggest a name** checkbox defaults to on. Disable it to enter a name. No project name is required before brainstorming.

## Autonomy guide

Page 2 now shows explanations for all ten autonomy levels, highlighting the selected level with an arrow as the slider moves. This describes how GPT should plan; it does not authorize automatic GitHub changes.
