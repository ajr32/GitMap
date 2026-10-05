# GitMap Roadmap Format Guide

This guide explains the Markdown format GitMap reads and writes for project roadmaps.

GitMap roadmaps are ordinary `.md` files, but GitMap gives specific meanings to heading levels, numbering, Requirements, Work Steps, and hidden metadata. You can create and edit roadmaps through the GitMap desktop application, or edit the Markdown manually when you follow this format.

> **Important:** GitMap currently uses automatic numbering in the desktop workflow. When manually editing an existing roadmap, preserve the numbering pattern and GitMap metadata already written by GitMap. Permanent `GitMap-ID` comments identify roadmap items independently of their visible numbers and should not be casually changed or reassigned.

---

## 1. Roadmap Header

A GitMap roadmap begins with roadmap-level metadata.

A typical header looks like this:

```markdown
Title: My Project

Numbering-Mode: automatic

Starting-Series: 0

<!-- GitMap-Section-Representation: issue -->
<!-- GitMap-Feature-Representation: issue -->

Sub-Title: A short description of the project.

Hierarchy-Issue-Title-Style: plain
```

### Title

`Title:` names the roadmap.

```markdown
Title: My Project
```

A valid GitMap roadmap needs a title and at least one Milestone.

### Numbering Mode

GitMap may store the numbering mode in the file:

```markdown
Numbering-Mode: automatic
```

The current desktop workflow uses automatic numbering.

### Starting Series

The starting series records the top-level numbering series selected when the roadmap was created.

```markdown
Starting-Series: 0
```

### Sub-Title

`Sub-Title:` stores the roadmap overview.

```markdown
Sub-Title: Build the first public version of the application.
```

### GitHub Representation Metadata

GitMap can store how Sections and Features should be represented on GitHub:

```markdown
<!-- GitMap-Section-Representation: issue -->
<!-- GitMap-Feature-Representation: issue -->
```

These are GitMap metadata comments. Because they are HTML comments, they remain hidden in normal rendered Markdown.

The desktop application manages these values. When manually editing a roadmap, it is safest to preserve them rather than recreate them.

### Hierarchy Issue Title Style

A roadmap may also contain:

```markdown
Hierarchy-Issue-Title-Style: plain
```

This controls how hierarchy Issues are titled when Sections or Features are represented as GitHub Issues. This is normally managed by GitMap.

---

# 2. Milestones

A **Milestone** is the highest structural level inside a GitMap roadmap.

Milestones use a level-one Markdown heading:

```markdown
# 0 First Release
```

The format is:

```text
# NUMBER TITLE
```

For example:

```markdown
# 0 Planning
# 1 First Release
# 2 Future Development
```

A Milestone can contain:

- Issues directly beneath the Milestone
- Sections
- or both, depending on the roadmap structure

On GitHub, GitMap maps roadmap Milestones to GitHub Milestones.

---

# 3. Sections

A **Section** groups related project work inside a Milestone.

Sections use a level-two Markdown heading:

```markdown
## 0.1 User Interface
```

The format is:

```text
## NUMBER TITLE
```

A Section belongs to the most recent Milestone above it.

For example:

```markdown
# 0 First Release

## 0.1 User Interface

## 0.2 GitHub Integration
```

A Section can contain Features and/or Issues, depending on the roadmap's configured structure.

Sections can also have descriptions:

```markdown
## 0.1 User Interface

Build the desktop interface used to create and edit roadmaps.
```

GitMap can represent Sections on GitHub according to the roadmap's GitHub representation settings.

---

# 4. Features

A **Feature** is an optional structural level below a Section.

Features use a level-three Markdown heading:

```markdown
### 0.1.1 Roadmap Editor
```

The format is:

```text
### NUMBER TITLE
```

A Feature belongs to the most recent Section above it.

For example:

```markdown
# 0 First Release

## 0.1 User Interface

### 0.1.1 Roadmap Editor

### 0.1.2 Review Changes
```

Features can contain Issues and can also have descriptions:

```markdown
### 0.1.1 Roadmap Editor

Allow users to modify roadmap structure graphically.
```

Features are optional. A roadmap can use Sections without Features.

---

# 5. Issues

An **Issue** represents a concrete piece of project work.

Issues use a level-four Markdown heading:

```markdown
#### 0.1.1.1 Add Item Dialog
```

The format is:

```text
#### NUMBER TITLE
```

An Issue can appear directly beneath:

- a Milestone,
- a Section, or
- a Feature.

Its parent is determined by the current roadmap hierarchy.

### Issue under a Milestone

```markdown
# 0 First Release

#### 0.1 Prepare release notes
```

### Issue under a Section

```markdown
# 0 First Release

## 0.1 Documentation

#### 0.1.1 Complete README
```

