Title: GitMap Roadmap

<!-- GitMap-Section-Representation: both -->
<!-- GitMap-Feature-Representation: both -->

Sub-Title: GitMap turns a project roadmap into a structured GitHub project.

Hierarchy-Issue-Title-Style: plain

# 0.1 Foundations (DONE)

## 0.1.1 Project Setup (DONE)
<!-- GitMap-ID: muredsir -->

#### 0.1.1.0.1 Create Python Project (DONE)
<!-- GitMap-ID: goredsox -->

Create the basic Python project structure for GitMap.

**Requirements:**
- Create the basic Python project structure for GitMap.

**Work Steps:**
- [ ] 0.1.1.0.1 (a) Create the `gitmap` package (DONE)
- [ ] 0.1.1.0.1 (b) Create `../pyproject.toml` (DONE)
- [ ] 0.1.1.0.1 (c) Create a `tests` directory (DONE)
- [ ] 0.1.1.0.1 (d) Create a `../.gitignore` (DONE)

#### 0.1.1.0.2 Install Dependencies (DONE)
<!-- GitMap-ID: horedsow -->

Set up the dependencies needed to develop and test GitMap.

**Requirements:**
- Set up the dependencies needed to develop and test GitMap.

**Work Steps:**
- [ ] 0.1.1.0.2 (a) Support editable installation (DONE)
- [ ] 0.1.1.0.2 (b) Add `pytest` as a development dependency (DONE)
- [ ] 0.1.1.0.2 (c) Confirm the development environment installs successfully (DONE)

#### 0.1.1.0.3 Create Command-Line Entry Point (DONE)
<!-- GitMap-ID: ioredsov -->

Create the basic command-line entry point for GitMap.

**Requirements:**
- Create the basic command-line entry point for GitMap.

**Work Steps:**
- [ ] 0.1.1.0.3 (a) Allow GitMap to be started from the command line (DONE)
- [ ] 0.1.1.0.3 (b) Display a simple welcome message (DONE)
- [ ] 0.1.1.0.3 (c) Exit cleanly (DONE)

#### 0.1.1.0.4 Add Initial Tests (DONE)
<!-- GitMap-ID: joredsou -->

Create the first automated tests for GitMap.

**Requirements:**
- Create the first automated tests for GitMap.

**Work Steps:**
- [ ] 0.1.1.0.4 (a) Confirm GitMap can be imported (DONE)
- [ ] 0.1.1.0.4 (b) Confirm the command-line entry point runs (DONE)
- [ ] 0.1.1.0.4 (c) Confirm the test suite can be run with `pytest` (DONE)

#### 0.1.1.0.5 Add Project Documentation (DONE)
<!-- GitMap-ID: koredsot -->

Create the basic documentation needed to understand and develop GitMap.

**Requirements:**
- Create the basic documentation needed to understand and develop GitMap.

**Work Steps:**
- [ ] 0.1.1.0.5 (a) Explain what GitMap does (DONE)
- [ ] 0.1.1.0.5 (b) Explain how to install GitMap for development (DONE)
- [ ] 0.1.1.0.5 (c) Explain how to run GitMap (DONE)
- [ ] 0.1.1.0.5 (d) Explain how to run the tests (DONE)

## 0.1.2 Roadmap Format (DONE)
<!-- GitMap-ID: nuredsiq -->

#### 0.1.2.0.1 Define Roadmap Structure (DONE)
<!-- GitMap-ID: loredsos -->

Define the hierarchy used in a GitMap roadmap.

**Requirements:**
- Define the hierarchy used in a GitMap roadmap.

**Work Steps:**
- [ ] 0.1.2.0.1 (a) Support milestones (DONE)
- [ ] 0.1.2.0.1 (b) Support Sections (DONE)
- [ ] 0.1.2.0.1 (c) Support issues (DONE)
- [ ] 0.1.2.0.1 (d) Support sub-issues (DONE)
- [ ] 0.1.2.0.1 (e) Support descriptions and requirements (DONE)
- [ ] 0.1.2.0.1 (f) Use Markdown headings to represent hierarchy (DONE)

#### 0.1.2.0.2 Create Example Roadmap (DONE)
<!-- GitMap-ID: moredsor -->

Create a complete example roadmap that can be used for development and testing.

**Requirements:**
- Create a complete example roadmap that can be used for development and testing.

**Work Steps:**
- [ ] 0.1.2.0.2 (a) Include at least one milestone (DONE)
- [ ] 0.1.2.0.2 (b) Include at least one Section (DONE)
- [ ] 0.1.2.0.2 (c) Include multiple issues (DONE)
- [ ] 0.1.2.0.2 (d) Include at least one sub-issue (DONE)
- [ ] 0.1.2.0.2 (e) Include descriptions and requirements (DONE)

#### 0.1.2.0.3 Document Roadmap Format (DONE)
<!-- GitMap-ID: noredsoq -->

Document how users should write a GitMap roadmap.

**Requirements:**
- Document how users should write a GitMap roadmap.

**Work Steps:**
- [ ] 0.1.2.0.3 (a) Explain each heading level (DONE)
- [ ] 0.1.2.0.3 (b) Show how milestones, Sections, issues, and sub-issues are represented (DONE)
- [ ] 0.1.2.0.3 (c) Provide a copyable example (DONE)

# 0.2 Roadmap Parser (DONE)

## 0.2.1 Markdown Parsing (DONE)
<!-- GitMap-ID: ouredsip -->

#### 0.2.1.0.1 Read Roadmap File (DONE)
<!-- GitMap-ID: ooredsop -->

Load a roadmap from a Markdown file.

**Requirements:**
- Load a roadmap from a Markdown file.

**Work Steps:**
- [ ] 0.2.1.0.1 (a) Accept a roadmap file path (DONE)
- [ ] 0.2.1.0.1 (b) Read the Markdown contents (DONE)
- [ ] 0.2.1.0.1 (c) Report a clear error if the file cannot be read (DONE)

#### 0.2.1.0.2 Parse Milestones (DONE)
<!-- GitMap-ID: poredsoo -->

Identify milestone headings in the roadmap.

**Requirements:**
- Identify milestone headings in the roadmap.

**Work Steps:**
- [ ] 0.2.1.0.2 (a) Recognize milestone headings (DONE)
- [ ] 0.2.1.0.2 (b) Capture the milestone number and title (DONE)
- [ ] 0.2.1.0.2 (c) Preserve the order of milestones (DONE)

#### 0.2.1.0.3 Parse Sections (DONE)
<!-- GitMap-ID: qoredson -->

Identify Sections within each milestone.

**Requirements:**
- Identify Sections within each milestone.

**Work Steps:**
- [ ] 0.2.1.0.3 (a) Associate each Section with its milestone (DONE)
- [ ] 0.2.1.0.3 (b) Capture the Section title (DONE)
- [ ] 0.2.1.0.3 (c) Capture the Section description (DONE)
- [ ] 0.2.1.0.3 (d) Recognize the Section type marker (DONE)

#### 0.2.1.0.4 Parse Issues (DONE)
<!-- GitMap-ID: roredsom -->

Identify issues within each Section.

**Requirements:**
- Identify issues within each Section.

**Work Steps:**
- [ ] 0.2.1.0.4 (a) Associate each issue with its Section (DONE)
- [ ] 0.2.1.0.4 (b) Capture the issue number and title (DONE)
- [ ] 0.2.1.0.4 (c) Capture the issue description (DONE)
- [ ] 0.2.1.0.4 (d) Capture requirements (DONE)

#### 0.2.1.0.5 Parse Work Steps (DONE)
<!-- GitMap-ID: soredsol -->

Support issues nested beneath other issues.

**Requirements:**
- Support issues nested beneath other issues.

**Work Steps:**
- [ ] 0.2.1.0.5 (a) Associate each sub-issue with its parent issue (DONE)
- [ ] 0.2.1.0.5 (b) Preserve the roadmap hierarchy (DONE)
- [ ] 0.2.1.0.5 (c) Support numbering such as `0.2.4.1` (DONE)

## 0.2.2 Roadmap Validation (DONE)
<!-- GitMap-ID: puredsio -->

#### 0.2.2.0.1 Validate Roadmap Structure (DONE)
<!-- GitMap-ID: toredsok -->

Check that the roadmap follows GitMap's expected hierarchy.

**Requirements:**
- Check that the roadmap follows GitMap's expected hierarchy.

**Work Steps:**
- [ ] 0.2.2.0.1 (a) Detect issues outside a Section (DONE)
- [ ] 0.2.2.0.1 (b) Detect Sections outside a milestone (DONE)
- [ ] 0.2.2.0.1 (c) Detect malformed hierarchy (DONE)
- [ ] 0.2.2.0.1 (d) Provide useful error messages (DONE)

#### 0.2.2.0.2 Validate Numbering (DONE)
<!-- GitMap-ID: uoredsoj -->

Check roadmap numbering for obvious errors.

**Requirements:**
- Check roadmap numbering for obvious errors.

**Work Steps:**
- [ ] 0.2.2.0.2 (a) Detect duplicate numbers (DONE)
- [ ] 0.2.2.0.2 (b) Detect invalid parent relationships (DONE)
- [ ] 0.2.2.0.2 (c) Identify the location of the problem (DONE)

#### 0.2.2.0.3 Preview Parsed Roadmap (DONE)
<!-- GitMap-ID: voredsoi -->

Allow users to see what GitMap understood before synchronization.

**Requirements:**
- Allow users to see what GitMap understood before synchronization.

**Work Steps:**
- [ ] 0.2.2.0.3 (a) Display milestones (DONE)
- [ ] 0.2.2.0.3 (b) Display Sections (DONE)
- [ ] 0.2.2.0.3 (c) Display issues and sub-issues (DONE)
- [ ] 0.2.2.0.3 (d) Preserve hierarchy in the preview (DONE)

# 0.3 GitHub Setup (DONE)

## 0.3.1 Repository Connection (DONE)
<!-- GitMap-ID: ruredsim -->

#### 0.3.1.0.1 Collect Repository Information (DONE)
<!-- GitMap-ID: woredsoh -->

Ask the user which GitHub repository should receive the roadmap.

**Requirements:**
- Ask the user which GitHub repository should receive the roadmap.

**Work Steps:**
- [ ] 0.3.1.0.1 (a) Ask for the GitHub username (DONE)
- [ ] 0.3.1.0.1 (b) Ask for the repository name (DONE)
- [ ] 0.3.1.0.1 (c) Do not create the repository automatically (DONE)
- [ ] 0.3.1.0.1 (d) Allow roadmap creation to be completed before GitHub setup begins (DONE)

#### 0.3.1.0.2 Configure GitHub Authentication (DONE)
<!-- GitMap-ID: xoredsog -->

Set up authentication required to work with the selected repository.

**Requirements:**
- Set up authentication required to work with the selected repository.

**Work Steps:**
- [ ] 0.3.1.0.2 (a) Keep credentials outside source control (DONE)
- [ ] 0.3.1.0.2 (b) Provide clear setup instructions (DONE)
- [ ] 0.3.1.0.2 (c) Detect missing authentication (DONE)
- [ ] 0.3.1.0.2 (d) Never store authentication tokens in the roadmap (DONE)

#### 0.3.1.0.3 Verify Repository (DONE)
<!-- GitMap-ID: yoredsof -->

Confirm that GitMap can access the repository before synchronization.

**Requirements:**
- Confirm that GitMap can access the repository before synchronization.

**Work Steps:**
- [ ] 0.3.1.0.3 (a) Verify that the repository exists (DONE)
- [ ] 0.3.1.0.3 (b) Verify that authentication works (DONE)
- [ ] 0.3.1.0.3 (c) Verify that the user has appropriate access (DONE)
- [ ] 0.3.1.0.3 (d) Stop synchronization if verification fails (DONE)

## 0.3.2 GitHub Project Structure (DONE)
<!-- GitMap-ID: suredsil -->

#### 0.3.2.0.1 Define Milestone Mapping (DONE)
<!-- GitMap-ID: zoredsoe -->

Define how roadmap milestones map to GitHub milestones.

**Requirements:**
- Define how roadmap milestones map to GitHub milestones.

**Work Steps:**
- [ ] 0.3.2.0.1 (a) Preserve milestone titles (DONE)
- [ ] 0.3.2.0.1 (b) Avoid creating duplicate milestones (DONE)
- [ ] 0.3.2.0.1 (c) Allow existing milestones to be recognized (DONE)

#### 0.3.2.0.2 Define Label Mapping (DONE)
<!-- GitMap-ID: aoredsod -->

Define the labels GitMap uses when creating GitHub items.

**Requirements:**
- Define the labels GitMap uses when creating GitHub items.

**Work Steps:**
- [ ] 0.3.2.0.2 (a) Support labels for Sections (DONE)
- [ ] 0.3.2.0.2 (b) Support labels for issues when defined by the roadmap (DONE)
- [ ] 0.3.2.0.2 (c) Avoid creating duplicate labels (DONE)
- [ ] 0.3.2.0.2 (d) Allow labels to be created before issues are synchronized (DONE)

#### 0.3.2.0.3 Define Issue Mapping (DONE)
<!-- GitMap-ID: boredsoc -->

Define how roadmap items become GitHub issues.

**Requirements:**
- Define how roadmap items become GitHub issues.

**Work Steps:**
- [ ] 0.3.2.0.3 (a) Preserve issue titles (DONE)
- [ ] 0.3.2.0.3 (b) Preserve descriptions (DONE)
- [ ] 0.3.2.0.3 (c) Preserve requirements (DONE)
- [ ] 0.3.2.0.3 (d) Associate issues with their milestone (DONE)
- [ ] 0.3.2.0.3 (e) Apply appropriate labels (DONE)

#### 0.3.2.0.4 Define Work Step Mapping (DONE)
<!-- GitMap-ID: coredsob -->

Define how roadmap hierarchy is represented in GitHub.

**Requirements:**
- Define how roadmap hierarchy is represented in GitHub.

**Work Steps:**
- [ ] 0.3.2.0.4 (a) Preserve parent-child relationships when supported (DONE)
- [ ] 0.3.2.0.4 (b) Keep sub-issues associated with their parent (DONE)
- [ ] 0.3.2.0.4 (c) Preserve roadmap numbering (DONE)

# 0.4 GitHub Synchronization (DONE)

## 0.4.1 Synchronization Engine (DONE)
<!-- GitMap-ID: turedsik -->

#### 0.4.1.0.1 Create Labels (DONE)
<!-- GitMap-ID: doredsoa -->

Create the labels required by the roadmap before synchronizing other items.

**Requirements:**
- Create the labels required by the roadmap before synchronizing other items.

**Work Steps:**
- [ ] 0.4.1.0.1 (a) Read required labels from the parsed roadmap (DONE)
- [ ] 0.4.1.0.1 (b) Detect labels that already exist (DONE)
- [ ] 0.4.1.0.1 (c) Create only missing labels (DONE)
- [ ] 0.4.1.0.1 (d) Do not create duplicates (DONE)

#### 0.4.1.0.2 Create Milestones (DONE)
<!-- GitMap-ID: eoredsoz -->

Create roadmap milestones in GitHub.

**Requirements:**
- Create roadmap milestones in GitHub.

**Work Steps:**
- [ ] 0.4.1.0.2 (a) Detect milestones that already exist (DONE)
- [ ] 0.4.1.0.2 (b) Create only missing milestones (DONE)
- [ ] 0.4.1.0.2 (c) Preserve milestone titles (DONE)
- [ ] 0.4.1.0.2 (d) Do not create duplicates (DONE)

#### 0.4.1.0.3 Create Sections (DONE)
<!-- GitMap-ID: foredsoy -->

Create GitHub issues representing roadmap Sections.

**Requirements:**
- Create GitHub issues representing roadmap Sections.

**Work Steps:**
- [ ] 0.4.1.0.3 (a) Create the Section before its child issues (DONE)
- [ ] 0.4.1.0.3 (b) Include the Section description (DONE)
- [ ] 0.4.1.0.3 (c) Apply the Section label (DONE)
- [ ] 0.4.1.0.3 (d) Associate the Section with its milestone (DONE)
- [ ] 0.4.1.0.3 (e) Detect an existing matching Section before creating another (DONE)

#### 0.4.1.0.4 Create Issues (DONE)
<!-- GitMap-ID: gpredsnx -->

Create GitHub issues from roadmap issues.

**Requirements:**
- Create GitHub issues from roadmap issues.

**Work Steps:**
- [ ] 0.4.1.0.4 (a) Preserve the issue title (DONE)
- [ ] 0.4.1.0.4 (b) Include the description (DONE)
- [ ] 0.4.1.0.4 (c) Include requirements using GitHub Markdown (DONE)
- [ ] 0.4.1.0.4 (d) Associate the issue with its milestone (DONE)
- [ ] 0.4.1.0.4 (e) Apply defined labels (DONE)
- [ ] 0.4.1.0.4 (f) Detect existing matching issues before creating another (DONE)

#### 0.4.1.0.5 Create Work Steps (DONE)
<!-- GitMap-ID: hpredsnw -->

Create roadmap sub-issues and associate them with their parent issues.

**Requirements:**
- Create roadmap sub-issues and associate them with their parent issues.

