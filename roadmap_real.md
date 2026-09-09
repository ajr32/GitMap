Title: GitMap Roadmap

Sub-Title: GitMap turns a project roadmap into a structured GitHub project.

Hierarchy-Issue-Title-Style: type_prefix

# 0.1 Foundations (DONE)

## 0.1.1 Project Setup (DONE)
<!-- GitMap-ID: muredsir -->

#### 0.1.1.0.1 Create Python Project (DONE)
<!-- GitMap-ID: goredsox -->

Create the basic Python project structure for GitMap.

**Requirements:**
- Create the basic Python project structure for GitMap.
- [ ] 0.1.1.0.1.1  (a) Create the `gitmap` package (DONE)
- [ ] 0.1.1.0.1.2  (b) Create `../pyproject.toml` (DONE)
- [ ] 0.1.1.0.1.3  (c) Create a `tests` directory (DONE)
- [ ] 0.1.1.0.1.4  (d) Create a `../.gitignore` (DONE)

#### 0.1.1.0.2 Install Dependencies (DONE)
<!-- GitMap-ID: horedsow -->

Set up the dependencies needed to develop and test GitMap.

**Requirements:**
- Set up the dependencies needed to develop and test GitMap.
- [ ] 0.1.1.0.2.1  (a) Support editable installation (DONE)
- [ ] 0.1.1.0.2.2  (b) Add `pytest` as a development dependency (DONE)
- [ ] 0.1.1.0.2.3  (c) Confirm the development environment installs successfully (DONE)

#### 0.1.1.0.3 Create Command-Line Entry Point (DONE)
<!-- GitMap-ID: ioredsov -->

Create the basic command-line entry point for GitMap.

**Requirements:**
- Create the basic command-line entry point for GitMap.
- [ ] 0.1.1.0.3.1  (a) Allow GitMap to be started from the command line (DONE)
- [ ] 0.1.1.0.3.2  (b) Display a simple welcome message (DONE)
- [ ] 0.1.1.0.3.3  (c) Exit cleanly (DONE)

#### 0.1.1.0.4 Add Initial Tests (DONE)
<!-- GitMap-ID: joredsou -->

Create the first automated tests for GitMap.

**Requirements:**
- Create the first automated tests for GitMap.
- [ ] 0.1.1.0.4.1  (a) Confirm GitMap can be imported (DONE)
- [ ] 0.1.1.0.4.2  (b) Confirm the command-line entry point runs (DONE)
- [ ] 0.1.1.0.4.3  (c) Confirm the test suite can be run with `pytest` (DONE)

#### 0.1.1.0.5 Add Project Documentation (DONE)
<!-- GitMap-ID: koredsot -->

Create the basic documentation needed to understand and develop GitMap.

**Requirements:**
- Create the basic documentation needed to understand and develop GitMap.
- [ ] 0.1.1.0.5.1  (a) Explain what GitMap does (DONE)
- [ ] 0.1.1.0.5.2  (b) Explain how to install GitMap for development (DONE)
- [ ] 0.1.1.0.5.3  (c) Explain how to run GitMap (DONE)
- [ ] 0.1.1.0.5.4  (d) Explain how to run the tests (DONE)

## 0.1.2 Roadmap Format (DONE)
<!-- GitMap-ID: nuredsiq -->

#### 0.1.2.0.1 Define Roadmap Structure (DONE)
<!-- GitMap-ID: loredsos -->

Define the hierarchy used in a GitMap roadmap.

**Requirements:**
- Define the hierarchy used in a GitMap roadmap.
- [ ] 0.1.2.0.1.1  (a) Support milestones (DONE)
- [ ] 0.1.2.0.1.2  (b) Support Sections (DONE)
- [ ] 0.1.2.0.1.3  (c) Support issues (DONE)
- [ ] 0.1.2.0.1.4  (d) Support sub-issues (DONE)
- [ ] 0.1.2.0.1.5  (e) Support descriptions and requirements (DONE)
- [ ] 0.1.2.0.1.6  (f) Use Markdown headings to represent hierarchy (DONE)

#### 0.1.2.0.2 Create Example Roadmap (DONE)
<!-- GitMap-ID: moredsor -->

Create a complete example roadmap that can be used for development and testing.

**Requirements:**
- Create a complete example roadmap that can be used for development and testing.
- [ ] 0.1.2.0.2.1  (a) Include at least one milestone (DONE)
- [ ] 0.1.2.0.2.2  (b) Include at least one Section (DONE)
- [ ] 0.1.2.0.2.3  (c) Include multiple issues (DONE)
- [ ] 0.1.2.0.2.4  (d) Include at least one sub-issue (DONE)
- [ ] 0.1.2.0.2.5  (e) Include descriptions and requirements (DONE)

#### 0.1.2.0.3 Document Roadmap Format (DONE)
<!-- GitMap-ID: noredsoq -->

Document how users should write a GitMap roadmap.

**Requirements:**
- Document how users should write a GitMap roadmap.
- [ ] 0.1.2.0.3.1  (a) Explain each heading level (DONE)
- [ ] 0.1.2.0.3.2  (b) Show how milestones, Sections, issues, and sub-issues are represented (DONE)
- [ ] 0.1.2.0.3.3  (c) Provide a copyable example (DONE)

# 0.2 Roadmap Parser (DONE)

## 0.2.1 Markdown Parsing (DONE)
<!-- GitMap-ID: ouredsip -->

#### 0.2.1.0.1 Read Roadmap File (DONE)
<!-- GitMap-ID: ooredsop -->

Load a roadmap from a Markdown file.

**Requirements:**
- Load a roadmap from a Markdown file.
- [ ] 0.2.1.0.1.1  (a) Accept a roadmap file path (DONE)
- [ ] 0.2.1.0.1.2  (b) Read the Markdown contents (DONE)
- [ ] 0.2.1.0.1.3  (c) Report a clear error if the file cannot be read (DONE)

#### 0.2.1.0.2 Parse Milestones (DONE)
<!-- GitMap-ID: poredsoo -->

Identify milestone headings in the roadmap.

**Requirements:**
- Identify milestone headings in the roadmap.
- [ ] 0.2.1.0.2.1  (a) Recognize milestone headings (DONE)
- [ ] 0.2.1.0.2.2  (b) Capture the milestone number and title (DONE)
- [ ] 0.2.1.0.2.3  (c) Preserve the order of milestones (DONE)

#### 0.2.1.0.3 Parse Sections (DONE)
<!-- GitMap-ID: qoredson -->

Identify Sections within each milestone.

**Requirements:**
- Identify Sections within each milestone.
- [ ] 0.2.1.0.3.1  (a) Associate each Section with its milestone (DONE)
- [ ] 0.2.1.0.3.2  (b) Capture the Section title (DONE)
- [ ] 0.2.1.0.3.3  (c) Capture the Section description (DONE)
- [ ] 0.2.1.0.3.4  (d) Recognize the Section type marker (DONE)

#### 0.2.1.0.4 Parse Issues (DONE)
<!-- GitMap-ID: roredsom -->

Identify issues within each Section.

**Requirements:**
- Identify issues within each Section.
- [ ] 0.2.1.0.4.1  (a) Associate each issue with its Section (DONE)
- [ ] 0.2.1.0.4.2  (b) Capture the issue number and title (DONE)
- [ ] 0.2.1.0.4.3  (c) Capture the issue description (DONE)
- [ ] 0.2.1.0.4.4  (d) Capture requirements (DONE)

#### 0.2.1.0.5 Parse Work Steps (DONE)
<!-- GitMap-ID: soredsol -->

Support issues nested beneath other issues.

**Requirements:**
- Support issues nested beneath other issues.
- [ ] 0.2.1.0.5.1  (a) Associate each sub-issue with its parent issue (DONE)
- [ ] 0.2.1.0.5.2  (b) Preserve the roadmap hierarchy (DONE)
- [ ] 0.2.1.0.5.3  (c) Support numbering such as `0.2.4.1` (DONE)

## 0.2.2 Roadmap Validation (DONE)
<!-- GitMap-ID: puredsio -->

#### 0.2.2.0.1 Validate Roadmap Structure (DONE)
<!-- GitMap-ID: toredsok -->

Check that the roadmap follows GitMap's expected hierarchy.

**Requirements:**
- Check that the roadmap follows GitMap's expected hierarchy.
- [ ] 0.2.2.0.1.1  (a) Detect issues outside a Section (DONE)
- [ ] 0.2.2.0.1.2  (b) Detect Sections outside a milestone (DONE)
- [ ] 0.2.2.0.1.3  (c) Detect malformed hierarchy (DONE)
- [ ] 0.2.2.0.1.4  (d) Provide useful error messages (DONE)

#### 0.2.2.0.2 Validate Numbering (DONE)
<!-- GitMap-ID: uoredsoj -->

Check roadmap numbering for obvious errors.

**Requirements:**
- Check roadmap numbering for obvious errors.
- [ ] 0.2.2.0.2.1  (a) Detect duplicate numbers (DONE)
- [ ] 0.2.2.0.2.2  (b) Detect invalid parent relationships (DONE)
- [ ] 0.2.2.0.2.3  (c) Identify the location of the problem (DONE)

#### 0.2.2.0.3 Preview Parsed Roadmap (DONE)
<!-- GitMap-ID: voredsoi -->

Allow users to see what GitMap understood before synchronization.

**Requirements:**
- Allow users to see what GitMap understood before synchronization.
- [ ] 0.2.2.0.3.1  (a) Display milestones (DONE)
- [ ] 0.2.2.0.3.2  (b) Display Sections (DONE)
- [ ] 0.2.2.0.3.3  (c) Display issues and sub-issues (DONE)
- [ ] 0.2.2.0.3.4  (d) Preserve hierarchy in the preview (DONE)

# 0.3 GitHub Setup (DONE)

## 0.3.1 Repository Connection (DONE)
<!-- GitMap-ID: ruredsim -->

#### 0.3.1.0.1 Collect Repository Information (DONE)
<!-- GitMap-ID: woredsoh -->

Ask the user which GitHub repository should receive the roadmap.

**Requirements:**
- Ask the user which GitHub repository should receive the roadmap.
- [ ] 0.3.1.0.1.1  (a) Ask for the GitHub username (DONE)
- [ ] 0.3.1.0.1.2  (b) Ask for the repository name (DONE)
- [ ] 0.3.1.0.1.3  (c) Do not create the repository automatically (DONE)
- [ ] 0.3.1.0.1.4  (d) Allow roadmap creation to be completed before GitHub setup begins (DONE)

#### 0.3.1.0.2 Configure GitHub Authentication (DONE)
<!-- GitMap-ID: xoredsog -->

Set up authentication required to work with the selected repository.

**Requirements:**
- Set up authentication required to work with the selected repository.
- [ ] 0.3.1.0.2.1  (a) Keep credentials outside source control (DONE)
- [ ] 0.3.1.0.2.2  (b) Provide clear setup instructions (DONE)
- [ ] 0.3.1.0.2.3  (c) Detect missing authentication (DONE)
- [ ] 0.3.1.0.2.4  (d) Never store authentication tokens in the roadmap (DONE)

#### 0.3.1.0.3 Verify Repository (DONE)
<!-- GitMap-ID: yoredsof -->

Confirm that GitMap can access the repository before synchronization.

**Requirements:**
- Confirm that GitMap can access the repository before synchronization.
- [ ] 0.3.1.0.3.1  (a) Verify that the repository exists (DONE)
- [ ] 0.3.1.0.3.2  (b) Verify that authentication works (DONE)
- [ ] 0.3.1.0.3.3  (c) Verify that the user has appropriate access (DONE)
- [ ] 0.3.1.0.3.4  (d) Stop synchronization if verification fails (DONE)

## 0.3.2 GitHub Project Structure (DONE)
<!-- GitMap-ID: suredsil -->

#### 0.3.2.0.1 Define Milestone Mapping (DONE)
<!-- GitMap-ID: zoredsoe -->

Define how roadmap milestones map to GitHub milestones.

**Requirements:**
- Define how roadmap milestones map to GitHub milestones.
- [ ] 0.3.2.0.1.1  (a) Preserve milestone titles (DONE)
- [ ] 0.3.2.0.1.2  (b) Avoid creating duplicate milestones (DONE)
- [ ] 0.3.2.0.1.3  (c) Allow existing milestones to be recognized (DONE)

#### 0.3.2.0.2 Define Label Mapping (DONE)
<!-- GitMap-ID: aoredsod -->

Define the labels GitMap uses when creating GitHub items.

**Requirements:**
- Define the labels GitMap uses when creating GitHub items.
- [ ] 0.3.2.0.2.1  (a) Support labels for Sections (DONE)
- [ ] 0.3.2.0.2.2  (b) Support labels for issues when defined by the roadmap (DONE)
- [ ] 0.3.2.0.2.3  (c) Avoid creating duplicate labels (DONE)
- [ ] 0.3.2.0.2.4  (d) Allow labels to be created before issues are synchronized (DONE)

#### 0.3.2.0.3 Define Issue Mapping (DONE)
<!-- GitMap-ID: boredsoc -->

Define how roadmap items become GitHub issues.

**Requirements:**
- Define how roadmap items become GitHub issues.
- [ ] 0.3.2.0.3.1  (a) Preserve issue titles (DONE)
- [ ] 0.3.2.0.3.2  (b) Preserve descriptions (DONE)
- [ ] 0.3.2.0.3.3  (c) Preserve requirements (DONE)
- [ ] 0.3.2.0.3.4  (d) Associate issues with their milestone (DONE)
- [ ] 0.3.2.0.3.5  (e) Apply appropriate labels (DONE)

#### 0.3.2.0.4 Define Work Step Mapping (DONE)
<!-- GitMap-ID: coredsob -->

Define how roadmap hierarchy is represented in GitHub.