### Issue under a Feature

```markdown
# 0 First Release

## 0.1 User Interface

### 0.1.1 Roadmap Editor

#### 0.1.1.1 Add Item Dialog
```

GitMap synchronizes normal roadmap Issues to GitHub Issues.

---

# 6. Descriptions

Sections, Features, and Issues can contain descriptive text.

For an Issue, place the description after the Issue heading and its GitMap ID, if present:

```markdown
#### 0.1.1 Complete README

<!-- GitMap-ID: abcdefgh -->

Create the main user-facing GitMap documentation.
```

Descriptions may contain more than one non-empty line:

```markdown
#### 0.1.1 Complete README

Create the main user-facing GitMap documentation.
Keep the README focused on normal users rather than internal architecture.
```

GitMap treats ordinary text following the current Section, Feature, or Issue as that item's description until another recognized structural element begins.

---

# 7. Requirements

Requirements describe what must be true for an Issue to be considered complete.

Use the exact heading:

```markdown
**Requirements:**
```

Then add each Requirement as a Markdown bullet:

```markdown
#### 0.1.1 Complete README

Create the main user-facing GitMap documentation.

**Requirements:**

- Explain what GitMap does
- Explain installation
- Provide a first-use example
```

GitMap also recognizes the older heading:

```markdown
**End Goal:**
```

However, GitMap's current serializer writes `**Requirements:**`, so that is the preferred format for new roadmaps.

Requirements belong to the current Issue.

---

# 8. Work Steps

A **Work Step** breaks an Issue into smaller actionable tasks.

GitMap writes Work Steps as Markdown task-list items under the exact heading:

```markdown
**Work Steps:**
```

A serialized Work Step has three pieces after the checkbox:

```text
NUMBER MARKER TITLE
```

For example:

```markdown
**Work Steps:**

- [ ] 0.1.1.1.1 (a) Create the README file
- [ ] 0.1.1.1.2 (b) Write the installation section
- [ ] 0.1.1.1.3 (c) Add the first-use example
```

GitMap's parser accepts unchecked and checked checkbox forms such as `[ ]`, `[x]`, and `[X]`.

GitMap can also represent nested Work Steps. When GitMap writes them, nested steps are indented beneath their parent.

Example:

```markdown
**Work Steps:**

- [ ] 0.1.1.1.1 (a) Document installation
  - [ ] 0.1.1.1.1.1 (i) Document Python requirements
  - [ ] 0.1.1.1.1.2 (ii) Document dependencies
```

Work Steps are part of their parent GitHub Issue rather than separate top-level roadmap Issues.

---

# 9. Sub-Issues and Hierarchy

GitMap uses the roadmap hierarchy to create parent/child relationships on GitHub when hierarchy levels are represented as Issues.

Conceptually:

```text
Milestone
└── Section
    ├── Issue
    └── Feature
        └── Issue
```

When Sections and Features are represented as GitHub Issues, GitMap can create relationships such as:

```text
Section Issue
├── Section-level Issue
└── Feature Issue
    └── Feature-level Issue
```

A normal Issue directly beneath a Section therefore becomes a child of that Section's hierarchy Issue. An Issue beneath a Feature becomes a child of the Feature hierarchy Issue.

You do **not** write a special `parent:` or `sub-issue:` line in the Markdown. The relationship comes from where the heading appears in the roadmap.

---

# 10. Permanent GitMap IDs

GitMap uses hidden comments to give Sections, Features, and Issues permanent identities:

```markdown
<!-- GitMap-ID: abcdefgh -->
```

Example:

```markdown
## 0.1 User Interface
<!-- GitMap-ID: abcdefgh -->

### 0.1.1 Roadmap Editor
<!-- GitMap-ID: bcdefghi -->

#### 0.1.1.1 Add Item Dialog
<!-- GitMap-ID: cdefghij -->
```

The visible number can change when GitMap renumbers a roadmap. The GitMap ID is what allows GitMap to recognize that the item itself is still the same item.

### When manually editing

Treat GitMap IDs as internal identifiers:

- Preserve an existing item's ID.
- Do not copy one item's ID onto another item.
- Do not deliberately create duplicate IDs.
- Do not change an ID just because an item's number or title changes.

When possible, let GitMap create and maintain IDs for you.

Milestones do not currently use a serialized `GitMap-ID` comment.

---

# 11. Heading Reference

The structural Markdown levels are:

| Markdown | GitMap object | Example |
| --- | --- | --- |
| `#` | Milestone | `# 0 First Release` |
| `##` | Section | `## 0.1 User Interface` |
| `###` | Feature | `### 0.1.1 Roadmap Editor` |
| `####` | Issue | `#### 0.1.1.1 Add Item Dialog` |

The hierarchy is determined by these heading levels, not by indentation.