**Work Steps:**
- [ ] 0.4.1.0.5 (a) Create the parent before its sub-issues (DONE)
- [ ] 0.4.1.0.5 (b) Preserve the parent-child hierarchy (DONE)
- [ ] 0.4.1.0.5 (c) Include descriptions and requirements (DONE)
- [ ] 0.4.1.0.5 (d) Associate sub-issues with the correct milestone (DONE)

## 0.4.2 Safe Synchronization (DONE)
<!-- GitMap-ID: uuredsij -->

#### 0.4.2.0.1 Add Dry Run (DONE)
<!-- GitMap-ID: ipredsnv -->

Allow users to preview what synchronization would change without changing GitHub.

**Requirements:**
- Allow users to preview what synchronization would change without changing GitHub.

**Work Steps:**
- [ ] 0.4.2.0.1 (a) Show items that would be created (DONE)
- [ ] 0.4.2.0.1 (b) Show items that already exist (DONE)
- [ ] 0.4.2.0.1 (c) Make no GitHub changes during a dry run (DONE)
- [ ] 0.4.2.0.1 (d) Clearly identify dry-run output (DONE)

#### 0.4.2.0.2 Prevent Duplicate Items (DONE)
<!-- GitMap-ID: jpredsnu -->

Make repeated synchronization safe.

**Requirements:**
- Make repeated synchronization safe.

**Work Steps:**
- [ ] 0.4.2.0.2 (a) Check GitHub before creating an item (DONE)
- [ ] 0.4.2.0.2 (b) Reuse existing matching items (DONE)
- [ ] 0.4.2.0.2 (c) Prevent duplicate labels (DONE)
- [ ] 0.4.2.0.2 (d) Prevent duplicate milestones (DONE)
- [ ] 0.4.2.0.2 (e) Prevent duplicate issues (DONE)

#### 0.4.2.0.3 Add Synchronization Summary (DONE)
<!-- GitMap-ID: kpredsnt -->

Display the result of synchronization.

**Requirements:**
- Display the result of synchronization.

**Work Steps:**
- [ ] 0.4.2.0.3 (a) Report items created (DONE)
- [ ] 0.4.2.0.3 (b) Report items already present (DONE)
- [ ] 0.4.2.0.3 (c) Report skipped items (DONE)
- [ ] 0.4.2.0.3 (d) Report errors (DONE)

# 0.5 Roadmap Updates (DONE)

## 0.5.1 Existing Project Import (DONE)
<!-- GitMap-ID: vuredsii -->

#### 0.5.1.0.1 Read Existing Milestones (DONE)
<!-- GitMap-ID: lpredsns -->

Retrieve existing milestones from the repository.

**Requirements:**
- Retrieve existing milestones from the repository.

**Work Steps:**
- [ ] 0.5.1.0.1 (a) Read open milestones (DONE)
- [ ] 0.5.1.0.1 (b) Recognize milestones already represented in the roadmap (DONE)
- [ ] 0.5.1.0.1 (c) Preserve GitHub milestone identifiers for later updates (DONE)

#### 0.5.1.0.2 Read Existing Labels (DONE)
<!-- GitMap-ID: mpredsnr -->

Retrieve existing repository labels.

**Requirements:**
- Retrieve existing repository labels.

**Work Steps:**
- [ ] 0.5.1.0.2 (a) Read current labels (DONE)
- [ ] 0.5.1.0.2 (b) Match existing labels to roadmap labels (DONE)
- [ ] 0.5.1.0.2 (c) Avoid recreating labels that already exist (DONE)

#### 0.5.1.0.3 Read Existing Issues (DONE)
<!-- GitMap-ID: npredsnq -->

Retrieve existing GitHub issues that correspond to roadmap items.

**Requirements:**
- Retrieve existing GitHub issues that correspond to roadmap items.

**Work Steps:**
- [ ] 0.5.1.0.3 (a) Read existing issues (DONE)
- [ ] 0.5.1.0.3 (b) Match issues to roadmap items (DONE)
- [ ] 0.5.1.0.3 (c) Preserve GitHub issue numbers (DONE)
- [ ] 0.5.1.0.3 (d) Distinguish GitMap-managed items from unrelated repository issues (DONE)

#### 0.5.1.0.4 Rebuild Roadmap State (DONE)
<!-- GitMap-ID: opredsnp -->

Use GitHub data to reconstruct the current state of a GitMap-managed project.

**Requirements:**
- Use GitHub data to reconstruct the current state of a GitMap-managed project.

**Work Steps:**
- [ ] 0.5.1.0.4 (a) Associate existing issues with milestones (DONE)
- [ ] 0.5.1.0.4 (b) Restore Section and issue relationships (DONE)
- [ ] 0.5.1.0.4 (c) Restore sub-issue relationships when available (DONE)
- [ ] 0.5.1.0.4 (d) Identify roadmap items that cannot be matched safely (DONE)

## 0.5.2 Roadmap Changes (DONE)
<!-- GitMap-ID: wuredsih -->

#### 0.5.2.0.1 Detect Roadmap Changes (DONE)
<!-- GitMap-ID: ppredsno -->

Compare the local roadmap with the current GitHub project.

**Requirements:**
- Compare the local roadmap with the current GitHub project.

**Work Steps:**
- [ ] 0.5.2.0.1 (a) Detect new roadmap items (DONE)
- [ ] 0.5.2.0.1 (b) Detect changed roadmap items (DONE)
- [ ] 0.5.2.0.1 (c) Detect items that already match GitHub (DONE)
- [ ] 0.5.2.0.1 (d) Present differences before synchronization (DONE)

#### 0.5.2.0.2 Update Existing Items (DONE)
<!-- GitMap-ID: qpredsnn -->

Update GitHub items when their corresponding roadmap entries change.

**Requirements:**
- Update GitHub items when their corresponding roadmap entries change.

**Work Steps:**
- [ ] 0.5.2.0.2 (a) Update titles when changed (DONE)
- [ ] 0.5.2.0.2 (b) Update descriptions when changed (DONE)
- [ ] 0.5.2.0.2 (c) Update requirements when changed (DONE)
- [ ] 0.5.2.0.2 (d) Preserve GitHub issue numbers (DONE)
- [ ] 0.5.2.0.2 (e) Avoid recreating existing items (DONE)

#### 0.5.2.0.3 Handle Removed Roadmap Items (DONE)
<!-- GitMap-ID: rpredsnm -->

Safely identify items that exist in GitHub but have been removed from the roadmap.

**Requirements:**
- Safely identify items that exist in GitHub but have been removed from the roadmap.

**Work Steps:**
- [ ] 0.5.2.0.3 (a) Never delete GitHub items automatically (DONE)
- [ ] 0.5.2.0.3 (b) Report removed roadmap items (DONE)
- [ ] 0.5.2.0.3 (c) Require an explicit user decision before destructive changes (DONE)
- [ ] 0.5.2.0.3 (d) Preserve historical GitHub data by default (DONE)

#### 0.5.2.0.4 Preview Updates (DONE)
<!-- GitMap-ID: spredsnl -->

Show the user exactly what an update synchronization will do.

**Requirements:**
- Show the user exactly what an update synchronization will do.

**Work Steps:**
- [ ] 0.5.2.0.4 (a) Show new items (DONE)
- [ ] 0.5.2.0.4 (b) Show changed items (DONE)
- [ ] 0.5.2.0.4 (c) Show unchanged items (DONE)
- [ ] 0.5.2.0.4 (d) Show roadmap items that were removed (DONE)
- [ ] 0.5.2.0.4 (e) Require confirmation before applying changes (DONE)

# 0.6 User Workflow

## 0.6.1 Interactive Roadmap Builder (DONE)
<!-- GitMap-ID: xuredsig -->

#### 0.6.1.0.1 Start New Roadmap (DONE)
<!-- GitMap-ID: tpredsnk -->

Begin an interactive roadmap-building session.

**Requirements:**
- Begin an interactive roadmap-building session.

**Work Steps:**
- [ ] 0.6.1.0.1 (a) Ask for the project name (DONE)
- [ ] 0.6.1.0.1 (b) Ask for a project overview (DONE)
- [ ] 0.6.1.0.1 (c) Create the initial roadmap structure (DONE)
- [ ] 0.6.1.0.1 (d) Do not require GitHub information yet (DONE)

#### 0.6.1.0.2 Collect Milestones (DONE)
<!-- GitMap-ID: upredsnj -->

Guide the user through defining project milestones.

**Requirements:**
- Guide the user through defining project milestones.

**Work Steps:**
- [ ] 0.6.1.0.2 (a) Ask for the milestone number (DONE)
- [ ] 0.6.1.0.2 (b) Ask for the milestone title (DONE)
- [ ] 0.6.1.0.2 (c) Allow multiple milestones (DONE)
- [ ] 0.6.1.0.2 (d) Allow the user to indicate when they are finished (DONE)

#### 0.6.1.0.3 Collect Sections (DONE)
<!-- GitMap-ID: vpredsni -->

Guide the user through defining Sections within each milestone.

**Requirements:**
- Guide the user through defining Sections within each milestone.

**Work Steps:**
- [ ] 0.6.1.0.3 (a) Ask for the Section title (DONE)
- [ ] 0.6.1.0.3 (b) Ask for a Section overview (DONE)
- [ ] 0.6.1.0.3 (c) Associate the Section with its milestone (DONE)
- [ ] 0.6.1.0.3 (d) Allow multiple Sections (DONE)

#### 0.6.1.0.4 Collect Issues (DONE)
<!-- GitMap-ID: wpredsnh -->

Guide the user through defining issues within a Section.

**Requirements:**
- Guide the user through defining issues within a Section.

**Work Steps:**
- [ ] 0.6.1.0.4 (a) Ask for the issue title (DONE)
- [ ] 0.6.1.0.4 (b) Ask for the issue description (DONE)
- [ ] 0.6.1.0.4 (c) Ask for requirements (DONE)
- [ ] 0.6.1.0.4 (d) Allow requirements to be entered individually (DONE)
- [ ] 0.6.1.0.4 (e) Treat a blank entry as finished (DONE)

#### 0.6.1.0.5 Collect Work Steps (DONE)
<!-- GitMap-ID: xpredsng -->

Allow an issue to contain smaller sub-issues.

**Requirements:**
- Allow an issue to contain smaller sub-issues.

**Work Steps:**
- [ ] 0.6.1.0.5 (a) Ask whether an issue needs sub-issues (DONE)
- [ ] 0.6.1.0.5 (b) Collect sub-issue titles (DONE)
- [ ] 0.6.1.0.5 (c) Collect descriptions and requirements (DONE)
- [ ] 0.6.1.0.5 (d) Preserve the parent-child relationship (DONE)
- [ ] 0.6.1.0.5 (e) Support additional nesting when appropriate (DONE)

#### 0.6.1.0.6 Support Pasted Content (DONE)
<!-- GitMap-ID: ypredsnf -->

Allow users to paste existing project information instead of answering every question individually.

**Requirements:**
- Allow users to paste existing project information instead of answering every question individually.

**Work Steps:**
- [ ] 0.6.1.0.6 (a) Accept pasted overview text (DONE)
- [ ] 0.6.1.0.6 (b) Accept pasted descriptions (DONE)
- [ ] 0.6.1.0.6 (c) Accept pasted requirements (DONE)
- [ ] 0.6.1.0.6 (d) Preserve multiline content (DONE)
- [ ] 0.6.1.0.6 (e) Allow interactive questions and pasted content to be mixed (DONE)

## 0.6.2 Roadmap Review (DONE)
<!-- GitMap-ID: yuredsif -->

#### 0.6.2.0.1 Display Completed Roadmap (DONE)
<!-- GitMap-ID: zpredsne -->

Show the complete generated roadmap.

**Requirements:**
- Show the complete generated roadmap.

**Work Steps:**
- [ ] 0.6.2.0.1 (a) Preserve Markdown hierarchy (DONE)
- [ ] 0.6.2.0.1 (b) Make milestone, Section, issue, and sub-issue relationships clear (DONE)
- [ ] 0.6.2.0.1 (c) Show descriptions and requirements (DONE)

#### 0.6.2.0.2 Edit Roadmap Before Sync
<!-- GitMap-ID: apredsnd -->

Allow changes before GitHub synchronization begins.

**Requirements:**
- Allow changes before GitHub synchronization begins.

**Work Steps:**
- [ ] 0.6.2.0.2 (a) Allow items to be renamed (DONE)
- [ ] 0.6.2.0.2 (b) Allow descriptions and requirements to be changed (DONE)
- [ ] 0.6.2.0.2 (c) Allow items to be added (DONE)
- [ ] 0.6.2.0.2 (d) Allow items to be removed
- [ ] 0.6.2.0.2 (e) Revalidate the roadmap after changes

#### 0.6.2.0.3 Save Roadmap (DONE)
<!-- GitMap-ID: bpredsnc -->

Save the completed roadmap to `roadmap.md`.

**Requirements:**
- Save the completed roadmap to `roadmap.md`.

**Work Steps:**
- [ ] 0.6.2.0.3 (a) Produce valid GitMap Markdown (DONE)
- [ ] 0.6.2.0.3 (b) Preserve the complete hierarchy (DONE)
- [ ] 0.6.2.0.3 (c) Confirm where the roadmap was saved (DONE)

# 0.7 Changes to make

## 0.7.1 Synchronization Workflow Improvements
<!-- GitMap-ID: zuredsie -->

#### 0.7.1.0.1 Improve Change Preview Flow (DONE)
<!-- GitMap-ID: cpredsnb -->

Avoid displaying detailed change lists before the user asks to review them.

**Requirements:**
- Present a concise synchronization summary first and allow the user to choose which details to inspect.

**Work Steps:**
- [ ] 0.7.1.0.1 (a) Display change counts before detailed change lists
- [ ] 0.7.1.0.1 (b) Do not automatically display the complete added-item list
- [ ] 0.7.1.0.1 (c) Allow added items to be reviewed on request
- [ ] 0.7.1.0.1 (d) Allow changed items to be reviewed on request
- [ ] 0.7.1.0.1 (e) Allow unchanged items to be reviewed on request
- [ ] 0.7.1.0.1 (f) Allow removed items to be reviewed on request
- [ ] 0.7.1.0.1 (g) Return to the synchronization prompt after reviewing a list

#### 0.7.1.0.2 Preserve Identity During Renumbering
<!-- GitMap-ID: dpredsna -->

Recognize existing roadmap items when their GitMap numbers change. items.

**Requirements:**
- Treat renumbered roadmap items as updates to existing GitHub items rather than unrelated removed and newly created

**Work Steps:**
- [ ] 0.7.1.0.2 (a) Detect an existing roadmap item after its number changes
- [ ] 0.7.1.0.2 (b) Avoid relying solely on the GitMap number as item identity
- [ ] 0.7.1.0.2 (c) Preserve the existing GitHub item when a roadmap item is renumbered
- [ ] 0.7.1.0.2 (d) Update the GitMap marker after renumbering
- [ ] 0.7.1.0.2 (e) Preserve existing GitHub issue numbers and relationships where possible

#### 0.7.1.0.3 Update Renumbered Milestones
<!-- GitMap-ID: epredsnz -->

Update existing GitHub milestones when roadmap milestone numbers change.

**Requirements:**
- Prevent duplicate GitHub milestones when roadmap milestones are renumbered.

**Work Steps:**
- [ ] 0.7.1.0.3 (a) Match a renumbered milestone to its existing GitHub milestone
- [ ] 0.7.1.0.3 (b) Rename the existing GitHub milestone
- [ ] 0.7.1.0.3 (c) Preserve the GitHub milestone ID
- [ ] 0.7.1.0.3 (d) Preserve issues assigned to the milestone
- [ ] 0.7.1.0.3 (e) Do not create a second milestone solely because its roadmap number changed
- [ ] 0.7.1.0.3 (f) Detect and report ambiguous milestone matches

#### 0.7.1.0.4 Preview Renumbering During Synchronization
<!-- GitMap-ID: fpredsny -->

Make renumbering visible before GitHub is changed.

**Requirements:**
- Clearly distinguish renumbering from ordinary additions and removals during synchronization preview.

**Work Steps:**
- [ ] 0.7.1.0.4 (a) Identify renumbered roadmap items
- [ ] 0.7.1.0.4 (b) Display the old roadmap number
- [ ] 0.7.1.0.4 (c) Display the new roadmap number
- [ ] 0.7.1.0.4 (d) Distinguish renumbering from newly added items
- [ ] 0.7.1.0.4 (e) Distinguish renumbering from removed items
- [ ] 0.7.1.0.4 (f) Require normal synchronization confirmation before applying renumbering

#### 0.7.1.0.5 Display Synchronization Progress
<!-- GitMap-ID: gqredsmx -->

Show where GitMap is during an active synchronization.

**Requirements:**
- Let the user see how much synchronization work has completed and what GitMap is currently processing.