**Requirements:**
- Define how roadmap hierarchy is represented in GitHub.
- [ ] 0.3.2.0.4.1  (a) Preserve parent-child relationships when supported (DONE)
- [ ] 0.3.2.0.4.2  (b) Keep sub-issues associated with their parent (DONE)
- [ ] 0.3.2.0.4.3  (c) Preserve roadmap numbering (DONE)

# 0.4 GitHub Synchronization (DONE)

## 0.4.1 Synchronization Engine (DONE)
<!-- GitMap-ID: turedsik -->

#### 0.4.1.0.1 Create Labels (DONE)
<!-- GitMap-ID: doredsoa -->

Create the labels required by the roadmap before synchronizing other items.

**Requirements:**
- Create the labels required by the roadmap before synchronizing other items.
- [ ] 0.4.1.0.1.1  (a) Read required labels from the parsed roadmap (DONE)
- [ ] 0.4.1.0.1.2  (b) Detect labels that already exist (DONE)
- [ ] 0.4.1.0.1.3  (c) Create only missing labels (DONE)
- [ ] 0.4.1.0.1.4  (d) Do not create duplicates (DONE)

#### 0.4.1.0.2 Create Milestones (DONE)
<!-- GitMap-ID: eoredsoz -->

Create roadmap milestones in GitHub.

**Requirements:**
- Create roadmap milestones in GitHub.
- [ ] 0.4.1.0.2.1  (a) Detect milestones that already exist (DONE)
- [ ] 0.4.1.0.2.2  (b) Create only missing milestones (DONE)
- [ ] 0.4.1.0.2.3  (c) Preserve milestone titles (DONE)
- [ ] 0.4.1.0.2.4  (d) Do not create duplicates (DONE)

#### 0.4.1.0.3 Create Sections (DONE)
<!-- GitMap-ID: foredsoy -->

Create GitHub issues representing roadmap Sections.

**Requirements:**
- Create GitHub issues representing roadmap Sections.
- [ ] 0.4.1.0.3.1  (a) Create the Section before its child issues (DONE)
- [ ] 0.4.1.0.3.2  (b) Include the Section description (DONE)
- [ ] 0.4.1.0.3.3  (c) Apply the Section label (DONE)
- [ ] 0.4.1.0.3.4  (d) Associate the Section with its milestone (DONE)
- [ ] 0.4.1.0.3.5  (e) Detect an existing matching Section before creating another (DONE)

#### 0.4.1.0.4 Create Issues (DONE)
<!-- GitMap-ID: gpredsnx -->

Create GitHub issues from roadmap issues.

**Requirements:**
- Create GitHub issues from roadmap issues.
- [ ] 0.4.1.0.4.1  (a) Preserve the issue title (DONE)
- [ ] 0.4.1.0.4.2  (b) Include the description (DONE)
- [ ] 0.4.1.0.4.3  (c) Include requirements using GitHub Markdown (DONE)
- [ ] 0.4.1.0.4.4  (d) Associate the issue with its milestone (DONE)
- [ ] 0.4.1.0.4.5  (e) Apply defined labels (DONE)
- [ ] 0.4.1.0.4.6  (f) Detect existing matching issues before creating another (DONE)

#### 0.4.1.0.5 Create Work Steps (DONE)
<!-- GitMap-ID: hpredsnw -->

Create roadmap sub-issues and associate them with their parent issues.

**Requirements:**
- Create roadmap sub-issues and associate them with their parent issues.
- [ ] 0.4.1.0.5.1  (a) Create the parent before its sub-issues (DONE)
- [ ] 0.4.1.0.5.2  (b) Preserve the parent-child hierarchy (DONE)
- [ ] 0.4.1.0.5.3  (c) Include descriptions and requirements (DONE)
- [ ] 0.4.1.0.5.4  (d) Associate sub-issues with the correct milestone (DONE)

## 0.4.2 Safe Synchronization (DONE)
<!-- GitMap-ID: uuredsij -->

#### 0.4.2.0.1 Add Dry Run (DONE)
<!-- GitMap-ID: ipredsnv -->

Allow users to preview what synchronization would change without changing GitHub.

**Requirements:**
- Allow users to preview what synchronization would change without changing GitHub.
- [ ] 0.4.2.0.1.1  (a) Show items that would be created (DONE)
- [ ] 0.4.2.0.1.2  (b) Show items that already exist (DONE)
- [ ] 0.4.2.0.1.3  (c) Make no GitHub changes during a dry run (DONE)
- [ ] 0.4.2.0.1.4  (d) Clearly identify dry-run output (DONE)

#### 0.4.2.0.2 Prevent Duplicate Items (DONE)
<!-- GitMap-ID: jpredsnu -->

Make repeated synchronization safe.

**Requirements:**
- Make repeated synchronization safe.
- [ ] 0.4.2.0.2.1  (a) Check GitHub before creating an item (DONE)
- [ ] 0.4.2.0.2.2  (b) Reuse existing matching items (DONE)
- [ ] 0.4.2.0.2.3  (c) Prevent duplicate labels (DONE)
- [ ] 0.4.2.0.2.4  (d) Prevent duplicate milestones (DONE)
- [ ] 0.4.2.0.2.5  (e) Prevent duplicate issues (DONE)

#### 0.4.2.0.3 Add Synchronization Summary (DONE)
<!-- GitMap-ID: kpredsnt -->

Display the result of synchronization.

**Requirements:**
- Display the result of synchronization.
- [ ] 0.4.2.0.3.1  (a) Report items created (DONE)
- [ ] 0.4.2.0.3.2  (b) Report items already present (DONE)
- [ ] 0.4.2.0.3.3  (c) Report skipped items (DONE)
- [ ] 0.4.2.0.3.4  (d) Report errors (DONE)

# 0.5 Roadmap Updates (DONE)

## 0.5.1 Existing Project Import (DONE)
<!-- GitMap-ID: vuredsii -->

#### 0.5.1.0.1 Read Existing Milestones (DONE)
<!-- GitMap-ID: lpredsns -->

Retrieve existing milestones from the repository.

**Requirements:**
- Retrieve existing milestones from the repository.
- [ ] 0.5.1.0.1.1  (a) Read open milestones (DONE)
- [ ] 0.5.1.0.1.2  (b) Recognize milestones already represented in the roadmap (DONE)
- [ ] 0.5.1.0.1.3  (c) Preserve GitHub milestone identifiers for later updates (DONE)

#### 0.5.1.0.2 Read Existing Labels (DONE)
<!-- GitMap-ID: mpredsnr -->

Retrieve existing repository labels.

**Requirements:**
- Retrieve existing repository labels.
- [ ] 0.5.1.0.2.1  (a) Read current labels (DONE)
- [ ] 0.5.1.0.2.2  (b) Match existing labels to roadmap labels (DONE)
- [ ] 0.5.1.0.2.3  (c) Avoid recreating labels that already exist (DONE)

#### 0.5.1.0.3 Read Existing Issues (DONE)
<!-- GitMap-ID: npredsnq -->

Retrieve existing GitHub issues that correspond to roadmap items.

**Requirements:**
- Retrieve existing GitHub issues that correspond to roadmap items.
- [ ] 0.5.1.0.3.1  (a) Read existing issues (DONE)
- [ ] 0.5.1.0.3.2  (b) Match issues to roadmap items (DONE)
- [ ] 0.5.1.0.3.3  (c) Preserve GitHub issue numbers (DONE)
- [ ] 0.5.1.0.3.4  (d) Distinguish GitMap-managed items from unrelated repository issues (DONE)

#### 0.5.1.0.4 Rebuild Roadmap State (DONE)
<!-- GitMap-ID: opredsnp -->

Use GitHub data to reconstruct the current state of a GitMap-managed project.

**Requirements:**
- Use GitHub data to reconstruct the current state of a GitMap-managed project.
- [ ] 0.5.1.0.4.1  (a) Associate existing issues with milestones (DONE)
- [ ] 0.5.1.0.4.2  (b) Restore Section and issue relationships (DONE)
- [ ] 0.5.1.0.4.3  (c) Restore sub-issue relationships when available (DONE)
- [ ] 0.5.1.0.4.4  (d) Identify roadmap items that cannot be matched safely (DONE)

## 0.5.2 Roadmap Changes (DONE)
<!-- GitMap-ID: wuredsih -->

#### 0.5.2.0.1 Detect Roadmap Changes (DONE)
<!-- GitMap-ID: ppredsno -->

Compare the local roadmap with the current GitHub project.

**Requirements:**
- Compare the local roadmap with the current GitHub project.
- [ ] 0.5.2.0.1.1  (a) Detect new roadmap items (DONE)
- [ ] 0.5.2.0.1.2  (b) Detect changed roadmap items (DONE)
- [ ] 0.5.2.0.1.3  (c) Detect items that already match GitHub (DONE)
- [ ] 0.5.2.0.1.4  (d) Present differences before synchronization (DONE)

#### 0.5.2.0.2 Update Existing Items (DONE)
<!-- GitMap-ID: qpredsnn -->

Update GitHub items when their corresponding roadmap entries change.

**Requirements:**
- Update GitHub items when their corresponding roadmap entries change.
- [ ] 0.5.2.0.2.1  (a) Update titles when changed (DONE)
- [ ] 0.5.2.0.2.2  (b) Update descriptions when changed (DONE)
- [ ] 0.5.2.0.2.3  (c) Update requirements when changed (DONE)
- [ ] 0.5.2.0.2.4  (d) Preserve GitHub issue numbers (DONE)
- [ ] 0.5.2.0.2.5  (e) Avoid recreating existing items (DONE)

#### 0.5.2.0.3 Handle Removed Roadmap Items (DONE)
<!-- GitMap-ID: rpredsnm -->

Safely identify items that exist in GitHub but have been removed from the roadmap.

**Requirements:**
- Safely identify items that exist in GitHub but have been removed from the roadmap.
- [ ] 0.5.2.0.3.1  (a) Never delete GitHub items automatically (DONE)
- [ ] 0.5.2.0.3.2  (b) Report removed roadmap items (DONE)
- [ ] 0.5.2.0.3.3  (c) Require an explicit user decision before destructive changes (DONE)
- [ ] 0.5.2.0.3.4  (d) Preserve historical GitHub data by default (DONE)

#### 0.5.2.0.4 Preview Updates (DONE)
<!-- GitMap-ID: spredsnl -->

Show the user exactly what an update synchronization will do.

**Requirements:**
- Show the user exactly what an update synchronization will do.
- [ ] 0.5.2.0.4.1  (a) Show new items (DONE)
- [ ] 0.5.2.0.4.2  (b) Show changed items (DONE)
- [ ] 0.5.2.0.4.3  (c) Show unchanged items (DONE)
- [ ] 0.5.2.0.4.4  (d) Show roadmap items that were removed (DONE)
- [ ] 0.5.2.0.4.5  (e) Require confirmation before applying changes (DONE)

# 0.6 User Workflow

## 0.6.1 Interactive Roadmap Builder (DONE)
<!-- GitMap-ID: xuredsig -->

#### 0.6.1.0.1 Start New Roadmap (DONE)
<!-- GitMap-ID: tpredsnk -->

Begin an interactive roadmap-building session.

**Requirements:**
- Begin an interactive roadmap-building session.
- [ ] 0.6.1.0.1.1  (a) Ask for the project name (DONE)
- [ ] 0.6.1.0.1.2  (b) Ask for a project overview (DONE)
- [ ] 0.6.1.0.1.3  (c) Create the initial roadmap structure (DONE)
- [ ] 0.6.1.0.1.4  (d) Do not require GitHub information yet (DONE)

#### 0.6.1.0.2 Collect Milestones (DONE)
<!-- GitMap-ID: upredsnj -->

Guide the user through defining project milestones.

**Requirements:**
- Guide the user through defining project milestones.
- [ ] 0.6.1.0.2.1  (a) Ask for the milestone number (DONE)
- [ ] 0.6.1.0.2.2  (b) Ask for the milestone title (DONE)
- [ ] 0.6.1.0.2.3  (c) Allow multiple milestones (DONE)
- [ ] 0.6.1.0.2.4  (d) Allow the user to indicate when they are finished (DONE)

#### 0.6.1.0.3 Collect Sections (DONE)
<!-- GitMap-ID: vpredsni -->

Guide the user through defining Sections within each milestone.

**Requirements:**
- Guide the user through defining Sections within each milestone.
- [ ] 0.6.1.0.3.1  (a) Ask for the Section title (DONE)
- [ ] 0.6.1.0.3.2  (b) Ask for a Section overview (DONE)
- [ ] 0.6.1.0.3.3  (c) Associate the Section with its milestone (DONE)
- [ ] 0.6.1.0.3.4  (d) Allow multiple Sections (DONE)

#### 0.6.1.0.4 Collect Issues (DONE)
<!-- GitMap-ID: wpredsnh -->

Guide the user through defining issues within a Section.

**Requirements:**
- Guide the user through defining issues within a Section.
- [ ] 0.6.1.0.4.1  (a) Ask for the issue title (DONE)
- [ ] 0.6.1.0.4.2  (b) Ask for the issue description (DONE)
- [ ] 0.6.1.0.4.3  (c) Ask for requirements (DONE)
- [ ] 0.6.1.0.4.4  (d) Allow requirements to be entered individually (DONE)
- [ ] 0.6.1.0.4.5  (e) Treat a blank entry as finished (DONE)

#### 0.6.1.0.5 Collect Work Steps (DONE)
<!-- GitMap-ID: xpredsng -->

Allow an issue to contain smaller sub-issues.

