Title: GitMap Roadmap

Sub-Title: GitMap turns a project roadmap into a structured GitHub project.

Hierarchy-Issue-Title-Style: type_prefix

# 0.1 Foundations (DONE)

## 0.1.1 Project Setup (DONE)

<!-- GitMap-ID: muredsir -->

Set up the basic GitMap project so it can be installed, run, tested, and developed safely.

#### 0.1.1.0.1 Create Python Project (DONE)

<!-- GitMap-ID: goredsox -->

Create the basic Python project structure for GitMap.

**End Goal:**

- Create the basic Python project structure for GitMap.

##### 0.1.1.0.1.1 (a) Create the `gitmap` package (DONE)

##### 0.1.1.0.1.2 (b) Create `../pyproject.toml` (DONE)

##### 0.1.1.0.1.3 (c) Create a `tests` directory (DONE)

##### 0.1.1.0.1.4 (d) Create a `../.gitignore` (DONE)

#### 0.1.1.0.2 Install Dependencies (DONE)

<!-- GitMap-ID: horedsow -->

Set up the dependencies needed to develop and test GitMap.

**End Goal:**

- Set up the dependencies needed to develop and test GitMap.

##### 0.1.1.0.2.1 (a) Support editable installation (DONE)

##### 0.1.1.0.2.2 (b) Add `pytest` as a development dependency (DONE)

##### 0.1.1.0.2.3 (c) Confirm the development environment installs successfully (DONE)

#### 0.1.1.0.3 Create Command-Line Entry Point (DONE)

<!-- GitMap-ID: ioredsov -->

Create the basic command-line entry point for GitMap.

**End Goal:**

- Create the basic command-line entry point for GitMap.

##### 0.1.1.0.3.1 (a) Allow GitMap to be started from the command line (DONE)

##### 0.1.1.0.3.2 (b) Display a simple welcome message (DONE)

##### 0.1.1.0.3.3 (c) Exit cleanly (DONE)

#### 0.1.1.0.4 Add Initial Tests (DONE)

<!-- GitMap-ID: joredsou -->

Create the first automated tests for GitMap.

**End Goal:**

- Create the first automated tests for GitMap.

##### 0.1.1.0.4.1 (a) Confirm GitMap can be imported (DONE)

##### 0.1.1.0.4.2 (b) Confirm the command-line entry point runs (DONE)

##### 0.1.1.0.4.3 (c) Confirm the test suite can be run with `pytest` (DONE)

#### 0.1.1.0.5 Add Project Documentation (DONE)

<!-- GitMap-ID: koredsot -->

Create the basic documentation needed to understand and develop GitMap.

**End Goal:**

- Create the basic documentation needed to understand and develop GitMap.

##### 0.1.1.0.5.1 (a) Explain what GitMap does (DONE)

##### 0.1.1.0.5.2 (b) Explain how to install GitMap for development (DONE)

##### 0.1.1.0.5.3 (c) Explain how to run GitMap (DONE)

##### 0.1.1.0.5.4 (d) Explain how to run the tests (DONE)

## 0.1.2 Roadmap Format (DONE)

<!-- GitMap-ID: nuredsiq -->

Define the Markdown structure GitMap will use to describe projects before they are synchronized with GitHub.

#### 0.1.2.0.1 Define Roadmap Structure (DONE)

<!-- GitMap-ID: loredsos -->

Define the hierarchy used in a GitMap roadmap.

**End Goal:**

- Define the hierarchy used in a GitMap roadmap.

##### 0.1.2.0.1.1 (a) Support milestones (DONE)

##### 0.1.2.0.1.2 (b) Support Sections (DONE)

##### 0.1.2.0.1.3 (c) Support issues (DONE)

##### 0.1.2.0.1.4 (d) Support sub-issues (DONE)

##### 0.1.2.0.1.5 (e) Support descriptions and requirements (DONE)

##### 0.1.2.0.1.6 (f) Use Markdown headings to represent hierarchy (DONE)

#### 0.1.2.0.2 Create Example Roadmap (DONE)

<!-- GitMap-ID: moredsor -->

Create a complete example roadmap that can be used for development and testing.

**End Goal:**

- Create a complete example roadmap that can be used for development and testing.

##### 0.1.2.0.2.1 (a) Include at least one milestone (DONE)

##### 0.1.2.0.2.2 (b) Include at least one Section (DONE)

##### 0.1.2.0.2.3 (c) Include multiple issues (DONE)

##### 0.1.2.0.2.4 (d) Include at least one sub-issue (DONE)

##### 0.1.2.0.2.5 (e) Include descriptions and requirements (DONE)

#### 0.1.2.0.3 Document Roadmap Format (DONE)

<!-- GitMap-ID: noredsoq -->

Document how users should write a GitMap roadmap.

**End Goal:**

- Document how users should write a GitMap roadmap.

##### 0.1.2.0.3.1 (a) Explain each heading level (DONE)

##### 0.1.2.0.3.2 (b) Show how milestones, Sections, issues, and sub-issues are represented (DONE)

##### 0.1.2.0.3.3 (c) Provide a copyable example (DONE)

# 0.2 Roadmap Parser (DONE)

## 0.2.1 Markdown Parsing (DONE)

<!-- GitMap-ID: ouredsip -->

Teach GitMap to read a roadmap and turn its Markdown structure into project data.

#### 0.2.1.0.1 Read Roadmap File (DONE)

<!-- GitMap-ID: ooredsop -->

Load a roadmap from a Markdown file.

**End Goal:**

- Load a roadmap from a Markdown file.

##### 0.2.1.0.1.1 (a) Accept a roadmap file path (DONE)

##### 0.2.1.0.1.2 (b) Read the Markdown contents (DONE)

##### 0.2.1.0.1.3 (c) Report a clear error if the file cannot be read (DONE)

#### 0.2.1.0.2 Parse Milestones (DONE)

<!-- GitMap-ID: poredsoo -->

Identify milestone headings in the roadmap.

**End Goal:**

- Identify milestone headings in the roadmap.

##### 0.2.1.0.2.1 (a) Recognize milestone headings (DONE)

##### 0.2.1.0.2.2 (b) Capture the milestone number and title (DONE)

##### 0.2.1.0.2.3 (c) Preserve the order of milestones (DONE)

#### 0.2.1.0.3 Parse Sections (DONE)

<!-- GitMap-ID: qoredson -->

Identify Sections within each milestone.

**End Goal:**

- Identify Sections within each milestone.

##### 0.2.1.0.3.1 (a) Associate each Section with its milestone (DONE)

##### 0.2.1.0.3.2 (b) Capture the Section title (DONE)

##### 0.2.1.0.3.3 (c) Capture the Section description (DONE)

##### 0.2.1.0.3.4 (d) Recognize the Section type marker (DONE)

#### 0.2.1.0.4 Parse Issues (DONE)

<!-- GitMap-ID: roredsom -->

Identify issues within each Section.

**End Goal:**

- Identify issues within each Section.

##### 0.2.1.0.4.1 (a) Associate each issue with its Section (DONE)

##### 0.2.1.0.4.2 (b) Capture the issue number and title (DONE)

##### 0.2.1.0.4.3 (c) Capture the issue description (DONE)

##### 0.2.1.0.4.4 (d) Capture requirements (DONE)

#### 0.2.1.0.5 Parse Work Steps (DONE)

<!-- GitMap-ID: soredsol -->

Support issues nested beneath other issues.

**End Goal:**

- Support issues nested beneath other issues.

##### 0.2.1.0.5.1 (a) Associate each sub-issue with its parent issue (DONE)

##### 0.2.1.0.5.2 (b) Preserve the roadmap hierarchy (DONE)

##### 0.2.1.0.5.3 (c) Support numbering such as `0.2.4.1` (DONE)

## 0.2.2 Roadmap Validation (DONE)

<!-- GitMap-ID: puredsio -->

Detect roadmap problems before anything is sent to GitHub.

#### 0.2.2.0.1 Validate Roadmap Structure (DONE)

<!-- GitMap-ID: toredsok -->

Check that the roadmap follows GitMap's expected hierarchy.

**End Goal:**

- Check that the roadmap follows GitMap's expected hierarchy.

##### 0.2.2.0.1.1 (a) Detect issues outside a Section (DONE)

##### 0.2.2.0.1.2 (b) Detect Sections outside a milestone (DONE)

##### 0.2.2.0.1.3 (c) Detect malformed hierarchy (DONE)

##### 0.2.2.0.1.4 (d) Provide useful error messages (DONE)

#### 0.2.2.0.2 Validate Numbering (DONE)

<!-- GitMap-ID: uoredsoj -->

Check roadmap numbering for obvious errors.

**End Goal:**

- Check roadmap numbering for obvious errors.

##### 0.2.2.0.2.1 (a) Detect duplicate numbers (DONE)

##### 0.2.2.0.2.2 (b) Detect invalid parent relationships (DONE)

##### 0.2.2.0.2.3 (c) Identify the location of the problem (DONE)

#### 0.2.2.0.3 Preview Parsed Roadmap (DONE)

<!-- GitMap-ID: voredsoi -->

Allow users to see what GitMap understood before synchronization.

**End Goal:**

- Allow users to see what GitMap understood before synchronization.

##### 0.2.2.0.3.1 (a) Display milestones (DONE)

##### 0.2.2.0.3.2 (b) Display Sections (DONE)

##### 0.2.2.0.3.3 (c) Display issues and sub-issues (DONE)

##### 0.2.2.0.3.4 (d) Preserve hierarchy in the preview (DONE)

# 0.3 GitHub Setup (DONE)

## 0.3.1 Repository Connection (DONE)

<!-- GitMap-ID: ruredsim -->

Connect a completed GitMap roadmap to a GitHub repository chosen by the user.

#### 0.3.1.0.1 Collect Repository Information (DONE)

<!-- GitMap-ID: woredsoh -->

Ask the user which GitHub repository should receive the roadmap.

**End Goal:**

- Ask the user which GitHub repository should receive the roadmap.

##### 0.3.1.0.1.1 (a) Ask for the GitHub username (DONE)

##### 0.3.1.0.1.2 (b) Ask for the repository name (DONE)

##### 0.3.1.0.1.3 (c) Do not create the repository automatically (DONE)

##### 0.3.1.0.1.4 (d) Allow roadmap creation to be completed before GitHub setup begins (DONE)

#### 0.3.1.0.2 Configure GitHub Authentication (DONE)

<!-- GitMap-ID: xoredsog -->

Set up authentication required to work with the selected repository.

**End Goal:**

- Set up authentication required to work with the selected repository.

##### 0.3.1.0.2.1 (a) Keep credentials outside source control (DONE)

##### 0.3.1.0.2.2 (b) Provide clear setup instructions (DONE)

##### 0.3.1.0.2.3 (c) Detect missing authentication (DONE)

##### 0.3.1.0.2.4 (d) Never store authentication tokens in the roadmap (DONE)

#### 0.3.1.0.3 Verify Repository (DONE)

<!-- GitMap-ID: yoredsof -->

Confirm that GitMap can access the repository before synchronization.

**End Goal:**

- Confirm that GitMap can access the repository before synchronization.

##### 0.3.1.0.3.1 (a) Verify that the repository exists (DONE)

##### 0.3.1.0.3.2 (b) Verify that authentication works (DONE)

##### 0.3.1.0.3.3 (c) Verify that the user has appropriate access (DONE)

##### 0.3.1.0.3.4 (d) Stop synchronization if verification fails (DONE)

## 0.3.2 GitHub Project Structure (DONE)

<!-- GitMap-ID: suredsil -->

Translate GitMap's roadmap concepts into the GitHub structures needed for synchronization.

#### 0.3.2.0.1 Define Milestone Mapping (DONE)

<!-- GitMap-ID: zoredsoe -->

Define how roadmap milestones map to GitHub milestones.

**End Goal:**

- Define how roadmap milestones map to GitHub milestones.

##### 0.3.2.0.1.1 (a) Preserve milestone titles (DONE)

##### 0.3.2.0.1.2 (b) Avoid creating duplicate milestones (DONE)

##### 0.3.2.0.1.3 (c) Allow existing milestones to be recognized (DONE)

#### 0.3.2.0.2 Define Label Mapping (DONE)

<!-- GitMap-ID: aoredsod -->

Define the labels GitMap uses when creating GitHub items.

**End Goal:**

- Define the labels GitMap uses when creating GitHub items.

##### 0.3.2.0.2.1 (a) Support labels for Sections (DONE)

##### 0.3.2.0.2.2 (b) Support labels for issues when defined by the roadmap (DONE)

##### 0.3.2.0.2.3 (c) Avoid creating duplicate labels (DONE)

##### 0.3.2.0.2.4 (d) Allow labels to be created before issues are synchronized (DONE)

#### 0.3.2.0.3 Define Issue Mapping (DONE)

<!-- GitMap-ID: boredsoc -->

Define how roadmap items become GitHub issues.

**End Goal:**

- Define how roadmap items become GitHub issues.

##### 0.3.2.0.3.1 (a) Preserve issue titles (DONE)

##### 0.3.2.0.3.2 (b) Preserve descriptions (DONE)

##### 0.3.2.0.3.3 (c) Preserve requirements (DONE)

##### 0.3.2.0.3.4 (d) Associate issues with their milestone (DONE)

##### 0.3.2.0.3.5 (e) Apply appropriate labels (DONE)