**Work Steps:**
- [ ] 0.7.1.0.5 (a) Count the total planned synchronization operations
- [ ] 0.7.1.0.5 (b) Display the current operation number
- [ ] 0.7.1.0.5 (c) Display the total number of operations
- [ ] 0.7.1.0.5 (d) Display the roadmap number of the item being processed
- [ ] 0.7.1.0.5 (e) Display the title of the item being processed
- [ ] 0.7.1.0.5 (f) Display whether the item is being created, updated, or checked
- [ ] 0.7.1.0.5 (g) Update progress as each operation completes
- [ ] 0.7.1.0.5 (h) Display a completion summary
- [ ] 0.7.1.0.5 (i) Display elapsed synchronization time

## 0.7.2 Synchronization Safety and Recovery
<!-- GitMap-ID: auredsid -->

#### 0.7.2.0.1 Validate Synchronization Plan
<!-- GitMap-ID: hqredsmw -->

**Work Steps:**
- [ ] 0.7.2.0.1 (a) Detect duplicate GitMap identifiers
- [ ] 0.7.2.0.1 (b) Detect duplicate milestone mappings
- [ ] 0.7.2.0.1 (c) Detect ambiguous identity matches
- [ ] 0.7.2.0.1 (d) Refuse to guess when identity cannot be determined safely
- [ ] 0.7.2.0.1 (e) Explain conflicts before synchronization
- [ ] 0.7.2.0.1 (f) Allow conflicts to be resolved before retrying

#### 0.7.2.0.2 Protect Partial Synchronization
<!-- GitMap-ID: iqredsmv -->

**Work Steps:**
- [ ] 0.7.2.0.2 (a) Track completed synchronization operations
- [ ] 0.7.2.0.2 (b) Identify the operation that failed
- [ ] 0.7.2.0.2 (c) Report operations completed before failure
- [ ] 0.7.2.0.2 (d) Report operations that remain incomplete
- [ ] 0.7.2.0.2 (e) Stop safely when synchronization cannot continue
- [ ] 0.7.2.0.2 (f) Preserve enough state for a safe retry

#### 0.7.2.0.3 Verify Synchronization Results
<!-- GitMap-ID: jqredsmu -->

**Work Steps:**
- [ ] 0.7.2.0.3 (a) Re-read affected GitHub items after synchronization
- [ ] 0.7.2.0.3 (b) Confirm expected items were created
- [ ] 0.7.2.0.3 (c) Confirm expected items were updated
- [ ] 0.7.2.0.3 (d) Confirm expected roadmap identities were preserved
- [ ] 0.7.2.0.3 (e) Detect unexpected duplicate identifiers
- [ ] 0.7.2.0.3 (f) Report differences between planned and actual results

#### 0.7.2.0.4 Support Safe Synchronization Retry
<!-- GitMap-ID: kqredsmt -->

**Work Steps:**
- [ ] 0.7.2.0.4 (a) Re-read GitHub state before retrying
- [ ] 0.7.2.0.4 (b) Recognize operations already completed
- [ ] 0.7.2.0.4 (c) Avoid recreating successfully created items
- [ ] 0.7.2.0.4 (d) Avoid reapplying unnecessary updates
- [ ] 0.7.2.0.4 (e) Continue remaining synchronization work safely
- [ ] 0.7.2.0.4 (f) Report final retry results

#### 0.7.2.0.5 Prevent Concurrent Synchronization
<!-- GitMap-ID: lqredsms -->

Prevent multiple GitMap synchronization operations from modifying the same repository at the same time.

**Requirements:**
- Prevent concurrent synchronization from creating duplicate or conflicting GitHub changes.

**Work Steps:**
- [ ] 0.7.2.0.5 (a) Detect when synchronization is already in progress
- [ ] 0.7.2.0.5 (b) Prevent a second synchronization from starting against the same repository
- [ ] 0.7.2.0.5 (c) Explain why the second synchronization was blocked
- [ ] 0.7.2.0.5 (d) Allow synchronization after the active operation completes
- [ ] 0.7.2.0.5 (e) Clear synchronization state after successful completion
- [ ] 0.7.2.0.5 (f) Clear synchronization state safely after failure
- [ ] 0.7.2.0.5 (g) Avoid leaving a stale synchronization lock after GitMap exits unexpectedly

## 0.7.3 Synchronization Performance
<!-- GitMap-ID: buredsic -->

#### 0.7.3.0.1 Skip Unchanged Items During Synchronization
<!-- GitMap-ID: mqredsmr -->

Avoid unnecessary GitHub operations for roadmap items that have already been determined to be unchanged.

**Requirements:**
- Reduce synchronization time by processing only items that require GitHub changes.

**Work Steps:**
- [ ] 0.7.3.0.1 (a) Identify unchanged items during synchronization planning
- [ ] 0.7.3.0.1 (b) Exclude unchanged items from synchronization operations
- [ ] 0.7.3.0.1 (c) Avoid unnecessary GitHub API calls for unchanged items
- [ ] 0.7.3.0.1 (d) Preserve unchanged items in the synchronization summary
- [ ] 0.7.3.0.1 (e) Count only actionable items in synchronization progress
- [ ] 0.7.3.0.1 (f) Report the number of unchanged items skipped

#### 0.7.3.0.2 Reuse Synchronization Plan
<!-- GitMap-ID: nqredsmq -->

Use the already-reviewed synchronization plan when applying changes.

**Requirements:**
- Avoid repeating work that was already completed while determining the synchronization preview.

**Work Steps:**
- [ ] 0.7.3.0.2 (a) Preserve the synchronization plan after preview
- [ ] 0.7.3.0.2 (b) Use the approved plan when synchronization begins
- [ ] 0.7.3.0.2 (c) Process only planned create and update operations
- [ ] 0.7.3.0.2 (d) Avoid recalculating unchanged items unnecessarily
- [ ] 0.7.3.0.2 (e) Ensure the applied plan matches the plan the user approved

## 0.7.4 GitHub Repository Setup
<!-- GitMap-ID: curedsib -->

#### 0.7.4.0.1 Choose Repository
<!-- GitMap-ID: sqredsml -->

Allow the user to choose where the roadmap will be synchronized.

**Requirements:**
- Connect the completed roadmap to the appropriate GitHub repository.

**Work Steps:**
- [ ] 0.7.4.0.1 (a) Use an existing repository
- [ ] 0.7.4.0.1 (b) Create a new repository

#### 0.7.4.0.2 Create Repository
<!-- GitMap-ID: tqredsmk -->

Create a GitHub repository directly from GitMap.

**Requirements:**
- Create the repository without requiring the user to leave GitMap.

**Work Steps:**
- [ ] 0.7.4.0.2 (a) Ask for the repository name
- [ ] 0.7.4.0.2 (b) Ask for a repository description
- [ ] 0.7.4.0.2 (c) Allow public or private visibility
- [ ] 0.7.4.0.2 (d) Create the repository through GitHub
- [ ] 0.7.4.0.2 (e) Confirm successful repository creation

#### 0.7.4.0.3 Connect Repository
<!-- GitMap-ID: uqredsmj -->

Connect the roadmap to the selected repository.

**Requirements:**
- Make the selected repository the synchronization target for the roadmap.

**Work Steps:**
- [ ] 0.7.4.0.3 (a) Verify repository access
- [ ] 0.7.4.0.3 (b) Store the repository association
- [ ] 0.7.4.0.3 (c) Prepare the repository for synchronization

#### 0.7.4.0.4 Initial Synchronization
<!-- GitMap-ID: vqredsmi -->

Allow the completed roadmap to proceed directly into GitMap's existing synchronization workflow.

**Requirements:**
- Move from roadmap creation to GitHub synchronization without restarting GitMap.

**Work Steps:**
- [ ] 0.7.4.0.4 (a) Preview the initial synchronization
- [ ] 0.7.4.0.4 (b) Require confirmation before synchronization
- [ ] 0.7.4.0.4 (c) Synchronize the roadmap to the repository
- [ ] 0.7.4.0.4 (d) Report synchronization results

## 0.7.5 Roadmap Numbering
<!-- GitMap-ID: duredsia -->

#### 0.7.5.0.1 Explain Roadmap Numbering
<!-- GitMap-ID: wqredsmh -->

Explain GitMap's numbering system when the user begins building a roadmap.

**Requirements:**
- Make the roadmap hierarchy and numbering rules clear before the user begins creating items.

**Work Steps:**
- [ ] 0.7.5.0.1 (a) Explain the milestone numbering format
- [ ] 0.7.5.0.1 (b) Explain how child numbers extend their parent number
- [ ] 0.7.5.0.1 (c) Show an example hierarchy
- [ ] 0.7.5.0.1 (d) Explain automatic numbering
- [ ] 0.7.5.0.1 (e) Explain manual numbering

#### 0.7.5.0.2 Choose Numbering Mode
<!-- GitMap-ID: mtredsjr -->

Allow the user to choose between automatic and manual numbering.

**Requirements:**
- Let users control whether GitMap assigns roadmap numbers or they enter them manually.

**Work Steps:**
- [ ] 0.7.5.0.2 (a) Offer automatic numbering
- [ ] 0.7.5.0.2 (b) Offer manual numbering
- [ ] 0.7.5.0.2 (c) Allow manual numbering when automatic numbering cannot be used

#### 0.7.5.0.3 Choose Starting Series
<!-- GitMap-ID: ntredsjq -->

Allow automatic numbering to reflect the project's development stage.

**Requirements:**
- Start roadmap numbering in the appropriate version series.

**Work Steps:**
- [ ] 0.7.5.0.3 (a) Offer pre-production numbering beginning with 0.x
- [ ] 0.7.5.0.3 (b) Offer production numbering beginning with 1.x

#### 0.7.5.0.4 Generate Hierarchical Numbers
<!-- GitMap-ID: otredsjp -->

Generate roadmap numbers based on the hierarchy the user actually creates.

**Requirements:**
- Automatically assign valid numbers without requiring every hierarchy level to be present.

**Work Steps:**
- [ ] 0.7.5.0.4 (a) Number milestones automatically
- [ ] 0.7.5.0.4 (b) Number Sections automatically
- [ ] 0.7.5.0.4 (c) Number features automatically
- [ ] 0.7.5.0.4 (d) Number issues automatically
- [ ] 0.7.5.0.4 (e) Number Work Steps automatically
- [ ] 0.7.5.0.4 (f) Increment sibling numbers automatically
- [ ] 0.7.5.0.4 (g) Support letter sequences such as (a), (b), and (c) where used

## 0.7.6 GitHub Roadmap Representation
<!-- GitMap-ID: euredsiz -->

#### 0.7.6.0.1 Create Roadmap Labels
<!-- GitMap-ID: ptredsjo -->

Create a searchable GitHub label identifying Issues belonging to a roadmap.

#### 0.7.6.0.2 Choose Section and Feature Representation
<!-- GitMap-ID: qtredsjn -->

Allow the user to choose whether Sections and Features are represented as GitHub Issues or labels.

#### 0.7.6.0.3 Create Hierarchy Issues
<!-- GitMap-ID: rtredsjm -->

When selected, create GitHub Issues for Sections and/or Features.

## 0.7.7 Behavior Corrections
<!-- GitMap-ID: furedsiy -->

#### 0.7.7.0.1 Create Hierarchy Issues on Existing Roadmaps
<!-- GitMap-ID: juredsiu -->

When Section or Feature Issues are enabled for a roadmap that already has synchronized GitHub content, GitMap should
detect that the hierarchy Issues do not yet exist and ask the user whether they should be created. Users explicitly
choose whether missing Section and Feature Issues are created for an existing synchronized roadmap.

**Work Steps:**
- [ ] 0.7.7.0.1 (a) Detect when Section or Feature Issues are enabled for an existing roadmap
- [ ] 0.7.7.0.1 (b) Determine whether the corresponding hierarchy Issues already exist
- [ ] 0.7.7.0.1 (c) Inform the user how many Section and Feature Issues will be created
- [ ] 0.7.7.0.1 (d) Ask the user whether to create the missing hierarchy Issues
- [ ] 0.7.7.0.1 (e) Create hierarchy Issues only after confirmation

#### 0.7.7.0.2 Require Approval Before Modifying Existing GitHub Items
<!-- GitMap-ID: kuredsit -->

Once a GitHub item already exists, GitMap must not update, close, or otherwise modify it unless the change appears in
the synchronization preview and has been approved by the user. Existing GitHub items are never modified without first
being shown to the user and explicitly approved.

**Work Steps:**
- [ ] 0.7.7.0.2 (a) Detect modifications to existing GitHub items
- [ ] 0.7.7.0.2 (b) Include all modifications in the synchronization preview
- [ ] 0.7.7.0.2 (c) Prevent updates that were not included in the approved synchronization plan
- [ ] 0.7.7.0.2 (d) Ensure updates and closures require user approval
- [ ] 0.7.7.0.2 (e) Verify only approved changes are applied

## 0.7.8 Finish 0.7.6
<!-- GitMap-ID: gvredshx -->

#### 0.7.8.0.1 Customize Hierarchy Issue Titles
<!-- GitMap-ID: quredsin -->

Allow users to choose how Section and Feature GitHub Issues are titled so they are easy to distinguish from normal
roadmap Issues. Users can easily distinguish hierarchy Issues from normal roadmap Issues while preserving a consistent
appearance across GitHub.

**Work Steps:**
- [ ] 0.7.8.0.1 (a) Add a hierarchy Issue title style option during roadmap creation.
- [ ] 0.7.8.0.1 (b) Store the selected title style in the roadmap.
- [ ] 0.7.8.0.1 (c) Update Section Issue title generation.
- [ ] 0.7.8.0.1 (d) Update Feature Issue title generation.
- [ ] 0.7.8.0.1 (e) Preserve title style during synchronization.
- [ ] 0.7.8.0.1 (f) Show the selected title style in synchronization preview.

#### 0.7.8.0.2 Create Parent/Child Relationships
<!-- GitMap-ID: stredsjl -->

When hierarchy items are created as GitHub Issues, create the appropriate GitHub sub-issue relationships between parents
and their children.

#### 0.7.8.0.3 Preserve GitHub Issue Identity
<!-- GitMap-ID: ttredsjk -->

Ensure Sections, Features, and Issues retain their GitHub Issue associations across subsequent synchronizations.

#### 0.7.8.0.4 Support Roadmap-Specific Searching
<!-- GitMap-ID: utredsjj -->

Allow the roadmap label and GitMap identifiers to be used to locate the appropriate GitHub Issues.

## 0.7.9 Automatic Numbering During Roadmap Editing
<!-- GitMap-ID: hvredshw -->

#### 0.7.9.0.1 Preserve Numbering Mode During Editing
<!-- GitMap-ID: vtredsji -->

Remember how the roadmap is being numbered and use that behavior when the user enters the roadmap options or editing
workflow.

**Requirements:**
- Automatic numbering remains automatic throughout creation and editing.

#### 0.7.9.0.2 Add Items at the End Automatically
<!-- GitMap-ID: wtredsjh -->

Determine the next available sibling number when a new item is added at the end of an existing list. it.

**Requirements:**
- If the last Milestone is 0.4, adding another Milestone automatically creates 0.5 without asking the user to calculate

#### 0.7.9.0.3 Insert Items Between Existing Items
<!-- GitMap-ID: xtredsjg -->

Allow an automatically numbered item to be inserted at a chosen position instead of requiring every new item to be
placed at the end.

**Requirements:**
- Users can place a new item where it logically belongs without manually renumbering the roadmap.

#### 0.7.9.0.4 Preview Automatic Renumbering
<!-- GitMap-ID: ytredsjf -->

Show the numbering changes before an insertion or other edit changes existing roadmap numbers.

**Requirements:**
- Existing roadmap numbers are never silently changed by automatic numbering.

#### 0.7.9.0.5 Preserve Identity During Renumbering
<!-- GitMap-ID: ztredsje -->

Keep roadmap and GitHub items associated with the same underlying item when their roadmap numbers change.

**Requirements:**
- Renumbering reorganizes the roadmap without making existing items appear new to GitMap or GitHub.

#### 0.7.9.0.6 Detect Numbering Conflicts
<!-- GitMap-ID: atredsjd -->

Protect automatically numbered roadmaps from invalid or conflicting numbers.

**Requirements:**
- Automatic numbering produces a valid and internally consistent roadmap.~~

#### 0.7.9.0.7 Respect Roadmap Structure During Editing
<!-- GitMap-ID: btredsjc -->

Ensure that editing and adding items follow the hierarchy selected for the roadmap.

**Requirements:**
- Editing an existing roadmap follows the same structural rules used when the roadmap was created.

## 0.7.10 GitHub Repository Setup
<!-- GitMap-ID: ivredshv -->

#### 0.7.10.0.1 Choose Repository
<!-- GitMap-ID: oqredsmp -->

Allow the user to choose where the roadmap will be synchronized.

**Requirements:**
- Connect the completed roadmap to the appropriate GitHub repository.

**Work Steps:**
- [ ] 0.7.10.0.1 (a) Use an existing repository
- [ ] 0.7.10.0.1 (b) Create a new repository

#### 0.7.10.0.2 Create Repository
<!-- GitMap-ID: pqredsmo -->

Create a GitHub repository directly from GitMap.

**Requirements:**
- Create the repository without requiring the user to leave GitMap.