**Requirements:**
- Allow an issue to contain smaller sub-issues.
- [ ] 0.6.1.0.5.1  (a) Ask whether an issue needs sub-issues (DONE)
- [ ] 0.6.1.0.5.2  (b) Collect sub-issue titles (DONE)
- [ ] 0.6.1.0.5.3  (c) Collect descriptions and requirements (DONE)
- [ ] 0.6.1.0.5.4  (d) Preserve the parent-child relationship (DONE)
- [ ] 0.6.1.0.5.5  (e) Support additional nesting when appropriate (DONE)

#### 0.6.1.0.6 Support Pasted Content (DONE)
<!-- GitMap-ID: ypredsnf -->

Allow users to paste existing project information instead of answering every question individually.

**Requirements:**
- Allow users to paste existing project information instead of answering every question individually.
- [ ] 0.6.1.0.6.1  (a) Accept pasted overview text (DONE)
- [ ] 0.6.1.0.6.2  (b) Accept pasted descriptions (DONE)
- [ ] 0.6.1.0.6.3  (c) Accept pasted requirements (DONE)
- [ ] 0.6.1.0.6.4  (d) Preserve multiline content (DONE)
- [ ] 0.6.1.0.6.5  (e) Allow interactive questions and pasted content to be mixed (DONE)

## 0.6.2 Roadmap Review (DONE)
<!-- GitMap-ID: yuredsif -->

#### 0.6.2.0.1 Display Completed Roadmap (DONE)
<!-- GitMap-ID: zpredsne -->

Show the complete generated roadmap.

**Requirements:**
- Show the complete generated roadmap.
- [ ] 0.6.2.0.1.1  (a) Preserve Markdown hierarchy (DONE)
- [ ] 0.6.2.0.1.2  (b) Make milestone, Section, issue, and sub-issue relationships clear (DONE)
- [ ] 0.6.2.0.1.3  (c) Show descriptions and requirements (DONE)

#### 0.6.2.0.2 Edit Roadmap Before Sync
<!-- GitMap-ID: apredsnd -->

Allow changes before GitHub synchronization begins.

**Requirements:**
- Allow changes before GitHub synchronization begins.
- [ ] 0.6.2.0.2.1  (a) Allow items to be renamed (DONE)
- [ ] 0.6.2.0.2.2  (b) Allow descriptions and requirements to be changed (DONE)
- [ ] 0.6.2.0.2.3  (c) Allow items to be added (DONE)
- [ ] 0.6.2.0.2.4  (d) Allow items to be removed
- [ ] 0.6.2.0.2.5  (e) Revalidate the roadmap after changes

#### 0.6.2.0.3 Save Roadmap (DONE)
<!-- GitMap-ID: bpredsnc -->

Save the completed roadmap to `roadmap.md`.

**Requirements:**
- Save the completed roadmap to `roadmap.md`.
- [ ] 0.6.2.0.3.1  (a) Produce valid GitMap Markdown (DONE)
- [ ] 0.6.2.0.3.2  (b) Preserve the complete hierarchy (DONE)
- [ ] 0.6.2.0.3.3  (c) Confirm where the roadmap was saved (DONE)

# 0.7 Changes to make

## 0.7.1 Synchronization Workflow Improvements
<!-- GitMap-ID: zuredsie -->

#### 0.7.1.0.1 Improve Change Preview Flow (DONE)
<!-- GitMap-ID: cpredsnb -->

Avoid displaying detailed change lists before the user asks to review them.

**Requirements:**
- Present a concise synchronization summary first and allow the user to choose which details to inspect.
- [ ] 0.7.1.0.1.1  (a) Display change counts before detailed change lists
- [ ] 0.7.1.0.1.2  (b) Do not automatically display the complete added-item list
- [ ] 0.7.1.0.1.3  (c) Allow added items to be reviewed on request
- [ ] 0.7.1.0.1.4  (d) Allow changed items to be reviewed on request
- [ ] 0.7.1.0.1.5  (e) Allow unchanged items to be reviewed on request
- [ ] 0.7.1.0.1.6  (f) Allow removed items to be reviewed on request
- [ ] 0.7.1.0.1.7  (g) Return to the synchronization prompt after reviewing a list

#### 0.7.1.0.2 Preserve Identity During Renumbering
<!-- GitMap-ID: dpredsna -->

Recognize existing roadmap items when their GitMap numbers change.
items.

**Requirements:**
- Treat renumbered roadmap items as updates to existing GitHub items rather than unrelated removed and newly created
- [ ] 0.7.1.0.2.1  (a) Detect an existing roadmap item after its number changes
- [ ] 0.7.1.0.2.2  (b) Avoid relying solely on the GitMap number as item identity
- [ ] 0.7.1.0.2.3  (c) Preserve the existing GitHub item when a roadmap item is renumbered
- [ ] 0.7.1.0.2.4  (d) Update the GitMap marker after renumbering
- [ ] 0.7.1.0.2.5  (e) Preserve existing GitHub issue numbers and relationships where possible

#### 0.7.1.0.3 Update Renumbered Milestones
<!-- GitMap-ID: epredsnz -->

Update existing GitHub milestones when roadmap milestone numbers change.

**Requirements:**
- Prevent duplicate GitHub milestones when roadmap milestones are renumbered.
- [ ] 0.7.1.0.3.1  (a) Match a renumbered milestone to its existing GitHub milestone
- [ ] 0.7.1.0.3.2  (b) Rename the existing GitHub milestone
- [ ] 0.7.1.0.3.3  (c) Preserve the GitHub milestone ID
- [ ] 0.7.1.0.3.4  (d) Preserve issues assigned to the milestone
- [ ] 0.7.1.0.3.5  (e) Do not create a second milestone solely because its roadmap number changed
- [ ] 0.7.1.0.3.6  (f) Detect and report ambiguous milestone matches

#### 0.7.1.0.4 Preview Renumbering During Synchronization
<!-- GitMap-ID: fpredsny -->

Make renumbering visible before GitHub is changed.

**Requirements:**
- Clearly distinguish renumbering from ordinary additions and removals during synchronization preview.
- [ ] 0.7.1.0.4.1  (a) Identify renumbered roadmap items
- [ ] 0.7.1.0.4.2  (b) Display the old roadmap number
- [ ] 0.7.1.0.4.3  (c) Display the new roadmap number
- [ ] 0.7.1.0.4.4  (d) Distinguish renumbering from newly added items
- [ ] 0.7.1.0.4.5  (e) Distinguish renumbering from removed items
- [ ] 0.7.1.0.4.6  (f) Require normal synchronization confirmation before applying renumbering

#### 0.7.1.0.5 Display Synchronization Progress
<!-- GitMap-ID: gqredsmx -->

Show where GitMap is during an active synchronization.

**Requirements:**
- Let the user see how much synchronization work has completed and what GitMap is currently processing.
- [ ] 0.7.1.0.5.1  (a) Count the total planned synchronization operations
- [ ] 0.7.1.0.5.2  (b) Display the current operation number
- [ ] 0.7.1.0.5.3  (c) Display the total number of operations
- [ ] 0.7.1.0.5.4  (d) Display the roadmap number of the item being processed
- [ ] 0.7.1.0.5.5  (e) Display the title of the item being processed
- [ ] 0.7.1.0.5.6  (f) Display whether the item is being created, updated, or checked
- [ ] 0.7.1.0.5.7  (g) Update progress as each operation completes
- [ ] 0.7.1.0.5.8  (h) Display a completion summary
- [ ] 0.7.1.0.5.9  (i) Display elapsed synchronization time

## 0.7.2 Synchronization Safety and Recovery
<!-- GitMap-ID: auredsid -->

#### 0.7.2.0.1 Validate Synchronization Plan
<!-- GitMap-ID: hqredsmw -->

**Requirements:**
- [ ] 0.7.2.0.1.1  (a) Detect duplicate GitMap identifiers
- [ ] 0.7.2.0.1.2  (b) Detect duplicate milestone mappings
- [ ] 0.7.2.0.1.3  (c) Detect ambiguous identity matches
- [ ] 0.7.2.0.1.4  (d) Refuse to guess when identity cannot be determined safely
- [ ] 0.7.2.0.1.5  (e) Explain conflicts before synchronization
- [ ] 0.7.2.0.1.6  (f) Allow conflicts to be resolved before retrying

#### 0.7.2.0.2 Protect Partial Synchronization
<!-- GitMap-ID: iqredsmv -->

**Requirements:**
- [ ] 0.7.2.0.2.1  (a) Track completed synchronization operations
- [ ] 0.7.2.0.2.2  (b) Identify the operation that failed
- [ ] 0.7.2.0.2.3  (c) Report operations completed before failure
- [ ] 0.7.2.0.2.4  (d) Report operations that remain incomplete
- [ ] 0.7.2.0.2.5  (e) Stop safely when synchronization cannot continue
- [ ] 0.7.2.0.2.6  (f) Preserve enough state for a safe retry

#### 0.7.2.0.3 Verify Synchronization Results
<!-- GitMap-ID: jqredsmu -->

**Requirements:**
- [ ] 0.7.2.0.3.1  (a) Re-read affected GitHub items after synchronization
- [ ] 0.7.2.0.3.2  (b) Confirm expected items were created
- [ ] 0.7.2.0.3.3  (c) Confirm expected items were updated
- [ ] 0.7.2.0.3.4  (d) Confirm expected roadmap identities were preserved
- [ ] 0.7.2.0.3.5  (e) Detect unexpected duplicate identifiers
- [ ] 0.7.2.0.3.6  (f) Report differences between planned and actual results

#### 0.7.2.0.4 Support Safe Synchronization Retry
<!-- GitMap-ID: kqredsmt -->

**Requirements:**
- [ ] 0.7.2.0.4.1  (a) Re-read GitHub state before retrying
- [ ] 0.7.2.0.4.2  (b) Recognize operations already completed
- [ ] 0.7.2.0.4.3  (c) Avoid recreating successfully created items
- [ ] 0.7.2.0.4.4  (d) Avoid reapplying unnecessary updates
- [ ] 0.7.2.0.4.5  (e) Continue remaining synchronization work safely
- [ ] 0.7.2.0.4.6  (f) Report final retry results

#### 0.7.2.0.5 Prevent Concurrent Synchronization
<!-- GitMap-ID: lqredsms -->

Prevent multiple GitMap synchronization operations from modifying the same repository at the same time.

**Requirements:**
- Prevent concurrent synchronization from creating duplicate or conflicting GitHub changes.
- [ ] 0.7.2.0.5.1  (a) Detect when synchronization is already in progress
- [ ] 0.7.2.0.5.2  (b) Prevent a second synchronization from starting against the same repository
- [ ] 0.7.2.0.5.3  (c) Explain why the second synchronization was blocked
- [ ] 0.7.2.0.5.4  (d) Allow synchronization after the active operation completes
- [ ] 0.7.2.0.5.5  (e) Clear synchronization state after successful completion
- [ ] 0.7.2.0.5.6  (f) Clear synchronization state safely after failure
- [ ] 0.7.2.0.5.7  (g) Avoid leaving a stale synchronization lock after GitMap exits unexpectedly

## 0.7.3 Synchronization Performance
<!-- GitMap-ID: buredsic -->

#### 0.7.3.0.1 Skip Unchanged Items During Synchronization
<!-- GitMap-ID: mqredsmr -->

Avoid unnecessary GitHub operations for roadmap items that have already been determined to be unchanged.

**Requirements:**
- Reduce synchronization time by processing only items that require GitHub changes.
- [ ] 0.7.3.0.1.1  (a) Identify unchanged items during synchronization planning
- [ ] 0.7.3.0.1.2  (b) Exclude unchanged items from synchronization operations
- [ ] 0.7.3.0.1.3  (c) Avoid unnecessary GitHub API calls for unchanged items
- [ ] 0.7.3.0.1.4  (d) Preserve unchanged items in the synchronization summary
- [ ] 0.7.3.0.1.5  (e) Count only actionable items in synchronization progress
- [ ] 0.7.3.0.1.6  (f) Report the number of unchanged items skipped

#### 0.7.3.0.2 Reuse Synchronization Plan
<!-- GitMap-ID: nqredsmq -->

Use the already-reviewed synchronization plan when applying changes.

**Requirements:**
- Avoid repeating work that was already completed while determining the synchronization preview.
- [ ] 0.7.3.0.2.1  (a) Preserve the synchronization plan after preview
- [ ] 0.7.3.0.2.2  (b) Use the approved plan when synchronization begins
- [ ] 0.7.3.0.2.3  (c) Process only planned create and update operations
- [ ] 0.7.3.0.2.4  (d) Avoid recalculating unchanged items unnecessarily
- [ ] 0.7.3.0.2.5  (e) Ensure the applied plan matches the plan the user approved

## 0.7.4 GitHub Repository Setup
<!-- GitMap-ID: curedsib -->

#### 0.7.4.0.1 Choose Repository
<!-- GitMap-ID: sqredsml -->

Allow the user to choose where the roadmap will be synchronized.

**Requirements:**
- Connect the completed roadmap to the appropriate GitHub repository.
- [ ] 0.7.4.0.1.1  (a) Use an existing repository
- [ ] 0.7.4.0.1.2  (b) Create a new repository

#### 0.7.4.0.2 Create Repository
<!-- GitMap-ID: tqredsmk -->

Create a GitHub repository directly from GitMap.

**Requirements:**
- Create the repository without requiring the user to leave GitMap.
- [ ] 0.7.4.0.2.1  (a) Ask for the repository name
- [ ] 0.7.4.0.2.2  (b) Ask for a repository description
- [ ] 0.7.4.0.2.3  (c) Allow public or private visibility
- [ ] 0.7.4.0.2.4  (d) Create the repository through GitHub
- [ ] 0.7.4.0.2.5  (e) Confirm successful repository creation

#### 0.7.4.0.3 Connect Repository
<!-- GitMap-ID: uqredsmj -->

Connect the roadmap to the selected repository.