#### 0.3.2.0.4 Define Work Step Mapping (DONE)

<!-- GitMap-ID: coredsob -->

Define how roadmap hierarchy is represented in GitHub.

**End Goal:**

- Define how roadmap hierarchy is represented in GitHub.

##### 0.3.2.0.4.1 (a) Preserve parent-child relationships when supported (DONE)

##### 0.3.2.0.4.2 (b) Keep sub-issues associated with their parent (DONE)

##### 0.3.2.0.4.3 (c) Preserve roadmap numbering (DONE)

# 0.4 GitHub Synchronization (DONE)

## 0.4.1 Synchronization Engine (DONE)

<!-- GitMap-ID: turedsik -->

Synchronize the validated roadmap with the selected GitHub repository.

#### 0.4.1.0.1 Create Labels (DONE)

<!-- GitMap-ID: doredsoa -->

Create the labels required by the roadmap before synchronizing other items.

**End Goal:**

- Create the labels required by the roadmap before synchronizing other items.

##### 0.4.1.0.1.1 (a) Read required labels from the parsed roadmap (DONE)

##### 0.4.1.0.1.2 (b) Detect labels that already exist (DONE)

##### 0.4.1.0.1.3 (c) Create only missing labels (DONE)

##### 0.4.1.0.1.4 (d) Do not create duplicates (DONE)

#### 0.4.1.0.2 Create Milestones (DONE)

<!-- GitMap-ID: eoredsoz -->

Create roadmap milestones in GitHub.

**End Goal:**

- Create roadmap milestones in GitHub.

##### 0.4.1.0.2.1 (a) Detect milestones that already exist (DONE)

##### 0.4.1.0.2.2 (b) Create only missing milestones (DONE)

##### 0.4.1.0.2.3 (c) Preserve milestone titles (DONE)

##### 0.4.1.0.2.4 (d) Do not create duplicates (DONE)

#### 0.4.1.0.3 Create Sections (DONE)

<!-- GitMap-ID: foredsoy -->

Create GitHub issues representing roadmap Sections.

**End Goal:**

- Create GitHub issues representing roadmap Sections.

##### 0.4.1.0.3.1 (a) Create the Section before its child issues (DONE)

##### 0.4.1.0.3.2 (b) Include the Section description (DONE)

##### 0.4.1.0.3.3 (c) Apply the Section label (DONE)

##### 0.4.1.0.3.4 (d) Associate the Section with its milestone (DONE)

##### 0.4.1.0.3.5 (e) Detect an existing matching Section before creating another (DONE)

#### 0.4.1.0.4 Create Issues (DONE)

<!-- GitMap-ID: gpredsnx -->

Create GitHub issues from roadmap issues.

**End Goal:**

- Create GitHub issues from roadmap issues.

##### 0.4.1.0.4.1 (a) Preserve the issue title (DONE)

##### 0.4.1.0.4.2 (b) Include the description (DONE)

##### 0.4.1.0.4.3 (c) Include requirements using GitHub Markdown (DONE)

##### 0.4.1.0.4.4 (d) Associate the issue with its milestone (DONE)

##### 0.4.1.0.4.5 (e) Apply defined labels (DONE)

##### 0.4.1.0.4.6 (f) Detect existing matching issues before creating another (DONE)

#### 0.4.1.0.5 Create Work Steps (DONE)

<!-- GitMap-ID: hpredsnw -->

Create roadmap sub-issues and associate them with their parent issues.

**End Goal:**

- Create roadmap sub-issues and associate them with their parent issues.

##### 0.4.1.0.5.1 (a) Create the parent before its sub-issues (DONE)

##### 0.4.1.0.5.2 (b) Preserve the parent-child hierarchy (DONE)

##### 0.4.1.0.5.3 (c) Include descriptions and requirements (DONE)

##### 0.4.1.0.5.4 (d) Associate sub-issues with the correct milestone (DONE)

## 0.4.2 Safe Synchronization (DONE)

<!-- GitMap-ID: uuredsij -->

Make synchronization predictable and safe to run more than once.

#### 0.4.2.0.1 Add Dry Run (DONE)

<!-- GitMap-ID: ipredsnv -->

Allow users to preview what synchronization would change without changing GitHub.

**End Goal:**

- Allow users to preview what synchronization would change without changing GitHub.

##### 0.4.2.0.1.1 (a) Show items that would be created (DONE)

##### 0.4.2.0.1.2 (b) Show items that already exist (DONE)

##### 0.4.2.0.1.3 (c) Make no GitHub changes during a dry run (DONE)

##### 0.4.2.0.1.4 (d) Clearly identify dry-run output (DONE)

#### 0.4.2.0.2 Prevent Duplicate Items (DONE)

<!-- GitMap-ID: jpredsnu -->

Make repeated synchronization safe.

**End Goal:**

- Make repeated synchronization safe.

##### 0.4.2.0.2.1 (a) Check GitHub before creating an item (DONE)

##### 0.4.2.0.2.2 (b) Reuse existing matching items (DONE)

##### 0.4.2.0.2.3 (c) Prevent duplicate labels (DONE)

##### 0.4.2.0.2.4 (d) Prevent duplicate milestones (DONE)

##### 0.4.2.0.2.5 (e) Prevent duplicate issues (DONE)

#### 0.4.2.0.3 Add Synchronization Summary (DONE)

<!-- GitMap-ID: kpredsnt -->

Display the result of synchronization.

**End Goal:**

- Display the result of synchronization.

##### 0.4.2.0.3.1 (a) Report items created (DONE)

##### 0.4.2.0.3.2 (b) Report items already present (DONE)

##### 0.4.2.0.3.3 (c) Report skipped items (DONE)

##### 0.4.2.0.3.4 (d) Report errors (DONE)

# 0.5 Roadmap Updates (DONE)

## 0.5.1 Existing Project Import (DONE)

<!-- GitMap-ID: vuredsii -->

Allow GitMap to understand what already exists in a connected GitHub repository.

#### 0.5.1.0.1 Read Existing Milestones (DONE)

<!-- GitMap-ID: lpredsns -->

Retrieve existing milestones from the repository.

**End Goal:**

- Retrieve existing milestones from the repository.

##### 0.5.1.0.1.1 (a) Read open milestones (DONE)

##### 0.5.1.0.1.2 (b) Recognize milestones already represented in the roadmap (DONE)

##### 0.5.1.0.1.3 (c) Preserve GitHub milestone identifiers for later updates (DONE)

#### 0.5.1.0.2 Read Existing Labels (DONE)

<!-- GitMap-ID: mpredsnr -->

Retrieve existing repository labels.

**End Goal:**

- Retrieve existing repository labels.

##### 0.5.1.0.2.1 (a) Read current labels (DONE)

##### 0.5.1.0.2.2 (b) Match existing labels to roadmap labels (DONE)

##### 0.5.1.0.2.3 (c) Avoid recreating labels that already exist (DONE)

#### 0.5.1.0.3 Read Existing Issues (DONE)

<!-- GitMap-ID: npredsnq -->

Retrieve existing GitHub issues that correspond to roadmap items.

**End Goal:**

- Retrieve existing GitHub issues that correspond to roadmap items.

##### 0.5.1.0.3.1 (a) Read existing issues (DONE)

##### 0.5.1.0.3.2 (b) Match issues to roadmap items (DONE)

##### 0.5.1.0.3.3 (c) Preserve GitHub issue numbers (DONE)

##### 0.5.1.0.3.4 (d) Distinguish GitMap-managed items from unrelated repository issues (DONE)

#### 0.5.1.0.4 Rebuild Roadmap State (DONE)

<!-- GitMap-ID: opredsnp -->

Use GitHub data to reconstruct the current state of a GitMap-managed project.

**End Goal:**

- Use GitHub data to reconstruct the current state of a GitMap-managed project.

##### 0.5.1.0.4.1 (a) Associate existing issues with milestones (DONE)

##### 0.5.1.0.4.2 (b) Restore Section and issue relationships (DONE)

##### 0.5.1.0.4.3 (c) Restore sub-issue relationships when available (DONE)

##### 0.5.1.0.4.4 (d) Identify roadmap items that cannot be matched safely (DONE)

## 0.5.2 Roadmap Changes (DONE)

<!-- GitMap-ID: wuredsih -->

Allow a user to modify the roadmap after the initial synchronization and safely apply those changes to GitHub.

#### 0.5.2.0.1 Detect Roadmap Changes (DONE)

<!-- GitMap-ID: ppredsno -->

Compare the local roadmap with the current GitHub project.

**End Goal:**

- Compare the local roadmap with the current GitHub project.

##### 0.5.2.0.1.1 (a) Detect new roadmap items (DONE)

##### 0.5.2.0.1.2 (b) Detect changed roadmap items (DONE)

##### 0.5.2.0.1.3 (c) Detect items that already match GitHub (DONE)

##### 0.5.2.0.1.4 (d) Present differences before synchronization (DONE)

#### 0.5.2.0.2 Update Existing Items (DONE)

<!-- GitMap-ID: qpredsnn -->

Update GitHub items when their corresponding roadmap entries change.

**End Goal:**

- Update GitHub items when their corresponding roadmap entries change.

##### 0.5.2.0.2.1 (a) Update titles when changed (DONE)

##### 0.5.2.0.2.2 (b) Update descriptions when changed (DONE)

##### 0.5.2.0.2.3 (c) Update requirements when changed (DONE)

##### 0.5.2.0.2.4 (d) Preserve GitHub issue numbers (DONE)

##### 0.5.2.0.2.5 (e) Avoid recreating existing items (DONE)

#### 0.5.2.0.3 Handle Removed Roadmap Items (DONE)

<!-- GitMap-ID: rpredsnm -->

Safely identify items that exist in GitHub but have been removed from the roadmap.

**End Goal:**

- Safely identify items that exist in GitHub but have been removed from the roadmap.

##### 0.5.2.0.3.1 (a) Never delete GitHub items automatically (DONE)

##### 0.5.2.0.3.2 (b) Report removed roadmap items (DONE)

##### 0.5.2.0.3.3 (c) Require an explicit user decision before destructive changes (DONE)

##### 0.5.2.0.3.4 (d) Preserve historical GitHub data by default (DONE)

#### 0.5.2.0.4 Preview Updates (DONE)

<!-- GitMap-ID: spredsnl -->

Show the user exactly what an update synchronization will do.

**End Goal:**

- Show the user exactly what an update synchronization will do.

##### 0.5.2.0.4.1 (a) Show new items (DONE)

##### 0.5.2.0.4.2 (b) Show changed items (DONE)

##### 0.5.2.0.4.3 (c) Show unchanged items (DONE)

##### 0.5.2.0.4.4 (d) Show roadmap items that were removed (DONE)

##### 0.5.2.0.4.5 (e) Require confirmation before applying changes (DONE)

# 0.6 User Workflow

## 0.6.1 Interactive Roadmap Builder (DONE)

<!-- GitMap-ID: xuredsig -->

Guide users through creating a roadmap without requiring them to know GitMap's Markdown format.

#### 0.6.1.0.1 Start New Roadmap (DONE)

<!-- GitMap-ID: tpredsnk -->

Begin an interactive roadmap-building session.

**End Goal:**

- Begin an interactive roadmap-building session.

##### 0.6.1.0.1.1 (a) Ask for the project name (DONE)

##### 0.6.1.0.1.2 (b) Ask for a project overview (DONE)

##### 0.6.1.0.1.3 (c) Create the initial roadmap structure (DONE)

##### 0.6.1.0.1.4 (d) Do not require GitHub information yet (DONE)

#### 0.6.1.0.2 Collect Milestones (DONE)

<!-- GitMap-ID: upredsnj -->

Guide the user through defining project milestones.

**End Goal:**

- Guide the user through defining project milestones.

##### 0.6.1.0.2.1 (a) Ask for the milestone number (DONE)

##### 0.6.1.0.2.2 (b) Ask for the milestone title (DONE)

##### 0.6.1.0.2.3 (c) Allow multiple milestones (DONE)

##### 0.6.1.0.2.4 (d) Allow the user to indicate when they are finished (DONE)

#### 0.6.1.0.3 Collect Sections (DONE)

<!-- GitMap-ID: vpredsni -->

Guide the user through defining Sections within each milestone.

**End Goal:**

- Guide the user through defining Sections within each milestone.

##### 0.6.1.0.3.1 (a) Ask for the Section title (DONE)

##### 0.6.1.0.3.2 (b) Ask for a Section overview (DONE)

##### 0.6.1.0.3.3 (c) Associate the Section with its milestone (DONE)

##### 0.6.1.0.3.4 (d) Allow multiple Sections (DONE)

#### 0.6.1.0.4 Collect Issues (DONE)

<!-- GitMap-ID: wpredsnh -->

Guide the user through defining issues within a Section.

**End Goal:**

- Guide the user through defining issues within a Section.

##### 0.6.1.0.4.1 (a) Ask for the issue title (DONE)

##### 0.6.1.0.4.2 (b) Ask for the issue description (DONE)

##### 0.6.1.0.4.3 (c) Ask for requirements (DONE)

##### 0.6.1.0.4.4 (d) Allow requirements to be entered individually (DONE)

##### 0.6.1.0.4.5 (e) Treat a blank entry as finished (DONE)

#### 0.6.1.0.5 Collect Work Steps (DONE)

<!-- GitMap-ID: xpredsng -->

Allow an issue to contain smaller sub-issues.