**Work Steps:**
- [ ] 0.7.10.0.2 (a) Ask for the repository name
- [ ] 0.7.10.0.2 (b) Ask for a repository description
- [ ] 0.7.10.0.2 (c) Allow public or private visibility
- [ ] 0.7.10.0.2 (d) Create the repository through GitHub
- [ ] 0.7.10.0.2 (e) Confirm successful repository creation

#### 0.7.10.0.3 Connect Repository
<!-- GitMap-ID: qqredsmn -->

Connect the roadmap to the selected repository.

**Requirements:**
- Make the selected repository the synchronization target for the roadmap.

**Work Steps:**
- [ ] 0.7.10.0.3 (a) Verify repository access
- [ ] 0.7.10.0.3 (b) Store the repository association
- [ ] 0.7.10.0.3 (c) Prepare the repository for synchronization

#### 0.7.10.0.4 Initial Synchronization
<!-- GitMap-ID: rqredsmm -->

Allow the completed roadmap to proceed directly into GitMap's existing synchronization workflow.

**Requirements:**
- Move from roadmap creation to GitHub synchronization without restarting GitMap.

**Work Steps:**
- [ ] 0.7.10.0.4 (a) Preview the initial synchronization
- [ ] 0.7.10.0.4 (b) Require confirmation before synchronization
- [ ] 0.7.10.0.4 (c) Synchronize the roadmap to the repository
- [ ] 0.7.10.0.4 (d) Report synchronization results

## 0.7.11 Roadmap Maintenance
<!-- GitMap-ID: jvredshu -->

#### 0.7.11.0.1 Reopen an Existing Roadmap
<!-- GitMap-ID: ctredsjb -->

Allow a saved roadmap to be loaded for continued work.

#### 0.7.11.0.2 Review Roadmap Status
<!-- GitMap-ID: dtredsja -->

Show the current state of roadmap items before making changes.

#### 0.7.11.0.3 Edit Existing Items
<!-- GitMap-ID: etredsjz -->

Allow users to change names, descriptions, requirements, and Work Steps.

#### 0.7.11.0.4 Add and Remove Items
<!-- GitMap-ID: ftredsjy -->

Allow users to add or remove roadmap items while preserving hierarchy, numbering, and identity.

#### 0.7.11.0.5 Synchronize Changes
<!-- GitMap-ID: guredsix -->

Allow changes made after the initial synchronization to proceed through the existing preview and synchronization
workflow.

#### 0.7.11.0.6 Recover From Cancelled Changes
<!-- GitMap-ID: huredsiw -->

Ensure that cancelling an edit or renumbering operation leaves the previous roadmap unchanged.

#### 0.7.11.0.7 Keep Roadmap and GitHub State Consistent
<!-- GitMap-ID: iuredsiv -->

Ensure that the roadmap saved locally and the corresponding GitHub items remain associated through subsequent edits and
synchronizations.

# 0.8 Command-Line Experience

## 0.8.1 GitMap Commands
<!-- GitMap-ID: kvredsht -->

#### 0.8.1.0.1 Create Main GitMap Command
<!-- GitMap-ID: xqredsmg -->

Create the primary command used to launch GitMap.

**Requirements:**
- Create the primary command used to launch GitMap.

**Work Steps:**
- [ ] 0.8.1.0.1 (a) Provide a `gitmap` command
- [ ] 0.8.1.0.1 (b) Display useful help
- [ ] 0.8.1.0.1 (c) Display the installed version
- [ ] 0.8.1.0.1 (d) Exit cleanly when requested

#### 0.8.1.0.2 Create Roadmap Command
<!-- GitMap-ID: yqredsmf -->

Provide a command for creating or working with a roadmap.

**Requirements:**
- Provide a command for creating or working with a roadmap.

**Work Steps:**
- [ ] 0.8.1.0.2 (a) Start the interactive roadmap builder
- [ ] 0.8.1.0.2 (b) Allow an existing roadmap to be opened
- [ ] 0.8.1.0.2 (c) Validate the roadmap before completing
- [ ] 0.8.1.0.2 (d) Save changes to `roadmap.md`

#### 0.8.1.0.3 Create Preview Command
<!-- GitMap-ID: zqredsme -->

Provide a command for previewing how GitMap interprets a roadmap.

**Requirements:**
- Provide a command for previewing how GitMap interprets a roadmap.

**Work Steps:**
- [ ] 0.8.1.0.3 (a) Parse the selected roadmap
- [ ] 0.8.1.0.3 (b) Display its hierarchy
- [ ] 0.8.1.0.3 (c) Report validation problems
- [ ] 0.8.1.0.3 (d) Make no GitHub changes

#### 0.8.1.0.4 Create Setup Command
<!-- GitMap-ID: aqredsmd -->

Guide the user through connecting a roadmap to a GitHub repository.

**Requirements:**
- Guide the user through connecting a roadmap to a GitHub repository.

**Work Steps:**
- [ ] 0.8.1.0.4 (a) Ask for the GitHub username
- [ ] 0.8.1.0.4 (b) Ask for the repository name
- [ ] 0.8.1.0.4 (c) Configure authentication
- [ ] 0.8.1.0.4 (d) Verify repository access
- [ ] 0.8.1.0.4 (e) Save non-sensitive repository configuration

#### 0.8.1.0.5 Create Sync Command
<!-- GitMap-ID: bqredsmc -->

Provide a command for synchronizing the roadmap with GitHub.

**Requirements:**
- Provide a command for synchronizing the roadmap with GitHub.

**Work Steps:**
- [ ] 0.8.1.0.5 (a) Validate before synchronization
- [ ] 0.8.1.0.5 (b) Verify repository access
- [ ] 0.8.1.0.5 (c) Support dry-run mode
- [ ] 0.8.1.0.5 (d) Display planned changes
- [ ] 0.8.1.0.5 (e) Display a synchronization summary

## 0.8.2 Errors and Guidance
<!-- GitMap-ID: lvredshs -->

#### 0.8.2.0.1 Add User-Friendly Errors
<!-- GitMap-ID: cqredsmb -->

Replace technical failures with useful messages when possible.

**Requirements:**
- Replace technical failures with useful messages when possible.

**Work Steps:**
- [ ] 0.8.2.0.1 (a) Explain missing roadmap files
- [ ] 0.8.2.0.1 (b) Explain malformed roadmaps
- [ ] 0.8.2.0.1 (c) Explain authentication failures
- [ ] 0.8.2.0.1 (d) Explain repository access failures
- [ ] 0.8.2.0.1 (e) Avoid unnecessary Python tracebacks during normal use

#### 0.8.2.0.2 Add Next-Step Guidance
<!-- GitMap-ID: dqredsma -->

Tell users what they can do after each major operation.

**Requirements:**
- Tell users what they can do after each major operation.

**Work Steps:**
- [ ] 0.8.2.0.2 (a) Provide guidance after roadmap creation
- [ ] 0.8.2.0.2 (b) Provide guidance after repository setup
- [ ] 0.8.2.0.2 (c) Provide guidance after preview
- [ ] 0.8.2.0.2 (d) Provide guidance after synchronization

# 0.9 GitMap Desktop GUI

## 0.9.1 Main GitMap Workspace
<!-- GitMap-ID: crredslb -->

#### 0.9.1.0.1 Load the Designer-Based Main Window
<!-- GitMap-ID: eqredsmz -->

Load the GitMap desktop interface from the Qt Designer file while keeping application behavior in Python.

**Requirements:**
- Load the GitMap GUI from a Qt Designer interface while keeping application behavior in Python.

**Work Steps:**
- [ ] 0.9.1.0.1 (a) Create `gitmap/gui/app_old.py`
- [ ] 0.9.1.0.1 (b) Create `../user_interfaces`
- [ ] 0.9.1.0.1 (c) Create the GUI module entry point
- [ ] 0.9.1.0.1 (d) Create the `QApplication`
- [ ] 0.9.1.0.1 (e) Locate `main_window.ui` relative to `app_old.py`
- [ ] 0.9.1.0.1 (f) Open the `.ui` file using `QFile`
- [ ] 0.9.1.0.1 (g) Load the interface using `QUiLoader`
- [ ] 0.9.1.0.1 (h) Display the loaded main window
- [ ] 0.9.1.0.1 (i) Verify GitMap launches without UI loading errors

#### 0.9.1.0.2 Create the Main Workspace Layout
<!-- GitMap-ID: fqredsmy -->

Create the main two-part application layout with a large roadmap workspace and a smaller navigation and action area.
application window.

**Requirements:**
- Provide a large roadmap workspace with a smaller navigation and action area that resizes correctly with the

**Work Steps:**
- [ ] 0.9.1.0.2 (a) Create the main central widget in Qt Designer
- [ ] 0.9.1.0.2 (b) Create the roadmap workspace area
- [ ] 0.9.1.0.2 (c) Create the navigation and action area
- [ ] 0.9.1.0.2 (d) Place the two areas inside a splitter
- [ ] 0.9.1.0.2 (e) Give the roadmap area the larger initial share of the window
- [ ] 0.9.1.0.2 (f) Configure layouts so controls resize with the window
- [ ] 0.9.1.0.2 (g) Test the interface at its normal startup size
- [ ] 0.9.1.0.2 (h) Test the interface maximized
- [ ] 0.9.1.0.2 (i) Verify the roadmap tree fills the available workspace

#### 0.9.1.0.3 Create the Empty Workspace State
<!-- GitMap-ID: grredslx -->

Define what GitMap displays before a roadmap is opened or created and how the interface changes after a roadmap becomes
active. when one becomes active.

**Requirements:**
- Clearly provide Create Roadmap and Open Roadmap when no roadmap is active and transition to roadmap-specific controls

**Work Steps:**
- [ ] 0.9.1.0.3 (a) Add the Create Roadmap button
- [ ] 0.9.1.0.3 (b) Add the Open Roadmap button
- [ ] 0.9.1.0.3 (c) Assign stable Designer object names to both buttons
- [ ] 0.9.1.0.3 (d) Locate both buttons from Python using `findChild`
- [ ] 0.9.1.0.3 (e) Define the empty-workspace state
- [ ] 0.9.1.0.3 (f) Define the active-roadmap state
- [ ] 0.9.1.0.3 (g) Switch between the states when appropriate

#### 0.9.1.0.4 Create the Roadmap Tree
<!-- GitMap-ID: hrredslw -->

Create the expandable and scrollable tree used to display the active roadmap.

**Requirements:**
- Display the active roadmap in a large expandable and scrollable tree without an unnecessary column heading.

**Work Steps:**
- [ ] 0.9.1.0.4 (a) Add the roadmap tree in Qt Designer
- [ ] 0.9.1.0.4 (b) Assign the roadmap tree a stable object name
- [ ] 0.9.1.0.4 (c) Locate the tree using `findChild`
- [ ] 0.9.1.0.4 (d) Hide the tree header
- [ ] 0.9.1.0.4 (e) Verify vertical scrolling
- [ ] 0.9.1.0.4 (f) Verify long roadmap items remain usable
- [ ] 0.9.1.0.4 (g) Verify the tree resizes with the workspace

#### 0.9.1.0.5 Display the Roadmap Name
<!-- GitMap-ID: irredslv -->

Show the name of the active roadmap in the main workspace.

**Requirements:**
- Display the active Roadmap model's name and keep it updated when the active roadmap or its name changes.

**Work Steps:**
- [ ] 0.9.1.0.5 (a) Read the roadmap name from the Roadmap model
- [ ] 0.9.1.0.5 (b) Display the roadmap name in the workspace
- [ ] 0.9.1.0.5 (c) Update the displayed name when another roadmap is opened
- [ ] 0.9.1.0.5 (d) Update the displayed name when the roadmap is renamed
- [ ] 0.9.1.0.5 (e) Support displaying the name of an unsaved roadmap

#### 0.9.1.0.6 Display Milestones
<!-- GitMap-ID: jrredslu -->

Add every Milestone in the active Roadmap model to the graphical hierarchy.

**Requirements:**
- Display every Milestone beneath the roadmap root using its roadmap number and title.

**Work Steps:**
- [ ] 0.9.1.0.6 (a) Iterate through `roadmap.milestones`
- [ ] 0.9.1.0.6 (b) Create a tree item for each Milestone
- [ ] 0.9.1.0.6 (c) Display the Milestone number
- [ ] 0.9.1.0.6 (d) Display the Milestone title
- [ ] 0.9.1.0.6 (e) Attach each Milestone beneath the roadmap root

#### 0.9.1.0.7 Display Sections
<!-- GitMap-ID: krredslt -->

Add Sections beneath their parent Milestones when the active roadmap uses Sections.

**Requirements:**
- Display Sections in their correct hierarchy while continuing to support roadmaps that do not use Sections.

**Work Steps:**
- [ ] 0.9.1.0.7 (a) Iterate through each Milestone's Sections
- [ ] 0.9.1.0.7 (b) Create a tree item for each Section
- [ ] 0.9.1.0.7 (c) Display the Section number and title
- [ ] 0.9.1.0.7 (d) Attach each Section beneath its parent Milestone
- [ ] 0.9.1.0.7 (e) Verify roadmaps without Sections remain supported

#### 0.9.1.0.8 Display Features
<!-- GitMap-ID: lrredsls -->

Add Features beneath their parent Sections when the active roadmap uses Features.

**Requirements:**
- Display Features in their correct hierarchy while continuing to support featureless roadmaps.

**Work Steps:**
- [ ] 0.9.1.0.8 (a) Iterate through each Section's Features
- [ ] 0.9.1.0.8 (b) Create a tree item for each Feature
- [ ] 0.9.1.0.8 (c) Display the Feature number and title
- [ ] 0.9.1.0.8 (d) Attach each Feature beneath its parent Section
- [ ] 0.9.1.0.8 (e) Verify featureless roadmaps remain supported

#### 0.9.1.0.9 Display Issues
<!-- GitMap-ID: mrredslr -->

Add Issues at each hierarchy location supported by the active roadmap.

**Requirements:**
- Display Issues correctly whether they belong to Features, Sections or directly to Milestones.

**Work Steps:**
- [ ] 0.9.1.0.9 (a) Display Issues beneath Features
- [ ] 0.9.1.0.9 (b) Display Issues directly beneath Sections
- [ ] 0.9.1.0.9 (c) Display Issues directly beneath Milestones
- [ ] 0.9.1.0.9 (d) Display each Issue number and title
- [ ] 0.9.1.0.9 (e) Reuse a common Issue tree helper
- [ ] 0.9.1.0.9 (f) Verify each Issue appears beneath the correct parent

#### 0.9.1.0.10 Display Requirements
<!-- GitMap-ID: nrredslq -->

Display each Issue's Requirement separately from its actionable Work Steps.

**Requirements:**
- Display Requirements as italicized non-checkbox text beneath their parent Issue.

**Work Steps:**
- [ ] 0.9.1.0.10 (a) Read the Requirement from `issue.requirements`
- [ ] 0.9.1.0.10 (b) Create a tree item for the Requirement
- [ ] 0.9.1.0.10 (c) Remove Markdown checkbox syntax if encountered in legacy content
- [ ] 0.9.1.0.10 (d) Display the Requirement without a GUI checkbox
- [ ] 0.9.1.0.10 (e) Apply an italic font to the Requirement
- [ ] 0.9.1.0.10 (f) Verify the Requirement is visually distinct from Work Steps

#### 0.9.1.0.11 Display Work Steps
<!-- GitMap-ID: orredslp -->

Display an Issue's actionable Work Steps beneath the Issue and preserve their markers and completion state.

**Requirements:**
- Display Work Steps separately from Requirements with their marker, text and completion state.

**Work Steps:**
- [ ] 0.9.1.0.11 (a) Iterate through `issue.work_steps`
- [ ] 0.9.1.0.11 (b) Create a tree item for each Work Step
- [ ] 0.9.1.0.11 (c) Display each Work Step marker
- [ ] 0.9.1.0.11 (d) Display each Work Step title
- [ ] 0.9.1.0.11 (e) Represent the Work Step completion state
- [ ] 0.9.1.0.11 (f) Verify Work Steps appear beneath the correct Issue

#### 0.9.1.0.12 Apply GitMap GUI Colors
<!-- GitMap-ID: prredslo -->

Carry GitMap's established command-line color conventions into the graphical roadmap display. the italic Requirement
distinction.

**Requirements:**
- Use the established CLI semantic colors in the GUI where practical while keeping the roadmap readable and preserving

**Work Steps:**
- [ ] 0.9.1.0.12 (a) Identify the semantic colors used by the GitMap CLI
- [ ] 0.9.1.0.12 (b) Map the CLI colors to GUI hierarchy types
- [ ] 0.9.1.0.12 (c) Apply the Milestone color
- [ ] 0.9.1.0.12 (d) Apply the Section color
- [ ] 0.9.1.0.12 (e) Apply the Feature color
- [ ] 0.9.1.0.12 (f) Apply the Issue color
- [ ] 0.9.1.0.12 (g) Apply appropriate Requirement and Work Step styling
- [ ] 0.9.1.0.12 (h) Verify the complete tree remains easy to read

## 0.9.2 Open Existing Roadmaps
<!-- GitMap-ID: hwredsgw -->

#### 0.9.2.0.1 Open a Roadmap File
<!-- GitMap-ID: qrredsln -->