**Requirements:**
- Make the selected repository the synchronization target for the roadmap.
- [ ] 0.7.4.0.3.1  (a) Verify repository access
- [ ] 0.7.4.0.3.2  (b) Store the repository association
- [ ] 0.7.4.0.3.3  (c) Prepare the repository for synchronization

#### 0.7.4.0.4 Initial Synchronization
<!-- GitMap-ID: vqredsmi -->

Allow the completed roadmap to proceed directly into GitMap's existing synchronization workflow.

**Requirements:**
- Move from roadmap creation to GitHub synchronization without restarting GitMap.
- [ ] 0.7.4.0.4.1  (a) Preview the initial synchronization
- [ ] 0.7.4.0.4.2  (b) Require confirmation before synchronization
- [ ] 0.7.4.0.4.3  (c) Synchronize the roadmap to the repository
- [ ] 0.7.4.0.4.4  (d) Report synchronization results

## 0.7.5 Roadmap Numbering
<!-- GitMap-ID: duredsia -->

#### 0.7.5.0.1 Explain Roadmap Numbering
<!-- GitMap-ID: wqredsmh -->

Explain GitMap's numbering system when the user begins building a roadmap.

**Requirements:**
- Make the roadmap hierarchy and numbering rules clear before the user begins creating items.
- [ ] 0.7.5.0.1.1  (a) Explain the milestone numbering format
- [ ] 0.7.5.0.1.2  (b) Explain how child numbers extend their parent number
- [ ] 0.7.5.0.1.3  (c) Show an example hierarchy
- [ ] 0.7.5.0.1.4  (d) Explain automatic numbering
- [ ] 0.7.5.0.1.5  (e) Explain manual numbering

#### 0.7.5.0.2 Choose Numbering Mode
<!-- GitMap-ID: mtredsjr -->

Allow the user to choose between automatic and manual numbering.

**Requirements:**
- Let users control whether GitMap assigns roadmap numbers or they enter them manually.
- [ ] 0.7.5.0.2.1  (a) Offer automatic numbering
- [ ] 0.7.5.0.2.2  (b) Offer manual numbering
- [ ] 0.7.5.0.2.3  (c) Allow manual numbering when automatic numbering cannot be used

#### 0.7.5.0.3 Choose Starting Series
<!-- GitMap-ID: ntredsjq -->

Allow automatic numbering to reflect the project's development stage.

**Requirements:**
- Start roadmap numbering in the appropriate version series.
- [ ] 0.7.5.0.3.1  (a) Offer pre-production numbering beginning with 0.x
- [ ] 0.7.5.0.3.2  (b) Offer production numbering beginning with 1.x

#### 0.7.5.0.4 Generate Hierarchical Numbers
<!-- GitMap-ID: otredsjp -->

Generate roadmap numbers based on the hierarchy the user actually creates.

**Requirements:**
- Automatically assign valid numbers without requiring every hierarchy level to be present.
- [ ] 0.7.5.0.4.1  (a) Number milestones automatically
- [ ] 0.7.5.0.4.2  (b) Number Sections automatically
- [ ] 0.7.5.0.4.3  (c) Number features automatically
- [ ] 0.7.5.0.4.4  (d) Number issues automatically
- [ ] 0.7.5.0.4.5  (e) Number Work Steps automatically
- [ ] 0.7.5.0.4.6  (f) Increment sibling numbers automatically
- [ ] 0.7.5.0.4.7  (g) Support letter sequences such as (a), (b), and (c) where used

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
detect that the hierarchy Issues do not yet exist and ask the user whether they should be created.
Users explicitly choose whether missing Section and Feature Issues are created for an existing synchronized roadmap.

**Requirements:**
- [ ] 0.7.7.0.1.1  (a) Detect when Section or Feature Issues are enabled for an existing roadmap
- [ ] 0.7.7.0.1.2  (b) Determine whether the corresponding hierarchy Issues already exist
- [ ] 0.7.7.0.1.3  (c) Inform the user how many Section and Feature Issues will be created
- [ ] 0.7.7.0.1.4  (d) Ask the user whether to create the missing hierarchy Issues
- [ ] 0.7.7.0.1.5  (e) Create hierarchy Issues only after confirmation

#### 0.7.7.0.2 Require Approval Before Modifying Existing GitHub Items
<!-- GitMap-ID: kuredsit -->

Once a GitHub item already exists, GitMap must not update, close, or otherwise modify it unless the change appears in
the synchronization preview and has been approved by the user.
Existing GitHub items are never modified without first being shown to the user and explicitly approved.

**Requirements:**
- [ ] 0.7.7.0.2.1  (a) Detect modifications to existing GitHub items
- [ ] 0.7.7.0.2.2  (b) Include all modifications in the synchronization preview
- [ ] 0.7.7.0.2.3  (c) Prevent updates that were not included in the approved synchronization plan
- [ ] 0.7.7.0.2.4  (d) Ensure updates and closures require user approval
- [ ] 0.7.7.0.2.5  (e) Verify only approved changes are applied

## 0.7.8 Finish 0.7.6
<!-- GitMap-ID: gvredshx -->

#### 0.7.8.0.1 Customize Hierarchy Issue Titles
<!-- GitMap-ID: quredsin -->

Allow users to choose how Section and Feature GitHub Issues are titled so they are easy to distinguish from normal
roadmap Issues.
Users can easily distinguish hierarchy Issues from normal roadmap Issues while preserving a consistent appearance across
GitHub.

**Requirements:**
- [ ] 0.7.8.0.1.1  (a) Add a hierarchy Issue title style option during roadmap creation.
- [ ] 0.7.8.0.1.2  (b) Store the selected title style in the roadmap.
- [ ] 0.7.8.0.1.3  (c) Update Section Issue title generation.
- [ ] 0.7.8.0.1.4  (d) Update Feature Issue title generation.
- [ ] 0.7.8.0.1.5  (e) Preserve title style during synchronization.
- [ ] 0.7.8.0.1.6  (f) Show the selected title style in synchronization preview.

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

Determine the next available sibling number when a new item is added at the end of an existing list.
it.

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
- [ ] 0.7.10.0.1.1  (a) Use an existing repository
- [ ] 0.7.10.0.1.2  (b) Create a new repository

#### 0.7.10.0.2 Create Repository
<!-- GitMap-ID: pqredsmo -->

Create a GitHub repository directly from GitMap.

**Requirements:**
- Create the repository without requiring the user to leave GitMap.
- [ ] 0.7.10.0.2.1  (a) Ask for the repository name
- [ ] 0.7.10.0.2.2  (b) Ask for a repository description
- [ ] 0.7.10.0.2.3  (c) Allow public or private visibility
- [ ] 0.7.10.0.2.4  (d) Create the repository through GitHub
- [ ] 0.7.10.0.2.5  (e) Confirm successful repository creation

#### 0.7.10.0.3 Connect Repository
<!-- GitMap-ID: qqredsmn -->

Connect the roadmap to the selected repository.

**Requirements:**
- Make the selected repository the synchronization target for the roadmap.
- [ ] 0.7.10.0.3.1  (a) Verify repository access
- [ ] 0.7.10.0.3.2  (b) Store the repository association
- [ ] 0.7.10.0.3.3  (c) Prepare the repository for synchronization

#### 0.7.10.0.4 Initial Synchronization
<!-- GitMap-ID: rqredsmm -->

Allow the completed roadmap to proceed directly into GitMap's existing synchronization workflow.

**Requirements:**
- Move from roadmap creation to GitHub synchronization without restarting GitMap.
- [ ] 0.7.10.0.4.1  (a) Preview the initial synchronization
- [ ] 0.7.10.0.4.2  (b) Require confirmation before synchronization
- [ ] 0.7.10.0.4.3  (c) Synchronize the roadmap to the repository
- [ ] 0.7.10.0.4.4  (d) Report synchronization results

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
- [ ] 0.8.1.0.1.1  (a) Provide a `gitmap` command
- [ ] 0.8.1.0.1.2  (b) Display useful help
- [ ] 0.8.1.0.1.3  (c) Display the installed version
- [ ] 0.8.1.0.1.4  (d) Exit cleanly when requested

#### 0.8.1.0.2 Create Roadmap Command
<!-- GitMap-ID: yqredsmf -->

Provide a command for creating or working with a roadmap.

**Requirements:**
- Provide a command for creating or working with a roadmap.
- [ ] 0.8.1.0.2.1  (a) Start the interactive roadmap builder
- [ ] 0.8.1.0.2.2  (b) Allow an existing roadmap to be opened
- [ ] 0.8.1.0.2.3  (c) Validate the roadmap before completing
- [ ] 0.8.1.0.2.4  (d) Save changes to `roadmap.md`

#### 0.8.1.0.3 Create Preview Command
<!-- GitMap-ID: zqredsme -->

Provide a command for previewing how GitMap interprets a roadmap.

**Requirements:**
- Provide a command for previewing how GitMap interprets a roadmap.
- [ ] 0.8.1.0.3.1  (a) Parse the selected roadmap
- [ ] 0.8.1.0.3.2  (b) Display its hierarchy
- [ ] 0.8.1.0.3.3  (c) Report validation problems
- [ ] 0.8.1.0.3.4  (d) Make no GitHub changes

#### 0.8.1.0.4 Create Setup Command
<!-- GitMap-ID: aqredsmd -->

Guide the user through connecting a roadmap to a GitHub repository.

**Requirements:**
- Guide the user through connecting a roadmap to a GitHub repository.
- [ ] 0.8.1.0.4.1  (a) Ask for the GitHub username
- [ ] 0.8.1.0.4.2  (b) Ask for the repository name
- [ ] 0.8.1.0.4.3  (c) Configure authentication
- [ ] 0.8.1.0.4.4  (d) Verify repository access
- [ ] 0.8.1.0.4.5  (e) Save non-sensitive repository configuration

#### 0.8.1.0.5 Create Sync Command
<!-- GitMap-ID: bqredsmc -->

Provide a command for synchronizing the roadmap with GitHub.

**Requirements:**
- Provide a command for synchronizing the roadmap with GitHub.
- [ ] 0.8.1.0.5.1  (a) Validate before synchronization
- [ ] 0.8.1.0.5.2  (b) Verify repository access
- [ ] 0.8.1.0.5.3  (c) Support dry-run mode
- [ ] 0.8.1.0.5.4  (d) Display planned changes
- [ ] 0.8.1.0.5.5  (e) Display a synchronization summary

## 0.8.2 Errors and Guidance
<!-- GitMap-ID: lvredshs -->

#### 0.8.2.0.1 Add User-Friendly Errors
<!-- GitMap-ID: cqredsmb -->

Replace technical failures with useful messages when possible.

**Requirements:**
- Replace technical failures with useful messages when possible.
- [ ] 0.8.2.0.1.1  (a) Explain missing roadmap files
- [ ] 0.8.2.0.1.2  (b) Explain malformed roadmaps
- [ ] 0.8.2.0.1.3  (c) Explain authentication failures
- [ ] 0.8.2.0.1.4  (d) Explain repository access failures
- [ ] 0.8.2.0.1.5  (e) Avoid unnecessary Python tracebacks during normal use

#### 0.8.2.0.2 Add Next-Step Guidance
<!-- GitMap-ID: dqredsma -->

Tell users what they can do after each major operation.

**Requirements:**
- Tell users what they can do after each major operation.
- [ ] 0.8.2.0.2.1  (a) Provide guidance after roadmap creation
- [ ] 0.8.2.0.2.2  (b) Provide guidance after repository setup
- [ ] 0.8.2.0.2.3  (c) Provide guidance after preview
- [ ] 0.8.2.0.2.4  (d) Provide guidance after synchronization

## 0.9 GitMap Desktop GUI
<!-- GitMap-ID: brredslc -->

### 0.9.1 Main GitMap Workspace
<!-- GitMap-ID: crredslb -->

Create the main GitMap desktop workspace for viewing and working with an active roadmap.

#### 0.9.1.0.1 Load the Designer-Based Main Window
<!-- GitMap-ID: eqredsmz -->

Load the GitMap desktop interface from the Qt Designer file while keeping application behavior in Python.

**Requirements:**
- Load the GitMap GUI from a Qt Designer interface while keeping application behavior in Python.
- [ ] 0.9.1.0.1.1  (a) Create `gitmap/gui/app.py`
- [ ] 0.9.1.0.1.2  (b) Create `gitmap/gui/main_window.ui`
- [ ] 0.9.1.0.1.3  (c) Create the GUI module entry point
- [ ] 0.9.1.0.1.4  (d) Create the `QApplication`
- [ ] 0.9.1.0.1.5  (e) Locate `main_window.ui` relative to `app.py`
- [ ] 0.9.1.0.1.6  (f) Open the `.ui` file using `QFile`
- [ ] 0.9.1.0.1.7  (g) Load the interface using `QUiLoader`
- [ ] 0.9.1.0.1.8  (h) Display the loaded main window
- [ ] 0.9.1.0.1.9  (i) Verify GitMap launches without UI loading errors

#### 0.9.1.0.2 Create the Main Workspace Layout
<!-- GitMap-ID: fqredsmy -->

Create the main two-part application layout with a large roadmap workspace and a smaller navigation and action area.

**Requirements:**
- Provide a large roadmap workspace with a smaller navigation and action area that resizes correctly with the application window.
- [ ] 0.9.1.0.2.1  (a) Create the main central widget in Qt Designer
- [ ] 0.9.1.0.2.2  (b) Create the roadmap workspace area
- [ ] 0.9.1.0.2.3  (c) Create the navigation and action area
- [ ] 0.9.1.0.2.4  (d) Place the two areas inside a splitter
- [ ] 0.9.1.0.2.5  (e) Give the roadmap area the larger initial share of the window
- [ ] 0.9.1.0.2.6  (f) Configure layouts so controls resize with the window
- [ ] 0.9.1.0.2.7  (g) Test the interface at its normal startup size
- [ ] 0.9.1.0.2.8  (h) Test the interface maximized
- [ ] 0.9.1.0.2.9  (i) Verify the roadmap tree fills the available workspace

