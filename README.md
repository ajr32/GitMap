# GitMap

GitMap turns a project roadmap into a structured GitHub project.

Instead of starting with a pile of GitHub Issues and trying to organize them afterward, GitMap starts with the plan. You build and maintain a roadmap, review changes locally, and then synchronize that roadmap with GitHub.

GitMap can represent a project with:

- **Milestones**
- **Sections**
- **Features**
- **Issues**
- **Requirements**
- **Work Steps**

Depending on the roadmap configuration, Sections and Features can also be represented on GitHub with Issues, Labels, both, or neither.

> GitMap is currently under active development. The desktop application is the primary user workflow.

---

## The Roadmap-First Workflow

GitMap treats the roadmap as the place where you design and organize the project.

A typical workflow is:

1. **Create or open a roadmap.**
2. **Edit the roadmap locally.**
3. **Review the changes.**
4. **Save the roadmap as Markdown.**
5. **Connect GitMap to a GitHub repository.**
6. **Synchronize the roadmap with GitHub.**
7. Continue editing the roadmap and synchronize again as the project changes.

This lets you work on project structure before making changes to GitHub.

GitMap also assigns permanent internal identities to roadmap items. That allows an item to keep its GitHub identity even when automatic numbering changes because the roadmap was reorganized.

---

## Roadmap Structure

Every GitMap roadmap contains Milestones. When creating a roadmap, GitMap currently supports three structural layouts:

```text
Roadmap
└── Milestone
    └── Issue
```

```text
Roadmap
└── Milestone
    └── Section
        └── Issue
```

or:

```text
Roadmap
└── Milestone
    └── Section
        ├── Issue
        └── Feature
            └── Issue
```

The exact Issue placement depends on the options selected when the roadmap is created.

GitMap currently uses **automatic numbering**. You choose the starting series during roadmap creation, and GitMap maintains numbering as items are added, removed, or moved.

---

## Installation

### Requirements

GitMap requires:

- **Python 3.11 or newer**
- Git
- A GitHub account if you want to use GitHub synchronization

Clone the repository:

```bash
git clone https://github.com/ajr32/GitMap.git
cd GitMap
```

Create a virtual environment:

### Windows

```powershell
py -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install GitMap in editable mode:

```bash
python -m pip install -e .
```

### Desktop dependencies

The current desktop application uses **PySide6**, and GitHub credentials use **keyring**. If these are not yet included by the package metadata in the version you are running, install them in the same environment:

```bash
python -m pip install PySide6 keyring
```

---

## Starting GitMap

The desktop application is currently started through the GUI application module in the source tree.

From the project root, run the module that contains `gitmap/gui/application/main.py` using your Python environment or your IDE.

For example, in PyCharm you can run:

```text
gitmap/gui/application/main.py
```

The package metadata also defines a `gitmap` command-line entry point. The command-line interface is still part of the project, but this README documents the current **desktop roadmap-first workflow**. CLI subcommands should be treated as development/legacy functionality until they are separately documented and verified for the release.

---

## GitHub Setup

Before synchronizing, open **Settings** in GitMap.

Enter:

- your GitHub username
- a GitHub Personal Access Token

GitMap can open GitHub's Personal Access Token creation page from the Settings window. Use **Test Connection** to verify the account before saving the settings.

GitMap stores the GitHub username in:

```text
~/.gitmap/settings.json
```

The Personal Access Token is stored separately using your operating system's credential/keyring storage rather than being written into that JSON file.

When synchronizing a roadmap, GitMap can either:

- connect to an **existing repository**, or
- **create a new repository** for the roadmap.

The detailed token permissions and GitHub setup process are documented separately in the GitHub Setup Guide.

---

## Basic GitMap Actions

The main desktop workflow uses these actions:

| Action | What it does |
| --- | --- |
| **New Roadmap** | Starts the guided roadmap-creation process. |
| **Open Roadmap** | Opens an existing GitMap Markdown roadmap. |
| **Edit Roadmap** | Opens the roadmap editor. |
| **Add** | Adds a structurally valid roadmap item. |
| **Edit** | Changes the selected item's content. |
| **Move** | Moves an item to a valid location and maintains numbering. |
| **Delete** | Removes an item after confirmation. |
| **Apply** | Applies the current edit to the in-memory roadmap. |
| **Never Mind** | Abandons the current editor action. |
| **Save** | Writes the active roadmap to its Markdown file. |
| **Save As** | Saves the roadmap to a different Markdown file. |
| **Review Changes** | Compares the current roadmap with its baseline. |
| **Cancel Changes** | Restores the roadmap to its baseline after confirmation. |
| **Sync to GitHub** | Prepares and performs GitHub synchronization. |

### Apply is not Save

This distinction is important.

**Apply** changes the roadmap currently loaded in GitMap. It does **not** write the Markdown file to disk.

Use **Save** or **Save As** to make those changes persistent.

---

## Creating Your First Roadmap

Here is a simple first-use walkthrough.

### 1. Start a new roadmap

Open GitMap and click **New Roadmap**.

The creation wizard asks how the roadmap should be organized. For a simple first project, choose:

- **Automatic numbering**
- **Sections only**
- a Section tracking option appropriate for your project
- a starting series, such as **0 - Pre-production**
- a project name, such as **My First Project**

GitMap then asks for the first Milestone.

Enter:

```text
First Release
```

GitMap automatically assigns its number.

### 2. Add a Section

In the Editor, select the first Milestone and choose **Add**.

Choose **Section** and create:

```text
Core Application
```

### 3. Add an Issue

Select the Section and choose **Add** again.

If your selected roadmap configuration permits Issues directly under Sections, choose **Issue** and enter something like:

```text
Create the main window
```

An Issue can also contain a description, Requirements, and Work Steps.

For example:

```text
Issue: Create the main window