Allow the user to select an existing roadmap using the desktop interface.

**Requirements:**
- Provide a graphical Open Roadmap workflow for selecting an existing GitMap roadmap file.

**Work Steps:**
- [ ] 0.9.2.0.1 (a) Connect the Open Roadmap button
- [ ] 0.9.2.0.1 (b) Display a `QFileDialog`
- [ ] 0.9.2.0.1 (c) Allow Markdown roadmap files to be selected
- [ ] 0.9.2.0.1 (d) Return without changing the active roadmap when the dialog is cancelled
- [ ] 0.9.2.0.1 (e) Preserve the selected roadmap path

#### 0.9.2.0.2 Parse an Opened Roadmap
<!-- GitMap-ID: rrredslm -->

Pass the selected roadmap through GitMap's existing parser rather than implementing separate GUI parsing logic.

**Requirements:**
- Parse roadmaps opened by the GUI using the existing `parse_roadmap` behavior.

**Work Steps:**
- [ ] 0.9.2.0.2 (a) Pass the selected path to `parse_roadmap`
- [ ] 0.9.2.0.2 (b) Receive the populated Roadmap model
- [ ] 0.9.2.0.2 (c) Preserve hierarchy configuration
- [ ] 0.9.2.0.2 (d) Preserve permanent GitMap IDs
- [ ] 0.9.2.0.2 (e) Make the parsed Roadmap the active GUI model

#### 0.9.2.0.3 Populate the Workspace
<!-- GitMap-ID: srredsll -->

Display a successfully parsed Roadmap model in the main workspace.

**Requirements:**
- Populate the same main workspace with successfully opened and newly created roadmaps.

**Work Steps:**
- [ ] 0.9.2.0.3 (a) Clear the previous roadmap tree
- [ ] 0.9.2.0.3 (b) Display the opened roadmap name
- [ ] 0.9.2.0.3 (c) Populate the roadmap hierarchy
- [ ] 0.9.2.0.3 (d) Display Requirements and Work Steps
- [ ] 0.9.2.0.3 (e) Expand the initial tree
- [ ] 0.9.2.0.3 (f) Transition to the active-roadmap state

#### 0.9.2.0.4 Handle Roadmap Opening Errors
<!-- GitMap-ID: trredslk -->

Handle inaccessible, malformed or otherwise invalid roadmap files without crashing the desktop application.

**Requirements:**
- Report roadmap opening failures graphically while leaving the currently active roadmap unchanged.

**Work Steps:**
- [ ] 0.9.2.0.4 (a) Catch file opening failures
- [ ] 0.9.2.0.4 (b) Catch parser failures
- [ ] 0.9.2.0.4 (c) Display a Qt error dialog
- [ ] 0.9.2.0.4 (d) Include useful error information
- [ ] 0.9.2.0.4 (e) Leave the existing roadmap intact after a failed open
- [ ] 0.9.2.0.4 (f) Preserve diagnostic information for development

## 0.9.3 Create New Roadmaps
<!-- GitMap-ID: iwredsgv -->

#### 0.9.3.0.1 Create the Structure Dialog
<!-- GitMap-ID: urredslj -->

Create a separate Qt Designer dialog for configuring the structure of a new roadmap.

**Requirements:**
- Open a graphical structure configuration dialog before creating a new in-memory roadmap.

**Work Steps:**
- [ ] 0.9.3.0.1 (a) Create `structure_dialog.ui`
- [ ] 0.9.3.0.1 (b) Load the structure dialog from Python
- [ ] 0.9.3.0.1 (c) Connect Create Roadmap to the structure dialog
- [ ] 0.9.3.0.1 (d) Add structure controls
- [ ] 0.9.3.0.1 (e) Add the live example area
- [ ] 0.9.3.0.1 (f) Add Create and Cancel actions

#### 0.9.3.0.2 Configure Sections
<!-- GitMap-ID: vrredsli -->

Allow Sections to be enabled or disabled when creating a new roadmap.

**Requirements:**
- Allow new roadmaps to use or omit Sections and disable Section-dependent options when Sections are unavailable.

**Work Steps:**
- [ ] 0.9.3.0.2 (a) Add Use Sections
- [ ] 0.9.3.0.2 (b) Enable Section-dependent controls when Sections are selected
- [ ] 0.9.3.0.2 (c) Disable and grey Section-dependent controls when Sections are not selected
- [ ] 0.9.3.0.2 (d) Update the live structure example

#### 0.9.3.0.3 Configure Features
<!-- GitMap-ID: wrredslh -->

Allow Features to be enabled or disabled where the selected hierarchy supports them.

**Requirements:**
- Allow new roadmaps to use or omit Features while keeping unavailable Feature controls visible but disabled.

**Work Steps:**
- [ ] 0.9.3.0.3 (a) Add Use Features
- [ ] 0.9.3.0.3 (b) Enable Feature-dependent controls when Features are selected
- [ ] 0.9.3.0.3 (c) Disable and grey Feature-dependent controls when Features are unavailable
- [ ] 0.9.3.0.3 (d) Update the live structure example

#### 0.9.3.0.4 Configure Issue Placement
<!-- GitMap-ID: xrredslg -->

Control which enabled hierarchy levels may directly contain Issues.

**Requirements:**
- Allow only valid Issue placement choices based on the hierarchy selected for the new roadmap.

**Work Steps:**
- [ ] 0.9.3.0.4 (a) Add Allow Issues under Sections
- [ ] 0.9.3.0.4 (b) Add Allow Issues under Features
- [ ] 0.9.3.0.4 (c) Disable Section Issue placement when Sections are disabled
- [ ] 0.9.3.0.4 (d) Disable Feature Issue placement when Features are disabled
- [ ] 0.9.3.0.4 (e) Validate the final configuration
- [ ] 0.9.3.0.4 (f) Update the live example after each change

#### 0.9.3.0.5 Create the Baseball Parks Example
<!-- GitMap-ID: yrredslf -->

Show a live example of how the selected hierarchy organizes roadmap content.

**Requirements:**
- Display a rendered Baseball Parks example that updates to demonstrate the currently selected roadmap structure.

**Work Steps:**
- [ ] 0.9.3.0.5 (a) Add MLB Parks as the primary example Milestone
- [ ] 0.9.3.0.5 (b) Add American League and National League examples
- [ ] 0.9.3.0.5 (c) Add AL East and NL East when Features are enabled
- [ ] 0.9.3.0.5 (d) Add Camden Yards and Nationals Park Issues
- [ ] 0.9.3.0.5 (e) Add example Requirements and Work Steps
- [ ] 0.9.3.0.5 (f) Add a small NFL Stadiums example
- [ ] 0.9.3.0.5 (g) Update example numbering when the hierarchy changes

#### 0.9.3.0.6 Explain GitMap Hierarchy Levels
<!-- GitMap-ID: zrredsle -->

Explain how each GitMap hierarchy level can be used without prescribing a particular project structure. mandatory
project meanings. structure

**Requirements:**
- Explain Milestones, Sections, Features, Issues, Requirements and Work Steps as organizational concepts rather than

**Work Steps:**
- [ ] 0.9.3.0.6 (a) Explain Milestone as a major phase
- [ ] 0.9.3.0.6 (b) Explain Section as an area or subsystem
- [ ] 0.9.3.0.6 (c) Explain Feature as a feature or capability
- [ ] 0.9.3.0.6 (d) Explain Issue as a specific task
- [ ] 0.9.3.0.6 (e) Explain Requirements as what should be done
- [ ] 0.9.3.0.6 (f) Explain Work Steps as steps for doing it
- [ ] 0.9.3.0.6 (g) Explain that the Baseball Parks example demonstrates organization rather than a prescribed

#### 0.9.3.0.7 Create an Unsaved Roadmap Workspace
<!-- GitMap-ID: arredsld -->

Create the Roadmap model after structure selection without forcing the user to choose a file location.

**Requirements:**
- Create a usable in-memory roadmap immediately after structure setup without automatically creating a file.

**Work Steps:**
- [ ] 0.9.3.0.7 (a) Create the Roadmap model
- [ ] 0.9.3.0.7 (b) Apply the selected structure settings
- [ ] 0.9.3.0.7 (c) Populate the main workspace
- [ ] 0.9.3.0.7 (d) Mark the roadmap as unsaved
- [ ] 0.9.3.0.7 (e) Enable roadmap editing controls
- [ ] 0.9.3.0.7 (f) Verify no file is created automatically

## 0.9.4 Roadmap Navigation
<!-- GitMap-ID: jwredsgu -->

#### 0.9.4.0.1 Associate Tree Items With Model Objects
<!-- GitMap-ID: drredsla -->

Maintain a connection between displayed tree items and their underlying GitMap model objects.

**Requirements:**
- Resolve each editable graphical roadmap item back to the model object it represents.

**Work Steps:**
- [ ] 0.9.4.0.1 (a) Choose a safe model association mechanism
- [ ] 0.9.4.0.1 (b) Associate Milestone tree items
- [ ] 0.9.4.0.1 (c) Associate Section tree items
- [ ] 0.9.4.0.1 (d) Associate Feature tree items
- [ ] 0.9.4.0.1 (e) Associate Issue tree items
- [ ] 0.9.4.0.1 (f) Verify associations remain correct after tree refreshes

#### 0.9.4.0.2 Select Roadmap Items
<!-- GitMap-ID: erredslz -->

Allow users to select items in the graphical hierarchy for further actions.

**Requirements:**
- Track the selected roadmap object and enable only actions valid for its type and location.

**Work Steps:**
- [ ] 0.9.4.0.2 (a) Detect tree selection changes
- [ ] 0.9.4.0.2 (b) Resolve the selected model object
- [ ] 0.9.4.0.2 (c) Determine actions valid for the selected object
- [ ] 0.9.4.0.2 (d) Enable valid actions
- [ ] 0.9.4.0.2 (e) Disable invalid actions

#### 0.9.4.0.3 Open Items From the Tree
<!-- GitMap-ID: frredsly -->

Open editable roadmap items directly from the graphical roadmap hierarchy. workspace.

**Requirements:**
- Open the appropriate pop-out Item Editor when an editable roadmap item is double-clicked without replacing the main

**Work Steps:**
- [ ] 0.9.4.0.3 (a) Detect tree double-clicks
- [ ] 0.9.4.0.3 (b) Resolve the clicked model object
- [ ] 0.9.4.0.3 (c) Determine whether the object is editable
- [ ] 0.9.4.0.3 (d) Open the appropriate Item Editor
- [ ] 0.9.4.0.3 (e) Leave the main workspace open

## 0.9.5 Item Editors
<!-- GitMap-ID: kwredsgt -->

#### 0.9.5.0.1 Create the Item Editor Window
<!-- GitMap-ID: gsredskx -->

Create a reusable graphical window for editing roadmap items. open.

**Requirements:**
- Provide a pop-out Item Editor that operates on the selected in-memory roadmap object while leaving the main workspace

**Work Steps:**
- [ ] 0.9.5.0.1 (a) Create `item_editor.ui`
- [ ] 0.9.5.0.1 (b) Load the Item Editor from Python
- [ ] 0.9.5.0.1 (c) Associate the editor with a model object
- [ ] 0.9.5.0.1 (d) Add controls for applying changes
- [ ] 0.9.5.0.1 (e) Add Cancel or Close behavior

#### 0.9.5.0.2 Adapt the Editor to Item Type
<!-- GitMap-ID: hsredskw -->

Configure the Item Editor according to the type of roadmap object being edited.

**Requirements:**
- Show only editing controls that are valid for the selected Milestone, Section, Feature or Issue.

**Work Steps:**
- [ ] 0.9.5.0.2 (a) Detect the selected item type
- [ ] 0.9.5.0.2 (b) Configure the editor for Milestones
- [ ] 0.9.5.0.2 (c) Configure the editor for Sections
- [ ] 0.9.5.0.2 (d) Configure the editor for Features
- [ ] 0.9.5.0.2 (e) Configure the editor for Issues

#### 0.9.5.0.3 Edit Item Content
<!-- GitMap-ID: isredskv -->

Edit supported roadmap titles and descriptions. synchronizing GitHub.

**Requirements:**
- Apply valid title and description edits to the in-memory model and refresh the workspace without automatically

**Work Steps:**
- [ ] 0.9.5.0.3 (a) Populate the title control
- [ ] 0.9.5.0.3 (b) Populate the description control
- [ ] 0.9.5.0.3 (c) Validate edited values
- [ ] 0.9.5.0.3 (d) Apply approved changes to the model
- [ ] 0.9.5.0.3 (e) Refresh the roadmap tree
- [ ] 0.9.5.0.3 (f) Mark the roadmap as modified

#### 0.9.5.0.4 Edit Requirements
<!-- GitMap-ID: jsredsku -->

Manage an Issue's Requirements graphically.

**Requirements:**
- Allow Requirements to be viewed, added, edited and removed independently from Work Steps.

**Work Steps:**
- [ ] 0.9.5.0.4 (a) Display the existing Requirement
- [ ] 0.9.5.0.4 (b) Add a Requirement
- [ ] 0.9.5.0.4 (c) Edit Requirement text
- [ ] 0.9.5.0.4 (d) Remove a Requirement
- [ ] 0.9.5.0.4 (e) Refresh the roadmap tree

#### 0.9.5.0.5 Edit Work Steps
<!-- GitMap-ID: ksredskt -->

Manage an Issue's Work Steps graphically.

**Requirements:**
- Allow Work Steps to be added, edited, completed and removed while maintaining correct numbering and markers.

**Work Steps:**
- [ ] 0.9.5.0.5 (a) Display existing Work Steps
- [ ] 0.9.5.0.5 (b) Add a Work Step
- [ ] 0.9.5.0.5 (c) Assign the next Work Step marker
- [ ] 0.9.5.0.5 (d) Edit Work Step text
- [ ] 0.9.5.0.5 (e) Change Work Step completion state
- [ ] 0.9.5.0.5 (f) Remove a Work Step
- [ ] 0.9.5.0.5 (g) Renumber Work Step markers when required
- [ ] 0.9.5.0.5 (h) Refresh the roadmap tree

## 0.9.6 Add Insert and Delete Roadmap Items
<!-- GitMap-ID: lwredsgs -->

#### 0.9.6.0.1 Add Valid Child Items
<!-- GitMap-ID: lsredsks -->

Add new roadmap items beneath compatible parent items.

**Requirements:**
- Offer only child item types permitted by the selected parent and the active roadmap's hierarchy configuration.

**Work Steps:**
- [ ] 0.9.6.0.1 (a) Determine the selected parent type
- [ ] 0.9.6.0.1 (b) Read the roadmap hierarchy configuration
- [ ] 0.9.6.0.1 (c) Determine valid child types
- [ ] 0.9.6.0.1 (d) Present only valid choices
- [ ] 0.9.6.0.1 (e) Create the selected child using automatic numbering
- [ ] 0.9.6.0.1 (f) Refresh the roadmap tree

#### 0.9.6.0.2 Insert Items Between Existing Siblings
<!-- GitMap-ID: msredskr -->

Use GitMap's automatic numbering logic to insert items at a selected sibling position.

**Requirements:**
- Insert items between existing siblings without requiring the user to manually calculate or repair roadmap numbers.

**Work Steps:**
- [ ] 0.9.6.0.2 (a) Display valid insertion positions
- [ ] 0.9.6.0.2 (b) Let the user choose a position
- [ ] 0.9.6.0.2 (c) Use GitMap's sibling numbering logic
- [ ] 0.9.6.0.2 (d) Determine affected descendants
- [ ] 0.9.6.0.2 (e) Generate the numbering preview
- [ ] 0.9.6.0.2 (f) Apply the insertion only after approval

#### 0.9.6.0.3 Delete Roadmap Items Safely
<!-- GitMap-ID: nsredskq -->

Delete roadmap items while previewing any hierarchy or numbering consequences.

**Requirements:**
- Require confirmation of the item, descendant and numbering effects before applying a destructive roadmap deletion.

**Work Steps:**
- [ ] 0.9.6.0.3 (a) Select the item to delete
- [ ] 0.9.6.0.3 (b) Determine its descendants
- [ ] 0.9.6.0.3 (c) Determine resulting numbering changes
- [ ] 0.9.6.0.3 (d) Display the proposed deletion
- [ ] 0.9.6.0.3 (e) Display numbering changes
- [ ] 0.9.6.0.3 (f) Allow approval or cancellation
- [ ] 0.9.6.0.3 (g) Apply only the approved deletion
- [ ] 0.9.6.0.3 (h) Refresh the roadmap tree

## 0.9.7 Graphical Change Preview
<!-- GitMap-ID: mwredsgr -->

#### 0.9.7.0.1 Create the Roadmap Preview Window
<!-- GitMap-ID: osredskp -->

Create a separate graphical window for reviewing proposed roadmap changes.

**Requirements:**
- Display proposed changes in a scrollable pop-out preview while leaving the main roadmap workspace available.

**Work Steps:**
- [ ] 0.9.7.0.1 (a) Create `preview_dialog.ui`
- [ ] 0.9.7.0.1 (b) Load the preview interface from Python
- [ ] 0.9.7.0.1 (c) Add a scrollable change area
- [ ] 0.9.7.0.1 (d) Add Approve and Cancel actions
- [ ] 0.9.7.0.1 (e) Keep the main workspace available