#### 0.9.1.0.3 Create the Empty Workspace State
<!-- GitMap-ID: grredslx -->

Define what GitMap displays before a roadmap is opened or created and how the interface changes after a roadmap becomes active.

**Requirements:**
- Clearly provide Create Roadmap and Open Roadmap when no roadmap is active and transition to roadmap-specific controls when one becomes active.
- [ ] 0.9.1.0.3.1  (a) Add the Create Roadmap button
- [ ] 0.9.1.0.3.2  (b) Add the Open Roadmap button
- [ ] 0.9.1.0.3.3  (c) Assign stable Designer object names to both buttons
- [ ] 0.9.1.0.3.4  (d) Locate both buttons from Python using `findChild`
- [ ] 0.9.1.0.3.5  (e) Define the empty-workspace state
- [ ] 0.9.1.0.3.6  (f) Define the active-roadmap state
- [ ] 0.9.1.0.3.7  (g) Switch between the states when appropriate

#### 0.9.1.0.4 Create the Roadmap Tree
<!-- GitMap-ID: hrredslw -->

Create the expandable and scrollable tree used to display the active roadmap.

**Requirements:**
- Display the active roadmap in a large expandable and scrollable tree without an unnecessary column heading.
- [ ] 0.9.1.0.4.1  (a) Add the roadmap tree in Qt Designer
- [ ] 0.9.1.0.4.2  (b) Assign the roadmap tree a stable object name
- [ ] 0.9.1.0.4.3  (c) Locate the tree using `findChild`
- [ ] 0.9.1.0.4.4  (d) Hide the tree header
- [ ] 0.9.1.0.4.5  (e) Verify vertical scrolling
- [ ] 0.9.1.0.4.6  (f) Verify long roadmap items remain usable
- [ ] 0.9.1.0.4.7  (g) Verify the tree resizes with the workspace

#### 0.9.1.0.5 Display the Roadmap Name
<!-- GitMap-ID: irredslv -->

Show the name of the active roadmap in the main workspace.

**Requirements:**
- Display the active Roadmap model's name and keep it updated when the active roadmap or its name changes.
- [ ] 0.9.1.0.5.1  (a) Read the roadmap name from the Roadmap model
- [ ] 0.9.1.0.5.2  (b) Display the roadmap name in the workspace
- [ ] 0.9.1.0.5.3  (c) Update the displayed name when another roadmap is opened
- [ ] 0.9.1.0.5.4  (d) Update the displayed name when the roadmap is renamed
- [ ] 0.9.1.0.5.5  (e) Support displaying the name of an unsaved roadmap

#### 0.9.1.0.6 Display Milestones
<!-- GitMap-ID: jrredslu -->

Add every Milestone in the active Roadmap model to the graphical hierarchy.

**Requirements:**
- Display every Milestone beneath the roadmap root using its roadmap number and title.
- [ ] 0.9.1.0.6.1  (a) Iterate through `roadmap.milestones`
- [ ] 0.9.1.0.6.2  (b) Create a tree item for each Milestone
- [ ] 0.9.1.0.6.3  (c) Display the Milestone number
- [ ] 0.9.1.0.6.4  (d) Display the Milestone title
- [ ] 0.9.1.0.6.5  (e) Attach each Milestone beneath the roadmap root

#### 0.9.1.0.7 Display Sections
<!-- GitMap-ID: krredslt -->

Add Sections beneath their parent Milestones when the active roadmap uses Sections.

**Requirements:**
- Display Sections in their correct hierarchy while continuing to support roadmaps that do not use Sections.
- [ ] 0.9.1.0.7.1  (a) Iterate through each Milestone's Sections
- [ ] 0.9.1.0.7.2  (b) Create a tree item for each Section
- [ ] 0.9.1.0.7.3  (c) Display the Section number and title
- [ ] 0.9.1.0.7.4  (d) Attach each Section beneath its parent Milestone
- [ ] 0.9.1.0.7.5  (e) Verify roadmaps without Sections remain supported

#### 0.9.1.0.8 Display Features
<!-- GitMap-ID: lrredsls -->

Add Features beneath their parent Sections when the active roadmap uses Features.

**Requirements:**
- Display Features in their correct hierarchy while continuing to support featureless roadmaps.
- [ ] 0.9.1.0.8.1  (a) Iterate through each Section's Features
- [ ] 0.9.1.0.8.2  (b) Create a tree item for each Feature
- [ ] 0.9.1.0.8.3  (c) Display the Feature number and title
- [ ] 0.9.1.0.8.4  (d) Attach each Feature beneath its parent Section
- [ ] 0.9.1.0.8.5  (e) Verify featureless roadmaps remain supported

#### 0.9.1.0.9 Display Issues
<!-- GitMap-ID: mrredslr -->

Add Issues at each hierarchy location supported by the active roadmap.

**Requirements:**
- Display Issues correctly whether they belong to Features, Sections or directly to Milestones.
- [ ] 0.9.1.0.9.1  (a) Display Issues beneath Features
- [ ] 0.9.1.0.9.2  (b) Display Issues directly beneath Sections
- [ ] 0.9.1.0.9.3  (c) Display Issues directly beneath Milestones
- [ ] 0.9.1.0.9.4  (d) Display each Issue number and title
- [ ] 0.9.1.0.9.5  (e) Reuse a common Issue tree helper
- [ ] 0.9.1.0.9.6  (f) Verify each Issue appears beneath the correct parent

#### 0.9.1.0.10 Display Requirements
<!-- GitMap-ID: nrredslq -->

Display each Issue's Requirement separately from its actionable Work Steps.

**Requirements:**
- Display Requirements as italicized non-checkbox text beneath their parent Issue.
- [ ] 0.9.1.0.10.1  (a) Read the Requirement from `issue.requirements`
- [ ] 0.9.1.0.10.2  (b) Create a tree item for the Requirement
- [ ] 0.9.1.0.10.3  (c) Remove Markdown checkbox syntax if encountered in legacy content
- [ ] 0.9.1.0.10.4  (d) Display the Requirement without a GUI checkbox
- [ ] 0.9.1.0.10.5  (e) Apply an italic font to the Requirement
- [ ] 0.9.1.0.10.6  (f) Verify the Requirement is visually distinct from Work Steps

#### 0.9.1.0.11 Display Work Steps
<!-- GitMap-ID: orredslp -->

Display an Issue's actionable Work Steps beneath the Issue and preserve their markers and completion state.

**Requirements:**
- Display Work Steps separately from Requirements with their marker, text and completion state.
- [ ] 0.9.1.0.11.1  (a) Iterate through `issue.work_steps`
- [ ] 0.9.1.0.11.2  (b) Create a tree item for each Work Step
- [ ] 0.9.1.0.11.3  (c) Display each Work Step marker
- [ ] 0.9.1.0.11.4  (d) Display each Work Step title
- [ ] 0.9.1.0.11.5  (e) Represent the Work Step completion state
- [ ] 0.9.1.0.11.6  (f) Verify Work Steps appear beneath the correct Issue

#### 0.9.1.0.12 Apply GitMap GUI Colors
<!-- GitMap-ID: prredslo -->

Carry GitMap's established command-line color conventions into the graphical roadmap display.

**Requirements:**
- Use the established CLI semantic colors in the GUI where practical while keeping the roadmap readable and preserving the italic Requirement distinction.
- [ ] 0.9.1.0.12.1  (a) Identify the semantic colors used by the GitMap CLI
- [ ] 0.9.1.0.12.2  (b) Map the CLI colors to GUI hierarchy types
- [ ] 0.9.1.0.12.3  (c) Apply the Milestone color
- [ ] 0.9.1.0.12.4  (d) Apply the Section color
- [ ] 0.9.1.0.12.5  (e) Apply the Feature color
- [ ] 0.9.1.0.12.6  (f) Apply the Issue color
- [ ] 0.9.1.0.12.7  (g) Apply appropriate Requirement and Work Step styling
- [ ] 0.9.1.0.12.8  (h) Verify the complete tree remains easy to read

### 0.9.2 Open Existing Roadmaps
<!-- GitMap-ID: hwredsgw -->

Allow users to open existing GitMap roadmap files and display them in the desktop workspace using the existing GitMap parser.

#### 0.9.2.0.1 Open a Roadmap File
<!-- GitMap-ID: qrredsln -->

Allow the user to select an existing roadmap using the desktop interface.

**Requirements:**
- Provide a graphical Open Roadmap workflow for selecting an existing GitMap roadmap file.
- [ ] 0.9.2.0.1.1  (a) Connect the Open Roadmap button
- [ ] 0.9.2.0.1.2  (b) Display a `QFileDialog`
- [ ] 0.9.2.0.1.3  (c) Allow Markdown roadmap files to be selected
- [ ] 0.9.2.0.1.4  (d) Return without changing the active roadmap when the dialog is cancelled
- [ ] 0.9.2.0.1.5  (e) Preserve the selected roadmap path

#### 0.9.2.0.2 Parse an Opened Roadmap
<!-- GitMap-ID: rrredslm -->

Pass the selected roadmap through GitMap's existing parser rather than implementing separate GUI parsing logic.

**Requirements:**
- Parse roadmaps opened by the GUI using the existing `parse_roadmap` behavior.
- [ ] 0.9.2.0.2.1  (a) Pass the selected path to `parse_roadmap`
- [ ] 0.9.2.0.2.2  (b) Receive the populated Roadmap model
- [ ] 0.9.2.0.2.3  (c) Preserve hierarchy configuration
- [ ] 0.9.2.0.2.4  (d) Preserve permanent GitMap IDs
- [ ] 0.9.2.0.2.5  (e) Make the parsed Roadmap the active GUI model

#### 0.9.2.0.3 Populate the Workspace
<!-- GitMap-ID: srredsll -->

Display a successfully parsed Roadmap model in the main workspace.

**Requirements:**
- Populate the same main workspace with successfully opened and newly created roadmaps.
- [ ] 0.9.2.0.3.1  (a) Clear the previous roadmap tree
- [ ] 0.9.2.0.3.2  (b) Display the opened roadmap name
- [ ] 0.9.2.0.3.3  (c) Populate the roadmap hierarchy
- [ ] 0.9.2.0.3.4  (d) Display Requirements and Work Steps
- [ ] 0.9.2.0.3.5  (e) Expand the initial tree
- [ ] 0.9.2.0.3.6  (f) Transition to the active-roadmap state

#### 0.9.2.0.4 Handle Roadmap Opening Errors
<!-- GitMap-ID: trredslk -->

Handle inaccessible, malformed or otherwise invalid roadmap files without crashing the desktop application.

**Requirements:**
- Report roadmap opening failures graphically while leaving the currently active roadmap unchanged.
- [ ] 0.9.2.0.4.1  (a) Catch file opening failures
- [ ] 0.9.2.0.4.2  (b) Catch parser failures
- [ ] 0.9.2.0.4.3  (c) Display a Qt error dialog
- [ ] 0.9.2.0.4.4  (d) Include useful error information
- [ ] 0.9.2.0.4.5  (e) Leave the existing roadmap intact after a failed open
- [ ] 0.9.2.0.4.6  (f) Preserve diagnostic information for development

### 0.9.3 Create New Roadmaps
<!-- GitMap-ID: iwredsgv -->

Allow users to create new roadmaps by selecting their desired hierarchy before entering an unsaved main workspace.

#### 0.9.3.0.1 Create the Structure Dialog
<!-- GitMap-ID: urredslj -->

Create a separate Qt Designer dialog for configuring the structure of a new roadmap.

**Requirements:**
- Open a graphical structure configuration dialog before creating a new in-memory roadmap.
- [ ] 0.9.3.0.1.1  (a) Create `structure_dialog.ui`
- [ ] 0.9.3.0.1.2  (b) Load the structure dialog from Python
- [ ] 0.9.3.0.1.3  (c) Connect Create Roadmap to the structure dialog
- [ ] 0.9.3.0.1.4  (d) Add structure controls
- [ ] 0.9.3.0.1.5  (e) Add the live example area
- [ ] 0.9.3.0.1.6  (f) Add Create and Cancel actions

#### 0.9.3.0.2 Configure Sections
<!-- GitMap-ID: vrredsli -->

Allow Sections to be enabled or disabled when creating a new roadmap.

**Requirements:**
- Allow new roadmaps to use or omit Sections and disable Section-dependent options when Sections are unavailable.
- [ ] 0.9.3.0.2.1  (a) Add Use Sections
- [ ] 0.9.3.0.2.2  (b) Enable Section-dependent controls when Sections are selected
- [ ] 0.9.3.0.2.3  (c) Disable and grey Section-dependent controls when Sections are not selected
- [ ] 0.9.3.0.2.4  (d) Update the live structure example

#### 0.9.3.0.3 Configure Features
<!-- GitMap-ID: wrredslh -->

Allow Features to be enabled or disabled where the selected hierarchy supports them.

**Requirements:**
- Allow new roadmaps to use or omit Features while keeping unavailable Feature controls visible but disabled.
- [ ] 0.9.3.0.3.1  (a) Add Use Features
- [ ] 0.9.3.0.3.2  (b) Enable Feature-dependent controls when Features are selected
- [ ] 0.9.3.0.3.3  (c) Disable and grey Feature-dependent controls when Features are unavailable
- [ ] 0.9.3.0.3.4  (d) Update the live structure example

#### 0.9.3.0.4 Configure Issue Placement
<!-- GitMap-ID: xrredslg -->

Control which enabled hierarchy levels may directly contain Issues.