**End Goal:**

- Allow an issue to contain smaller sub-issues.

##### 0.6.1.0.5.1 (a) Ask whether an issue needs sub-issues (DONE)

##### 0.6.1.0.5.2 (b) Collect sub-issue titles (DONE)

##### 0.6.1.0.5.3 (c) Collect descriptions and requirements (DONE)

##### 0.6.1.0.5.4 (d) Preserve the parent-child relationship (DONE)

##### 0.6.1.0.5.5 (e) Support additional nesting when appropriate (DONE)

#### 0.6.1.0.6 Support Pasted Content (DONE)

<!-- GitMap-ID: ypredsnf -->

Allow users to paste existing project information instead of answering every question individually.

**End Goal:**

- Allow users to paste existing project information instead of answering every question individually.

##### 0.6.1.0.6.1 (a) Accept pasted overview text (DONE)

##### 0.6.1.0.6.2 (b) Accept pasted descriptions (DONE)

##### 0.6.1.0.6.3 (c) Accept pasted requirements (DONE)

##### 0.6.1.0.6.4 (d) Preserve multiline content (DONE)

##### 0.6.1.0.6.5 (e) Allow interactive questions and pasted content to be mixed (DONE)

## 0.6.2 Roadmap Review (DONE)

<!-- GitMap-ID: yuredsif -->

Let the user review and revise the roadmap before connecting it to GitHub.

#### 0.6.2.0.1 Display Completed Roadmap (DONE)

<!-- GitMap-ID: zpredsne -->

Show the complete generated roadmap.

**End Goal:**

- Show the complete generated roadmap.

##### 0.6.2.0.1.1 (a) Preserve Markdown hierarchy (DONE)

##### 0.6.2.0.1.2 (b) Make milestone, Section, issue, and sub-issue relationships clear (DONE)

##### 0.6.2.0.1.3 (c) Show descriptions and requirements (DONE)

#### 0.6.2.0.2 Edit Roadmap Before Sync

<!-- GitMap-ID: apredsnd -->

Allow changes before GitHub synchronization begins.

**End Goal:**

- Allow changes before GitHub synchronization begins.

##### 0.6.2.0.2.1 (a) Allow items to be renamed (DONE)

##### 0.6.2.0.2.2 (b) Allow descriptions and requirements to be changed (DONE)

##### 0.6.2.0.2.3 (c) Allow items to be added (DONE)

##### 0.6.2.0.2.4 (d) Allow items to be removed

##### 0.6.2.0.2.5 (e) Revalidate the roadmap after changes

#### 0.6.2.0.3 Save Roadmap (DONE)

<!-- GitMap-ID: bpredsnc -->

Save the completed roadmap to `roadmap.md`.

**End Goal:**

- Save the completed roadmap to `roadmap.md`.

##### 0.6.2.0.3.1 (a) Produce valid GitMap Markdown (DONE)

##### 0.6.2.0.3.2 (b) Preserve the complete hierarchy (DONE)

##### 0.6.2.0.3.3 (c) Confirm where the roadmap was saved (DONE)

# 0.7 Changes to make

## 0.7.1 Synchronization Workflow Improvements

<!-- GitMap-ID: zuredsie -->

Improve roadmap synchronization behavior discovered during real-world GitMap use.

#### 0.7.1.0.1 Improve Change Preview Flow (DONE)

<!-- GitMap-ID: cpredsnb -->

Avoid displaying detailed change lists before the user asks to review them.

**End Goal:**

- Present a concise synchronization summary first and allow the user to choose which details to inspect.

##### 0.7.1.0.1.1 (a) Display change counts before detailed change lists

##### 0.7.1.0.1.2 (b) Do not automatically display the complete added-item list

##### 0.7.1.0.1.3 (c) Allow added items to be reviewed on request

##### 0.7.1.0.1.4 (d) Allow changed items to be reviewed on request

##### 0.7.1.0.1.5 (e) Allow unchanged items to be reviewed on request

##### 0.7.1.0.1.6 (f) Allow removed items to be reviewed on request

##### 0.7.1.0.1.7 (g) Return to the synchronization prompt after reviewing a list

#### 0.7.1.0.2 Preserve Identity During Renumbering

<!-- GitMap-ID: dpredsna -->

Recognize existing roadmap items when their GitMap numbers change.

**End Goal:**

- Treat renumbered roadmap items as updates to existing GitHub items rather than unrelated removed and newly created
  items.

##### 0.7.1.0.2.1 (a) Detect an existing roadmap item after its number changes

##### 0.7.1.0.2.2 (b) Avoid relying solely on the GitMap number as item identity

##### 0.7.1.0.2.3 (c) Preserve the existing GitHub item when a roadmap item is renumbered

##### 0.7.1.0.2.4 (d) Update the GitMap marker after renumbering

##### 0.7.1.0.2.5 (e) Preserve existing GitHub issue numbers and relationships where possible

#### 0.7.1.0.3 Update Renumbered Milestones

<!-- GitMap-ID: epredsnz -->

Update existing GitHub milestones when roadmap milestone numbers change.

**End Goal:**

- Prevent duplicate GitHub milestones when roadmap milestones are renumbered.

##### 0.7.1.0.3.1 (a) Match a renumbered milestone to its existing GitHub milestone

##### 0.7.1.0.3.2 (b) Rename the existing GitHub milestone

##### 0.7.1.0.3.3 (c) Preserve the GitHub milestone ID

##### 0.7.1.0.3.4 (d) Preserve issues assigned to the milestone

##### 0.7.1.0.3.5 (e) Do not create a second milestone solely because its roadmap number changed

##### 0.7.1.0.3.6 (f) Detect and report ambiguous milestone matches

#### 0.7.1.0.4 Preview Renumbering During Synchronization

<!-- GitMap-ID: fpredsny -->

Make renumbering visible before GitHub is changed.

**End Goal:**

- Clearly distinguish renumbering from ordinary additions and removals during synchronization preview.

##### 0.7.1.0.4.1 (a) Identify renumbered roadmap items

##### 0.7.1.0.4.2 (b) Display the old roadmap number

##### 0.7.1.0.4.3 (c) Display the new roadmap number

##### 0.7.1.0.4.4 (d) Distinguish renumbering from newly added items

##### 0.7.1.0.4.5 (e) Distinguish renumbering from removed items

##### 0.7.1.0.4.6 (f) Require normal synchronization confirmation before applying renumbering

#### 0.7.1.0.5 Display Synchronization Progress

<!-- GitMap-ID: gqredsmx -->

Show where GitMap is during an active synchronization.

**End Goal:**

- Let the user see how much synchronization work has completed and what GitMap is currently processing.

##### 0.7.1.0.5.1 (a) Count the total planned synchronization operations

##### 0.7.1.0.5.2 (b) Display the current operation number

##### 0.7.1.0.5.3 (c) Display the total number of operations

##### 0.7.1.0.5.4 (d) Display the roadmap number of the item being processed

##### 0.7.1.0.5.5 (e) Display the title of the item being processed

##### 0.7.1.0.5.6 (f) Display whether the item is being created, updated, or checked

##### 0.7.1.0.5.7 (g) Update progress as each operation completes

##### 0.7.1.0.5.8 (h) Display a completion summary

##### 0.7.1.0.5.9 (i) Display elapsed synchronization time

## 0.7.2 Synchronization Safety and Recovery

<!-- GitMap-ID: auredsid -->

#### 0.7.2.0.1 Validate Synchronization Plan

<!-- GitMap-ID: hqredsmw -->

##### 0.7.2.0.1.1 (a) Detect duplicate GitMap identifiers

##### 0.7.2.0.1.2 (b) Detect duplicate milestone mappings

##### 0.7.2.0.1.3 (c) Detect ambiguous identity matches

##### 0.7.2.0.1.4 (d) Refuse to guess when identity cannot be determined safely

##### 0.7.2.0.1.5 (e) Explain conflicts before synchronization

##### 0.7.2.0.1.6 (f) Allow conflicts to be resolved before retrying

#### 0.7.2.0.2 Protect Partial Synchronization

<!-- GitMap-ID: iqredsmv -->

##### 0.7.2.0.2.1 (a) Track completed synchronization operations

##### 0.7.2.0.2.2 (b) Identify the operation that failed

##### 0.7.2.0.2.3 (c) Report operations completed before failure

##### 0.7.2.0.2.4 (d) Report operations that remain incomplete

##### 0.7.2.0.2.5 (e) Stop safely when synchronization cannot continue

##### 0.7.2.0.2.6 (f) Preserve enough state for a safe retry

#### 0.7.2.0.3 Verify Synchronization Results

<!-- GitMap-ID: jqredsmu -->

##### 0.7.2.0.3.1 (a) Re-read affected GitHub items after synchronization

##### 0.7.2.0.3.2 (b) Confirm expected items were created

##### 0.7.2.0.3.3 (c) Confirm expected items were updated

##### 0.7.2.0.3.4 (d) Confirm expected roadmap identities were preserved

##### 0.7.2.0.3.5 (e) Detect unexpected duplicate identifiers

##### 0.7.2.0.3.6 (f) Report differences between planned and actual results

#### 0.7.2.0.4 Support Safe Synchronization Retry

<!-- GitMap-ID: kqredsmt -->

##### 0.7.2.0.4.1 (a) Re-read GitHub state before retrying

##### 0.7.2.0.4.2 (b) Recognize operations already completed

##### 0.7.2.0.4.3 (c) Avoid recreating successfully created items

##### 0.7.2.0.4.4 (d) Avoid reapplying unnecessary updates

##### 0.7.2.0.4.5 (e) Continue remaining synchronization work safely

##### 0.7.2.0.4.6 (f) Report final retry results

#### 0.7.2.0.5 Prevent Concurrent Synchronization

<!-- GitMap-ID: lqredsms -->

Prevent multiple GitMap synchronization operations from modifying the same repository at the same time.

**End Goal:**

- Prevent concurrent synchronization from creating duplicate or conflicting GitHub changes.

##### 0.7.2.0.5.1 (a) Detect when synchronization is already in progress

##### 0.7.2.0.5.2 (b) Prevent a second synchronization from starting against the same repository

##### 0.7.2.0.5.3 (c) Explain why the second synchronization was blocked

##### 0.7.2.0.5.4 (d) Allow synchronization after the active operation completes

##### 0.7.2.0.5.5 (e) Clear synchronization state after successful completion

##### 0.7.2.0.5.6 (f) Clear synchronization state safely after failure

##### 0.7.2.0.5.7 (g) Avoid leaving a stale synchronization lock after GitMap exits unexpectedly

## 0.7.3 Synchronization Performance

<!-- GitMap-ID: buredsic -->

Improve command-line synchronization performance by avoiding unnecessary work.

#### 0.7.3.0.1 Skip Unchanged Items During Synchronization

<!-- GitMap-ID: mqredsmr -->

Avoid unnecessary GitHub operations for roadmap items that have already been determined to be unchanged.

**End Goal:**

- Reduce synchronization time by processing only items that require GitHub changes.

##### 0.7.3.0.1.1 (a) Identify unchanged items during synchronization planning

##### 0.7.3.0.1.2 (b) Exclude unchanged items from synchronization operations

##### 0.7.3.0.1.3 (c) Avoid unnecessary GitHub API calls for unchanged items

##### 0.7.3.0.1.4 (d) Preserve unchanged items in the synchronization summary

##### 0.7.3.0.1.5 (e) Count only actionable items in synchronization progress

##### 0.7.3.0.1.6 (f) Report the number of unchanged items skipped

#### 0.7.3.0.2 Reuse Synchronization Plan

<!-- GitMap-ID: nqredsmq -->

Use the already-reviewed synchronization plan when applying changes.

**End Goal:**

- Avoid repeating work that was already completed while determining the synchronization preview.

##### 0.7.3.0.2.1 (a) Preserve the synchronization plan after preview

##### 0.7.3.0.2.2 (b) Use the approved plan when synchronization begins

##### 0.7.3.0.2.3 (c) Process only planned create and update operations

##### 0.7.3.0.2.4 (d) Avoid recalculating unchanged items unnecessarily

##### 0.7.3.0.2.5 (e) Ensure the applied plan matches the plan the user approved

## 0.7.4 GitHub Repository Setup

<!-- GitMap-ID: curedsib -->

Allow a completed roadmap to be connected to a new or existing GitHub repository.

#### 0.7.4.0.1 Choose Repository

<!-- GitMap-ID: sqredsml -->

Allow the user to choose where the roadmap will be synchronized.

**End Goal:**

- Connect the completed roadmap to the appropriate GitHub repository.

##### 0.7.4.0.1.1 (a) Use an existing repository

##### 0.7.4.0.1.2 (b) Create a new repository

#### 0.7.4.0.2 Create Repository

<!-- GitMap-ID: tqredsmk -->

Create a GitHub repository directly from GitMap.

**End Goal:**

- Create the repository without requiring the user to leave GitMap.

##### 0.7.4.0.2.1 (a) Ask for the repository name

##### 0.7.4.0.2.2 (b) Ask for a repository description

##### 0.7.4.0.2.3 (c) Allow public or private visibility

##### 0.7.4.0.2.4 (d) Create the repository through GitHub

##### 0.7.4.0.2.5 (e) Confirm successful repository creation

#### 0.7.4.0.3 Connect Repository

<!-- GitMap-ID: uqredsmj -->