#### 0.9.7.0.2 Display Before and After Changes
<!-- GitMap-ID: psredsko -->

Show the original and proposed state of affected roadmap items.

**Requirements:**
- Make hierarchy, numbering, additions, changes and removals understandable before a proposed operation is approved.

**Work Steps:**
- [ ] 0.9.7.0.2 (a) Collect the original state
- [ ] 0.9.7.0.2 (b) Collect the proposed state
- [ ] 0.9.7.0.2 (c) Display before values
- [ ] 0.9.7.0.2 (d) Display after values
- [ ] 0.9.7.0.2 (e) Highlight added items
- [ ] 0.9.7.0.2 (f) Highlight changed items
- [ ] 0.9.7.0.2 (g) Highlight removed items

#### 0.9.7.0.3 Cancel Previewed Changes
<!-- GitMap-ID: qsredskn -->

Restore the original roadmap state when the user cancels a proposed operation.

**Requirements:**
- Leave the roadmap exactly as it was before the proposed operation when a preview is cancelled.

**Work Steps:**
- [ ] 0.9.7.0.3 (a) Preserve the original state before generating changes
- [ ] 0.9.7.0.3 (b) Detect cancellation
- [ ] 0.9.7.0.3 (c) Restore original numbering
- [ ] 0.9.7.0.3 (d) Restore original hierarchy
- [ ] 0.9.7.0.3 (e) Refresh the roadmap tree
- [ ] 0.9.7.0.3 (f) Verify cancellation produces no saved changes

## 0.9.8 Save Roadmaps
<!-- GitMap-ID: nwredsgq -->

#### 0.9.8.0.1 Save an Existing Roadmap
<!-- GitMap-ID: rsredskm -->

Write changes to the active roadmap file.

**Requirements:**
- Save an existing roadmap to its current path while preserving valid GitMap Markdown and permanent identities.

**Work Steps:**
- [ ] 0.9.8.0.1 (a) Determine the active roadmap path
- [ ] 0.9.8.0.1 (b) Serialize the in-memory Roadmap
- [ ] 0.9.8.0.1 (c) Write the roadmap file
- [ ] 0.9.8.0.1 (d) Mark the roadmap as saved
- [ ] 0.9.8.0.1 (e) Update GUI status

#### 0.9.8.0.2 Save a New Roadmap
<!-- GitMap-ID: ssredskl -->

Choose a file location the first time an unsaved roadmap is saved.

**Requirements:**
- Prompt for a destination when saving an unsaved roadmap and make the successful destination its active file.

**Work Steps:**
- [ ] 0.9.8.0.2 (a) Detect that the roadmap has no active path
- [ ] 0.9.8.0.2 (b) Open a save dialog
- [ ] 0.9.8.0.2 (c) Write the roadmap to the selected path
- [ ] 0.9.8.0.2 (d) Store the selected path
- [ ] 0.9.8.0.2 (e) Change the roadmap from unsaved to saved

#### 0.9.8.0.3 Save As
<!-- GitMap-ID: tsredskk -->

Write the active roadmap to a user-selected new file.

**Requirements:**
- Save the current roadmap to a different path and make that path active after the operation succeeds.

**Work Steps:**
- [ ] 0.9.8.0.3 (a) Add Save As
- [ ] 0.9.8.0.3 (b) Open the Save As dialog
- [ ] 0.9.8.0.3 (c) Write the current roadmap to the selected path
- [ ] 0.9.8.0.3 (d) Update the active roadmap path
- [ ] 0.9.8.0.3 (e) Update the window state

#### 0.9.8.0.4 Track Modified Roadmaps
<!-- GitMap-ID: usredskj -->

Track whether the in-memory roadmap differs from its last saved state.

**Requirements:**
- Maintain and display an accurate modified state for the active roadmap.

**Work Steps:**
- [ ] 0.9.8.0.4 (a) Establish a modified-state flag
- [ ] 0.9.8.0.4 (b) Mark content edits as modified
- [ ] 0.9.8.0.4 (c) Mark structural changes as modified
- [ ] 0.9.8.0.4 (d) Clear modified state after a successful save
- [ ] 0.9.8.0.4 (e) Indicate modified state in the GUI

#### 0.9.8.0.5 Protect Unsaved Work
<!-- GitMap-ID: vsredski -->

Prevent unsaved changes from being silently discarded.

**Requirements:**
- Prompt before closing or replacing an active roadmap that contains unsaved changes.

**Work Steps:**
- [ ] 0.9.8.0.5 (a) Detect unsaved changes before replacement
- [ ] 0.9.8.0.5 (b) Offer Save
- [ ] 0.9.8.0.5 (c) Offer Discard
- [ ] 0.9.8.0.5 (d) Offer Cancel
- [ ] 0.9.8.0.5 (e) Stop the requested operation when Cancel is selected
- [ ] 0.9.8.0.5 (f) Verify application closing also protects unsaved work

## 0.9.9 Roadmap Settings
<!-- GitMap-ID: owredsgp -->

#### 0.9.9.0.1 Create Roadmap Settings
<!-- GitMap-ID: wsredskh -->

Create a graphical settings interface for viewing the active roadmap's configuration.

**Requirements:**
- Display supported configuration values from the active Roadmap model in a dedicated settings interface.

**Work Steps:**
- [ ] 0.9.9.0.1 (a) Create the settings interface
- [ ] 0.9.9.0.1 (b) Load settings from the active Roadmap
- [ ] 0.9.9.0.1 (c) Display numbering configuration
- [ ] 0.9.9.0.1 (d) Display hierarchy configuration
- [ ] 0.9.9.0.1 (e) Display hierarchy Issue title style

#### 0.9.9.0.2 Safely Modify Roadmap Settings
<!-- GitMap-ID: xsredskg -->

Allow supported settings to change without bypassing validation or preview protections.

**Requirements:**
- Validate settings changes and preview any changes that would alter existing roadmap numbering or hierarchy.

**Work Steps:**
- [ ] 0.9.9.0.2 (a) Determine editable settings
- [ ] 0.9.9.0.2 (b) Validate proposed settings
- [ ] 0.9.9.0.2 (c) Determine whether existing items are affected
- [ ] 0.9.9.0.2 (d) Generate a preview when required
- [ ] 0.9.9.0.2 (e) Apply only approved changes
- [ ] 0.9.9.0.2 (f) Refresh the workspace

## 0.9.10 GitHub Synchronization
<!-- GitMap-ID: pwredsgo -->

#### 0.9.10.0.1 Start Synchronization From the GUI
<!-- GitMap-ID: luredsis -->

Begin synchronization using a graphical action in the main workspace. validation or preview behavior.

**Requirements:**
- Start synchronization through the existing GitMap synchronization system without bypassing discovery, mapping,

**Work Steps:**
- [ ] 0.9.10.0.1 (a) Add the synchronization action
- [ ] 0.9.10.0.1 (b) Validate the active roadmap
- [ ] 0.9.10.0.1 (c) Start existing GitHub discovery
- [ ] 0.9.10.0.1 (d) Build the synchronization plan
- [ ] 0.9.10.0.1 (e) Pass the plan to graphical preview

#### 0.9.10.0.2 Display the Synchronization Preview
<!-- GitMap-ID: mvredshr -->

Display the existing GitMap synchronization preview graphically.

**Requirements:**
- Clearly distinguish added, changed, unchanged and removed GitHub items before synchronization approval.

**Work Steps:**
- [ ] 0.9.10.0.2 (a) Display summary counts
- [ ] 0.9.10.0.2 (b) Display added items
- [ ] 0.9.10.0.2 (c) Display changed items
- [ ] 0.9.10.0.2 (d) Display unchanged items when requested
- [ ] 0.9.10.0.2 (e) Display removed items
- [ ] 0.9.10.0.2 (f) Provide approval and cancellation

#### 0.9.10.0.3 Apply Only Approved GitHub Changes
<!-- GitMap-ID: nvredshq -->

Preserve GitMap's approval boundary when synchronization is controlled through the GUI.

**Requirements:**
- Allow only GitHub operations contained in the approved synchronization plan to modify existing GitHub state.

**Work Steps:**
- [ ] 0.9.10.0.3 (a) Preserve the approved synchronization plan
- [ ] 0.9.10.0.3 (b) Reject operations absent from the approved plan
- [ ] 0.9.10.0.3 (c) Apply approved creations
- [ ] 0.9.10.0.3 (d) Apply approved updates
- [ ] 0.9.10.0.3 (e) Apply approved closures
- [ ] 0.9.10.0.3 (f) Verify cancellation modifies nothing

#### 0.9.10.0.4 Display Synchronization Results
<!-- GitMap-ID: ovredshp -->

Show the outcome of synchronization inside the graphical interface. console.

**Requirements:**
- Display created, updated, closed, skipped and failed synchronization operations without requiring the development

**Work Steps:**
- [ ] 0.9.10.0.4 (a) Collect synchronization results
- [ ] 0.9.10.0.4 (b) Display created items
- [ ] 0.9.10.0.4 (c) Display updated items
- [ ] 0.9.10.0.4 (d) Display closed items
- [ ] 0.9.10.0.4 (e) Display skipped operations
- [ ] 0.9.10.0.4 (f) Display failures
- [ ] 0.9.10.0.4 (g) Refresh the roadmap workspace after synchronization

## 0.9.11 User Feedback and Error Handling
<!-- GitMap-ID: qwredsgn -->

#### 0.9.11.0.1 Use the Status Bar
<!-- GitMap-ID: pvredsho -->

Use the main window status bar for lightweight feedback.

**Requirements:**
- Report routine application status without unnecessarily interrupting the user's workflow.

**Work Steps:**
- [ ] 0.9.11.0.1 (a) Locate the Designer status bar
- [ ] 0.9.11.0.1 (b) Display roadmap-open status
- [ ] 0.9.11.0.1 (c) Display save status
- [ ] 0.9.11.0.1 (d) Display validation status
- [ ] 0.9.11.0.1 (e) Display synchronization status

#### 0.9.11.0.2 Display User-Friendly Errors
<!-- GitMap-ID: qvredshn -->

Present expected application failures as understandable graphical messages.

**Requirements:**
- Display useful graphical error messages while preserving more detailed diagnostic information for development.

**Work Steps:**
- [ ] 0.9.11.0.2 (a) Create a common GUI error-display helper
- [ ] 0.9.11.0.2 (b) Handle roadmap file errors
- [ ] 0.9.11.0.2 (c) Handle parser errors
- [ ] 0.9.11.0.2 (d) Handle validation errors
- [ ] 0.9.11.0.2 (e) Handle save errors
- [ ] 0.9.11.0.2 (f) Handle GitHub errors
- [ ] 0.9.11.0.2 (g) Preserve useful diagnostic logging

## 0.9.12 Desktop Application Behavior
<!-- GitMap-ID: rwredsgm -->

#### 0.9.12.0.1 Add Standard Keyboard Shortcuts
<!-- GitMap-ID: rvredshm -->

Provide familiar keyboard shortcuts for common desktop actions.

**Requirements:**
- Use standard desktop shortcuts for common GitMap actions where they do not conflict with application behavior.

**Work Steps:**
- [ ] 0.9.12.0.1 (a) Add Ctrl+O for Open
- [ ] 0.9.12.0.1 (b) Add Ctrl+S for Save
- [ ] 0.9.12.0.1 (c) Add a Save As shortcut
- [ ] 0.9.12.0.1 (d) Add appropriate new-roadmap navigation
- [ ] 0.9.12.0.1 (e) Verify shortcuts do not conflict with Item Editors

#### 0.9.12.0.2 Support Normal Desktop Window Behavior
<!-- GitMap-ID: svredshl -->

Manage the relationship between the main workspace and GitMap's pop-out windows. main workspace.

**Requirements:**
- Allow editors, previews and dialogs to behave as normal child windows without unexpectedly closing or replacing the

**Work Steps:**
- [ ] 0.9.12.0.2 (a) Establish ownership for dialogs
- [ ] 0.9.12.0.2 (b) Establish ownership for Item Editors
- [ ] 0.9.12.0.2 (c) Establish ownership for Preview windows
- [ ] 0.9.12.0.2 (d) Test multiple simultaneous Item Editors
- [ ] 0.9.12.0.2 (e) Test closing individual child windows
- [ ] 0.9.12.0.2 (f) Test closing the main application

## 0.9.13 Preserve the GitMap Core Architecture
<!-- GitMap-ID: swredsgl -->

#### 0.9.13.0.1 Reuse the Existing Parser
<!-- GitMap-ID: tvredshk -->

Use GitMap's established parser for GUI roadmap loading.

**Requirements:**
- Use the existing GitMap parser as the authoritative parser for roadmaps opened by the desktop interface.

**Work Steps:**
- [ ] 0.9.13.0.1 (a) Route GUI file loading through `parse_roadmap`
- [ ] 0.9.13.0.1 (b) Preserve parser behavior shared with the CLI
- [ ] 0.9.13.0.1 (c) Verify representative existing roadmaps

#### 0.9.13.0.2 Reuse the Existing Model
<!-- GitMap-ID: uvredshj -->

Use the existing GitMap model as the application's roadmap state.

**Requirements:**
- Keep the existing Roadmap model and its hierarchy objects authoritative for GUI state and editing.

**Work Steps:**
- [ ] 0.9.13.0.2 (a) Store the active Roadmap model
- [ ] 0.9.13.0.2 (b) Read hierarchy data from existing model classes
- [ ] 0.9.13.0.2 (c) Apply GUI edits to existing model classes
- [ ] 0.9.13.0.2 (d) Avoid introducing duplicate GUI-only roadmap models

#### 0.9.13.0.3 Reuse Automatic Numbering
<!-- GitMap-ID: vvredshi -->

Use GitMap's existing automatic numbering system for graphical roadmap changes.

**Requirements:**
- Route GUI creation, insertion and renumbering operations through the existing automatic numbering behavior.

**Work Steps:**
- [ ] 0.9.13.0.3 (a) Reuse sibling-number calculation
- [ ] 0.9.13.0.3 (b) Reuse insertion numbering
- [ ] 0.9.13.0.3 (c) Reuse descendant renumbering
- [ ] 0.9.13.0.3 (d) Preserve Work Step marker behavior
- [ ] 0.9.13.0.3 (e) Verify numbering results match CLI behavior

#### 0.9.13.0.4 Reuse Validation
<!-- GitMap-ID: wvredshh -->

Use existing GitMap validation before applying graphical roadmap changes.

**Requirements:**
- Apply the existing roadmap validation rules to GUI operations rather than creating weaker GUI-specific rules.

**Work Steps:**
- [ ] 0.9.13.0.4 (a) Validate edited roadmaps
- [ ] 0.9.13.0.4 (b) Validate hierarchy changes
- [ ] 0.9.13.0.4 (c) Detect duplicate numbers
- [ ] 0.9.13.0.4 (d) Detect invalid structures
- [ ] 0.9.13.0.4 (e) Display validation failures graphically

#### 0.9.13.0.5 Reuse GitHub Mapping
<!-- GitMap-ID: bvredshc -->

Use GitMap's existing identity, mapping and synchronization protections from the desktop GUI. when synchronizing through
the GUI.

**Requirements:**
- Preserve existing GitHub mapping, permanent identity, roadmap-specific searching, hierarchy and approval protections

**Work Steps:**
- [ ] 0.9.13.0.5 (a) Route GUI synchronization through existing GitHub mapping
- [ ] 0.9.13.0.5 (b) Preserve permanent GitMap IDs
- [ ] 0.9.13.0.5 (c) Preserve roadmap-specific searching
- [ ] 0.9.13.0.5 (d) Preserve parent and child GitHub relationships
- [ ] 0.9.13.0.5 (e) Preserve Issue identity during renumbering
- [ ] 0.9.13.0.5 (f) Preserve approval before modifying existing GitHub items

## 0.9.14 GUI Integration Testing
<!-- GitMap-ID: twredsgk -->

#### 0.9.14.0.1 Test Existing Roadmaps
<!-- GitMap-ID: cvredshb -->

Verify that existing roadmap files work correctly in the desktop interface.

**Requirements:**
- Open and display representative existing GitMap roadmaps without changing their intended hierarchy or content.

**Work Steps:**
- [ ] 0.9.14.0.1 (a) Test a roadmap using Sections and Features
- [ ] 0.9.14.0.1 (b) Test a featureless roadmap
- [ ] 0.9.14.0.1 (c) Test Issues directly beneath Sections
- [ ] 0.9.14.0.1 (d) Test Issues directly beneath Milestones
- [ ] 0.9.14.0.1 (e) Verify Requirements
- [ ] 0.9.14.0.1 (f) Verify Work Steps

#### 0.9.14.0.2 Test New Roadmap Creation
<!-- GitMap-ID: dvredsha -->

Verify each supported new-roadmap structure configuration.

**Requirements:**
- Create valid in-memory roadmaps for every hierarchy configuration offered by the structure dialog.