---

# 12. Complete Example — Sections and Features

The following example shows a roadmap using the complete Milestone → Section → Feature → Issue hierarchy.

```markdown
Title: Weather Station

Numbering-Mode: automatic

Starting-Series: 0

<!-- GitMap-Section-Representation: issue -->
<!-- GitMap-Feature-Representation: issue -->

Sub-Title: Build a small weather station application.

Hierarchy-Issue-Title-Style: plain

# 0 First Release

## 0.1 Application
<!-- GitMap-ID: abcdefgh -->

Build the main weather application.

### 0.1.1 Current Conditions
<!-- GitMap-ID: bcdefghi -->

Display the latest weather observations.

#### 0.1.1.1 Display Temperature
<!-- GitMap-ID: cdefghij -->

Show the current temperature in the main window.

**Requirements:**

- Display the current temperature
- Include the temperature unit
- Refresh when new data is loaded

**Work Steps:**

- [ ] 0.1.1.1.1 (a) Add the temperature label
- [ ] 0.1.1.1.2 (b) Connect the label to weather data
- [ ] 0.1.1.1.3 (c) Test the display

#### 0.1.1.2 Display Humidity
<!-- GitMap-ID: defghijk -->

Show the current relative humidity.

**Requirements:**

- Display humidity as a percentage

### 0.1.2 Forecast
<!-- GitMap-ID: efghijkl -->

Display upcoming conditions.

#### 0.1.2.1 Display Tomorrow's Forecast
<!-- GitMap-ID: fghijklm -->

Show tomorrow's forecast in the application.

**Requirements:**

- Display the forecast high
- Display the forecast low
- Display expected conditions

## 0.2 Documentation
<!-- GitMap-ID: ghijklmn -->

#### 0.2.1 Write User Guide
<!-- GitMap-ID: hijklmno -->

Explain how to use the weather station.

**Requirements:**

- Explain installation
- Explain configuration
- Explain the main display
```

---

# 13. Complete Example — Sections Without Features

Features are not required.

```markdown
Title: Small Website

Numbering-Mode: automatic

Starting-Series: 1

<!-- GitMap-Section-Representation: issue -->
<!-- GitMap-Feature-Representation:  -->

# 1 Initial Release

## 1.1 Website
<!-- GitMap-ID: abcdefgh -->

#### 1.1.1 Create Home Page
<!-- GitMap-ID: bcdefghi -->

Build the site's home page.

**Requirements:**

- Include the project name
- Include navigation

**Work Steps:**

- [ ] 1.1.1.1 (a) Create the HTML
- [ ] 1.1.1.2 (b) Add the navigation

#### 1.1.2 Add About Page
<!-- GitMap-ID: cdefghij -->

Create an About page.
```

---

# 14. Complete Example — Issues Directly Under a Milestone

GitMap also supports Issues directly beneath a Milestone when the roadmap structure permits it.

```markdown
Title: Simple Project

Numbering-Mode: automatic

Starting-Series: 0

# 0 First Release

#### 0.1 Create Project
<!-- GitMap-ID: abcdefgh -->

Create the initial project.

**Requirements:**

- Create the source directory
- Create the project configuration

#### 0.2 Build First Feature
<!-- GitMap-ID: bcdefghi -->

Implement the first working feature.

**Work Steps:**

- [ ] 0.2.1 (a) Write the implementation
- [ ] 0.2.2 (b) Test the implementation
```

---

# 15. Manual Editing Guidelines

When editing a GitMap roadmap by hand:

1. Keep `Title:` near the top of the file.
2. Keep at least one `#` Milestone.
3. Use `##` only for Sections.
4. Use `###` only for Features.
5. Use `####` for normal Issues.
6. Keep each heading's number before its title.
7. Preserve existing `GitMap-ID` comments.
8. Use `**Requirements:**` followed by `- ` bullets.
9. Use `**Work Steps:**` followed by GitMap-formatted task-list items.
10. Open the file in GitMap after manual editing and verify that the hierarchy is interpreted as intended before synchronizing it to GitHub.

Because GitMap uses the Markdown structure to determine project hierarchy, a misplaced heading can change the parent of an Issue even when its text is otherwise correct.

---

# 16. What GitMap Manages for You

You do not normally need to hand-edit every part of this format.

The desktop application manages:

- automatic numbering,
- permanent GitMap IDs,
- structural placement,
- supported parent/child relationships,
- GitHub representation settings,
- roadmap serialization,
- renumbering after structural changes.

Manual Markdown editing is most useful when you want to make text changes directly, inspect the roadmap outside GitMap, use normal source-control tools, or create a roadmap from a known valid template.

For normal structural editing, using the GitMap Editor is the safest way to keep numbering, identities, and hierarchy consistent.