**Requirements:**
- Allow only valid Issue placement choices based on the hierarchy selected for the new roadmap.
- [ ] 0.9.3.0.4.1  (a) Add Allow Issues under Sections
- [ ] 0.9.3.0.4.2  (b) Add Allow Issues under Features
- [ ] 0.9.3.0.4.3  (c) Disable Section Issue placement when Sections are disabled
- [ ] 0.9.3.0.4.4  (d) Disable Feature Issue placement when Features are disabled
- [ ] 0.9.3.0.4.5  (e) Validate the final configuration
- [ ] 0.9.3.0.4.6  (f) Update the live example after each change

#### 0.9.3.0.5 Create the Baseball Parks Example
<!-- GitMap-ID: yrredslf -->

Show a live example of how the selected hierarchy organizes roadmap content.

**Requirements:**
- Display a rendered Baseball Parks example that updates to demonstrate the currently selected roadmap structure.
- [ ] 0.9.3.0.5.1  (a) Add MLB Parks as the primary example Milestone
- [ ] 0.9.3.0.5.2  (b) Add American League and National League examples
- [ ] 0.9.3.0.5.3  (c) Add AL East and NL East when Features are enabled
- [ ] 0.9.3.0.5.4  (d) Add Camden Yards and Nationals Park Issues
- [ ] 0.9.3.0.5.5  (e) Add example Requirements and Work Steps
- [ ] 0.9.3.0.5.6  (f) Add a small NFL Stadiums example
- [ ] 0.9.3.0.5.7  (g) Update example numbering when the hierarchy changes

#### 0.9.3.0.6 Explain GitMap Hierarchy Levels
<!-- GitMap-ID: zrredsle -->

Explain how each GitMap hierarchy level can be used without prescribing a particular project structure.

**Requirements:**
- Explain Milestones, Sections, Features, Issues, Requirements and Work Steps as organizational concepts rather than mandatory project meanings.
- [ ] 0.9.3.0.6.1  (a) Explain Milestone as a major phase
- [ ] 0.9.3.0.6.2  (b) Explain Section as an area or subsystem
- [ ] 0.9.3.0.6.3  (c) Explain Feature as a feature or capability
- [ ] 0.9.3.0.6.4  (d) Explain Issue as a specific task
- [ ] 0.9.3.0.6.5  (e) Explain Requirements as what should be done
- [ ] 0.9.3.0.6.6  (f) Explain Work Steps as steps for doing it
- [ ] 0.9.3.0.6.7  (g) Explain that the Baseball Parks example demonstrates organization rather than a prescribed structure

#### 0.9.3.0.7 Create an Unsaved Roadmap Workspace
<!-- GitMap-ID: arredsld -->

Create the Roadmap model after structure selection without forcing the user to choose a file location.

**Requirements:**
- Create a usable in-memory roadmap immediately after structure setup without automatically creating a file.
- [ ] 0.9.3.0.7.1  (a) Create the Roadmap model
- [ ] 0.9.3.0.7.2  (b) Apply the selected structure settings
- [ ] 0.9.3.0.7.3  (c) Populate the main workspace
- [ ] 0.9.3.0.7.4  (d) Mark the roadmap as unsaved
- [ ] 0.9.3.0.7.5  (e) Enable roadmap editing controls
- [ ] 0.9.3.0.7.6  (f) Verify no file is created automatically

### 0.9.4 Roadmap Navigation
<!-- GitMap-ID: jwredsgu -->

Make the graphical roadmap hierarchy interactive while keeping the main workspace available.

#### 0.9.4.0.1 Associate Tree Items With Model Objects
<!-- GitMap-ID: drredsla -->

Maintain a connection between displayed tree items and their underlying GitMap model objects.

**Requirements:**
- Resolve each editable graphical roadmap item back to the model object it represents.
- [ ] 0.9.4.0.1.1  (a) Choose a safe model association mechanism
- [ ] 0.9.4.0.1.2  (b) Associate Milestone tree items
- [ ] 0.9.4.0.1.3  (c) Associate Section tree items
- [ ] 0.9.4.0.1.4  (d) Associate Feature tree items
- [ ] 0.9.4.0.1.5  (e) Associate Issue tree items
- [ ] 0.9.4.0.1.6  (f) Verify associations remain correct after tree refreshes

#### 0.9.4.0.2 Select Roadmap Items
<!-- GitMap-ID: erredslz -->

Allow users to select items in the graphical hierarchy for further actions.

**Requirements:**
- Track the selected roadmap object and enable only actions valid for its type and location.
- [ ] 0.9.4.0.2.1  (a) Detect tree selection changes
- [ ] 0.9.4.0.2.2  (b) Resolve the selected model object
- [ ] 0.9.4.0.2.3  (c) Determine actions valid for the selected object
- [ ] 0.9.4.0.2.4  (d) Enable valid actions
- [ ] 0.9.4.0.2.5  (e) Disable invalid actions

#### 0.9.4.0.3 Open Items From the Tree
<!-- GitMap-ID: frredsly -->

Open editable roadmap items directly from the graphical roadmap hierarchy.

**Requirements:**
- Open the appropriate pop-out Item Editor when an editable roadmap item is double-clicked without replacing the main workspace.
- [ ] 0.9.4.0.3.1  (a) Detect tree double-clicks
- [ ] 0.9.4.0.3.2  (b) Resolve the clicked model object
- [ ] 0.9.4.0.3.3  (c) Determine whether the object is editable
- [ ] 0.9.4.0.3.4  (d) Open the appropriate Item Editor
- [ ] 0.9.4.0.3.5  (e) Leave the main workspace open

### 0.9.5 Item Editors
<!-- GitMap-ID: kwredsgt -->

Provide pop-out windows for editing roadmap content without replacing the main roadmap workspace.

#### 0.9.5.0.1 Create the Item Editor Window
<!-- GitMap-ID: gsredskx -->

Create a reusable graphical window for editing roadmap items.

**Requirements:**
- Provide a pop-out Item Editor that operates on the selected in-memory roadmap object while leaving the main workspace open.
- [ ] 0.9.5.0.1.1  (a) Create `item_editor.ui`
- [ ] 0.9.5.0.1.2  (b) Load the Item Editor from Python
- [ ] 0.9.5.0.1.3  (c) Associate the editor with a model object
- [ ] 0.9.5.0.1.4  (d) Add controls for applying changes
- [ ] 0.9.5.0.1.5  (e) Add Cancel or Close behavior

#### 0.9.5.0.2 Adapt the Editor to Item Type
<!-- GitMap-ID: hsredskw -->

Configure the Item Editor according to the type of roadmap object being edited.

**Requirements:**
- Show only editing controls that are valid for the selected Milestone, Section, Feature or Issue.
- [ ] 0.9.5.0.2.1  (a) Detect the selected item type
- [ ] 0.9.5.0.2.2  (b) Configure the editor for Milestones
- [ ] 0.9.5.0.2.3  (c) Configure the editor for Sections
- [ ] 0.9.5.0.2.4  (d) Configure the editor for Features
- [ ] 0.9.5.0.2.5  (e) Configure the editor for Issues

#### 0.9.5.0.3 Edit Item Content
<!-- GitMap-ID: isredskv -->

Edit supported roadmap titles and descriptions.

**Requirements:**
- Apply valid title and description edits to the in-memory model and refresh the workspace without automatically synchronizing GitHub.
- [ ] 0.9.5.0.3.1  (a) Populate the title control
- [ ] 0.9.5.0.3.2  (b) Populate the description control
- [ ] 0.9.5.0.3.3  (c) Validate edited values
- [ ] 0.9.5.0.3.4  (d) Apply approved changes to the model
- [ ] 0.9.5.0.3.5  (e) Refresh the roadmap tree
- [ ] 0.9.5.0.3.6  (f) Mark the roadmap as modified

#### 0.9.5.0.4 Edit Requirements
<!-- GitMap-ID: jsredsku -->

Manage an Issue's Requirements graphically.

**Requirements:**
- Allow Requirements to be viewed, added, edited and removed independently from Work Steps.
- [ ] 0.9.5.0.4.1  (a) Display the existing Requirement
- [ ] 0.9.5.0.4.2  (b) Add a Requirement
- [ ] 0.9.5.0.4.3  (c) Edit Requirement text
- [ ] 0.9.5.0.4.4  (d) Remove a Requirement
- [ ] 0.9.5.0.4.5  (e) Refresh the roadmap tree

#### 0.9.5.0.5 Edit Work Steps
<!-- GitMap-ID: ksredskt -->

Manage an Issue's Work Steps graphically.

**Requirements:**
- Allow Work Steps to be added, edited, completed and removed while maintaining correct numbering and markers.
- [ ] 0.9.5.0.5.1  (a) Display existing Work Steps
- [ ] 0.9.5.0.5.2  (b) Add a Work Step
- [ ] 0.9.5.0.5.3  (c) Assign the next Work Step marker
- [ ] 0.9.5.0.5.4  (d) Edit Work Step text
- [ ] 0.9.5.0.5.5  (e) Change Work Step completion state
- [ ] 0.9.5.0.5.6  (f) Remove a Work Step
- [ ] 0.9.5.0.5.7  (g) Renumber Work Step markers when required
- [ ] 0.9.5.0.5.8  (h) Refresh the roadmap tree

### 0.9.6 Add, Insert and Delete Roadmap Items
<!-- GitMap-ID: lwredsgs -->

Expose GitMap's existing hierarchy and automatic numbering operations through graphical controls.

#### 0.9.6.0.1 Add Valid Child Items
<!-- GitMap-ID: lsredsks -->

Add new roadmap items beneath compatible parent items.

**Requirements:**
- Offer only child item types permitted by the selected parent and the active roadmap's hierarchy configuration.
- [ ] 0.9.6.0.1.1  (a) Determine the selected parent type
- [ ] 0.9.6.0.1.2  (b) Read the roadmap hierarchy configuration
- [ ] 0.9.6.0.1.3  (c) Determine valid child types
- [ ] 0.9.6.0.1.4  (d) Present only valid choices
- [ ] 0.9.6.0.1.5  (e) Create the selected child using automatic numbering
- [ ] 0.9.6.0.1.6  (f) Refresh the roadmap tree

#### 0.9.6.0.2 Insert Items Between Existing Siblings
<!-- GitMap-ID: msredskr -->

Use GitMap's automatic numbering logic to insert items at a selected sibling position.

**Requirements:**
- Insert items between existing siblings without requiring the user to manually calculate or repair roadmap numbers.
- [ ] 0.9.6.0.2.1  (a) Display valid insertion positions
- [ ] 0.9.6.0.2.2  (b) Let the user choose a position
- [ ] 0.9.6.0.2.3  (c) Use GitMap's sibling numbering logic
- [ ] 0.9.6.0.2.4  (d) Determine affected descendants
- [ ] 0.9.6.0.2.5  (e) Generate the numbering preview
- [ ] 0.9.6.0.2.6  (f) Apply the insertion only after approval

#### 0.9.6.0.3 Delete Roadmap Items Safely
<!-- GitMap-ID: nsredskq -->

Delete roadmap items while previewing any hierarchy or numbering consequences.

**Requirements:**
- Require confirmation of the item, descendant and numbering effects before applying a destructive roadmap deletion.
- [ ] 0.9.6.0.3.1  (a) Select the item to delete
- [ ] 0.9.6.0.3.2  (b) Determine its descendants
- [ ] 0.9.6.0.3.3  (c) Determine resulting numbering changes
- [ ] 0.9.6.0.3.4  (d) Display the proposed deletion
- [ ] 0.9.6.0.3.5  (e) Display numbering changes
- [ ] 0.9.6.0.3.6  (f) Allow approval or cancellation
- [ ] 0.9.6.0.3.7  (g) Apply only the approved deletion
- [ ] 0.9.6.0.3.8  (h) Refresh the roadmap tree

### 0.9.7 Graphical Change Preview
<!-- GitMap-ID: mwredsgr -->

Provide a graphical version of GitMap's preview-before-change workflow.

#### 0.9.7.0.1 Create the Roadmap Preview Window
<!-- GitMap-ID: osredskp -->

Create a separate graphical window for reviewing proposed roadmap changes.

**Requirements:**
- Display proposed changes in a scrollable pop-out preview while leaving the main roadmap workspace available.
- [ ] 0.9.7.0.1.1  (a) Create `preview_dialog.ui`
- [ ] 0.9.7.0.1.2  (b) Load the preview interface from Python
- [ ] 0.9.7.0.1.3  (c) Add a scrollable change area
- [ ] 0.9.7.0.1.4  (d) Add Approve and Cancel actions
- [ ] 0.9.7.0.1.5  (e) Keep the main workspace available

#### 0.9.7.0.2 Display Before and After Changes
<!-- GitMap-ID: psredsko -->

Show the original and proposed state of affected roadmap items.

**Requirements:**
- Make hierarchy, numbering, additions, changes and removals understandable before a proposed operation is approved.
- [ ] 0.9.7.0.2.1  (a) Collect the original state
- [ ] 0.9.7.0.2.2  (b) Collect the proposed state
- [ ] 0.9.7.0.2.3  (c) Display before values
- [ ] 0.9.7.0.2.4  (d) Display after values
- [ ] 0.9.7.0.2.5  (e) Highlight added items
- [ ] 0.9.7.0.2.6  (f) Highlight changed items
- [ ] 0.9.7.0.2.7  (g) Highlight removed items

#### 0.9.7.0.3 Cancel Previewed Changes
<!-- GitMap-ID: qsredskn -->

Restore the original roadmap state when the user cancels a proposed operation.

**Requirements:**
- Leave the roadmap exactly as it was before the proposed operation when a preview is cancelled.
- [ ] 0.9.7.0.3.1  (a) Preserve the original state before generating changes
- [ ] 0.9.7.0.3.2  (b) Detect cancellation
- [ ] 0.9.7.0.3.3  (c) Restore original numbering
- [ ] 0.9.7.0.3.4  (d) Restore original hierarchy
- [ ] 0.9.7.0.3.5  (e) Refresh the roadmap tree
- [ ] 0.9.7.0.3.6  (f) Verify cancellation produces no saved changes

