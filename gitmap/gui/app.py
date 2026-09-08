import tkinter as tk

from gitmap.roadmap_creation import start_new_roadmap
from tkinter import filedialog

# ============================================================
# APPLICATION STATUS
# Creates the bottom status bar used for messages and feedback.
# ============================================================

def create_status_bar(root):
    """Create the application status area."""

    # --- Status Label ---
    # Displays the current application status at the bottom.
    status_label = tk.Label(
        root,
        text="Ready",
        anchor="w",
        relief="sunken",
        borderwidth=1,
    )

    # --- Status Bar Layout ---
    # Stretches the status bar across the bottom of the window.
    status_label.pack(
        side="bottom",
        fill="x",
    )

    # --- Status Bar Result ---
    # Returns the label so other GUI areas can change its text.
    return status_label


# ============================================================
# ROADMAP NAVIGATION
# Creates the left workspace used to browse roadmap items.
# ============================================================

def create_navigation_area(root):
    """Create the roadmap navigation area."""

    # --- Navigation Panel ---
    # Creates the fixed-width panel on the left side.
    navigation_frame = tk.Frame(
        root,
        width=250,
        relief="sunken",
        borderwidth=1,
    )

    # --- Navigation Panel Layout ---
    # Places the navigation panel along the left side.
    navigation_frame.pack(
        side="left",
        fill="y",
    )

    # --- Preserve Navigation Width ---
    # Prevents child widgets from changing the panel width.
    navigation_frame.pack_propagate(False)

    # --- Open Roadmap Button ---
    # Opens a roadmap and later displays the loaded roadmap's name.
    roadmap_button = tk.Button(
        navigation_frame,
        text="Open Roadmap",
    )

    # --- Countries Roadmap Button Layout ---
    # Places the roadmap button at the top of navigation.
    roadmap_button.pack(
        padx=10,
        pady=10,
        fill="x",
    )

    # --- Roadmap List Container ---
    # Groups the roadmap list and scrollbar together.
    list_frame = tk.Frame(
        navigation_frame,
    )

    # --- Roadmap List Container Layout ---
    # Allows the list container to use the remaining panel space.
    list_frame.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=5,
    )

    # --- Roadmap List ---
    # Displays roadmap items that the user can select.
    roadmap_list = tk.Listbox(
        list_frame,
    )

    # --- Roadmap Scrollbar ---
    # Allows large roadmaps to be scrolled vertically.
    roadmap_scrollbar = tk.Scrollbar(
        list_frame,
        command=roadmap_list.yview,
    )

    # --- Connect List and Scrollbar ---
    # Keeps the scrollbar synchronized with the roadmap list.
    roadmap_list.config(
        yscrollcommand=roadmap_scrollbar.set,
    )

    # --- Scrollbar Layout ---
    # Places the scrollbar on the right edge of the list.
    roadmap_scrollbar.pack(
        side="right",
        fill="y",
    )

    # --- Roadmap List Layout ---
    # Allows the roadmap list to fill all remaining space.
    roadmap_list.pack(
        side="left",
        fill="both",
        expand=True,
    )

    # --- Navigation Result ---
    # Returns the roadmap button and list so other GUI code
    # can control the opened roadmap and its contents.
    return roadmap_button, roadmap_list


# ============================================================
# ITEM EDITOR
# Creates the center workspace used to edit roadmap items.
# ============================================================

def create_editor_area(root):
    """Create the roadmap item editor area."""

    # --- Editor Panel ---
    # Creates the main center portion of the workspace.
    editor_frame = tk.Frame(
        root,
        relief="sunken",
        borderwidth=1,
    )

    # --- Editor Panel Layout ---
    # Allows the editor to consume available workspace space.
    editor_frame.pack(
        side="left",
        fill="both",
        expand=True,
    )

    # --- Editor Heading ---
    # Identifies the item editor workspace.
    editor_label = tk.Label(
        editor_frame,
        text="Item Editor",
    )

    # --- Editor Heading Layout ---
    # Places the editor heading near the top.
    editor_label.pack(
        padx=10,
        pady=10,
    )

    # --- Editor Result ---
    # Returns the label so selection changes can update it.
    return editor_label


# ============================================================
# LIVE PREVIEW
# Creates the right workspace used to preview roadmap changes.
# ============================================================