**Work Steps:**
- [ ] 0.9.14.0.2 (a) Test Sections with Features
- [ ] 0.9.14.0.2 (b) Test Sections without Features
- [ ] 0.9.14.0.2 (c) Test supported no-Section structures
- [ ] 0.9.14.0.2 (d) Test Issue placement choices
- [ ] 0.9.14.0.2 (e) Verify the resulting roadmap model

#### 0.9.14.0.3 Test Editing and Numbering
<!-- GitMap-ID: evredshz -->

Verify graphical editing preserves GitMap's automatic numbering rules. logic.

**Requirements:**
- Produce the same valid hierarchy and numbering results through GUI editing that GitMap produces through its existing

**Work Steps:**
- [ ] 0.9.14.0.3 (a) Add roadmap items
- [ ] 0.9.14.0.3 (b) Insert between siblings
- [ ] 0.9.14.0.3 (c) Delete roadmap items
- [ ] 0.9.14.0.3 (d) Verify descendant renumbering
- [ ] 0.9.14.0.3 (e) Verify Work Step numbering and markers
- [ ] 0.9.14.0.3 (f) Cancel a numbering preview and verify rollback

#### 0.9.14.0.4 Test Saving and Unsaved Changes
<!-- GitMap-ID: fvredshy -->

Verify roadmap files can be safely created and modified through the GUI.

**Requirements:**
- Preserve roadmap content through Save, Save As, reopening and unsaved-change protection.

**Work Steps:**
- [ ] 0.9.14.0.4 (a) Save a new roadmap
- [ ] 0.9.14.0.4 (b) Save changes to an existing roadmap
- [ ] 0.9.14.0.4 (c) Test Save As
- [ ] 0.9.14.0.4 (d) Reopen each saved roadmap
- [ ] 0.9.14.0.4 (e) Verify permanent GitMap IDs
- [ ] 0.9.14.0.4 (f) Verify unsaved-change protection

#### 0.9.14.0.5 Test GitHub Synchronization
<!-- GitMap-ID: gwredsgx -->

Verify that graphical synchronization preserves all existing GitMap protections. workflow.

**Requirements:**
- Produce the same protected GitHub synchronization results from the GUI as from the established GitMap synchronization

**Work Steps:**
- [ ] 0.9.14.0.5 (a) Preview synchronization containing new items
- [ ] 0.9.14.0.5 (b) Preview synchronization containing changed items
- [ ] 0.9.14.0.5 (c) Preview synchronization containing removed items
- [ ] 0.9.14.0.5 (d) Cancel synchronization and verify GitHub remains unchanged
- [ ] 0.9.14.0.5 (e) Approve synchronization
- [ ] 0.9.14.0.5 (f) Verify only approved operations occurred
- [ ] 0.9.14.0.5 (g) Verify GitMap IDs remain associated with the correct GitHub Issues
- [ ] 0.9.14.0.5 (h) Verify GitHub parent and child relationships remain correct

# 0.10 Fresh Roadmap Import and Validation

## 0.10.1 Fresh Roadmap Identity
<!-- GitMap-ID: kdvnvzsp -->

#### 0.10.1.0.1 Trace import and validation order
<!-- GitMap-ID: rigogvvg -->

Identify where parsing, ID assignment, validation, saving, and sync preparation occur. Reproduce the HouseCall import
failure before changing behavior.

**Requirements:**
- Identify why a fresh roadmap without IDs is rejected.
- Identify common GUI and CLI preparation responsibilities.
- Reuse existing identity services and consolidate duplicate preparation logic where practical.

**Work Steps:**
- [ ] 0.10.1.0.1 (a) Reproduce the failure with the HouseCall roadmap.
- [ ] 0.10.1.0.1 (b) Trace import and sync preparation calls.
- [ ] 0.10.1.0.1 (c) Establish the correct order for normalization, validation, and persistence.

#### 0.10.1.0.2 Assign missing IDs before identity validation
<!-- GitMap-ID: qkfdkusy -->

Missing IDs are expected on newly created roadmaps. Assign permanent IDs before checks that require them.

**Requirements:**
- Assign unique eight-letter, letters-only IDs to items requiring identity.
- Preserve all existing valid IDs.
- Report malformed or duplicate existing IDs rather than silently replacing them.
- Use the shared ID allocator rather than introduce another implementation.

**Work Steps:**
- [ ] 0.10.1.0.2 (a) Inspect the existing allocator and identity preparation service.
- [ ] 0.10.1.0.2 (b) Separate missing-ID normalization from invalid-ID checks.
- [ ] 0.10.1.0.2 (c) Connect preparation to the applicable GUI and CLI workflows.

#### 0.10.1.0.3 Persist generated IDs safely
<!-- GitMap-ID: hosraduk -->

Store assigned IDs in the roadmap before syncing so reopening and repeated syncs retain identity.

**Requirements:**
- Save generated IDs before GitHub synchronization begins.
- Preserve content, numbering, completion status, and representation settings.
- Stop synchronization with an actionable message if saving fails.
- Respect unsaved user edits through the existing save workflow.

**Work Steps:**
- [ ] 0.10.1.0.3 (a) Reuse roadmap serialization and modified-state handling.
- [ ] 0.10.1.0.3 (b) Connect ID persistence to the existing save workflow.
- [ ] 0.10.1.0.3 (c) Verify IDs remain unchanged after reopening and repeated preparation.

## 0.10.2 Usable Validation Feedback
<!-- GitMap-ID: iutqqcub -->

#### 0.10.2.0.1 Display long reports in a scrollable error dialog
<!-- GitMap-ID: njajsipf -->

Replace oversized error popups with a bounded window that remains usable for large reports.

**Requirements:**
- Show a short summary and error count.
- Provide scrollable, selectable details and Copy Details.
- Keep dismissal controls visible regardless of report length.
- Extend the shared error display rather than duplicate error handling.

**Work Steps:**
- [ ] 0.10.2.0.1 (a) Inspect the shared error display and its callers.
- [ ] 0.10.2.0.1 (b) Add the bounded details view and clipboard action.
- [ ] 0.10.2.0.1 (c) Check a report containing hundreds of errors.

#### 0.10.2.0.2 Make validation errors actionable
<!-- GitMap-ID: wugibwwl -->

Help users locate and correct failures without reading a wall of repeated messages.

**Requirements:**
- Include item number or title and the affected field when available.
- Include file location or line number when available.
- Group repeated error types while retaining every affected item in full details.
- Distinguish blocking errors from warnings.

**Work Steps:**
- [ ] 0.10.2.0.2 (a) Review validation result structures.
- [ ] 0.10.2.0.2 (b) Add available context and correction guidance.
- [ ] 0.10.2.0.2 (c) Build summaries without losing detailed failures.

## 0.10.3 Workflow Verification
<!-- GitMap-ID: zlabmlpl -->

#### 0.10.3.0.1 Verify identity handling and fresh-roadmap synchronization
<!-- GitMap-ID: qaafyhdi -->

Use the HouseCall roadmap as a regression case for AI-created input.

**Requirements:**
- Cover no IDs, some missing IDs, and all valid IDs.
- Cover malformed IDs, duplicate IDs, and save failures.
- Repeated preparation must not regenerate IDs.
- The HouseCall test file parses into 10 milestones, 33 sections, and 161 ordinary issues.
- Check configured section representation separately from ordinary issue counts.
- Re-syncing unchanged input must not create duplicate GitHub items.

**Work Steps:**
- [ ] 0.10.3.0.1 (a) Add focused identity-preparation regression coverage.
- [ ] 0.10.3.0.1 (b) Import, review, and save the HouseCall test file.
- [ ] 0.10.3.0.1 (c) Check the corresponding CLI preparation path.
- [ ] 0.10.3.0.1 (d) Sync to a test repository and inspect the results.
- [ ] 0.10.3.0.1 (e) Repeat sync and confirm identity preservation.

# 0.11 GitMap Custom GPT

## 0.11.1 Roadmap Format Contract
<!-- GitMap-ID: cedtwafk -->

#### 0.11.1.0.1 Establish the authoritative generation specification
<!-- GitMap-ID: fyicbcta -->

Give the GPT one maintained source of truth for the current roadmap format. work steps.

**Requirements:**
- Document metadata, representation settings, hierarchy, numbering, completion status, descriptions, requirements, and
- Document supported layouts with and without sections and features.
- Omit IDs for new items and preserve existing IDs when editing uploaded roadmaps.
- Never fabricate GitHub issue numbers or mark unverified work complete.

**Work Steps:**
- [ ] 0.11.1.0.1 (a) Reconcile documentation with the parser and serializer.
- [ ] 0.11.1.0.1 (b) Remove or clearly mark obsolete examples.
- [ ] 0.11.1.0.1 (c) Prepare a concise GPT generation specification.

#### 0.11.1.0.2 Create validated example roadmaps
<!-- GitMap-ID: hzoeqxpx -->

Provide examples the GPT can follow consistently.

**Requirements:**
- Include a fresh roadmap without IDs.
- Include direct issues under sections and a layout with features.
- Include meaningful descriptions, measurable requirements, and concrete work steps.
- Each example must pass GitMap preparation and validation.

**Work Steps:**
- [ ] 0.11.1.0.2 (a) Create representative examples.
- [ ] 0.11.1.0.2 (b) Import and validate every example.
- [ ] 0.11.1.0.2 (c) Resolve inconsistent format rules exposed by testing.

## 0.11.2 GPT Configuration
<!-- GitMap-ID: ourswawt -->

#### 0.11.2.0.1 Write planning and roadmap editing instructions
<!-- GitMap-ID: trvuejre -->

Define how the assistant creates useful plans and updates existing roadmaps.

**Requirements:**
- Ask only questions needed to establish goals, scope, and structure.
- Produce actionable issue titles, descriptions, requirements, and work steps.
- Requirements describe outcomes; work steps describe implementation actions.
- Preserve unrelated content and existing IDs during edits.
- Preserve numbering unless the requested change requires renumbering.
- Distinguish proposed scope from recovered historical decisions.

**Work Steps:**
- [ ] 0.11.2.0.1 (a) Draft project-planning instructions.
- [ ] 0.11.2.0.1 (b) Add fresh-generation, section-expansion, and editing instructions.
- [ ] 0.11.2.0.1 (c) Review representative user requests against the instructions.

#### 0.11.2.0.2 Configure the custom GPT
<!-- GitMap-ID: zgzmucpg -->

Build the assistant with the format specification, examples, and planning instructions.

**Requirements:**
- Provide a clear name, description, and conversation starters.
- Include the authoritative format specification and validated examples.
- Configure downloadable roadmap output where supported.
- Generation must not require GitHub credentials, Home Assistant tokens, or GitHub write access.

**Work Steps:**
- [ ] 0.11.2.0.2 (a) Configure the GPT and reference materials.
- [ ] 0.11.2.0.2 (b) Add starters for creating a roadmap and expanding a section.
- [ ] 0.11.2.0.2 (c) Verify generated files can be downloaded and opened.

## 0.11.3 Acceptance and Handoff
<!-- GitMap-ID: ayuwolcg -->

#### 0.11.3.0.1 Test generated and edited roadmaps in GitMap
<!-- GitMap-ID: kavyyytz -->

Evaluate the assistant through the actual creation, import, review, and sync workflow.

**Requirements:**
- Import fresh generated output without manually adding IDs.
- Exercise supported hierarchy layouts.
- Expand an identified roadmap section without changing existing IDs.
- Validate downloaded output locally before synchronization.
- Correct recurring format failures.

**Work Steps:**
- [ ] 0.11.3.0.1 (a) Run fresh-generation scenarios.
- [ ] 0.11.3.0.1 (b) Run existing-roadmap editing scenarios.
- [ ] 0.11.3.0.1 (c) Validate output and complete a test-repository sync.

#### 0.11.3.0.2 Document and share the plug-and-play workflow
<!-- GitMap-ID: nzcduzjn -->

Make the assistant discoverable and maintain alignment with GitMap's format.

**Requirements:**
- Document describe project, download roadmap, open GitMap, review, and sync.
- Provide the GPT link through the chosen sharing setting.
- Explain that GitMap owns IDs, validation, and synchronization.
- Document how instructions and examples are updated when the format changes.

**Work Steps:**
- [ ] 0.11.3.0.2 (a) Write concise onboarding instructions.
- [ ] 0.11.3.0.2 (b) Choose the sharing setting and publish the GPT accordingly.
- [ ] 0.11.3.0.2 (c) Add the link and maintenance guidance to GitMap documentation.

# 0.12 Plan GitMap 27

## 0.12.1 Project Direction
<!-- GitMap-ID: tdloakln -->

#### 0.12.1.0.1 Define Z’s vision and ownership
<!-- GitMap-ID: dbveyepr -->

Work with Zachary to decide what GitMap 27 should be and which parts he wants to build himself.

**Requirements:**
- Record intended users, devices, and primary use cases.
- Give Z meaningful ownership of product and coding decisions.
- Treat a native iOS app as his current preference, subject to discussion.
- Use GitMap 27 as the working project name.

**Work Steps:**
- [ ] 0.12.1.0.1 (a) Brainstorm directly with Z.
- [ ] 0.12.1.0.1 (b) Sketch his ideal first workflow.
- [ ] 0.12.1.0.1 (c) Record agreed goals and unresolved questions.

#### 0.12.1.0.2 Define the first usable edition
<!-- GitMap-ID: npjrsadh -->

Separate the eventual full app from a small first version that proves the approach.

**Requirements:**
- Identify a complete first user workflow rather than an arbitrary collection of screens.
- Compare roadmap browsing, local editing, work-step updates, review, and GitHub sync as possible starting scope.
- Explicitly defer capabilities outside the first version.
- Do not assume the first version is read-only or a web app without Z’s agreement.

**Work Steps:**
- [ ] 0.12.1.0.2 (a) List desired capabilities and dependencies.
- [ ] 0.12.1.0.2 (b) Choose one achievable end-to-end workflow with Z.
- [ ] 0.12.1.0.2 (c) Record first-version acceptance criteria and deferred scope.

## 0.12.2 Development Environment and Language
<!-- GitMap-ID: rkmynoak -->

#### 0.12.2.0.1 Evaluate languages and app approaches
<!-- GitMap-ID: hllyvfpk -->

Choose a development approach with Z based on native app goals, existing code, and available equipment.

**Requirements:**
- Compare Swift/SwiftUI with relevant alternatives only when they fit the agreed goals.
- Account for Windows and iPad as current equipment.
- Distinguish reuse of Python implementations from reuse of format, models, and domain rules.
- Document the reasons for the selected approach and remaining constraints.

**Work Steps:**
- [ ] 0.12.2.0.1 (a) Identify which languages and tools Z wants to use.
- [ ] 0.12.2.0.1 (b) Compare candidate approaches against the agreed first workflow.
- [ ] 0.12.2.0.1 (c) Select a provisional approach for a small feasibility experiment.

#### 0.12.2.0.2 Prove the Windows-to-iPad coding workflow
<!-- GitMap-ID: mevezbja -->

Test whether Z can do substantial text editing on Windows and build and run the app on his iPad.

**Requirements:**
- Verify a minimal editable project on the actual devices.
- Test shared-folder transfer or synchronization rather than assume it works.
- Confirm whether whole-project editing works or source-file import is required.
- Identify where compiler errors, previews, and debugging are available.
- Avoid simultaneous edits that overwrite changes.

**Work Steps:**
- [ ] 0.12.2.0.2 (a) Create a minimal app using the chosen iPad-capable tool.
- [ ] 0.12.2.0.2 (b) Change one source file on Windows and transfer or sync it.
- [ ] 0.12.2.0.2 (c) Run the changed app on iPad and repeat the round trip.
- [ ] 0.12.2.0.2 (d) Document reliable steps and limitations.

#### 0.12.2.0.3 Decide whether additional tooling is necessary
<!-- GitMap-ID: hpowrouw -->

Identify any equipment or service requirements before substantial development begins.

**Requirements:**
- Distinguish requirements for the prototype, full development, device installation, and distribution.
- Evaluate Mac access only if the chosen workflow requires it.
- Treat macOS emulation as an unproven option rather than the development foundation.
- Do not commit to purchases, paid services, or accounts during planning.

**Work Steps:**
- [ ] 0.12.2.0.3 (a) List toolchain limitations found by the experiment.
- [ ] 0.12.2.0.3 (b) Investigate practical alternatives for unresolved limitations.
- [ ] 0.12.2.0.3 (c) Record required versus optional resources.

## 0.12.3 Existing GitMap Reuse
<!-- GitMap-ID: uhkpswjd -->

#### 0.12.3.0.1 Audit the reusable Python core
<!-- GitMap-ID: qktcqhmh -->

Determine which current GitMap responsibilities can be reused and which depend on the desktop GUI.

**Requirements:**
- Inventory parser, serializer, models, ID allocation, numbering, validation, comparison, and GitHub synchronization.
- Identify PySide6 imports and GUI assumptions in candidate core services.
- Flag duplicate implementations and shared responsibilities worth consolidating.
- Report findings without committing to a full port or backend rewrite.

**Work Steps:**
- [ ] 0.12.3.0.1 (a) Trace dependencies for the selected first workflow.
- [ ] 0.12.3.0.1 (b) Classify candidate modules as reusable, adaptable, or desktop-specific.
- [ ] 0.12.3.0.1 (c) Document the smallest necessary core changes.