Connect the roadmap to the selected repository.

**End Goal:**

- Make the selected repository the synchronization target for the roadmap.

##### 0.7.4.0.3.1 (a) Verify repository access

##### 0.7.4.0.3.2 (b) Store the repository association

##### 0.7.4.0.3.3 (c) Prepare the repository for synchronization

#### 0.7.4.0.4 Initial Synchronization

<!-- GitMap-ID: vqredsmi -->

Allow the completed roadmap to proceed directly into GitMap's existing synchronization workflow.

**End Goal:**

- Move from roadmap creation to GitHub synchronization without restarting GitMap.

##### 0.7.4.0.4.1 (a) Preview the initial synchronization

##### 0.7.4.0.4.2 (b) Require confirmation before synchronization

##### 0.7.4.0.4.3 (c) Synchronize the roadmap to the repository

##### 0.7.4.0.4.4 (d) Report synchronization results

## 0.7.5 Roadmap Numbering

<!-- GitMap-ID: duredsia -->

Allow users to choose how roadmap item numbers are assigned while building and editing a roadmap.

#### 0.7.5.0.1 Explain Roadmap Numbering

<!-- GitMap-ID: wqredsmh -->

Explain GitMap's numbering system when the user begins building a roadmap.

**End Goal:**

- Make the roadmap hierarchy and numbering rules clear before the user begins creating items.

##### 0.7.5.0.1.1 (a) Explain the milestone numbering format

##### 0.7.5.0.1.2 (b) Explain how child numbers extend their parent number

##### 0.7.5.0.1.3 (c) Show an example hierarchy

##### 0.7.5.0.1.4 (d) Explain automatic numbering

##### 0.7.5.0.1.5 (e) Explain manual numbering

#### 0.7.5.0.2 Choose Numbering Mode

<!-- GitMap-ID: mtredsjr -->

Allow the user to choose between automatic and manual numbering.

**End Goal:**

- Let users control whether GitMap assigns roadmap numbers or they enter them manually.

##### 0.7.5.0.2.1 (a) Offer automatic numbering

##### 0.7.5.0.2.2 (b) Offer manual numbering

##### 0.7.5.0.2.3 (c) Allow manual numbering when automatic numbering cannot be used

#### 0.7.5.0.3 Choose Starting Series

<!-- GitMap-ID: ntredsjq -->

Allow automatic numbering to reflect the project's development stage.

**End Goal:**

- Start roadmap numbering in the appropriate version series.

##### 0.7.5.0.3.1 (a) Offer pre-production numbering beginning with 0.x

##### 0.7.5.0.3.2 (b) Offer production numbering beginning with 1.x

#### 0.7.5.0.4 Generate Hierarchical Numbers

<!-- GitMap-ID: otredsjp -->

Generate roadmap numbers based on the hierarchy the user actually creates.

**End Goal:**

- Automatically assign valid numbers without requiring every hierarchy level to be present.

##### 0.7.5.0.4.1 (a) Number milestones automatically

##### 0.7.5.0.4.2 (b) Number Sections automatically

##### 0.7.5.0.4.3 (c) Number features automatically

##### 0.7.5.0.4.4 (d) Number issues automatically

##### 0.7.5.0.4.5 (e) Number Work Steps automatically

##### 0.7.5.0.4.6 (f) Increment sibling numbers automatically

##### 0.7.5.0.4.7 (g) Support letter sequences such as (a), (b), and (c) where used

## 0.7.6 GitHub Roadmap Representation

<!-- GitMap-ID: euredsiz -->

Allow users to choose how roadmap hierarchy is represented in GitHub.

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

##### 0.7.7.0.1.1 (a) Detect when Section or Feature Issues are enabled for an existing roadmap

##### 0.7.7.0.1.2 (b) Determine whether the corresponding hierarchy Issues already exist

##### 0.7.7.0.1.3 (c) Inform the user how many Section and Feature Issues will be created

##### 0.7.7.0.1.4 (d) Ask the user whether to create the missing hierarchy Issues

##### 0.7.7.0.1.5 (e) Create hierarchy Issues only after confirmation

**End Goal**
Users explicitly choose whether missing Section and Feature Issues are created for an existing synchronized roadmap.

#### 0.7.7.0.2 Require Approval Before Modifying Existing GitHub Items

<!-- GitMap-ID: kuredsit -->


Once a GitHub item already exists, GitMap must not update, close, or otherwise modify it unless the change appears in
the synchronization preview and has been approved by the user.

##### 0.7.7.0.2.1 (a) Detect modifications to existing GitHub items

##### 0.7.7.0.2.2 (b) Include all modifications in the synchronization preview

##### 0.7.7.0.2.3 (c) Prevent updates that were not included in the approved synchronization plan

##### 0.7.7.0.2.4 (d) Ensure updates and closures require user approval

##### 0.7.7.0.2.5 (e) Verify only approved changes are applied

**End Goal**

Existing GitHub items are never modified without first being shown to the user and explicitly approved.

## 0.7.8 Finish 0.7.6

<!-- GitMap-ID: gvredshx -->

#### 0.7.8.0.1 Customize Hierarchy Issue Titles

<!-- GitMap-ID: quredsin -->


Allow users to choose how Section and Feature GitHub Issues are titled so they are easy to distinguish from normal
roadmap Issues.

##### 0.7.8.0.1.1 (a) Add a hierarchy Issue title style option during roadmap creation.

##### 0.7.8.0.1.2 (b) Store the selected title style in the roadmap.

##### 0.7.8.0.1.3 (c) Update Section Issue title generation.

##### 0.7.8.0.1.4 (d) Update Feature Issue title generation.

##### 0.7.8.0.1.5 (e) Preserve title style during synchronization.

##### 0.7.8.0.1.6 (f) Show the selected title style in synchronization preview.

**End Goal**

Users can easily distinguish hierarchy Issues from normal roadmap Issues while preserving a consistent appearance across
GitHub.

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

Extend automatic numbering beyond initial roadmap creation so users do not have to manually manage numbers while editing
a roadmap.

#### 0.7.9.0.1 Preserve Numbering Mode During Editing

<!-- GitMap-ID: vtredsji -->





Remember how the roadmap is being numbered and use that behavior when the user enters the roadmap options or editing
workflow.

**Work Steps:**

- [ ] (a) Preserve the selected numbering mode after roadmap creation
- [ ] (b) Make the editing workflow aware of automatic numbering
- [ ] (c) Avoid asking for numbers manually when automatic numbering is active
- [ ] (d) Continue allowing manual numbers when manual numbering is selected

**End Goal:**

- Automatic numbering remains automatic throughout creation and editing.

#### 0.7.9.0.2 Add Items at the End Automatically

<!-- GitMap-ID: wtredsjh -->





Determine the next available sibling number when a new item is added at the end of an existing list.

**Work Steps:**

- [ ] (a) Determine the last existing sibling number
- [ ] (b) Tell the user what the last existing number is
- [ ] (c) Generate the next sibling number automatically
- [ ] (d) Apply the same behavior to Milestones, Sections, Features, and Issues
- [ ] (e) Generate the next Work Step letter automatically

**End Goal:**

- If the last Milestone is 0.4, adding another Milestone automatically creates 0.5 without asking the user to calculate
  it.

#### 0.7.9.0.3 Insert Items Between Existing Items

<!-- GitMap-ID: xtredsjg -->





Allow an automatically numbered item to be inserted at a chosen position instead of requiring every new item to be
placed at the end.

**Work Steps:**

- [ ] (a) Show the existing sibling items when choosing an insertion point
- [ ] (b) Allow the user to choose where the new item belongs
- [ ] (c) Assign the inserted item the appropriate number
- [ ] (d) Shift following sibling numbers as necessary
- [ ] (e) Renumber descendants when their parent number changes

**End Goal:**

- Users can place a new item where it logically belongs without manually renumbering the roadmap.

#### 0.7.9.0.4 Preview Automatic Renumbering

<!-- GitMap-ID: ytredsjf -->





Show the numbering changes before an insertion or other edit changes existing roadmap numbers.

**Work Steps:**

- [ ] (a) Calculate all numbers affected by the proposed change
- [ ] (b) Show old and new numbers for affected items
- [ ] (c) Include descendants whose numbers change with their parent
- [ ] (d) Allow the user to approve or cancel the renumbering
- [ ] (e) Apply numbering changes only after approval

**End Goal:**

- Existing roadmap numbers are never silently changed by automatic numbering.

#### 0.7.9.0.5 Preserve Identity During Renumbering

<!-- GitMap-ID: ztredsje -->





Keep roadmap and GitHub items associated with the same underlying item when their roadmap numbers change.

**Work Steps:**

- [ ] (a) Use the permanent GitMap ID as the stable item identity
- [ ] (b) Do not rely on the roadmap number alone to identify an existing item
- [ ] (c) Preserve existing GitHub Issue associations after renumbering
- [ ] (d) Update displayed GitMap numbers without creating replacement Issues
- [ ] (e) Verify descendants retain their identities after parent renumbering

**End Goal:**

- Renumbering reorganizes the roadmap without making existing items appear new to GitMap or GitHub.

#### 0.7.9.0.6 Detect Numbering Conflicts

<!-- GitMap-ID: atredsjd -->





Protect automatically numbered roadmaps from invalid or conflicting numbers.

**Work Steps:**

- [ ] (a) Detect duplicate numbers
- [ ] (b) Detect numbers that do not match their hierarchy
- [ ] (c) Detect gaps or conflicts created during insertion or renumbering
- [ ] (d) Report the affected roadmap items clearly
- [ ] (e) Revalidate the roadmap after numbering changes

**End Goal:**

- Automatic numbering produces a valid and internally consistent roadmap.~~

#### 0.7.9.0.7 Respect Roadmap Structure During Editing

<!-- GitMap-ID: btredsjc -->





Ensure that editing and adding items follow the hierarchy selected for the roadmap.

**Work Steps:**

- [ ] (a) Read the roadmap's selected structure before presenting edit options
- [ ] (b) Offer only valid parent levels for new items
- [ ] (c) Do not offer direct Milestone Issues when Sections are enabled
- [ ] (d) Do not offer direct Section Issues when Features are enabled
- [ ] (e) Preserve the selected hierarchy when adding new items
- [ ] (f) Validate the resulting hierarchy after an edit

**End Goal:**

- Editing an existing roadmap follows the same structural rules used when the roadmap was created.

## 0.7.10 GitHub Repository Setup

<!-- GitMap-ID: ivredshv -->

Allow a completed roadmap to be connected to a new or existing GitHub repository.

#### 0.7.10.0.1 Choose Repository

<!-- GitMap-ID: oqredsmp -->






Allow the user to choose where the roadmap will be synchronized.

**End Goal:**

- Connect the completed roadmap to the appropriate GitHub repository.

##### 0.7.10.0.1.1 (a) Use an existing repository

##### 0.7.10.0.1.2 (b) Create a new repository

#### 0.7.10.0.2 Create Repository

<!-- GitMap-ID: pqredsmo -->






Create a GitHub repository directly from GitMap.

**End Goal:**

- Create the repository without requiring the user to leave GitMap.

##### 0.7.10.0.2.1 (a) Ask for the repository name

##### 0.7.10.0.2.2 (b) Ask for a repository description

##### 0.7.10.0.2.3 (c) Allow public or private visibility

##### 0.7.10.0.2.4 (d) Create the repository through GitHub

##### 0.7.10.0.2.5 (e) Confirm successful repository creation

#### 0.7.10.0.3 Connect Repository

<!-- GitMap-ID: qqredsmn -->






Connect the roadmap to the selected repository.

**End Goal:**

- Make the selected repository the synchronization target for the roadmap.

##### 0.7.10.0.3.1 (a) Verify repository access

##### 0.7.10.0.3.2 (b) Store the repository association

##### 0.7.10.0.3.3 (c) Prepare the repository for synchronization

#### 0.7.10.0.4 Initial Synchronization

<!-- GitMap-ID: rqredsmm -->






Allow the completed roadmap to proceed directly into GitMap's existing synchronization workflow.

**End Goal:**

- Move from roadmap creation to GitHub synchronization without restarting GitMap.

##### 0.7.10.0.4.1 (a) Preview the initial synchronization

##### 0.7.10.0.4.2 (b) Require confirmation before synchronization

##### 0.7.10.0.4.3 (c) Synchronize the roadmap to the repository

##### 0.7.10.0.4.4 (d) Report synchronization results

## 0.7.11 Roadmap Maintenance

<!-- GitMap-ID: jvredshu -->

Allow users to continue managing a roadmap after it has been created and connected to GitHub.

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

Provide a simple command-line interface for the complete GitMap workflow.

#### 0.8.1.0.1 Create Main GitMap Command

<!-- GitMap-ID: xqredsmg -->






Create the primary command used to launch GitMap.

**End Goal:**

- Create the primary command used to launch GitMap.

##### 0.8.1.0.1.1 (a) Provide a `gitmap` command

##### 0.8.1.0.1.2 (b) Display useful help

##### 0.8.1.0.1.3 (c) Display the installed version

##### 0.8.1.0.1.4 (d) Exit cleanly when requested

#### 0.8.1.0.2 Create Roadmap Command

<!-- GitMap-ID: yqredsmf -->






Provide a command for creating or working with a roadmap.

**End Goal:**

- Provide a command for creating or working with a roadmap.

##### 0.8.1.0.2.1 (a) Start the interactive roadmap builder

