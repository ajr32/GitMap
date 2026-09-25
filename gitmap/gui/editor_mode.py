def clear_editor_fields(editor):
    editor.item_title.clear()
    editor.item_number.clear()
    editor.item_description.clear()
    editor.item_require.clear()
    editor.item_work_step.clear()

    editor.roadmap_object = None
    editor.roadmap_detail = None


def set_editor_mode(editor, mode):
    normal_buttons = [
        editor.edit_button,
        editor.delete_button,
        editor.add_button,
        editor.add_milestone,
        editor.save_button,
        editor.save_exit_button,
    ]

    action_buttons = [
        editor.apply_button,
        editor.never_mind_button,
    ]

    if mode == "normal":
        for button in normal_buttons:
            button.show()

        for button in action_buttons:
	        button.hide()

        clear_editor_fields(editor)

    elif mode in ("edit", "add"):
        for button in normal_buttons:
            button.hide()

        for button in action_buttons:
            button.show()

    else:
        raise ValueError(f"Unknown editor mode: {mode}")