### 0.9.8 Save Roadmaps
<!-- GitMap-ID: nwredsgq -->

Save the in-memory roadmap independently from the roadmap creation workflow.

#### 0.9.8.0.1 Save an Existing Roadmap
<!-- GitMap-ID: rsredskm -->

Write changes to the active roadmap file.

**Requirements:**
- Save an existing roadmap to its current path while preserving valid GitMap Markdown and permanent identities.
- [ ] 0.9.8.0.1.1  (a) Determine the active roadmap path
- [ ] 0.9.8.0.1.2  (b) Serialize the in-memory Roadmap
- [ ] 0.9.8.0.1.3  (c) Write the roadmap file
- [ ] 0.9.8.0.1.4  (d) Mark the roadmap as saved
- [ ] 0.9.8.0.1.5  (e) Update GUI status

#### 0.9.8.0.2 Save a New Roadmap
<!-- GitMap-ID: ssredskl -->

Choose a file location the first time an unsaved roadmap is saved.

**Requirements:**
- Prompt for a destination when saving an unsaved roadmap and make the successful destination its active file.
- [ ] 0.9.8.0.2.1  (a) Detect that the roadmap has no active path
- [ ] 0.9.8.0.2.2  (b) Open a save dialog
- [ ] 0.9.8.0.2.3  (c) Write the roadmap to the selected path
- [ ] 0.9.8.0.2.4  (d) Store the selected path
- [ ] 0.9.8.0.2.5  (e) Change the roadmap from unsaved to saved

#### 0.9.8.0.3 Save As
<!-- GitMap-ID: tsredskk -->

Write the active roadmap to a user-selected new file.

**Requirements:**
- Save the current roadmap to a different path and make that path active after the operation succeeds.
- [ ] 0.9.8.0.3.1  (a) Add Save As
- [ ] 0.9.8.0.3.2  (b) Open the Save As dialog
- [ ] 0.9.8.0.3.3  (c) Write the current roadmap to the selected path
- [ ] 0.9.8.0.3.4  (d) Update the active roadmap path
- [ ] 0.9.8.0.3.5  (e) Update the window state

#### 0.9.8.0.4 Track Modified Roadmaps
<!-- GitMap-ID: usredskj -->

Track whether the in-memory roadmap differs from its last saved state.

**Requirements:**
- Maintain and display an accurate modified state for the active roadmap.
- [ ] 0.9.8.0.4.1  (a) Establish a modified-state flag
- [ ] 0.9.8.0.4.2  (b) Mark content edits as modified
- [ ] 0.9.8.0.4.3  (c) Mark structural changes as modified
- [ ] 0.9.8.0.4.4  (d) Clear modified state after a successful save
- [ ] 0.9.8.0.4.5  (e) Indicate modified state in the GUI

#### 0.9.8.0.5 Protect Unsaved Work
<!-- GitMap-ID: vsredski -->

Prevent unsaved changes from being silently discarded.

**Requirements:**
- Prompt before closing or replacing an active roadmap that contains unsaved changes.
- [ ] 0.9.8.0.5.1  (a) Detect unsaved changes before replacement
- [ ] 0.9.8.0.5.2  (b) Offer Save
- [ ] 0.9.8.0.5.3  (c) Offer Discard
- [ ] 0.9.8.0.5.4  (d) Offer Cancel
- [ ] 0.9.8.0.5.5  (e) Stop the requested operation when Cancel is selected
- [ ] 0.9.8.0.5.6  (f) Verify application closing also protects unsaved work

### 0.9.9 Roadmap Settings
<!-- GitMap-ID: owredsgp -->

Provide graphical access to supported configuration for the active roadmap.

#### 0.9.9.0.1 Create Roadmap Settings
<!-- GitMap-ID: wsredskh -->

Create a graphical settings interface for viewing the active roadmap's configuration.

**Requirements:**
- Display supported configuration values from the active Roadmap model in a dedicated settings interface.
- [ ] 0.9.9.0.1.1  (a) Create the settings interface
- [ ] 0.9.9.0.1.2  (b) Load settings from the active Roadmap
- [ ] 0.9.9.0.1.3  (c) Display numbering configuration
- [ ] 0.9.9.0.1.4  (d) Display hierarchy configuration
- [ ] 0.9.9.0.1.5  (e) Display hierarchy Issue title style

#### 0.9.9.0.2 Safely Modify Roadmap Settings
<!-- GitMap-ID: xsredskg -->

Allow supported settings to change without bypassing validation or preview protections.

**Requirements:**
- Validate settings changes and preview any changes that would alter existing roadmap numbering or hierarchy.
- [ ] 0.9.9.0.2.1  (a) Determine editable settings
- [ ] 0.9.9.0.2.2  (b) Validate proposed settings
- [ ] 0.9.9.0.2.3  (c) Determine whether existing items are affected
- [ ] 0.9.9.0.2.4  (d) Generate a preview when required
- [ ] 0.9.9.0.2.5  (e) Apply only approved changes
- [ ] 0.9.9.0.2.6  (f) Refresh the workspace

### 0.9.10 GitHub Synchronization
<!-- GitMap-ID: pwredsgo -->

Expose GitMap's existing protected GitHub synchronization workflow through the desktop application.

#### 0.9.10.0.1 Start Synchronization From the GUI
<!-- GitMap-ID: luredsis -->

Begin synchronization using a graphical action in the main workspace.

**Requirements:**
- Start synchronization through the existing GitMap synchronization system without bypassing discovery, mapping, validation or preview behavior.
- [ ] 0.9.10.0.1.1  (a) Add the synchronization action
- [ ] 0.9.10.0.1.2  (b) Validate the active roadmap
- [ ] 0.9.10.0.1.3  (c) Start existing GitHub discovery
- [ ] 0.9.10.0.1.4  (d) Build the synchronization plan
- [ ] 0.9.10.0.1.5  (e) Pass the plan to graphical preview

#### 0.9.10.0.2 Display the Synchronization Preview
<!-- GitMap-ID: mvredshr -->

Display the existing GitMap synchronization preview graphically.

**Requirements:**
- Clearly distinguish added, changed, unchanged and removed GitHub items before synchronization approval.
- [ ] 0.9.10.0.2.1  (a) Display summary counts
- [ ] 0.9.10.0.2.2  (b) Display added items
- [ ] 0.9.10.0.2.3  (c) Display changed items
- [ ] 0.9.10.0.2.4  (d) Display unchanged items when requested
- [ ] 0.9.10.0.2.5  (e) Display removed items
- [ ] 0.9.10.0.2.6  (f) Provide approval and cancellation

#### 0.9.10.0.3 Apply Only Approved GitHub Changes
<!-- GitMap-ID: nvredshq -->

Preserve GitMap's approval boundary when synchronization is controlled through the GUI.

**Requirements:**
- Allow only GitHub operations contained in the approved synchronization plan to modify existing GitHub state.
- [ ] 0.9.10.0.3.1  (a) Preserve the approved synchronization plan
- [ ] 0.9.10.0.3.2  (b) Reject operations absent from the approved plan
- [ ] 0.9.10.0.3.3  (c) Apply approved creations
- [ ] 0.9.10.0.3.4  (d) Apply approved updates
- [ ] 0.9.10.0.3.5  (e) Apply approved closures
- [ ] 0.9.10.0.3.6  (f) Verify cancellation modifies nothing

#### 0.9.10.0.4 Display Synchronization Results
<!-- GitMap-ID: ovredshp -->

Show the outcome of synchronization inside the graphical interface.

**Requirements:**
- Display created, updated, closed, skipped and failed synchronization operations without requiring the development console.
- [ ] 0.9.10.0.4.1  (a) Collect synchronization results
- [ ] 0.9.10.0.4.2  (b) Display created items
- [ ] 0.9.10.0.4.3  (c) Display updated items
- [ ] 0.9.10.0.4.4  (d) Display closed items
- [ ] 0.9.10.0.4.5  (e) Display skipped operations
- [ ] 0.9.10.0.4.6  (f) Display failures
- [ ] 0.9.10.0.4.7  (g) Refresh the roadmap workspace after synchronization

### 0.9.11 User Feedback and Error Handling
<!-- GitMap-ID: qwredsgn -->

Provide graphical feedback for normal GitMap operations and expected application failures.

#### 0.9.11.0.1 Use the Status Bar
<!-- GitMap-ID: pvredsho -->

Use the main window status bar for lightweight feedback.

**Requirements:**
- Report routine application status without unnecessarily interrupting the user's workflow.
- [ ] 0.9.11.0.1.1  (a) Locate the Designer status bar
- [ ] 0.9.11.0.1.2  (b) Display roadmap-open status
- [ ] 0.9.11.0.1.3  (c) Display save status
- [ ] 0.9.11.0.1.4  (d) Display validation status
- [ ] 0.9.11.0.1.5  (e) Display synchronization status

#### 0.9.11.0.2 Display User-Friendly Errors
<!-- GitMap-ID: qvredshn -->

Present expected application failures as understandable graphical messages.

**Requirements:**
- Display useful graphical error messages while preserving more detailed diagnostic information for development.
- [ ] 0.9.11.0.2.1  (a) Create a common GUI error-display helper
- [ ] 0.9.11.0.2.2  (b) Handle roadmap file errors
- [ ] 0.9.11.0.2.3  (c) Handle parser errors
- [ ] 0.9.11.0.2.4  (d) Handle validation errors
- [ ] 0.9.11.0.2.5  (e) Handle save errors
- [ ] 0.9.11.0.2.6  (f) Handle GitHub errors
- [ ] 0.9.11.0.2.7  (g) Preserve useful diagnostic logging

### 0.9.12 Desktop Application Behavior
<!-- GitMap-ID: rwredsgm -->

Make GitMap behave like a normal desktop application.

#### 0.9.12.0.1 Add Standard Keyboard Shortcuts
<!-- GitMap-ID: rvredshm -->

Provide familiar keyboard shortcuts for common desktop actions.

**Requirements:**
- Use standard desktop shortcuts for common GitMap actions where they do not conflict with application behavior.
- [ ] 0.9.12.0.1.1  (a) Add Ctrl+O for Open
- [ ] 0.9.12.0.1.2  (b) Add Ctrl+S for Save
- [ ] 0.9.12.0.1.3  (c) Add a Save As shortcut
- [ ] 0.9.12.0.1.4  (d) Add appropriate new-roadmap navigation
- [ ] 0.9.12.0.1.5  (e) Verify shortcuts do not conflict with Item Editors

#### 0.9.12.0.2 Support Normal Desktop Window Behavior
<!-- GitMap-ID: svredshl -->

Manage the relationship between the main workspace and GitMap's pop-out windows.

**Requirements:**
- Allow editors, previews and dialogs to behave as normal child windows without unexpectedly closing or replacing the main workspace.
- [ ] 0.9.12.0.2.1  (a) Establish ownership for dialogs
- [ ] 0.9.12.0.2.2  (b) Establish ownership for Item Editors
- [ ] 0.9.12.0.2.3  (c) Establish ownership for Preview windows
- [ ] 0.9.12.0.2.4  (d) Test multiple simultaneous Item Editors
- [ ] 0.9.12.0.2.5  (e) Test closing individual child windows
- [ ] 0.9.12.0.2.6  (f) Test closing the main application

### 0.9.13 Preserve the GitMap Core Architecture
<!-- GitMap-ID: swredsgl -->

Keep the desktop GUI as an interface to the existing GitMap system rather than creating a separate implementation.

#### 0.9.13.0.1 Reuse the Existing Parser
<!-- GitMap-ID: tvredshk -->

Use GitMap's established parser for GUI roadmap loading.

**Requirements:**
- Use the existing GitMap parser as the authoritative parser for roadmaps opened by the desktop interface.
- [ ] 0.9.13.0.1.1  (a) Route GUI file loading through `parse_roadmap`
- [ ] 0.9.13.0.1.2  (b) Preserve parser behavior shared with the CLI
- [ ] 0.9.13.0.1.3  (c) Verify representative existing roadmaps

#### 0.9.13.0.2 Reuse the Existing Model
<!-- GitMap-ID: uvredshj -->

Use the existing GitMap model as the application's roadmap state.

**Requirements:**
- Keep the existing Roadmap model and its hierarchy objects authoritative for GUI state and editing.
- [ ] 0.9.13.0.2.1  (a) Store the active Roadmap model
- [ ] 0.9.13.0.2.2  (b) Read hierarchy data from existing model classes
- [ ] 0.9.13.0.2.3  (c) Apply GUI edits to existing model classes
- [ ] 0.9.13.0.2.4  (d) Avoid introducing duplicate GUI-only roadmap models

#### 0.9.13.0.3 Reuse Automatic Numbering
<!-- GitMap-ID: vvredshi -->

Use GitMap's existing automatic numbering system for graphical roadmap changes.

**Requirements:**
- Route GUI creation, insertion and renumbering operations through the existing automatic numbering behavior.
- [ ] 0.9.13.0.3.1  (a) Reuse sibling-number calculation
- [ ] 0.9.13.0.3.2  (b) Reuse insertion numbering
- [ ] 0.9.13.0.3.3  (c) Reuse descendant renumbering
- [ ] 0.9.13.0.3.4  (d) Preserve Work Step marker behavior
- [ ] 0.9.13.0.3.5  (e) Verify numbering results match CLI behavior

#### 0.9.13.0.4 Reuse Validation
<!-- GitMap-ID: wvredshh -->

Use existing GitMap validation before applying graphical roadmap changes.