##### 0.8.1.0.2.2 (b) Allow an existing roadmap to be opened

##### 0.8.1.0.2.3 (c) Validate the roadmap before completing

##### 0.8.1.0.2.4 (d) Save changes to `roadmap.md`

#### 0.8.1.0.3 Create Preview Command

<!-- GitMap-ID: zqredsme -->






Provide a command for previewing how GitMap interprets a roadmap.

**End Goal:**

- Provide a command for previewing how GitMap interprets a roadmap.

##### 0.8.1.0.3.1 (a) Parse the selected roadmap

##### 0.8.1.0.3.2 (b) Display its hierarchy

##### 0.8.1.0.3.3 (c) Report validation problems

##### 0.8.1.0.3.4 (d) Make no GitHub changes

#### 0.8.1.0.4 Create Setup Command

<!-- GitMap-ID: aqredsmd -->






Guide the user through connecting a roadmap to a GitHub repository.

**End Goal:**

- Guide the user through connecting a roadmap to a GitHub repository.

##### 0.8.1.0.4.1 (a) Ask for the GitHub username

##### 0.8.1.0.4.2 (b) Ask for the repository name

##### 0.8.1.0.4.3 (c) Configure authentication

##### 0.8.1.0.4.4 (d) Verify repository access

##### 0.8.1.0.4.5 (e) Save non-sensitive repository configuration

#### 0.8.1.0.5 Create Sync Command

<!-- GitMap-ID: bqredsmc -->






Provide a command for synchronizing the roadmap with GitHub.

**End Goal:**

- Provide a command for synchronizing the roadmap with GitHub.

##### 0.8.1.0.5.1 (a) Validate before synchronization

##### 0.8.1.0.5.2 (b) Verify repository access

##### 0.8.1.0.5.3 (c) Support dry-run mode

##### 0.8.1.0.5.4 (d) Display planned changes

##### 0.8.1.0.5.5 (e) Display a synchronization summary

## 0.8.2 Errors and Guidance

<!-- GitMap-ID: lvredshs -->

Make GitMap understandable when something goes wrong.

#### 0.8.2.0.1 Add User-Friendly Errors

<!-- GitMap-ID: cqredsmb -->






Replace technical failures with useful messages when possible.

**End Goal:**

- Replace technical failures with useful messages when possible.

##### 0.8.2.0.1.1 (a) Explain missing roadmap files

##### 0.8.2.0.1.2 (b) Explain malformed roadmaps

##### 0.8.2.0.1.3 (c) Explain authentication failures

##### 0.8.2.0.1.4 (d) Explain repository access failures

##### 0.8.2.0.1.5 (e) Avoid unnecessary Python tracebacks during normal use

#### 0.8.2.0.2 Add Next-Step Guidance

<!-- GitMap-ID: dqredsma -->


Tell users what they can do after each major operation.

**End Goal:**

- Tell users what they can do after each major operation.

##### 0.8.2.0.2.1 (a) Provide guidance after roadmap creation

##### 0.8.2.0.2.2 (b) Provide guidance after repository setup

##### 0.8.2.0.2.3 (c) Provide guidance after preview

##### 0.8.2.0.2.4 (d) Provide guidance after synchronization

## 0.9 GitMap Desktop GUI

Create a graphical desktop interface for GitMap using PySide6 and Qt Designer.

The GUI will provide a visual workspace for creating, opening, viewing, editing, saving, previewing and synchronizing
GitMap roadmaps while reusing the existing GitMap parser, model, numbering, validation and GitHub synchronization logic.

The GUI must act as an interface to the existing GitMap core rather than becoming a separate implementation of GitMap.

### 0.9.1 Main GitMap Workspace

#### 0.9.1.0.1 Load the Designer-Based Main Window

**Requirements:**

- [ ] Load the GitMap GUI from a Qt Designer interface while keeping application behavior in Python.

**Work Steps:**

- [ ] (a) Create `gitmap/gui/app.py`
- [ ] (b) Create `gitmap/gui/main_window.ui`
- [ ] (c) Create the GUI module entry point
- [ ] (d) Create the `QApplication`
- [ ] (e) Locate `main_window.ui` relative to `app.py`
- [ ] (f) Open the `.ui` file using `QFile`
- [ ] (g) Load the interface using `QUiLoader`
- [ ] (h) Display the loaded main window
- [ ] (i) Verify GitMap launches without UI loading errors

#### 0.9.1.0.2 Create the Main Workspace Layout

**Requirements:**

- [ ] Provide a large roadmap workspace with a smaller navigation and action area that resizes correctly with the
  application window.

**Work Steps:**

- [ ] (a) Create the main central widget in Qt Designer
- [ ] (b) Create the roadmap workspace area
- [ ] (c) Create the navigation and action area
- [ ] (d) Place the two areas inside a splitter
- [ ] (e) Give the roadmap area the larger initial share of the window
- [ ] (f) Configure layouts so controls resize with the window
- [ ] (g) Test the interface at its normal startup size
- [ ] (h) Test the interface maximized
- [ ] (i) Verify the roadmap tree fills the available workspace

#### 0.9.1.0.3 Create the Empty Workspace State

**Requirements:**

- [ ] When no roadmap is loaded, clearly provide Create Roadmap and Open Roadmap actions and transition to
  roadmap-specific controls after a roadmap becomes active.

**Work Steps:**

- [ ] (a) Add the Create Roadmap button
- [ ] (b) Add the Open Roadmap button
- [ ] (c) Assign stable Designer object names to both buttons
- [ ] (d) Locate both buttons from Python using `findChild`
- [ ] (e) Define the empty-workspace state
- [ ] (f) Define the active-roadmap state
- [ ] (g) Switch between the states when appropriate

#### 0.9.1.0.4 Create the Roadmap Tree

**Requirements:**

- [ ] Display the active roadmap in a large expandable and scrollable tree without an unnecessary column heading.

**Work Steps:**

- [ ] (a) Add the roadmap tree in Qt Designer
- [ ] (b) Assign the roadmap tree a stable object name
- [ ] (c) Locate the tree using `findChild`
- [ ] (d) Hide the tree header
- [ ] (e) Verify vertical scrolling
- [ ] (f) Verify long roadmap items remain usable
- [ ] (g) Verify the tree resizes with the workspace

#### 0.9.1.0.5 Display the Roadmap Name

**Requirements:**

- [ ] Display the name of the active roadmap from the Roadmap model and update it whenever the active roadmap changes.

**Work Steps:**

- [ ] (a) Read the roadmap name from the Roadmap model
- [ ] (b) Display the roadmap name in the workspace
- [ ] (c) Update the displayed name when another roadmap is opened
- [ ] (d) Update the displayed name when the roadmap is renamed
- [ ] (e) Support displaying the name of an unsaved roadmap

### 0.9.2 Open Existing Roadmaps

#### 0.9.2.0 Open Roadmap Workflow

##### 0.9.2.0.1 Open a Roadmap File

**Requirements:**

- The Open Roadmap button must open the operating system's file picker.
- Markdown files must be the preferred file type.
- Cancelling the dialog must leave the current application state unchanged.

**Work Steps:**

- [ ] 0.9.2.0.1 (a) Locate the Open Roadmap button from the Designer UI.
- [ ] 0.9.2.0.1 (b) Connect its clicked signal.
- [ ] 0.9.2.0.1 (c) Open `QFileDialog`.
- [ ] 0.9.2.0.1 (d) Configure the Markdown file filter.
- [ ] 0.9.2.0.1 (e) Capture the selected path.
- [ ] 0.9.2.0.1 (f) Handle cancellation without changing the workspace.

##### 0.9.2.0.2 Parse an Opened Roadmap

**Requirements:**

- Existing roadmaps must be parsed using GitMap's existing parser.
- The GUI must not have its own Markdown parser.
- All model information available to the CLI must remain available to the GUI.

**Work Steps:**

- [ ] 0.9.2.0.2 (a) Import `parse_roadmap`.
- [ ] 0.9.2.0.2 (b) Pass the selected path to `parse_roadmap`.
- [ ] 0.9.2.0.2 (c) Store the resulting Roadmap model.
- [ ] 0.9.2.0.2 (d) Verify the roadmap name.
- [ ] 0.9.2.0.2 (e) Verify Milestones.
- [ ] 0.9.2.0.2 (f) Verify Sections.
- [ ] 0.9.2.0.2 (g) Verify Features.
- [ ] 0.9.2.0.2 (h) Verify Issues.
- [ ] 0.9.2.0.2 (i) Verify Requirements.
- [ ] 0.9.2.0.2 (j) Verify Work Steps.

##### 0.9.2.0.3 Populate the Workspace

**Requirements:**

- A successfully parsed roadmap must replace the previous tree contents.
- The workspace must display the newly opened roadmap.
- Opening a roadmap must not modify its Markdown file.

**Work Steps:**

- [ ] 0.9.2.0.3 (a) Clear the existing roadmap tree.
- [ ] 0.9.2.0.3 (b) Display the roadmap name.
- [ ] 0.9.2.0.3 (c) Populate the complete hierarchy.
- [ ] 0.9.2.0.3 (d) Expand the tree.
- [ ] 0.9.2.0.3 (e) Store the active roadmap path.
- [ ] 0.9.2.0.3 (f) Change the GUI to its active-roadmap state.
- [ ] 0.9.2.0.3 (g) Verify merely opening a roadmap causes no file changes.

##### 0.9.2.0.4 Handle Roadmap Opening Errors

**Requirements:**

- A bad or invalid roadmap must not crash the desktop application.
- File and parser errors must eventually be presented graphically.
- Diagnostic information must remain available for development.

**Work Steps:**

- [ ] 0.9.2.0.4 (a) Catch file opening failures.
- [ ] 0.9.2.0.4 (b) Catch parser failures.
- [ ] 0.9.2.0.4 (c) Display a Qt error dialog.
- [ ] 0.9.2.0.4 (d) Include useful error information.
- [ ] 0.9.2.0.4 (e) Leave the existing roadmap intact after a failed open.
- [ ] 0.9.2.0.4 (f) Preserve diagnostic output for debugging.

### 0.9.3 Create New Roadmaps

#### 0.9.3.0 Roadmap Structure Setup

##### 0.9.3.0.1 Create the Structure Dialog

**Requirements:**

- Create Roadmap must open a separate structure configuration dialog.
- Structure selection must occur before the new roadmap workspace is created.
- Structure configuration must remain separate from saving.
- The user must not be forced to select a file location before beginning work.

**Work Steps:**

- [ ] 0.9.3.0.1 (a) Create `structure_dialog.ui`.
- [ ] 0.9.3.0.1 (b) Load the dialog from Python.
- [ ] 0.9.3.0.1 (c) Connect Create Roadmap to the dialog.
- [ ] 0.9.3.0.1 (d) Add confirmation and cancellation controls.
- [ ] 0.9.3.0.1 (e) Return the selected structure configuration.
- [ ] 0.9.3.0.1 (f) Verify cancelling returns to the existing workspace unchanged.

##### 0.9.3.0.2 Configure Sections

**Requirements:**

- The user must be able to enable or disable Sections.
- Section-related options must be disabled when Sections are unavailable.
- Controls should remain visible while disabled so the interface does not jump around.

**Work Steps:**

- [ ] 0.9.3.0.2 (a) Add the Use Sections option.
- [ ] 0.9.3.0.2 (b) Detect changes to the option.
- [ ] 0.9.3.0.2 (c) Enable Section-dependent controls when Sections are enabled.
- [ ] 0.9.3.0.2 (d) Grey out Section-dependent controls when Sections are disabled.
- [ ] 0.9.3.0.2 (e) Update the live example immediately.

##### 0.9.3.0.3 Configure Features

**Requirements:**

- The user must be able to enable or disable Features.
- Feature-related controls must be disabled when Features are unavailable.
- Feature controls should remain visible while disabled.

**Work Steps:**

- [ ] 0.9.3.0.3 (a) Add the Use Features option.
- [ ] 0.9.3.0.3 (b) Detect changes to the option.
- [ ] 0.9.3.0.3 (c) Enable Feature-dependent controls when appropriate.
- [ ] 0.9.3.0.3 (d) Grey out unavailable Feature controls.
- [ ] 0.9.3.0.3 (e) Update the live example immediately.

##### 0.9.3.0.4 Configure Issue Placement

**Requirements:**

- The structure dialog must control valid Issue locations.
- It must support Issues under Sections when Sections are enabled.
- It must support Issues under Features when Features are enabled.
- Invalid combinations must not be selectable.

**Work Steps:**

- [ ] 0.9.3.0.4 (a) Add Allow Issues under Sections.
- [ ] 0.9.3.0.4 (b) Add Allow Issues under Features.
- [ ] 0.9.3.0.4 (c) Disable Section Issue placement when Sections are disabled.
- [ ] 0.9.3.0.4 (d) Disable Feature Issue placement when Features are disabled.
- [ ] 0.9.3.0.4 (e) Validate the final configuration.
- [ ] 0.9.3.0.4 (f) Update the live example after each change.

#### 0.9.3.1 Live Structure Example

##### 0.9.3.1.1 Create the Baseball Parks Example

**Requirements:**

- The structure dialog must contain a live visual hierarchy example.
- The example must demonstrate organization rather than prescribe project structure.
- The example must be rendered visually rather than shown as raw Markdown.
- The example must change as structural options change.

**Work Steps:**