#### 0.12.3.0.2 Establish the shared roadmap compatibility contract
<!-- GitMap-ID: ervbjaak -->

Make desktop and mobile editions agree on roadmap meaning and permanent identity.

**Requirements:**
- Use the current GitMap format as the source of truth.
- Cover hierarchy, numbering, IDs, completion status, representation settings, requirements, and work steps.
- Preserve existing IDs during mobile edits.
- Identify unsupported constructs explicitly and avoid silently dropping them.
- Distinguish original GitHub issue numbers from GitMap IDs.

**Work Steps:**
- [ ] 0.12.3.0.2 (a) Review parser and serializer behavior using representative files.
- [ ] 0.12.3.0.2 (b) Document the shared format and identity rules.
- [ ] 0.12.3.0.2 (c) Collect compatibility fixtures for both editions.

#### 0.12.3.0.3 Choose local processing or a shared backend
<!-- GitMap-ID: mjncjtpc -->

Decide how GitMap 27 will use existing functionality.

**Requirements:**
- Compare an independent native implementation with an app using a Python backend.
- Consider offline use, network access, deployment, latency, authentication, and maintenance.
- If porting logic, identify how compatibility will be maintained.
- If using a backend, define which responsibilities stay on the server.
- Do not build both architectures before selecting one.

**Work Steps:**
- [ ] 0.12.3.0.3 (a) Sketch both options using the first workflow.
- [ ] 0.12.3.0.3 (b) Evaluate tradeoffs with Z.
- [ ] 0.12.3.0.3 (c) Record a provisional decision and criteria that would justify changing it.

## 0.12.4 Product and Data Design
<!-- GitMap-ID: hfrgtnck -->

#### 0.12.4.0.1 Design touch-friendly roadmap navigation
<!-- GitMap-ID: nhktamoa -->

Sketch an interface that suits phone and iPad use rather than reproducing every desktop panel.

**Requirements:**
- Cover navigation through milestones, sections, optional features, issues, and work steps.
- Keep important actions discoverable and usable with touch.
- Consider long titles, large roadmaps, search, and return navigation.
- Include keyboard use on iPad where useful.
- Use sketches and a small prototype to test the design.

**Work Steps:**
- [ ] 0.12.4.0.1 (a) Sketch the selected workflow with Z.
- [ ] 0.12.4.0.1 (b) Try representative HouseCall and GitMap content.
- [ ] 0.12.4.0.1 (c) Refine navigation based on the prototype.

#### 0.12.4.0.2 Define file ownership and safe editing
<!-- GitMap-ID: nzgtfwmw -->

Plan how the app opens, saves, and exchanges roadmaps.

**Requirements:**
- Identify whether files are local, cloud-backed, or server-managed.
- Define Save, Save As, unsaved edits, and reopening behavior where applicable.
- Prevent silent overwrite when desktop and mobile edits conflict.
- Preserve roadmap data and IDs through a save round trip.
- Treat cloud file synchronization separately from GitHub synchronization.

**Work Steps:**
- [ ] 0.12.4.0.2 (a) Map file movement between desktop, cloud folder, and app.
- [ ] 0.12.4.0.2 (b) Choose a first-version save and conflict policy.
- [ ] 0.12.4.0.2 (c) Specify recovery behavior for failed writes or transfers.

#### 0.12.4.0.3 Plan GitHub access and review before sync
<!-- GitMap-ID: nxhscoia -->

Determine when and how GitHub integration belongs in GitMap 27.

**Requirements:**
- Decide whether GitHub sync is first-version or later scope.
- If included, choose an authentication approach and appropriate credential storage.
- Keep secrets out of roadmap files, source code, and logs.
- Provide a review of intended changes before applying them.
- Identify required shared sync behavior and failure handling.

**Work Steps:**
- [ ] 0.12.4.0.3 (a) Describe the intended account and repository workflow.
- [ ] 0.12.4.0.3 (b) Investigate authentication options for the selected architecture.
- [ ] 0.12.4.0.3 (c) Define review, cancellation, progress, and error expectations.

## 0.12.5 Feasibility Prototype
<!-- GitMap-ID: jfmcfsmp -->

#### 0.12.5.0.1 Build one end-to-end proof with Z
<!-- GitMap-ID: mkybyseo -->

Implement the smallest experiment that validates the selected language, environment, and reuse approach.

**Requirements:**
- Use real roadmap content rather than only hard-coded sample cards.
- Load and display enough hierarchy to exercise the chosen approach.
- If editing is in scope, change one item and verify a safe save round trip.
- If server-backed, exercise one actual core operation through the proposed interface.
- Prototype work must be understandable and editable by Z.

**Work Steps:**
- [ ] 0.12.5.0.1 (a) Choose the proof’s acceptance criteria.
- [ ] 0.12.5.0.1 (b) Have Z implement the interface with support as needed.
- [ ] 0.12.5.0.1 (c) Connect the selected data path and test on his iPad.
- [ ] 0.12.5.0.1 (d) Record blockers, findings, and reusable prototype code.

#### 0.12.5.0.2 Check compatibility and practical usability
<!-- GitMap-ID: kwtidjpf -->

Use the prototype to decide whether the approach is ready for its own development roadmap.

**Requirements:**
- Verify that existing roadmap identities are preserved.
- Try a small fixture and the larger HouseCall roadmap.
- Check usability on the intended phone and iPad sizes where devices or tools permit.
- Record unsupported behavior and unresolved architecture risks.
- Do not label the prototype a complete mobile edition.

**Work Steps:**
- [ ] 0.12.5.0.2 (a) Run the agreed compatibility checks.
- [ ] 0.12.5.0.2 (b) Have Z try the primary workflow.
- [ ] 0.12.5.0.2 (c) Resolve critical feasibility blockers or document the required pivot.

## 0.12.6 Separate Project Handoff
<!-- GitMap-ID: wrvuinez -->

#### 0.12.6.0.1 Create the GitMap 27 roadmap and project boundaries
<!-- GitMap-ID: izfvbvhw -->

Move full app development into its own tree once the direction is proven.

**Requirements:**
- Create an independent milestone and version sequence for GitMap 27.
- Carry over first-version goals, acceptance criteria, and deferred scope.
- Keep changes to shared GitMap core tracked in the main roadmap.
- Decide whether a separate repository or a shared repository best fits the chosen architecture.
- Give Z ownership of suitable app implementation issues.

**Work Steps:**
- [ ] 0.12.6.0.1 (a) Review feasibility findings and finalize the initial direction.
- [ ] 0.12.6.0.1 (b) Create the GitMap 27 roadmap using GitMap-compatible structure.
- [ ] 0.12.6.0.1 (c) Record repository boundaries and cross-project dependencies.
- [ ] 0.12.6.0.1 (d) Assign or identify Z-owned work with him.

#### 0.12.6.0.2 Complete the planning milestone
<!-- GitMap-ID: pcooinoi -->

Close 0.14 when there is enough evidence to start the separate project.

**Requirements:**
- Z has participated in the scope, language, and architecture choices.
- The development workflow has run successfully on available equipment or required access is identified.
- At least one end-to-end feasibility proof has been evaluated.
- The reuse and compatibility strategy is documented.
- GitMap 27 has its own actionable first-version roadmap.
- Completion of 0.14 does not imply the full iOS app is complete.

**Work Steps:**
- [ ] 0.12.6.0.2 (a) Review outcomes and unresolved questions with Z.
- [ ] 0.12.6.0.2 (b) Confirm the handoff criteria.
- [ ] 0.12.6.0.2 (c) Continue implementation under GitMap 27’s own tree.

# 0.13 New Bugs

## 0.13.1 Logs
<!-- GitMap-ID: awredsgd -->

#### 0.13.1.0.1 Have the logs go to same location
<!-- GitMap-ID: brredslc -->

or at least similar

## 0.13.2 Figure out 544 issues
<!-- GitMap-ID: uwredsgj -->

## 0.13.3 Numbering and Editing
<!-- GitMap-ID: xefonibo -->

#### 0.13.3.0.1 Large Numbering Dialog
<!-- GitMap-ID: vwredsgi -->

#### 0.13.3.0.2 Legacy Work Step Numbers
<!-- GitMap-ID: wwredsgh -->

#### 0.13.3.0.3 Restore Work Steps on Cancel
<!-- GitMap-ID: xwredsgg -->

## 0.13.4 Synchronization Bugs
<!-- GitMap-ID: begaqufi -->

#### 0.13.4.0.1 Remote Change Detection
<!-- GitMap-ID: ywredsgf -->

#### 0.13.4.0.2 Validate Label Length
<!-- GitMap-ID: zwredsge -->

# 0.14 Testing

## 0.14.1 Automated Testing
<!-- GitMap-ID: xvredshg -->

#### 0.14.1.0.1 Test Roadmap Parsing
<!-- GitMap-ID: ysredskf -->

Test conversion of Markdown roadmaps into GitMap project data.

**Requirements:**
- Test conversion of Markdown roadmaps into GitMap project data.

**Work Steps:**
- [ ] 0.14.1.0.1 (a) Test milestones
- [ ] 0.14.1.0.1 (b) Test Sections
- [ ] 0.14.1.0.1 (c) Test issues
- [ ] 0.14.1.0.1 (d) Test sub-issues
- [ ] 0.14.1.0.1 (e) Test descriptions and requirements

#### 0.14.1.0.2 Test Roadmap Validation
<!-- GitMap-ID: zsredske -->

Test detection of invalid roadmap structures.

**Requirements:**
- Test detection of invalid roadmap structures.

**Work Steps:**
- [ ] 0.14.1.0.2 (a) Test malformed hierarchy
- [ ] 0.14.1.0.2 (b) Test duplicate numbering
- [ ] 0.14.1.0.2 (c) Test invalid parent relationships
- [ ] 0.14.1.0.2 (d) Test useful validation messages

#### 0.14.1.0.3 Test GitHub Mapping
<!-- GitMap-ID: asredskd -->

Test conversion of roadmap data into GitHub structures.

**Requirements:**
- Test conversion of roadmap data into GitHub structures.

**Work Steps:**
- [ ] 0.14.1.0.3 (a) Test milestone mapping
- [ ] 0.14.1.0.3 (b) Test label mapping
- [ ] 0.14.1.0.3 (c) Test Section mapping
- [ ] 0.14.1.0.3 (d) Test issue mapping
- [ ] 0.14.1.0.3 (e) Test sub-issue relationships

#### 0.14.1.0.4 Test Duplicate Prevention
<!-- GitMap-ID: bsredskc -->

Verify that synchronization can safely run more than once.

**Requirements:**
- Verify that synchronization can safely run more than once.

**Work Steps:**
- [ ] 0.14.1.0.4 (a) Test existing labels
- [ ] 0.14.1.0.4 (b) Test existing milestones
- [ ] 0.14.1.0.4 (c) Test existing issues
- [ ] 0.14.1.0.4 (d) Confirm repeated synchronization does not create duplicates

#### 0.14.1.0.5 Test Roadmap Updates
<!-- GitMap-ID: csredskb -->

Test synchronization after a roadmap has changed.

**Requirements:**
- Test synchronization after a roadmap has changed.

**Work Steps:**
- [ ] 0.14.1.0.5 (a) Test newly added items
- [ ] 0.14.1.0.5 (b) Test changed items
- [ ] 0.14.1.0.5 (c) Test unchanged items
- [ ] 0.14.1.0.5 (d) Test removed roadmap items
- [ ] 0.14.1.0.5 (e) Confirm destructive changes are not automatic

## 0.14.2 Failure Protection
<!-- GitMap-ID: yvredshf -->

#### 0.14.2.0.1 Handle GitHub API Failures
<!-- GitMap-ID: dsredska -->

Handle failures while communicating with GitHub.

**Requirements:**
- Handle failures while communicating with GitHub.

**Work Steps:**
- [ ] 0.14.2.0.1 (a) Detect API errors
- [ ] 0.14.2.0.1 (b) Report which operation failed
- [ ] 0.14.2.0.1 (c) Preserve useful error details
- [ ] 0.14.2.0.1 (d) Stop safely when synchronization cannot continue

#### 0.14.2.0.2 Test Dry Run Safety
<!-- GitMap-ID: esredskz -->

Verify that dry-run mode never changes GitHub.

**Requirements:**
- Verify that dry-run mode never changes GitHub.

**Work Steps:**
- [ ] 0.14.2.0.2 (a) Exercise the complete synchronization path
- [ ] 0.14.2.0.2 (b) Confirm no create operations occur
- [ ] 0.14.2.0.2 (c) Confirm no update operations occur
- [ ] 0.14.2.0.2 (d) Confirm planned changes are still reported

#### 0.14.2.0.3 Add Integration Tests
<!-- GitMap-ID: fsredsky -->

Test complete GitMap workflows using representative roadmap data.

**Requirements:**
- Test complete GitMap workflows using representative roadmap data.

**Work Steps:**
- [ ] 0.14.2.0.3 (a) Test roadmap creation through parsing
- [ ] 0.14.2.0.3 (b) Test parsing through synchronization planning
- [ ] 0.14.2.0.3 (c) Test existing-project update workflows
- [ ] 0.14.2.0.3 (d) Keep tests independent of a user's real GitHub repository where possible

# 0.15 Release Prep

## 0.15.1 Documentation
<!-- GitMap-ID: zvredshe -->

#### 0.15.1.0.1 Complete README
<!-- GitMap-ID: gtredsjx -->

Create the main user-facing GitMap documentation.

**Requirements:**
- Create the main user-facing GitMap documentation.

**Work Steps:**
- [ ] 0.15.1.0.1 (a) Explain what GitMap does
- [ ] 0.15.1.0.1 (b) Explain the roadmap-first workflow
- [ ] 0.15.1.0.1 (c) Explain installation
- [ ] 0.15.1.0.1 (d) Explain basic commands
- [ ] 0.15.1.0.1 (e) Provide a simple first-use example

#### 0.15.1.0.2 Create Roadmap Format Guide
<!-- GitMap-ID: htredsjw -->

Create detailed documentation for writing GitMap roadmaps manually.

**Requirements:**
- Create detailed documentation for writing GitMap roadmaps manually.

**Work Steps:**
- [ ] 0.15.1.0.2 (a) Explain milestones
- [ ] 0.15.1.0.2 (b) Explain Sections
- [ ] 0.15.1.0.2 (c) Explain issues
- [ ] 0.15.1.0.2 (d) Explain sub-issues
- [ ] 0.15.1.0.2 (e) Explain descriptions and requirements
- [ ] 0.15.1.0.2 (f) Provide complete examples

#### 0.15.1.0.3 Create GitHub Setup Guide
<!-- GitMap-ID: itredsjv -->

Document how to prepare a GitHub repository for GitMap.

**Requirements:**
- Document how to prepare a GitHub repository for GitMap.

**Work Steps:**
- [ ] 0.15.1.0.3 (a) Explain that the user creates the repository
- [ ] 0.15.1.0.3 (b) Explain authentication setup
- [ ] 0.15.1.0.3 (c) Explain required repository permissions
- [ ] 0.15.1.0.3 (d) Explain how GitMap connects to the repository
- [ ] 0.15.1.0.3 (e) Include troubleshooting guidance

## 0.15.2 Release
<!-- GitMap-ID: avredshd -->

#### 0.15.2.0.1 Add Version Information
<!-- GitMap-ID: jtredsju -->

Provide consistent GitMap version information.

**Requirements:**
- Provide consistent GitMap version information.

**Work Steps:**
- [ ] 0.15.2.0.1 (a) Define the application version
- [ ] 0.15.2.0.1 (b) Make the version available from the command line
- [ ] 0.15.2.0.1 (c) Keep package and application versions consistent

#### 0.15.2.0.2 Run Release Test
<!-- GitMap-ID: ktredsjt -->

Test GitMap from a clean environment before release.

**Requirements:**
- Test GitMap from a clean environment before release.

**Work Steps:**
- [ ] 0.15.2.0.2 (a) Install GitMap from scratch
- [ ] 0.15.2.0.2 (b) Create a new roadmap
- [ ] 0.15.2.0.2 (c) Connect to a test repository
- [ ] 0.15.2.0.2 (d) Preview synchronization
- [ ] 0.15.2.0.2 (e) Perform synchronization
- [ ] 0.15.2.0.2 (f) Run synchronization again to verify duplicate prevention

#### 0.15.2.0.3 Create Version 1.0 Release
<!-- GitMap-ID: ltredsjs -->

Publish the first stable GitMap release.
<!-- Append these milestones to the existing GitMap roadmap. Keep its metadata and representation settings. New items have permanent eight-letter GitMap IDs assigned as an import workaround. -->

**Requirements:**
- Publish the first stable GitMap release.

**Work Steps:**
- [ ] 0.15.2.0.3 (a) Complete all required tests
- [ ] 0.15.2.0.3 (b) Complete user documentation
- [ ] 0.15.2.0.3 (c) Confirm the roadmap-first workflow works end to end
- [ ] 0.15.2.0.3 (d) Tag the release as `v1.0.0`