def create_preview_area(root):
    """Create the live roadmap preview area."""

    # --- Preview Panel ---
    # Creates the fixed-width panel on the right side.
    preview_frame = tk.Frame(
        root,
        width=300,
        relief="sunken",
        borderwidth=1,
    )

    # --- Preview Panel Layout ---
    # Places the preview along the right side of the workspace.
    preview_frame.pack(
        side="right",
        fill="y",
    )

    # --- Preserve Preview Width ---
    # Prevents child widgets from changing the panel width.
    preview_frame.pack_propagate(False)

    # --- Preview Heading ---
    # Identifies the live preview workspace.
    preview_label = tk.Label(
        preview_frame,
        text="Live Preview",
    )

    # --- Preview Heading Layout ---
    # Places the heading at the top of the preview panel.
    preview_label.pack(
        padx=10,
        pady=10,
    )

    # --- Preview Result ---
    # Returns the label so selection changes can update it.
    return preview_label


# ============================================================
# COUNTRIES ROADMAP
# Temporary entry point for opening the Countries roadmap
# while the real roadmap-opening system is being built.
# ============================================================

def configure_roadmap_opener(
    root,
    roadmap_button,
    roadmap_list,
    editor_label,
    preview_label,
    status_label,
):
    """Create the temporary Countries roadmap button."""

    # --- Open Countries Roadmap ---
    # Opens the Countries roadmap when its button is clicked.
    def open_countries_roadmap():

        # --- Choose Countries Roadmap ---
        # Opens a file picker so the Countries roadmap.md can be selected.
        roadmap_path = filedialog.askopenfilename(
            title="Open Countries Roadmap",
            filetypes=[
                ("Markdown Roadmaps", "*.md"),
                ("All Files", "*.*"),
            ],
        )

        # --- Cancel Open ---
        # Stops if no roadmap file was selected.
        if not roadmap_path:
            return

        # --- Update Roadmap Button ---
        # Changes the Open Roadmap button to the opened roadmap's name.
        roadmap_button.config(text="Countries")

        # --- Update Editor ---
        # Shows which roadmap is currently open.
        editor_label.config(
            text="Item Editor — Countries"
        )

        # --- Update Preview ---
        # Shows which roadmap is currently being previewed.
        preview_label.config(
            text="Live Preview — Countries"
        )

        # --- Update Status ---
        # Shows the path of the roadmap that was opened.
        status_label.config(
            text=f"Opened: {roadmap_path}"
        )

    # --- Connect Open Roadmap Button ---
    # Connects the navigation button to the roadmap file picker.
    roadmap_button.config(
        command=open_countries_roadmap,
    )


# ============================================================
# APPLICATION SHUTDOWN
# Handles closing the GitMap graphical application.
# ============================================================

def close_app(root):
    """Close the GitMap GUI cleanly."""

    # --- Destroy Main Window ---
    # Ends the Tkinter application and closes the window.
    root.destroy()


# ============================================================
# MAIN APPLICATION
# Creates the GitMap window and assembles the GUI workspace.
# ============================================================

def main():
    """Launch the GitMap graphical application."""

    # --- Main Window ---
    # Creates the root Tkinter application window.
    root = tk.Tk()

    # --- Application Identity ---
    # Sets the name displayed in the window title bar.
    root.title("GitMap")

    # --- Initial Window Size ---
    # Starts GitMap maximized on Windows.
    root.state("zoomed")

    # --- Status Area ---
    # Creates the status bar before the main workspace.
    status_label = create_status_bar(root)

    # --- Navigation Area ---
    # Creates the roadmap opener and browser on the left.
    roadmap_button, roadmap_list = create_navigation_area(root)

    # --- Editor Area ---
    # Creates the selected-item editor in the center.
    editor_label = create_editor_area(root)

    # --- Preview Area ---
    # Creates the live roadmap preview on the right.
    preview_label = create_preview_area(root)

    # --- Countries Roadmap ---
    # Adds the temporary Countries roadmap opener.
    configure_roadmap_opener(
        root,
        roadmap_button,
        roadmap_list,
        editor_label,
        preview_label,
        status_label,
    )

    # --- Window Close Handler ---
    # Routes the window X button through GitMap's shutdown function.
    root.protocol(
        "WM_DELETE_WINDOW",
        lambda: close_app(root),
    )

    # --- Application Event Loop ---
    # Keeps the GUI running and responding to user interaction.
    root.mainloop()


# ============================================================
# MODULE ENTRY POINT
# Allows this file to launch directly when executed.
# ============================================================

if __name__ == "__main__":

    # --- Launch GitMap ---
    # Starts the graphical application.
    main()