**Requirements:**
- Apply the existing roadmap validation rules to GUI operations rather than creating weaker GUI-specific rules.
- [ ] 0.9.13.0.4.1  (a) Validate edited roadmaps
- [ ] 0.9.13.0.4.2  (b) Validate hierarchy changes
- [ ] 0.9.13.0.4.3  (c) Detect duplicate numbers
- [ ] 0.9.13.0.4.4  (d) Detect invalid structures
- [ ] 0.9.13.0.4.5  (e) Display validation failures graphically

#### 0.9.13.0.5 Reuse GitHub Mapping
<!-- GitMap-ID: bvredshc -->

Use GitMap's existing identity, mapping and synchronization protections from the desktop GUI.

**Requirements:**
- Preserve existing GitHub mapping, permanent identity, roadmap-specific searching, hierarchy and approval protections when synchronizing through the GUI.
- [ ] 0.9.13.0.5.1  (a) Route GUI synchronization through existing GitHub mapping
- [ ] 0.9.13.0.5.2  (b) Preserve permanent GitMap IDs
- [ ] 0.9.13.0.5.3  (c) Preserve roadmap-specific searching
- [ ] 0.9.13.0.5.4  (d) Preserve parent and child GitHub relationships
- [ ] 0.9.13.0.5.5  (e) Preserve Issue identity during renumbering
- [ ] 0.9.13.0.5.6  (f) Preserve approval before modifying existing GitHub items

### 0.9.14 GUI Integration Testing
<!-- GitMap-ID: twredsgk -->

Verify the complete desktop workflow against existing GitMap behavior.

#### 0.9.14.0.1 Test Existing Roadmaps
<!-- GitMap-ID: cvredshb -->

Verify that existing roadmap files work correctly in the desktop interface.

**Requirements:**
- Open and display representative existing GitMap roadmaps without changing their intended hierarchy or content.
- [ ] 0.9.14.0.1.1  (a) Test a roadmap using Sections and Features
- [ ] 0.9.14.0.1.2  (b) Test a featureless roadmap
- [ ] 0.9.14.0.1.3  (c) Test Issues directly beneath Sections
- [ ] 0.9.14.0.1.4  (d) Test Issues directly beneath Milestones
- [ ] 0.9.14.0.1.5  (e) Verify Requirements
- [ ] 0.9.14.0.1.6  (f) Verify Work Steps

#### 0.9.14.0.2 Test New Roadmap Creation
<!-- GitMap-ID: dvredsha -->

Verify each supported new-roadmap structure configuration.

**Requirements:**
- Create valid in-memory roadmaps for every hierarchy configuration offered by the structure dialog.
- [ ] 0.9.14.0.2.1  (a) Test Sections with Features
- [ ] 0.9.14.0.2.2  (b) Test Sections without Features
- [ ] 0.9.14.0.2.3  (c) Test supported no-Section structures
- [ ] 0.9.14.0.2.4  (d) Test Issue placement choices
- [ ] 0.9.14.0.2.5  (e) Verify the resulting roadmap model

#### 0.9.14.0.3 Test Editing and Numbering
<!-- GitMap-ID: evredshz -->

Verify graphical editing preserves GitMap's automatic numbering rules.

**Requirements:**
- Produce the same valid hierarchy and numbering results through GUI editing that GitMap produces through its existing logic.
- [ ] 0.9.14.0.3.1  (a) Add roadmap items
- [ ] 0.9.14.0.3.2  (b) Insert between siblings
- [ ] 0.9.14.0.3.3  (c) Delete roadmap items
- [ ] 0.9.14.0.3.4  (d) Verify descendant renumbering
- [ ] 0.9.14.0.3.5  (e) Verify Work Step numbering and markers
- [ ] 0.9.14.0.3.6  (f) Cancel a numbering preview and verify rollback

#### 0.9.14.0.4 Test Saving and Unsaved Changes
<!-- GitMap-ID: fvredshy -->

Verify roadmap files can be safely created and modified through the GUI.

**Requirements:**
- Preserve roadmap content through Save, Save As, reopening and unsaved-change protection.
- [ ] 0.9.14.0.4.1  (a) Save a new roadmap
- [ ] 0.9.14.0.4.2  (b) Save changes to an existing roadmap
- [ ] 0.9.14.0.4.3  (c) Test Save As
- [ ] 0.9.14.0.4.4  (d) Reopen each saved roadmap
- [ ] 0.9.14.0.4.5  (e) Verify permanent GitMap IDs
- [ ] 0.9.14.0.4.6  (f) Verify unsaved-change protection

#### 0.9.14.0.5 Test GitHub Synchronization
<!-- GitMap-ID: gwredsgx -->

Verify that graphical synchronization preserves all existing GitMap protections.

**Requirements:**
- Produce the same protected GitHub synchronization results from the GUI as from the established GitMap synchronization workflow.
- [ ] 0.9.14.0.5.1  (a) Preview synchronization containing new items
- [ ] 0.9.14.0.5.2  (b) Preview synchronization containing changed items
- [ ] 0.9.14.0.5.3  (c) Preview synchronization containing removed items
- [ ] 0.9.14.0.5.4  (d) Cancel synchronization and verify GitHub remains unchanged
- [ ] 0.9.14.0.5.5  (e) Approve synchronization
- [ ] 0.9.14.0.5.6  (f) Verify only approved operations occurred
- [ ] 0.9.14.0.5.7  (g) Verify GitMap IDs remain associated with the correct GitHub Issues
- [ ] 0.9.14.0.5.8  (h) Verify GitHub parent and child relationships remain correct

# 0.10 Testing and Reliability

## 0.10.1 Automated Testing
<!-- GitMap-ID: xvredshg -->

#### 0.10.1.0.1 Test Roadmap Parsing
<!-- GitMap-ID: ysredskf -->

Test conversion of Markdown roadmaps into GitMap project data.

**Requirements:**
- Test conversion of Markdown roadmaps into GitMap project data.
- [ ] 0.10.1.0.1.1  (a) Test milestones
- [ ] 0.10.1.0.1.2  (b) Test Sections
- [ ] 0.10.1.0.1.3  (c) Test issues
- [ ] 0.10.1.0.1.4  (d) Test sub-issues
- [ ] 0.10.1.0.1.5  (e) Test descriptions and requirements

#### 0.10.1.0.2 Test Roadmap Validation
<!-- GitMap-ID: zsredske -->

Test detection of invalid roadmap structures.

**Requirements:**
- Test detection of invalid roadmap structures.
- [ ] 0.10.1.0.2.1  (a) Test malformed hierarchy
- [ ] 0.10.1.0.2.2  (b) Test duplicate numbering
- [ ] 0.10.1.0.2.3  (c) Test invalid parent relationships
- [ ] 0.10.1.0.2.4  (d) Test useful validation messages

#### 0.10.1.0.3 Test GitHub Mapping
<!-- GitMap-ID: asredskd -->

Test conversion of roadmap data into GitHub structures.

**Requirements:**
- Test conversion of roadmap data into GitHub structures.
- [ ] 0.10.1.0.3.1  (a) Test milestone mapping
- [ ] 0.10.1.0.3.2  (b) Test label mapping
- [ ] 0.10.1.0.3.3  (c) Test Section mapping
- [ ] 0.10.1.0.3.4  (d) Test issue mapping
- [ ] 0.10.1.0.3.5  (e) Test sub-issue relationships

#### 0.10.1.0.4 Test Duplicate Prevention
<!-- GitMap-ID: bsredskc -->

Verify that synchronization can safely run more than once.

**Requirements:**
- Verify that synchronization can safely run more than once.
- [ ] 0.10.1.0.4.1  (a) Test existing labels
- [ ] 0.10.1.0.4.2  (b) Test existing milestones
- [ ] 0.10.1.0.4.3  (c) Test existing issues
- [ ] 0.10.1.0.4.4  (d) Confirm repeated synchronization does not create duplicates

#### 0.10.1.0.5 Test Roadmap Updates
<!-- GitMap-ID: csredskb -->

Test synchronization after a roadmap has changed.

**Requirements:**
- Test synchronization after a roadmap has changed.
- [ ] 0.10.1.0.5.1  (a) Test newly added items
- [ ] 0.10.1.0.5.2  (b) Test changed items
- [ ] 0.10.1.0.5.3  (c) Test unchanged items
- [ ] 0.10.1.0.5.4  (d) Test removed roadmap items
- [ ] 0.10.1.0.5.5  (e) Confirm destructive changes are not automatic

## 0.10.2 Failure Protection
<!-- GitMap-ID: yvredshf -->

#### 0.10.2.0.1 Handle GitHub API Failures
<!-- GitMap-ID: dsredska -->

Handle failures while communicating with GitHub.

**Requirements:**
- Handle failures while communicating with GitHub.
- [ ] 0.10.2.0.1.1  (a) Detect API errors
- [ ] 0.10.2.0.1.2  (b) Report which operation failed
- [ ] 0.10.2.0.1.3  (c) Preserve useful error details
- [ ] 0.10.2.0.1.4  (d) Stop safely when synchronization cannot continue

#### 0.10.2.0.2 Test Dry Run Safety
<!-- GitMap-ID: esredskz -->

Verify that dry-run mode never changes GitHub.

**Requirements:**
- Verify that dry-run mode never changes GitHub.
- [ ] 0.10.2.0.2.1  (a) Exercise the complete synchronization path
- [ ] 0.10.2.0.2.2  (b) Confirm no create operations occur
- [ ] 0.10.2.0.2.3  (c) Confirm no update operations occur
- [ ] 0.10.2.0.2.4  (d) Confirm planned changes are still reported

#### 0.10.2.0.3 Add Integration Tests
<!-- GitMap-ID: fsredsky -->

Test complete GitMap workflows using representative roadmap data.

**Requirements:**
- Test complete GitMap workflows using representative roadmap data.
- [ ] 0.10.2.0.3.1  (a) Test roadmap creation through parsing
- [ ] 0.10.2.0.3.2  (b) Test parsing through synchronization planning
- [ ] 0.10.2.0.3.3  (c) Test existing-project update workflows
- [ ] 0.10.2.0.3.4  (d) Keep tests independent of a user's real GitHub repository where possible

# 0.11 Release Preparation

## 0.11.1 Documentation
<!-- GitMap-ID: zvredshe -->

#### 0.11.1.0.1 Complete README
<!-- GitMap-ID: gtredsjx -->

Create the main user-facing GitMap documentation.

**Requirements:**
- Create the main user-facing GitMap documentation.
- [ ] 0.11.1.0.1.1  (a) Explain what GitMap does
- [ ] 0.11.1.0.1.2  (b) Explain the roadmap-first workflow
- [ ] 0.11.1.0.1.3  (c) Explain installation
- [ ] 0.11.1.0.1.4  (d) Explain basic commands
- [ ] 0.11.1.0.1.5  (e) Provide a simple first-use example

#### 0.11.1.0.2 Create Roadmap Format Guide
<!-- GitMap-ID: htredsjw -->

Create detailed documentation for writing GitMap roadmaps manually.

**Requirements:**
- Create detailed documentation for writing GitMap roadmaps manually.
- [ ] 0.11.1.0.2.1  (a) Explain milestones
- [ ] 0.11.1.0.2.2  (b) Explain Sections
- [ ] 0.11.1.0.2.3  (c) Explain issues
- [ ] 0.11.1.0.2.4  (d) Explain sub-issues
- [ ] 0.11.1.0.2.5  (e) Explain descriptions and requirements
- [ ] 0.11.1.0.2.6  (f) Provide complete examples

#### 0.11.1.0.3 Create GitHub Setup Guide
<!-- GitMap-ID: itredsjv -->

Document how to prepare a GitHub repository for GitMap.

**Requirements:**
- Document how to prepare a GitHub repository for GitMap.
- [ ] 0.11.1.0.3.1  (a) Explain that the user creates the repository
- [ ] 0.11.1.0.3.2  (b) Explain authentication setup
- [ ] 0.11.1.0.3.3  (c) Explain required repository permissions
- [ ] 0.11.1.0.3.4  (d) Explain how GitMap connects to the repository
- [ ] 0.11.1.0.3.5  (e) Include troubleshooting guidance

## 0.11.2 Release
<!-- GitMap-ID: avredshd -->

#### 0.11.2.0.1 Add Version Information
<!-- GitMap-ID: jtredsju -->

Provide consistent GitMap version information.

**Requirements:**
- Provide consistent GitMap version information.
- [ ] 0.11.2.0.1.1  (a) Define the application version
- [ ] 0.11.2.0.1.2  (b) Make the version available from the command line
- [ ] 0.11.2.0.1.3  (c) Keep package and application versions consistent

#### 0.11.2.0.2 Run Release Test
<!-- GitMap-ID: ktredsjt -->

Test GitMap from a clean environment before release.

**Requirements:**
- Test GitMap from a clean environment before release.
- [ ] 0.11.2.0.2.1  (a) Install GitMap from scratch
- [ ] 0.11.2.0.2.2  (b) Create a new roadmap
- [ ] 0.11.2.0.2.3  (c) Connect to a test repository
- [ ] 0.11.2.0.2.4  (d) Preview synchronization
- [ ] 0.11.2.0.2.5  (e) Perform synchronization
- [ ] 0.11.2.0.2.6  (f) Run synchronization again to verify duplicate prevention

#### 0.11.2.0.3 Create Version 1.0 Release
<!-- GitMap-ID: ltredsjs -->

Publish the first stable GitMap release.

**Requirements:**
- Publish the first stable GitMap release.
- [ ] 0.11.2.0.3.1  (a) Complete all required tests
- [ ] 0.11.2.0.3.2  (b) Complete user documentation
- [ ] 0.11.2.0.3.3  (c) Confirm the roadmap-first workflow works end to end
- [ ] 0.11.2.0.3.4  (d) Tag the release as `v1.0.0`