- [ ] 0.9.3.1.1 (a) Add a Live Example area.
- [ ] 0.9.3.1.1 (b) Add `0.1 MLB Parks`.
- [ ] 0.9.3.1.1 (c) Use American League and National League as Section examples.
- [ ] 0.9.3.1.1 (d) Use baseball divisions such as AL East and NL East as Feature examples.
- [ ] 0.9.3.1.1 (e) Use Camden Yards and Nationals Park as Issue examples.
- [ ] 0.9.3.1.1 (f) Add a small `0.2 NFL Stadiums` example.
- [ ] 0.9.3.1.1 (g) Include example Requirements.
- [ ] 0.9.3.1.1 (h) Include example Work Steps.
- [ ] 0.9.3.1.1 (i) Update the example when Sections are toggled.
- [ ] 0.9.3.1.1 (j) Update the example when Features are toggled.
- [ ] 0.9.3.1.1 (k) Update the example when Issue placement changes.

##### 0.9.3.1.2 Explain GitMap Hierarchy Levels

**Requirements:**

- The structure dialog must explain what each level can represent.
- Explanations must be examples rather than restrictions.
- Requirements must be described as what should be done.
- Work Steps must be described as steps for doing it.

**Work Steps:**

- [ ] 0.9.3.1.2 (a) Explain Milestone as a major phase.
- [ ] 0.9.3.1.2 (b) Explain Section as an area or subsystem.
- [ ] 0.9.3.1.2 (c) Explain Feature as a feature or capability.
- [ ] 0.9.3.1.2 (d) Explain Issue as a specific task.
- [ ] 0.9.3.1.2 (e) Explain Requirements as what should be done.
- [ ] 0.9.3.1.2 (f) Explain Work Steps as steps for doing it.
- [ ] 0.9.3.1.2 (g) State that the Baseball Parks example demonstrates organization rather than a prescribed project
  structure.

#### 0.9.3.2 Unsaved Roadmaps

##### 0.9.3.2.1 Create an Unsaved Roadmap Workspace

**Requirements:**

- Finishing structure setup must create an in-memory Roadmap.
- The user must immediately be able to work with it.
- A file path must not be required yet.
- The GUI must identify the roadmap as unsaved.

**Work Steps:**

- [ ] 0.9.3.2.1 (a) Create the Roadmap model.
- [ ] 0.9.3.2.1 (b) Apply the selected structure settings.
- [ ] 0.9.3.2.1 (c) Populate the empty main workspace.
- [ ] 0.9.3.2.1 (d) Mark the roadmap as unsaved.
- [ ] 0.9.3.2.1 (e) Enable roadmap editing controls.
- [ ] 0.9.3.2.1 (f) Verify no file is created automatically.

### 0.9.4 Roadmap Navigation

#### 0.9.4.0 Interactive Tree Navigation

##### 0.9.4.0.1 Associate Tree Items With Model Objects

**Requirements:**

- A tree item must identify its underlying GitMap object.
- The GUI must not identify an object solely by displayed text.
- Permanent GitMap IDs should be used where available.
- Renumbering must not destroy GUI identity.

**Work Steps:**

- [ ] 0.9.4.0.1 (a) Store model information on each tree item.
- [ ] 0.9.4.0.1 (b) Store the item type.
- [ ] 0.9.4.0.1 (c) Store the permanent GitMap ID where available.
- [ ] 0.9.4.0.1 (d) Resolve selections back to their model objects.
- [ ] 0.9.4.0.1 (e) Test object lookup after renumbering.

##### 0.9.4.0.2 Select Roadmap Items

**Requirements:**

- Users must be able to select roadmap items.
- Selection must provide the context needed for roadmap actions.
- Available actions must reflect the selected item type.

**Work Steps:**

- [ ] 0.9.4.0.2 (a) Detect tree selection changes.
- [ ] 0.9.4.0.2 (b) Resolve the selected model object.
- [ ] 0.9.4.0.2 (c) Determine the selected item type.
- [ ] 0.9.4.0.2 (d) Update available navigation actions.

##### 0.9.4.0.3 Open Items From the Tree

**Requirements:**

- Editable roadmap items must be openable from the roadmap tree.
- Double-clicking an editable item should open its Item Editor.
- Opening an editor must not replace the main roadmap workspace.

**Work Steps:**

- [ ] 0.9.4.0.3 (a) Detect tree double-clicks.
- [ ] 0.9.4.0.3 (b) Resolve the clicked model object.
- [ ] 0.9.4.0.3 (c) Determine whether the item is editable.
- [ ] 0.9.4.0.3 (d) Open the appropriate Item Editor.
- [ ] 0.9.4.0.3 (e) Leave the main workspace open.

### 0.9.5 Item Editors

#### 0.9.5.0 Pop-Out Item Editor

##### 0.9.5.0.1 Create the Item Editor Window

**Requirements:**

- Roadmap editing must occur in a separate window.
- The main roadmap must remain visible while an editor is open.
- Multiple editor windows should be able to remain open simultaneously.
- The editor interface should be defined using Qt Designer.

**Work Steps:**

- [ ] 0.9.5.0.1 (a) Create `item_editor.ui`.
- [ ] 0.9.5.0.1 (b) Create the Python controller for Item Editors.
- [ ] 0.9.5.0.1 (c) Pass the selected model object into the editor.
- [ ] 0.9.5.0.1 (d) Populate the editor from the selected item.
- [ ] 0.9.5.0.1 (e) Keep the main workspace available.
- [ ] 0.9.5.0.1 (f) Support more than one editor window.
- [ ] 0.9.5.0.1 (g) Verify closing an editor does not close GitMap.

##### 0.9.5.0.2 Adapt the Editor to Item Type

**Requirements:**

- The editor must adapt to Milestones, Sections, Features, Issues, Requirements and Work Steps.
- Controls that do not apply to the selected type must not be editable.
- Common editing behavior should be shared where practical.

**Work Steps:**

- [ ] 0.9.5.0.2 (a) Detect the model object type.
- [ ] 0.9.5.0.2 (b) Configure the editor for Milestones.
- [ ] 0.9.5.0.2 (c) Configure the editor for Sections.
- [ ] 0.9.5.0.2 (d) Configure the editor for Features.
- [ ] 0.9.5.0.2 (e) Configure the editor for Issues.
- [ ] 0.9.5.0.2 (f) Configure the editor for Requirements.
- [ ] 0.9.5.0.2 (g) Configure the editor for Work Steps.

##### 0.9.5.0.3 Edit Item Content

**Requirements:**

- Titles must be editable where supported.
- Descriptions must be editable where supported.
- Changes must first affect the in-memory roadmap.
- Editing must not automatically synchronize GitHub.

**Work Steps:**

- [ ] 0.9.5.0.3 (a) Populate the title control.
- [ ] 0.9.5.0.3 (b) Populate the description control.
- [ ] 0.9.5.0.3 (c) Validate edited values.
- [ ] 0.9.5.0.3 (d) Apply approved changes to the model.
- [ ] 0.9.5.0.3 (e) Refresh the roadmap tree.
- [ ] 0.9.5.0.3 (f) Mark the roadmap as modified.

#### 0.9.5.1 Issue Contents

##### 0.9.5.1.1 Edit Requirements

**Requirements:**

- Requirements must be manageable without editing Markdown manually.
- Users must be able to add, edit, remove and check Requirements.

**Work Steps:**

- [ ] 0.9.5.1.1 (a) Display existing Requirements.
- [ ] 0.9.5.1.1 (b) Add a Requirement.
- [ ] 0.9.5.1.1 (c) Edit Requirement text.
- [ ] 0.9.5.1.1 (d) Change Requirement completion state.
- [ ] 0.9.5.1.1 (e) Remove a Requirement.
- [ ] 0.9.5.1.1 (f) Refresh the roadmap tree after changes.

##### 0.9.5.1.2 Edit Work Steps

**Requirements:**

- Work Steps must be manageable without manually editing Markdown.
- Users must be able to add, edit, remove and check Work Steps.
- Work Step markers must remain consistent.

**Work Steps:**

- [ ] 0.9.5.1.2 (a) Display existing Work Steps.
- [ ] 0.9.5.1.2 (b) Add a Work Step.
- [ ] 0.9.5.1.2 (c) Assign the next Work Step marker.
- [ ] 0.9.5.1.2 (d) Edit Work Step text.
- [ ] 0.9.5.1.2 (e) Change Work Step completion state.
- [ ] 0.9.5.1.2 (f) Remove a Work Step.
- [ ] 0.9.5.1.2 (g) Renumber Work Step markers when required.
- [ ] 0.9.5.1.2 (h) Refresh the roadmap tree.

### 0.9.6 Add, Insert and Delete Roadmap Items

#### 0.9.6.0 Add Items

##### 0.9.6.0.1 Add Valid Child Items

**Requirements:**

- The GUI must determine which child types are valid for the selected parent.
- Available child types must respect the roadmap's structure configuration.
- The GUI must not allow invalid hierarchy relationships.

**Work Steps:**

- [ ] 0.9.6.0.1 (a) Determine the selected parent type.
- [ ] 0.9.6.0.1 (b) Determine the roadmap structure configuration.
- [ ] 0.9.6.0.1 (c) Build the list of valid child types.
- [ ] 0.9.6.0.1 (d) Disable invalid choices.
- [ ] 0.9.6.0.1 (e) Create the selected child.
- [ ] 0.9.6.0.1 (f) Assign its GitMap identity.
- [ ] 0.9.6.0.1 (g) Refresh the roadmap tree.

##### 0.9.6.0.2 Insert Items Between Existing Siblings

**Requirements:**

- The GUI must support insertion between existing siblings.
- Users must not need to manually calculate the new roadmap number.
- Existing GitMap automatic numbering logic must be used.

**Work Steps:**

- [ ] 0.9.6.0.2 (a) Display valid insertion positions.
- [ ] 0.9.6.0.2 (b) Let the user choose a position.
- [ ] 0.9.6.0.2 (c) Use GitMap's sibling numbering logic.
- [ ] 0.9.6.0.2 (d) Determine affected descendants.
- [ ] 0.9.6.0.2 (e) Generate the numbering preview.
- [ ] 0.9.6.0.2 (f) Apply the insertion only after approval.

#### 0.9.6.1 Delete Items

##### 0.9.6.1.1 Delete Roadmap Items Safely

**Requirements:**

- Users must be able to delete supported roadmap items.
- Descendant effects must be made clear.
- Renumbering caused by deletion must use existing GitMap logic.
- Destructive changes must require appropriate confirmation.

**Work Steps:**

- [ ] 0.9.6.1.1 (a) Select the item to delete.
- [ ] 0.9.6.1.1 (b) Determine its descendants.
- [ ] 0.9.6.1.1 (c) Determine resulting numbering changes.
- [ ] 0.9.6.1.1 (d) Display the proposed deletion.
- [ ] 0.9.6.1.1 (e) Display numbering changes.
- [ ] 0.9.6.1.1 (f) Allow approval or cancellation.
- [ ] 0.9.6.1.1 (g) Apply only the approved deletion.
- [ ] 0.9.6.1.1 (h) Refresh the roadmap tree.

### 0.9.7 Graphical Change Preview

#### 0.9.7.0 Preview Window

##### 0.9.7.0.1 Create the Roadmap Preview Window

**Requirements:**

- Changes that require approval must have a dedicated graphical preview.
- The preview must not replace the main workspace.
- The preview should be implemented as a separate Designer interface.

**Work Steps:**

- [ ] 0.9.7.0.1 (a) Create `preview_dialog.ui`.
- [ ] 0.9.7.0.1 (b) Create the preview controller.
- [ ] 0.9.7.0.1 (c) Pass proposed changes to the preview.
- [ ] 0.9.7.0.1 (d) Display the preview as a separate window.
- [ ] 0.9.7.0.1 (e) Provide Approve and Cancel actions.

##### 0.9.7.0.2 Display Before and After Changes

**Requirements:**

- The preview must make changed values understandable.
- Number changes must clearly identify both the old and proposed number.
- The user must be able to determine which roadmap items are affected before approval.

**Work Steps:**

- [ ] 0.9.7.0.2 (a) Collect the original values.
- [ ] 0.9.7.0.2 (b) Collect the proposed values.
- [ ] 0.9.7.0.2 (c) Display Before information.
- [ ] 0.9.7.0.2 (d) Display After information.
- [ ] 0.9.7.0.2 (e) Highlight affected roadmap items.
- [ ] 0.9.7.0.2 (f) Make large previews scrollable.

##### 0.9.7.0.3 Cancel Previewed Changes

**Requirements:**

- Cancelling must leave the roadmap exactly as it was before the proposed operation.
- Existing GitMap rollback behavior should be reused where applicable.

**Work Steps:**

- [ ] 0.9.7.0.3 (a) Preserve the original state before generating changes.
- [ ] 0.9.7.0.3 (b) Detect cancellation.
- [ ] 0.9.7.0.3 (c) Restore original numbering.
- [ ] 0.9.7.0.3 (d) Restore original hierarchy.
- [ ] 0.9.7.0.3 (e) Refresh the tree.
- [ ] 0.9.7.0.3 (f) Verify cancellation produces no saved changes.

### 0.9.8 Save Roadmaps

#### 0.9.8.0 Save and Save As

##### 0.9.8.0.1 Save an Existing Roadmap

**Requirements:**