Requirement:
The user can open an existing roadmap.

Work Step:
Add the Open Roadmap button.
```

### 4. Save the roadmap

Click **Save**.

Because this is a new roadmap, GitMap asks where to save the Markdown file. After the first save, future saves use that active file unless you choose **Save As**.

### 5. Review your work

Use **Review Changes** to inspect the roadmap before synchronizing it.

The Review window can identify changes such as:

- added items
- removed items
- renumbered items
- retitled items
- hierarchy changes
- unchanged items

### 6. Configure GitHub

Open **Settings**, enter your GitHub username and Personal Access Token, and use **Test Connection**.

### 7. Synchronize

Choose **Sync to GitHub**.

Enter a repository name and choose whether GitMap should connect to an existing repository or create a new one.

GitMap prepares the synchronization before modifying GitHub. If synchronization would close GitHub Issues that were removed from the roadmap, GitMap asks for confirmation before continuing.

During synchronization, GitMap reports progress through stages including repository setup, inspection, planning, Milestones, Labels, Issues, hierarchy, and parent/child relationships.

At the end, GitMap displays a result log showing operations such as:

- created
- updated
- closed
- skipped
- failed

Synchronization logs are also saved under the roadmap's `.gitmap/sync_logs` directory.

---

## Editing an Existing Roadmap

Use **Open Roadmap** to load an existing GitMap Markdown file.

GitMap reconstructs the roadmap hierarchy and its saved GitHub representation settings. Older roadmaps without all current metadata use compatibility inference where possible.

From there you can add, edit, move, and remove roadmap items using the same Editor.

When an operation causes automatic renumbering, GitMap can show the proposed numbering changes before applying them.

Permanent GitMap identities are designed to remain attached to the same roadmap items even when their visible numbers change.

---

## Reviewing and Cancelling Changes

**Review Changes** compares the working roadmap with its baseline and can show added, removed, renumbered, retitled, hierarchy-changed, and unchanged items.

If you decide you do not want the current set of changes, **Cancel Changes** can restore the baseline roadmap after confirmation.

Saving and synchronization are separate operations: saving writes the roadmap Markdown file; synchronization applies the planned roadmap state to GitHub.

---

## GitHub Synchronization

GitMap's synchronization process is deliberately staged.

Before the mutation phase, GitMap:

1. creates or verifies the repository,
2. inspects existing GitMap-managed GitHub Issues,
3. builds a synchronization plan,
4. validates the plan,
5. identifies removals that require confirmation.

The synchronization phase then handles Milestones, Labels, removed Issues, normal Issues, hierarchy Issues, and parent/sub-issue relationships.

GitMap keeps a structured synchronization result log so you can see what was created, updated, closed, skipped, or failed.

---

## Errors and Diagnostic Logs

GitMap presents normal application failures as graphical messages instead of requiring the development console.

For troubleshooting, GitMap also maintains an append-only diagnostic log at:

```text
.gitmap/logs/errors.log
```

Unexpected errors recorded there can include the timestamp, operation context, diagnostic information, and Python traceback.

This diagnostic log is separate from the per-roadmap synchronization logs.

---

## Roadmap Markdown

GitMap roadmaps are saved as Markdown files. The Markdown contains both the human-readable roadmap and GitMap metadata used to preserve identity and synchronization behavior.

You can therefore read the roadmap outside GitMap, commit it to source control, and review its changes as text.

For the exact Markdown syntax, hierarchy rules, metadata, Requirements, Work Steps, and complete hand-written examples, see the **Roadmap Format Guide**.

---

## Development

Install development dependencies with:

```bash
python -m pip install -e ".[dev]"
```

The current development extras include:

- `pytest`
- `ruff`

---

## Current Status

GitMap is approaching its first stable release. Some release preparation, automated testing, documentation, and desktop polish are still in progress.

The README intentionally documents the behavior of the current desktop application rather than older experimental workflows.