- Save must write the current roadmap to its existing file.
- Only the current approved model state may be saved.
- Save must not require another file-selection dialog when a path is already known.

**Work Steps:**

- [ ] 0.9.8.0.1 (a) Track the active roadmap path.
- [ ] 0.9.8.0.1 (b) Serialize the current Roadmap model.
- [ ] 0.9.8.0.1 (c) Write the roadmap to its existing path.
- [ ] 0.9.8.0.1 (d) Clear the unsaved-change state.
- [ ] 0.9.8.0.1 (e) Report successful saving.

##### 0.9.8.0.2 Save a New Roadmap

**Requirements:**

- A new roadmap must remain usable before it has a file path.
- Its first Save must prompt for a location.
- The selected location becomes the active roadmap path.

**Work Steps:**

- [ ] 0.9.8.0.2 (a) Detect that the roadmap has no saved path.
- [ ] 0.9.8.0.2 (b) Open the Save dialog.
- [ ] 0.9.8.0.2 (c) Suggest a Markdown file.
- [ ] 0.9.8.0.2 (d) Save the roadmap.
- [ ] 0.9.8.0.2 (e) Store the selected path.
- [ ] 0.9.8.0.2 (f) Clear the unsaved state.

##### 0.9.8.0.3 Save As

**Requirements:**

- Save As must allow a roadmap to be written to a different file.
- The new file must become the active roadmap file after success.

**Work Steps:**

- [ ] 0.9.8.0.3 (a) Add Save As.
- [ ] 0.9.8.0.3 (b) Open the Save As dialog.
- [ ] 0.9.8.0.3 (c) Write the current roadmap to the selected path.
- [ ] 0.9.8.0.3 (d) Update the active roadmap path.
- [ ] 0.9.8.0.3 (e) Update the window state.

#### 0.9.8.1 Unsaved Changes

##### 0.9.8.1.1 Track Modified Roadmaps

**Requirements:**

- GitMap must know when the in-memory roadmap differs from its last saved version.
- The GUI must visibly indicate unsaved changes.

**Work Steps:**

- [ ] 0.9.8.1.1 (a) Add a modified-state flag.
- [ ] 0.9.8.1.1 (b) Set it after approved edits.
- [ ] 0.9.8.1.1 (c) Set it after additions.
- [ ] 0.9.8.1.1 (d) Set it after deletions.
- [ ] 0.9.8.1.1 (e) Clear it after successful Save.
- [ ] 0.9.8.1.1 (f) Display the modified state in the GUI.

##### 0.9.8.1.2 Protect Unsaved Work

**Requirements:**

- Unsaved work must not be silently destroyed.
- Protection must apply when closing GitMap, opening another roadmap or creating a replacement roadmap.

**Work Steps:**

- [ ] 0.9.8.1.2 (a) Detect unsaved changes before replacement.
- [ ] 0.9.8.1.2 (b) Offer Save.
- [ ] 0.9.8.1.2 (c) Offer Discard.
- [ ] 0.9.8.1.2 (d) Offer Cancel.
- [ ] 0.9.8.1.2 (e) Stop the requested operation when Cancel is selected.
- [ ] 0.9.8.1.2 (f) Verify closing the application protects unsaved work.

### 0.9.9 Roadmap Settings

#### 0.9.9.0 Roadmap Configuration

##### 0.9.9.0.1 Create Roadmap Settings

**Requirements:**

- Roadmap-wide configuration must be separate from individual item editing.
- Existing roadmap settings must be viewable graphically.

**Work Steps:**

- [ ] 0.9.9.0.1 (a) Create the Roadmap Settings interface.
- [ ] 0.9.9.0.1 (b) Display the roadmap name.
- [ ] 0.9.9.0.1 (c) Display numbering mode.
- [ ] 0.9.9.0.1 (d) Display starting series.
- [ ] 0.9.9.0.1 (e) Display GitHub representation.
- [ ] 0.9.9.0.1 (f) Display hierarchy Issue title style.
- [ ] 0.9.9.0.1 (g) Display GUI structure configuration.

##### 0.9.9.0.2 Safely Modify Roadmap Settings

**Requirements:**

- Supported settings must be editable.
- Changes that affect existing numbering or hierarchy must be previewed before application.
- Invalid structural changes must be rejected.

**Work Steps:**

- [ ] 0.9.9.0.2 (a) Determine editable settings.
- [ ] 0.9.9.0.2 (b) Validate proposed settings.
- [ ] 0.9.9.0.2 (c) Determine whether existing items are affected.
- [ ] 0.9.9.0.2 (d) Generate a preview when required.
- [ ] 0.9.9.0.2 (e) Apply only approved changes.
- [ ] 0.9.9.0.2 (f) Refresh the workspace.

### 0.9.10 GitHub Synchronization

#### 0.9.10.0 GUI Synchronization Workflow

##### 0.9.10.0.1 Start Synchronization From the GUI

**Requirements:**

- The GUI must expose GitMap's existing GitHub synchronization.
- Synchronization must use existing GitMap GitHub logic.
- The GUI must not implement a second synchronization engine.

**Work Steps:**

- [ ] 0.9.10.0.1 (a) Add the synchronization action.
- [ ] 0.9.10.0.1 (b) Validate the current roadmap.
- [ ] 0.9.10.0.1 (c) Call the existing synchronization preview logic.
- [ ] 0.9.10.0.1 (d) Display the synchronization preview.
- [ ] 0.9.10.0.1 (e) Continue only after approval.

##### 0.9.10.0.2 Display the Synchronization Preview

**Requirements:**

- The GUI must display Added, Changed, Unchanged and Removed items.
- Existing GitHub modifications must remain protected by GitMap's approval system.
- A modification not included in the approved plan must not be performed.

**Work Steps:**

- [ ] 0.9.10.0.2 (a) Display Added items.
- [ ] 0.9.10.0.2 (b) Display Changed items.
- [ ] 0.9.10.0.2 (c) Display Unchanged items.
- [ ] 0.9.10.0.2 (d) Display Removed items.
- [ ] 0.9.10.0.2 (e) Allow detailed review.
- [ ] 0.9.10.0.2 (f) Require approval.
- [ ] 0.9.10.0.2 (g) Preserve the approved synchronization plan.

##### 0.9.10.0.3 Apply Only Approved GitHub Changes

**Requirements:**

- Existing GitHub items must not be modified unless their modification was shown in the synchronization preview and
  approved.
- The GUI must preserve the protections introduced by GitMap 0.7.7.0.2.

**Work Steps:**

- [ ] 0.9.10.0.3 (a) Pass the approved plan to synchronization.
- [ ] 0.9.10.0.3 (b) Create approved new GitHub items.
- [ ] 0.9.10.0.3 (c) Modify approved existing GitHub items.
- [ ] 0.9.10.0.3 (d) Close approved removed GitHub items.
- [ ] 0.9.10.0.3 (e) Block operations absent from the approved plan.
- [ ] 0.9.10.0.3 (f) Verify GitMap IDs remain intact.

##### 0.9.10.0.4 Display Synchronization Results

**Requirements:**

- Users must not need the development console to determine synchronization results.
- Successes, skipped operations and errors must be visible in the GUI.

**Work Steps:**

- [ ] 0.9.10.0.4 (a) Collect synchronization results.
- [ ] 0.9.10.0.4 (b) Display created items.
- [ ] 0.9.10.0.4 (c) Display updated items.
- [ ] 0.9.10.0.4 (d) Display closed items.
- [ ] 0.9.10.0.4 (e) Display skipped operations.
- [ ] 0.9.10.0.4 (f) Display failures.
- [ ] 0.9.10.0.4 (g) Refresh the roadmap workspace after synchronization.

### 0.9.11 User Feedback and Error Handling

#### 0.9.11.0 Application Feedback

##### 0.9.11.0.1 Use the Status Bar

**Requirements:**

- Normal application state must be visible without inspecting the console.
- Short-lived status information should use the main window status bar.

**Work Steps:**

- [ ] 0.9.11.0.1 (a) Initialize the status bar.
- [ ] 0.9.11.0.1 (b) Display Ready.
- [ ] 0.9.11.0.1 (c) Display Roadmap opened.
- [ ] 0.9.11.0.1 (d) Display Roadmap saved.
- [ ] 0.9.11.0.1 (e) Display Unsaved changes.
- [ ] 0.9.11.0.1 (f) Display Synchronizing.
- [ ] 0.9.11.0.1 (g) Display Synchronization complete.
- [ ] 0.9.11.0.1 (h) Display Operation cancelled when appropriate.

##### 0.9.11.0.2 Display User-Friendly Errors

**Requirements:**

- Expected application errors must be presented graphically.
- Errors must explain what failed without exposing unnecessary implementation details.
- Developer diagnostics may still be logged separately.

**Work Steps:**

- [ ] 0.9.11.0.2 (a) Create a common GUI error-display helper.
- [ ] 0.9.11.0.2 (b) Handle roadmap file errors.
- [ ] 0.9.11.0.2 (c) Handle parser errors.
- [ ] 0.9.11.0.2 (d) Handle validation errors.
- [ ] 0.9.11.0.2 (e) Handle save errors.
- [ ] 0.9.11.0.2 (f) Handle GitHub errors.
- [ ] 0.9.11.0.2 (g) Preserve useful diagnostic logging.

### 0.9.12 Desktop Application Behavior

#### 0.9.12.0 Keyboard and Window Behavior

##### 0.9.12.0.1 Add Standard Keyboard Shortcuts

**Requirements:**

- Common desktop actions should have familiar keyboard shortcuts.
- Shortcuts must call the same application actions as their GUI controls.

**Work Steps:**

- [ ] 0.9.12.0.1 (a) Add Ctrl+O for Open Roadmap.
- [ ] 0.9.12.0.1 (b) Add Ctrl+S for Save.
- [ ] 0.9.12.0.1 (c) Add Ctrl+Shift+S for Save As.
- [ ] 0.9.12.0.1 (d) Add appropriate shortcuts for additional common actions.
- [ ] 0.9.12.0.1 (e) Verify shortcuts do not conflict with text editing.

##### 0.9.12.0.2 Support Normal Desktop Window Behavior

**Requirements:**

- The main workspace must remain independent from pop-out editors and previews.
- Closing a child window must not close GitMap.
- Closing GitMap must close its child windows appropriately.
- Window resizing must remain functional.

**Work Steps:**

- [ ] 0.9.12.0.2 (a) Establish ownership for dialogs.
- [ ] 0.9.12.0.2 (b) Establish ownership for Item Editors.
- [ ] 0.9.12.0.2 (c) Establish ownership for Preview windows.
- [ ] 0.9.12.0.2 (d) Test multiple simultaneous Item Editors.
- [ ] 0.9.12.0.2 (e) Test closing individual child windows.
- [ ] 0.9.12.0.2 (f) Test closing the main application.

### 0.9.13 Preserve the GitMap Core Architecture

#### 0.9.13.0 Reuse Existing GitMap Logic

##### 0.9.13.0.1 Reuse the Existing Parser

**Requirements:**

- The GUI must use the existing GitMap roadmap parser.
- GUI-specific parsing behavior must not duplicate the parser.

**Work Steps:**

- [ ] 0.9.13.0.1 (a) Route roadmap opening through `parse_roadmap`.
- [ ] 0.9.13.0.1 (b) Remove any temporary GUI parsing logic.
- [ ] 0.9.13.0.1 (c) Add parser regression tests discovered during GUI development.

##### 0.9.13.0.2 Reuse the Existing Model

**Requirements:**

- The GUI must operate on GitMap's existing model objects.
- GUI-only duplicate roadmap models must not be introduced.

**Work Steps:**

- [ ] 0.9.13.0.2 (a) Use the existing Roadmap model.
- [ ] 0.9.13.0.2 (b) Use the existing Milestone model.
- [ ] 0.9.13.0.2 (c) Use the existing Section model.
- [ ] 0.9.13.0.2 (d) Use the existing Feature model.
- [ ] 0.9.13.0.2 (e) Use the existing Issue model.
- [ ] 0.9.13.0.2 (f) Use the existing Requirement model.
- [ ] 0.9.13.0.2 (g) Use the existing Work Step representation.

##### 0.9.13.0.3 Reuse Automatic Numbering

**Requirements:**

- The GUI must use GitMap's existing automatic numbering system.
- GUI code must not independently calculate roadmap numbering.
- Existing insertion and sibling-renumbering behavior must remain authoritative.

**Work Steps:**

- [ ] 0.9.13.0.3 (a) Route GUI insertion through existing numbering functions.
- [ ] 0.9.13.0.3 (b) Route GUI deletion through existing renumbering functions.
- [ ] 0.9.13.0.3 (c) Route Work Step numbering through existing Work Step logic.
- [ ] 0.9.13.0.3 (d) Verify descendant numbering after GUI operations.
- [ ] 0.9.13.0.3 (e) Verify manual GUI calculations are not used.

##### 0.9.13.0.4 Reuse Validation

**Requirements:**

- GUI-created and GUI-edited roadmaps must obey the same validation rules as CLI-created roadmaps.
- The GUI must not permit invalid roadmaps merely because an operation originated graphically.

**Work Steps:**

- [ ] 0.9.13.0.4 (a) Validate newly created roadmap items.
- [ ] 0.9.13.0.4 (b) Validate edited roadmap items.
- [ ] 0.9.13.0.4 (c) Validate structural changes.
- [ ] 0.9.13.0.4 (d) Display validation failures graphically.
- [ ] 0.9.13.0.4 (e) Prevent invalid changes from being committed.

##### 0.9.13.0.5 Reuse GitHub Mapping

**Requirements:**

- The GUI must use existing GitMap GitHub mapping and synchronization logic.
- Permanent GitMap IDs must remain authoritative.
- Roadmap-specific GitHub searching must remain in effect.
- Existing synchronization approval protections must remain in effect.

**Work Steps:**

- [ ] 0.9.13.0.5 (a) Route GUI synchronization through existing GitHub mapping.
- [ ] 0.9.13.0.5 (b) Preserve permanent GitMap IDs.
- [ ] 0.9.13.0.5 (c) Preserve roadmap-specific searching.
- [ ] 0.9.13.0.5 (d) Preserve parent/child GitHub relationships.
- [ ] 0.9.13.0.5 (e) Preserve Issue identity during renumbering.
- [ ] 0.9.13.0.5 (f) Preserve approval before modifying existing GitHub items.

### 0.9.14 GUI Integration Testing

#### 0.9.14.0 End-to-End GUI Testing

##### 0.9.14.0.1 Test Existing Roadmaps

**Requirements:**

- Existing GitMap roadmaps must open without losing supported information.
- Different hierarchy configurations must be tested.

**Work Steps:**

- [ ] 0.9.14.0.1 (a) Open a roadmap using Milestones, Sections, Features and Issues.
- [ ] 0.9.14.0.1 (b) Open a roadmap containing direct Section Issues.
- [ ] 0.9.14.0.1 (c) Open a roadmap containing direct Milestone Issues.
- [ ] 0.9.14.0.1 (d) Open a roadmap containing Requirements.
- [ ] 0.9.14.0.1 (e) Open a roadmap containing Work Steps.
- [ ] 0.9.14.0.1 (f) Open a roadmap containing both Requirements and Work Steps.
- [ ] 0.9.14.0.1 (g) Verify all hierarchy levels render correctly.

##### 0.9.14.0.2 Test New Roadmap Creation

**Requirements:**

- Every supported structure configuration must produce a usable roadmap workspace.

**Work Steps:**

- [ ] 0.9.14.0.2 (a) Create a roadmap with Sections and Features.
- [ ] 0.9.14.0.2 (b) Create a roadmap with Sections but without Features.
- [ ] 0.9.14.0.2 (c) Create a roadmap without Sections.
- [ ] 0.9.14.0.2 (d) Test each supported Issue placement.
- [ ] 0.9.14.0.2 (e) Add items to each structure.
- [ ] 0.9.14.0.2 (f) Save each structure.
- [ ] 0.9.14.0.2 (g) Reopen each saved roadmap.
- [ ] 0.9.14.0.2 (h) Verify the reopened structure matches the created structure.

##### 0.9.14.0.3 Test Editing and Numbering

**Requirements:**

- GUI editing must preserve GitMap numbering, identity and approval behavior.

**Work Steps:**

- [ ] 0.9.14.0.3 (a) Add an item at the end of a sibling list.
- [ ] 0.9.14.0.3 (b) Insert an item between siblings.
- [ ] 0.9.14.0.3 (c) Preview resulting number changes.
- [ ] 0.9.14.0.3 (d) Cancel the insertion and verify rollback.
- [ ] 0.9.14.0.3 (e) Approve the insertion and verify numbering.
- [ ] 0.9.14.0.3 (f) Delete an item.
- [ ] 0.9.14.0.3 (g) Verify descendant numbering.
- [ ] 0.9.14.0.3 (h) Verify permanent GitMap IDs do not change.

##### 0.9.14.0.4 Test Saving and Unsaved Changes

**Requirements:**

- Saving and unsaved-work protection must operate reliably.

**Work Steps:**

- [ ] 0.9.14.0.4 (a) Modify an existing roadmap.
- [ ] 0.9.14.0.4 (b) Verify the unsaved indicator appears.
- [ ] 0.9.14.0.4 (c) Save the roadmap.
- [ ] 0.9.14.0.4 (d) Verify the indicator clears.
- [ ] 0.9.14.0.4 (e) Modify the roadmap again.
- [ ] 0.9.14.0.4 (f) Attempt to close GitMap.
- [ ] 0.9.14.0.4 (g) Test Save.
- [ ] 0.9.14.0.4 (h) Test Discard.
- [ ] 0.9.14.0.4 (i) Test Cancel.

##### 0.9.14.0.5 Test GitHub Synchronization

**Requirements:**

- GUI synchronization must produce the same protected results as CLI synchronization.

**Work Steps:**

- [ ] 0.9.14.0.5 (a) Preview a synchronization containing new items.
- [ ] 0.9.14.0.5 (b) Preview a synchronization containing changed items.
- [ ] 0.9.14.0.5 (c) Preview a synchronization containing removed items.
- [ ] 0.9.14.0.5 (d) Cancel synchronization and verify GitHub remains unchanged.
- [ ] 0.9.14.0.5 (e) Approve synchronization.
- [ ] 0.9.14.0.5 (f) Verify only approved operations occurred.
- [ ] 0.9.14.0.5 (g) Verify GitMap IDs remain associated with the correct GitHub Issues.
- [ ] 0.9.14.0.5 (h) Verify GitHub parent/child relationships remain correct.

# 0.10 Testing and Reliability

## 0.10.1 Automated Testing

<!-- GitMap-ID: xvredshg -->

Build a test suite that protects GitMap's roadmap and synchronization behavior.

#### 0.10.1.0.1 Test Roadmap Parsing

<!-- GitMap-ID: ysredskf -->

Test conversion of Markdown roadmaps into GitMap project data.

**End Goal:**

- Test conversion of Markdown roadmaps into GitMap project data.

##### 0.10.1.0.1.1 (a) Test milestones

##### 0.10.1.0.1.2 (b) Test Sections

##### 0.10.1.0.1.3 (c) Test issues

##### 0.10.1.0.1.4 (d) Test sub-issues

##### 0.10.1.0.1.5 (e) Test descriptions and requirements

#### 0.10.1.0.2 Test Roadmap Validation

<!-- GitMap-ID: zsredske -->






Test detection of invalid roadmap structures.

**End Goal:**

- Test detection of invalid roadmap structures.

##### 0.10.1.0.2.1 (a) Test malformed hierarchy

##### 0.10.1.0.2.2 (b) Test duplicate numbering

##### 0.10.1.0.2.3 (c) Test invalid parent relationships

##### 0.10.1.0.2.4 (d) Test useful validation messages

#### 0.10.1.0.3 Test GitHub Mapping

<!-- GitMap-ID: asredskd -->






Test conversion of roadmap data into GitHub structures.

**End Goal:**

- Test conversion of roadmap data into GitHub structures.

##### 0.10.1.0.3.1 (a) Test milestone mapping

##### 0.10.1.0.3.2 (b) Test label mapping

##### 0.10.1.0.3.3 (c) Test Section mapping

##### 0.10.1.0.3.4 (d) Test issue mapping

##### 0.10.1.0.3.5 (e) Test sub-issue relationships

#### 0.10.1.0.4 Test Duplicate Prevention

<!-- GitMap-ID: bsredskc -->






Verify that synchronization can safely run more than once.

**End Goal:**

- Verify that synchronization can safely run more than once.

##### 0.10.1.0.4.1 (a) Test existing labels

##### 0.10.1.0.4.2 (b) Test existing milestones

##### 0.10.1.0.4.3 (c) Test existing issues

##### 0.10.1.0.4.4 (d) Confirm repeated synchronization does not create duplicates

#### 0.10.1.0.5 Test Roadmap Updates

<!-- GitMap-ID: csredskb -->






Test synchronization after a roadmap has changed.

**End Goal:**

- Test synchronization after a roadmap has changed.

##### 0.10.1.0.5.1 (a) Test newly added items

##### 0.10.1.0.5.2 (b) Test changed items

##### 0.10.1.0.5.3 (c) Test unchanged items

##### 0.10.1.0.5.4 (d) Test removed roadmap items

##### 0.10.1.0.5.5 (e) Confirm destructive changes are not automatic

## 0.10.2 Failure Protection

<!-- GitMap-ID: yvredshf -->

Prevent partial or failed synchronization from leaving a project in a confusing state.

#### 0.10.2.0.1 Handle GitHub API Failures

<!-- GitMap-ID: dsredska -->






Handle failures while communicating with GitHub.

**End Goal:**

- Handle failures while communicating with GitHub.

##### 0.10.2.0.1.1 (a) Detect API errors

##### 0.10.2.0.1.2 (b) Report which operation failed

##### 0.10.2.0.1.3 (c) Preserve useful error details

##### 0.10.2.0.1.4 (d) Stop safely when synchronization cannot continue

#### 0.10.2.0.2 Test Dry Run Safety

<!-- GitMap-ID: esredskz -->






Verify that dry-run mode never changes GitHub.

**End Goal:**

- Verify that dry-run mode never changes GitHub.

##### 0.10.2.0.2.1 (a) Exercise the complete synchronization path

##### 0.10.2.0.2.2 (b) Confirm no create operations occur

##### 0.10.2.0.2.3 (c) Confirm no update operations occur

##### 0.10.2.0.2.4 (d) Confirm planned changes are still reported

#### 0.10.2.0.3 Add Integration Tests

<!-- GitMap-ID: fsredsky -->






Test complete GitMap workflows using representative roadmap data.

**End Goal:**

- Test complete GitMap workflows using representative roadmap data.

##### 0.10.2.0.3.1 (a) Test roadmap creation through parsing

##### 0.10.2.0.3.2 (b) Test parsing through synchronization planning

##### 0.10.2.0.3.3 (c) Test existing-project update workflows

##### 0.10.2.0.3.4 (d) Keep tests independent of a user's real GitHub repository where possible

# 0.11 Release Preparation

## 0.11.1 Documentation

<!-- GitMap-ID: zvredshe -->

Prepare GitMap for people other than its developers to install and use.

#### 0.11.1.0.1 Complete README

<!-- GitMap-ID: gtredsjx -->






Create the main user-facing GitMap documentation.

**End Goal:**

- Create the main user-facing GitMap documentation.

##### 0.11.1.0.1.1 (a) Explain what GitMap does

##### 0.11.1.0.1.2 (b) Explain the roadmap-first workflow

##### 0.11.1.0.1.3 (c) Explain installation

##### 0.11.1.0.1.4 (d) Explain basic commands

##### 0.11.1.0.1.5 (e) Provide a simple first-use example

#### 0.11.1.0.2 Create Roadmap Format Guide

<!-- GitMap-ID: htredsjw -->






Create detailed documentation for writing GitMap roadmaps manually.

**End Goal:**

- Create detailed documentation for writing GitMap roadmaps manually.

##### 0.11.1.0.2.1 (a) Explain milestones

##### 0.11.1.0.2.2 (b) Explain Sections

##### 0.11.1.0.2.3 (c) Explain issues

##### 0.11.1.0.2.4 (d) Explain sub-issues

##### 0.11.1.0.2.5 (e) Explain descriptions and requirements

##### 0.11.1.0.2.6 (f) Provide complete examples

#### 0.11.1.0.3 Create GitHub Setup Guide

<!-- GitMap-ID: itredsjv -->






Document how to prepare a GitHub repository for GitMap.

**End Goal:**

- Document how to prepare a GitHub repository for GitMap.

##### 0.11.1.0.3.1 (a) Explain that the user creates the repository

##### 0.11.1.0.3.2 (b) Explain authentication setup

##### 0.11.1.0.3.3 (c) Explain required repository permissions

##### 0.11.1.0.3.4 (d) Explain how GitMap connects to the repository

##### 0.11.1.0.3.5 (e) Include troubleshooting guidance

## 0.11.2 Release

<!-- GitMap-ID: avredshd -->

Prepare the first usable GitMap release.

#### 0.11.2.0.1 Add Version Information

<!-- GitMap-ID: jtredsju -->






Provide consistent GitMap version information.

**End Goal:**

- Provide consistent GitMap version information.

##### 0.11.2.0.1.1 (a) Define the application version

##### 0.11.2.0.1.2 (b) Make the version available from the command line

##### 0.11.2.0.1.3 (c) Keep package and application versions consistent

#### 0.11.2.0.2 Run Release Test

<!-- GitMap-ID: ktredsjt -->






Test GitMap from a clean environment before release.

**End Goal:**

- Test GitMap from a clean environment before release.

##### 0.11.2.0.2.1 (a) Install GitMap from scratch

##### 0.11.2.0.2.2 (b) Create a new roadmap

##### 0.11.2.0.2.3 (c) Connect to a test repository

##### 0.11.2.0.2.4 (d) Preview synchronization

##### 0.11.2.0.2.5 (e) Perform synchronization

##### 0.11.2.0.2.6 (f) Run synchronization again to verify duplicate prevention

#### 0.11.2.0.3 Create Version 1.0 Release

<!-- GitMap-ID: ltredsjs -->






Publish the first stable GitMap release.

**End Goal:**

- Publish the first stable GitMap release.

##### 0.11.2.0.3.1 (a) Complete all required tests

##### 0.11.2.0.3.2 (b) Complete user documentation

##### 0.11.2.0.3.3 (c) Confirm the roadmap-first workflow works end to end

##### 0.11.2.0.3.4 (d) Tag the release as `v1.0.0`
