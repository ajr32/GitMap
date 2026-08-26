Title: GitMap Roadmap

Sub-Title: GitMap turns a project roadmap into a structured GitHub project.

# 0.1 Foundations (DONE)

## 0.1.1 Project Setup (DONE)

Set up the basic GitMap project so it can be installed, run, tested, and developed safely.

#### 0.1.1.0.1 Create Python Project (DONE)

Create the basic Python project structure for GitMap.

**End Goal:**
- Create the basic Python project structure for GitMap.

##### 0.1.1.0.1.1 (a) Create the `gitmap` package (DONE)

##### 0.1.1.0.1.2 (b) Create `../pyproject.toml` (DONE)

##### 0.1.1.0.1.3 (c) Create a `tests` directory (DONE)

##### 0.1.1.0.1.4 (d) Create a `../.gitignore` (DONE)

#### 0.1.1.0.2 Install Dependencies (DONE)

Set up the dependencies needed to develop and test GitMap.

**End Goal:**
- Set up the dependencies needed to develop and test GitMap.

##### 0.1.1.0.2.1 (a) Support editable installation (DONE)

##### 0.1.1.0.2.2 (b) Add `pytest` as a development dependency (DONE)

##### 0.1.1.0.2.3 (c) Confirm the development environment installs successfully (DONE)

#### 0.1.1.0.3 Create Command-Line Entry Point (DONE)

Create the basic command-line entry point for GitMap.

**End Goal:**
- Create the basic command-line entry point for GitMap.

##### 0.1.1.0.3.1 (a) Allow GitMap to be started from the command line (DONE)

##### 0.1.1.0.3.2 (b) Display a simple welcome message (DONE)

##### 0.1.1.0.3.3 (c) Exit cleanly (DONE)

#### 0.1.1.0.4 Add Initial Tests (DONE)

Create the first automated tests for GitMap.

**End Goal:**
- Create the first automated tests for GitMap.

##### 0.1.1.0.4.1 (a) Confirm GitMap can be imported (DONE)

##### 0.1.1.0.4.2 (b) Confirm the command-line entry point runs (DONE)

##### 0.1.1.0.4.3 (c) Confirm the test suite can be run with `pytest` (DONE)

#### 0.1.1.0.5 Add Project Documentation (DONE)

Create the basic documentation needed to understand and develop GitMap.

**End Goal:**
- Create the basic documentation needed to understand and develop GitMap.

##### 0.1.1.0.5.1 (a) Explain what GitMap does (DONE)

##### 0.1.1.0.5.2 (b) Explain how to install GitMap for development (DONE)

##### 0.1.1.0.5.3 (c) Explain how to run GitMap (DONE)

##### 0.1.1.0.5.4 (d) Explain how to run the tests (DONE)

## 0.1.2 Roadmap Format (DONE)

Define the Markdown structure GitMap will use to describe projects before they are synchronized with GitHub.

#### 0.1.2.0.1 Define Roadmap Structure (DONE)

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

Create a complete example roadmap that can be used for development and testing.

**End Goal:**
- Create a complete example roadmap that can be used for development and testing.

##### 0.1.2.0.2.1 (a) Include at least one milestone (DONE)

##### 0.1.2.0.2.2 (b) Include at least one Section (DONE)

##### 0.1.2.0.2.3 (c) Include multiple issues (DONE)

##### 0.1.2.0.2.4 (d) Include at least one sub-issue (DONE)

##### 0.1.2.0.2.5 (e) Include descriptions and requirements (DONE)

#### 0.1.2.0.3 Document Roadmap Format (DONE)

Document how users should write a GitMap roadmap.

**End Goal:**
- Document how users should write a GitMap roadmap.

##### 0.1.2.0.3.1 (a) Explain each heading level (DONE)

##### 0.1.2.0.3.2 (b) Show how milestones, Sections, issues, and sub-issues are represented (DONE)

##### 0.1.2.0.3.3 (c) Provide a copyable example (DONE)

# 0.2 Roadmap Parser (DONE)

## 0.2.1 Markdown Parsing (DONE)

Teach GitMap to read a roadmap and turn its Markdown structure into project data.

#### 0.2.1.0.1 Read Roadmap File (DONE)

Load a roadmap from a Markdown file.

**End Goal:**
- Load a roadmap from a Markdown file.

##### 0.2.1.0.1.1 (a) Accept a roadmap file path (DONE)

##### 0.2.1.0.1.2 (b) Read the Markdown contents (DONE)

##### 0.2.1.0.1.3 (c) Report a clear error if the file cannot be read (DONE)

#### 0.2.1.0.2 Parse Milestones (DONE)

Identify milestone headings in the roadmap.

**End Goal:**
- Identify milestone headings in the roadmap.

##### 0.2.1.0.2.1 (a) Recognize milestone headings (DONE)

##### 0.2.1.0.2.2 (b) Capture the milestone number and title (DONE)

##### 0.2.1.0.2.3 (c) Preserve the order of milestones (DONE)

#### 0.2.1.0.3 Parse Sections (DONE)

Identify Sections within each milestone.

**End Goal:**
- Identify Sections within each milestone.

##### 0.2.1.0.3.1 (a) Associate each Section with its milestone (DONE)

##### 0.2.1.0.3.2 (b) Capture the Section title (DONE)

##### 0.2.1.0.3.3 (c) Capture the Section description (DONE)

##### 0.2.1.0.3.4 (d) Recognize the Section type marker (DONE)

#### 0.2.1.0.4 Parse Issues (DONE)

Identify issues within each Section.

**End Goal:**
- Identify issues within each Section.

##### 0.2.1.0.4.1 (a) Associate each issue with its Section (DONE)

##### 0.2.1.0.4.2 (b) Capture the issue number and title (DONE)

##### 0.2.1.0.4.3 (c) Capture the issue description (DONE)

##### 0.2.1.0.4.4 (d) Capture requirements (DONE)

#### 0.2.1.0.5 Parse Work Steps (DONE)

Support issues nested beneath other issues.

**End Goal:**
- Support issues nested beneath other issues.

##### 0.2.1.0.5.1 (a) Associate each sub-issue with its parent issue (DONE)

##### 0.2.1.0.5.2 (b) Preserve the roadmap hierarchy (DONE)

##### 0.2.1.0.5.3 (c) Support numbering such as `0.2.4.1` (DONE)

## 0.2.2 Roadmap Validation (DONE)

Detect roadmap problems before anything is sent to GitHub.

#### 0.2.2.0.1 Validate Roadmap Structure (DONE)

Check that the roadmap follows GitMap's expected hierarchy.

**End Goal:**
- Check that the roadmap follows GitMap's expected hierarchy.

##### 0.2.2.0.1.1 (a) Detect issues outside a Section (DONE)

##### 0.2.2.0.1.2 (b) Detect Sections outside a milestone (DONE)

##### 0.2.2.0.1.3 (c) Detect malformed hierarchy (DONE)

##### 0.2.2.0.1.4 (d) Provide useful error messages (DONE)

#### 0.2.2.0.2 Validate Numbering (DONE)

Check roadmap numbering for obvious errors.

**End Goal:**
- Check roadmap numbering for obvious errors.

##### 0.2.2.0.2.1 (a) Detect duplicate numbers (DONE)

##### 0.2.2.0.2.2 (b) Detect invalid parent relationships (DONE)

##### 0.2.2.0.2.3 (c) Identify the location of the problem (DONE)

#### 0.2.2.0.3 Preview Parsed Roadmap (DONE)

Allow users to see what GitMap understood before synchronization.

**End Goal:**
- Allow users to see what GitMap understood before synchronization.

##### 0.2.2.0.3.1 (a) Display milestones (DONE)

##### 0.2.2.0.3.2 (b) Display Sections (DONE)

##### 0.2.2.0.3.3 (c) Display issues and sub-issues (DONE)

##### 0.2.2.0.3.4 (d) Preserve hierarchy in the preview (DONE)

# 0.3 GitHub Setup (DONE)

## 0.3.1 Repository Connection (DONE)

Connect a completed GitMap roadmap to a GitHub repository chosen by the user.

#### 0.3.1.0.1 Collect Repository Information (DONE)

Ask the user which GitHub repository should receive the roadmap.

**End Goal:**
- Ask the user which GitHub repository should receive the roadmap.

##### 0.3.1.0.1.1 (a) Ask for the GitHub username (DONE)

##### 0.3.1.0.1.2 (b) Ask for the repository name (DONE)

##### 0.3.1.0.1.3 (c) Do not create the repository automatically (DONE)

##### 0.3.1.0.1.4 (d) Allow roadmap creation to be completed before GitHub setup begins (DONE)

#### 0.3.1.0.2 Configure GitHub Authentication (DONE)

Set up authentication required to work with the selected repository.

**End Goal:**
- Set up authentication required to work with the selected repository.

##### 0.3.1.0.2.1 (a) Keep credentials outside source control (DONE)

##### 0.3.1.0.2.2 (b) Provide clear setup instructions (DONE)

##### 0.3.1.0.2.3 (c) Detect missing authentication (DONE)

##### 0.3.1.0.2.4 (d) Never store authentication tokens in the roadmap (DONE)

#### 0.3.1.0.3 Verify Repository (DONE)

Confirm that GitMap can access the repository before synchronization.

**End Goal:**
- Confirm that GitMap can access the repository before synchronization.

##### 0.3.1.0.3.1 (a) Verify that the repository exists (DONE)

##### 0.3.1.0.3.2 (b) Verify that authentication works (DONE)

##### 0.3.1.0.3.3 (c) Verify that the user has appropriate access (DONE)

##### 0.3.1.0.3.4 (d) Stop synchronization if verification fails (DONE)

## 0.3.2 GitHub Project Structure (DONE)

Translate GitMap's roadmap concepts into the GitHub structures needed for synchronization.

#### 0.3.2.0.1 Define Milestone Mapping (DONE)

Define how roadmap milestones map to GitHub milestones.

**End Goal:**
- Define how roadmap milestones map to GitHub milestones.

##### 0.3.2.0.1.1 (a) Preserve milestone titles (DONE)

##### 0.3.2.0.1.2 (b) Avoid creating duplicate milestones (DONE)

##### 0.3.2.0.1.3 (c) Allow existing milestones to be recognized (DONE)

#### 0.3.2.0.2 Define Label Mapping (DONE)

Define the labels GitMap uses when creating GitHub items.

**End Goal:**
- Define the labels GitMap uses when creating GitHub items.

##### 0.3.2.0.2.1 (a) Support labels for Sections (DONE)

##### 0.3.2.0.2.2 (b) Support labels for issues when defined by the roadmap (DONE)

##### 0.3.2.0.2.3 (c) Avoid creating duplicate labels (DONE)

##### 0.3.2.0.2.4 (d) Allow labels to be created before issues are synchronized (DONE)

#### 0.3.2.0.3 Define Issue Mapping (DONE)

Define how roadmap items become GitHub issues.

**End Goal:**
- Define how roadmap items become GitHub issues.

##### 0.3.2.0.3.1 (a) Preserve issue titles (DONE)

##### 0.3.2.0.3.2 (b) Preserve descriptions (DONE)

##### 0.3.2.0.3.3 (c) Preserve requirements (DONE)

##### 0.3.2.0.3.4 (d) Associate issues with their milestone (DONE)

##### 0.3.2.0.3.5 (e) Apply appropriate labels (DONE)

#### 0.3.2.0.4 Define Work Step Mapping (DONE)

Define how roadmap hierarchy is represented in GitHub.

**End Goal:**
- Define how roadmap hierarchy is represented in GitHub.

##### 0.3.2.0.4.1 (a) Preserve parent-child relationships when supported (DONE)

##### 0.3.2.0.4.2 (b) Keep sub-issues associated with their parent (DONE)

##### 0.3.2.0.4.3 (c) Preserve roadmap numbering (DONE)

# 0.4 GitHub Synchronization (DONE)

## 0.4.1 Synchronization Engine (DONE)

Synchronize the validated roadmap with the selected GitHub repository.

#### 0.4.1.0.1 Create Labels (DONE)

Create the labels required by the roadmap before synchronizing other items.

**End Goal:**
- Create the labels required by the roadmap before synchronizing other items.

##### 0.4.1.0.1.1 (a) Read required labels from the parsed roadmap (DONE)

##### 0.4.1.0.1.2 (b) Detect labels that already exist (DONE)

##### 0.4.1.0.1.3 (c) Create only missing labels (DONE)

##### 0.4.1.0.1.4 (d) Do not create duplicates (DONE)

#### 0.4.1.0.2 Create Milestones (DONE)

Create roadmap milestones in GitHub.

**End Goal:**
- Create roadmap milestones in GitHub.

##### 0.4.1.0.2.1 (a) Detect milestones that already exist (DONE)

##### 0.4.1.0.2.2 (b) Create only missing milestones (DONE)

##### 0.4.1.0.2.3 (c) Preserve milestone titles (DONE)

##### 0.4.1.0.2.4 (d) Do not create duplicates (DONE)

#### 0.4.1.0.3 Create Sections (DONE)

Create GitHub issues representing roadmap Sections.

**End Goal:**
- Create GitHub issues representing roadmap Sections.

##### 0.4.1.0.3.1 (a) Create the Section before its child issues (DONE)

##### 0.4.1.0.3.2 (b) Include the Section description (DONE)

##### 0.4.1.0.3.3 (c) Apply the Section label (DONE)

##### 0.4.1.0.3.4 (d) Associate the Section with its milestone (DONE)

##### 0.4.1.0.3.5 (e) Detect an existing matching Section before creating another (DONE)

#### 0.4.1.0.4 Create Issues (DONE)

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

Create roadmap sub-issues and associate them with their parent issues.

**End Goal:**
- Create roadmap sub-issues and associate them with their parent issues.

##### 0.4.1.0.5.1 (a) Create the parent before its sub-issues (DONE)

##### 0.4.1.0.5.2 (b) Preserve the parent-child hierarchy (DONE)

##### 0.4.1.0.5.3 (c) Include descriptions and requirements (DONE)

##### 0.4.1.0.5.4 (d) Associate sub-issues with the correct milestone (DONE)

## 0.4.2 Safe Synchronization (DONE)

Make synchronization predictable and safe to run more than once.

#### 0.4.2.0.1 Add Dry Run (DONE)

Allow users to preview what synchronization would change without changing GitHub.

**End Goal:**
- Allow users to preview what synchronization would change without changing GitHub.

##### 0.4.2.0.1.1 (a) Show items that would be created (DONE)

##### 0.4.2.0.1.2 (b) Show items that already exist (DONE)

##### 0.4.2.0.1.3 (c) Make no GitHub changes during a dry run (DONE)

##### 0.4.2.0.1.4 (d) Clearly identify dry-run output (DONE)

#### 0.4.2.0.2 Prevent Duplicate Items (DONE)

Make repeated synchronization safe.

**End Goal:**
- Make repeated synchronization safe.

##### 0.4.2.0.2.1 (a) Check GitHub before creating an item (DONE)

##### 0.4.2.0.2.2 (b) Reuse existing matching items (DONE)

##### 0.4.2.0.2.3 (c) Prevent duplicate labels (DONE)

##### 0.4.2.0.2.4 (d) Prevent duplicate milestones (DONE)

##### 0.4.2.0.2.5 (e) Prevent duplicate issues (DONE)

#### 0.4.2.0.3 Add Synchronization Summary (DONE)

Display the result of synchronization.

**End Goal:**
- Display the result of synchronization.

##### 0.4.2.0.3.1 (a) Report items created (DONE)

##### 0.4.2.0.3.2 (b) Report items already present (DONE)

##### 0.4.2.0.3.3 (c) Report skipped items (DONE)

##### 0.4.2.0.3.4 (d) Report errors (DONE)

# 0.5 Roadmap Updates (DONE)

## 0.5.1 Existing Project Import (DONE)

Allow GitMap to understand what already exists in a connected GitHub repository.

#### 0.5.1.0.1 Read Existing Milestones (DONE)

Retrieve existing milestones from the repository.

**End Goal:**
- Retrieve existing milestones from the repository.

##### 0.5.1.0.1.1 (a) Read open milestones (DONE)

##### 0.5.1.0.1.2 (b) Recognize milestones already represented in the roadmap (DONE)

##### 0.5.1.0.1.3 (c) Preserve GitHub milestone identifiers for later updates (DONE)

#### 0.5.1.0.2 Read Existing Labels (DONE)

Retrieve existing repository labels.

**End Goal:**
- Retrieve existing repository labels.

##### 0.5.1.0.2.1 (a) Read current labels (DONE)

##### 0.5.1.0.2.2 (b) Match existing labels to roadmap labels (DONE)

##### 0.5.1.0.2.3 (c) Avoid recreating labels that already exist (DONE)

#### 0.5.1.0.3 Read Existing Issues (DONE)

Retrieve existing GitHub issues that correspond to roadmap items.

**End Goal:**
- Retrieve existing GitHub issues that correspond to roadmap items.

##### 0.5.1.0.3.1 (a) Read existing issues (DONE)

##### 0.5.1.0.3.2 (b) Match issues to roadmap items (DONE)

##### 0.5.1.0.3.3 (c) Preserve GitHub issue numbers (DONE)

##### 0.5.1.0.3.4 (d) Distinguish GitMap-managed items from unrelated repository issues (DONE)

#### 0.5.1.0.4 Rebuild Roadmap State (DONE)

Use GitHub data to reconstruct the current state of a GitMap-managed project.

**End Goal:**
- Use GitHub data to reconstruct the current state of a GitMap-managed project.

##### 0.5.1.0.4.1 (a) Associate existing issues with milestones (DONE)

##### 0.5.1.0.4.2 (b) Restore Section and issue relationships (DONE)

##### 0.5.1.0.4.3 (c) Restore sub-issue relationships when available (DONE)

##### 0.5.1.0.4.4 (d) Identify roadmap items that cannot be matched safely (DONE)

## 0.5.2 Roadmap Changes (DONE)

Allow a user to modify the roadmap after the initial synchronization and safely apply those changes to GitHub.

#### 0.5.2.0.1 Detect Roadmap Changes  (DONE)

Compare the local roadmap with the current GitHub project.

**End Goal:**
- Compare the local roadmap with the current GitHub project.

##### 0.5.2.0.1.1 (a) Detect new roadmap items (DONE)

##### 0.5.2.0.1.2 (b) Detect changed roadmap items (DONE)

##### 0.5.2.0.1.3 (c) Detect items that already match GitHub (DONE)

##### 0.5.2.0.1.4 (d) Present differences before synchronization (DONE)

#### 0.5.2.0.2 Update Existing Items (DONE)

Update GitHub items when their corresponding roadmap entries change.

**End Goal:**
- Update GitHub items when their corresponding roadmap entries change.

##### 0.5.2.0.2.1 (a) Update titles when changed (DONE)

##### 0.5.2.0.2.2 (b) Update descriptions when changed (DONE)

##### 0.5.2.0.2.3 (c) Update requirements when changed (DONE)

##### 0.5.2.0.2.4 (d) Preserve GitHub issue numbers (DONE)

##### 0.5.2.0.2.5 (e) Avoid recreating existing items (DONE)

#### 0.5.2.0.3 Handle Removed Roadmap Items (DONE)

Safely identify items that exist in GitHub but have been removed from the roadmap.

**End Goal:**
- Safely identify items that exist in GitHub but have been removed from the roadmap.

##### 0.5.2.0.3.1 (a) Never delete GitHub items automatically (DONE)

##### 0.5.2.0.3.2 (b) Report removed roadmap items (DONE)

##### 0.5.2.0.3.3 (c) Require an explicit user decision before destructive changes (DONE)

##### 0.5.2.0.3.4 (d) Preserve historical GitHub data by default (DONE)

#### 0.5.2.0.4 Preview Updates (DONE)

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

Guide users through creating a roadmap without requiring them to know GitMap's Markdown format.

#### 0.6.1.0.1 Start New Roadmap (DONE)

Begin an interactive roadmap-building session.

**End Goal:**
- Begin an interactive roadmap-building session.

##### 0.6.1.0.1.1 (a) Ask for the project name (DONE)

##### 0.6.1.0.1.2 (b) Ask for a project overview (DONE)

##### 0.6.1.0.1.3 (c) Create the initial roadmap structure (DONE)

##### 0.6.1.0.1.4 (d) Do not require GitHub information yet (DONE)

#### 0.6.1.0.2 Collect Milestones (DONE)

Guide the user through defining project milestones.

**End Goal:**
- Guide the user through defining project milestones.

##### 0.6.1.0.2.1 (a) Ask for the milestone number (DONE)

##### 0.6.1.0.2.2 (b) Ask for the milestone title (DONE)

##### 0.6.1.0.2.3 (c) Allow multiple milestones (DONE)

##### 0.6.1.0.2.4 (d) Allow the user to indicate when they are finished (DONE)

#### 0.6.1.0.3 Collect Sections (DONE)

Guide the user through defining Sections within each milestone.

**End Goal:**
- Guide the user through defining Sections within each milestone.

##### 0.6.1.0.3.1 (a) Ask for the Section title (DONE)

##### 0.6.1.0.3.2 (b) Ask for a Section overview (DONE)

##### 0.6.1.0.3.3 (c) Associate the Section with its milestone (DONE)

##### 0.6.1.0.3.4 (d) Allow multiple Sections (DONE)

#### 0.6.1.0.4 Collect Issues (DONE)

Guide the user through defining issues within a Section.

**End Goal:**
- Guide the user through defining issues within a Section.

##### 0.6.1.0.4.1 (a) Ask for the issue title (DONE)

##### 0.6.1.0.4.2 (b) Ask for the issue description (DONE)

##### 0.6.1.0.4.3 (c) Ask for requirements (DONE)

##### 0.6.1.0.4.4 (d) Allow requirements to be entered individually (DONE)

##### 0.6.1.0.4.5 (e) Treat a blank entry as finished (DONE)

#### 0.6.1.0.5 Collect Work Steps (DONE)

Allow an issue to contain smaller sub-issues.

**End Goal:**
- Allow an issue to contain smaller sub-issues.

##### 0.6.1.0.5.1 (a) Ask whether an issue needs sub-issues (DONE)

##### 0.6.1.0.5.2 (b) Collect sub-issue titles (DONE)

##### 0.6.1.0.5.3 (c) Collect descriptions and requirements (DONE)

##### 0.6.1.0.5.4 (d) Preserve the parent-child relationship (DONE)

##### 0.6.1.0.5.5 (e) Support additional nesting when appropriate (DONE)

#### 0.6.1.0.6 Support Pasted Content (DONE)

Allow users to paste existing project information instead of answering every question individually.

**End Goal:**
- Allow users to paste existing project information instead of answering every question individually.

##### 0.6.1.0.6.1 (a) Accept pasted overview text (DONE)

##### 0.6.1.0.6.2 (b) Accept pasted descriptions (DONE)

##### 0.6.1.0.6.3 (c) Accept pasted requirements (DONE)

##### 0.6.1.0.6.4 (d) Preserve multiline content (DONE)

##### 0.6.1.0.6.5 (e) Allow interactive questions and pasted content to be mixed (DONE)

## 0.6.2 Roadmap Review (DONE)

Let the user review and revise the roadmap before connecting it to GitHub.

#### 0.6.2.0.1 Display Completed Roadmap (DONE)

Show the complete generated roadmap.

**End Goal:**
- Show the complete generated roadmap.

##### 0.6.2.0.1.1 (a) Preserve Markdown hierarchy (DONE)

##### 0.6.2.0.1.2 (b) Make milestone, Section, issue, and sub-issue relationships clear (DONE)

##### 0.6.2.0.1.3 (c) Show descriptions and requirements (DONE)

#### 0.6.2.0.2 Edit Roadmap Before Sync

Allow changes before GitHub synchronization begins.

**End Goal:**
- Allow changes before GitHub synchronization begins.

##### 0.6.2.0.2.1 (a) Allow items to be renamed (DONE)

##### 0.6.2.0.2.2 (b) Allow descriptions and requirements to be changed (DONE)

##### 0.6.2.0.2.3 (c) Allow items to be added (DONE)

##### 0.6.2.0.2.4 (d) Allow items to be removed

##### 0.6.2.0.2.5 (e) Revalidate the roadmap after changes

#### 0.6.2.0.3 Save Roadmap (DONE)

Save the completed roadmap to `roadmap.md`.

**End Goal:**
- Save the completed roadmap to `roadmap.md`.

##### 0.6.2.0.3.1 (a) Produce valid GitMap Markdown (DONE)

##### 0.6.2.0.3.2 (b) Preserve the complete hierarchy (DONE)

##### 0.6.2.0.3.3 (c) Confirm where the roadmap was saved (DONE)

# 0.7 Changes to make

## 0.7.1 Synchronization Workflow Improvements

Improve roadmap synchronization behavior discovered during real-world GitMap use.

#### 0.7.1.0.1 Improve Change Preview Flow (DONE)

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

Recognize existing roadmap items when their GitMap numbers change.

**End Goal:**
- Treat renumbered roadmap items as updates to existing GitHub items rather than unrelated removed and newly created items.

##### 0.7.1.0.2.1 (a) Detect an existing roadmap item after its number changes

##### 0.7.1.0.2.2 (b) Avoid relying solely on the GitMap number as item identity

##### 0.7.1.0.2.3 (c) Preserve the existing GitHub item when a roadmap item is renumbered

##### 0.7.1.0.2.4 (d) Update the GitMap marker after renumbering

##### 0.7.1.0.2.5 (e) Preserve existing GitHub issue numbers and relationships where possible

#### 0.7.1.0.3 Update Renumbered Milestones

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

#### 0.7.2.0.1 Validate Synchronization Plan

##### 0.7.2.0.1.1 (a) Detect duplicate GitMap identifiers
##### 0.7.2.0.1.2 (b) Detect duplicate milestone mappings
##### 0.7.2.0.1.3 (c) Detect ambiguous identity matches
##### 0.7.2.0.1.4 (d) Refuse to guess when identity cannot be determined safely
##### 0.7.2.0.1.5 (e) Explain conflicts before synchronization
##### 0.7.2.0.1.6 (f) Allow conflicts to be resolved before retrying

#### 0.7.2.0.2 Protect Partial Synchronization

##### 0.7.2.0.2.1 (a) Track completed synchronization operations
##### 0.7.2.0.2.2 (b) Identify the operation that failed
##### 0.7.2.0.2.3 (c) Report operations completed before failure
##### 0.7.2.0.2.4 (d) Report operations that remain incomplete
##### 0.7.2.0.2.5 (e) Stop safely when synchronization cannot continue
##### 0.7.2.0.2.6 (f) Preserve enough state for a safe retry

#### 0.7.2.0.3 Verify Synchronization Results

##### 0.7.2.0.3.1 (a) Re-read affected GitHub items after synchronization
##### 0.7.2.0.3.2 (b) Confirm expected items were created
##### 0.7.2.0.3.3 (c) Confirm expected items were updated
##### 0.7.2.0.3.4 (d) Confirm expected roadmap identities were preserved
##### 0.7.2.0.3.5 (e) Detect unexpected duplicate identifiers
##### 0.7.2.0.3.6 (f) Report differences between planned and actual results

#### 0.7.2.0.4 Support Safe Synchronization Retry

##### 0.7.2.0.4.1 (a) Re-read GitHub state before retrying
##### 0.7.2.0.4.2 (b) Recognize operations already completed
##### 0.7.2.0.4.3 (c) Avoid recreating successfully created items
##### 0.7.2.0.4.4 (d) Avoid reapplying unnecessary updates
##### 0.7.2.0.4.5 (e) Continue remaining synchronization work safely
##### 0.7.2.0.4.6 (f) Report final retry results

#### 0.7.2.0.5 Prevent Concurrent Synchronization

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

Improve command-line synchronization performance by avoiding unnecessary work.

#### 0.7.3.0.1 Skip Unchanged Items During Synchronization

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

Use the already-reviewed synchronization plan when applying changes.

**End Goal:**
- Avoid repeating work that was already completed while determining the synchronization preview.

##### 0.7.3.0.2.1 (a) Preserve the synchronization plan after preview

##### 0.7.3.0.2.2 (b) Use the approved plan when synchronization begins

##### 0.7.3.0.2.3 (c) Process only planned create and update operations

##### 0.7.3.0.2.4 (d) Avoid recalculating unchanged items unnecessarily

##### 0.7.3.0.2.5 (e) Ensure the applied plan matches the plan the user approved

## 0.7.4 GitHub Repository Setup

Allow a completed roadmap to be connected to a new or existing GitHub repository.

#### 0.7.4.0.1 Choose Repository

Allow the user to choose where the roadmap will be synchronized.

**End Goal:**
- Connect the completed roadmap to the appropriate GitHub repository.

##### 0.7.4.0.1.1 (a) Use an existing repository

##### 0.7.4.0.1.2 (b) Create a new repository

#### 0.7.4.0.2 Create Repository

Create a GitHub repository directly from GitMap.

**End Goal:**
- Create the repository without requiring the user to leave GitMap.

##### 0.7.4.0.2.1 (a) Ask for the repository name

##### 0.7.4.0.2.2 (b) Ask for a repository description

##### 0.7.4.0.2.3 (c) Allow public or private visibility

##### 0.7.4.0.2.4 (d) Create the repository through GitHub

##### 0.7.4.0.2.5 (e) Confirm successful repository creation

#### 0.7.4.0.3 Connect Repository

Connect the roadmap to the selected repository.

**End Goal:**
- Make the selected repository the synchronization target for the roadmap.

##### 0.7.4.0.3.1 (a) Verify repository access

##### 0.7.4.0.3.2 (b) Store the repository association

##### 0.7.4.0.3.3 (c) Prepare the repository for synchronization

#### 0.7.4.0.4 Initial Synchronization

Allow the completed roadmap to proceed directly into GitMap's existing synchronization workflow.

**End Goal:**
- Move from roadmap creation to GitHub synchronization without restarting GitMap.

##### 0.7.4.0.4.1 (a) Preview the initial synchronization

##### 0.7.4.0.4.2 (b) Require confirmation before synchronization

##### 0.7.4.0.4.3 (c) Synchronize the roadmap to the repository

##### 0.7.4.0.4.4 (d) Report synchronization results

## 0.7.5 Roadmap Numbering

Allow users to choose how roadmap item numbers are assigned while building and editing a roadmap.

#### 0.7.5.0.1 Explain Roadmap Numbering

Explain GitMap's numbering system when the user begins building a roadmap.

**End Goal:**
- Make the roadmap hierarchy and numbering rules clear before the user begins creating items.

##### 0.7.5.0.1.1 (a) Explain the milestone numbering format

##### 0.7.5.0.1.2 (b) Explain how child numbers extend their parent number

##### 0.7.5.0.1.3 (c) Show an example hierarchy

##### 0.7.5.0.1.4 (d) Explain automatic numbering

##### 0.7.5.0.1.5 (e) Explain manual numbering

#### 0.7.5.0.2 Choose Numbering Mode

Allow the user to choose between automatic and manual numbering.

**End Goal:**
- Let users control whether GitMap assigns roadmap numbers or they enter them manually.

##### 0.7.5.0.2.1 (a) Offer automatic numbering

##### 0.7.5.0.2.2 (b) Offer manual numbering

##### 0.7.5.0.2.3 (c) Allow manual numbering when automatic numbering cannot be used

#### 0.7.5.0.3 Choose Starting Series

Allow automatic numbering to reflect the project's development stage.

**End Goal:**
- Start roadmap numbering in the appropriate version series.

##### 0.7.5.0.3.1 (a) Offer pre-production numbering beginning with 0.x

##### 0.7.5.0.3.2 (b) Offer production numbering beginning with 1.x

#### 0.7.5.0.4 Generate Hierarchical Numbers

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

#### 0.7.5.0.5 Handle Numbering Conflicts

Prevent duplicate or conflicting roadmap numbers.

**End Goal:**
- Detect numbering conflicts and let the user decide how they should be resolved.

##### 0.7.5.0.5.1 (a) Detect duplicate roadmap numbers

##### 0.7.5.0.5.2 (b) Warn before changing existing numbers

##### 0.7.5.0.5.3 (c) Offer to renumber following items

##### 0.7.5.0.5.4 (d) Preview affected numbers before renumbering

##### 0.7.5.0.5.5 (e) Require confirmation before renumbering

##### 0.7.5.0.5.6 (f) Allow the user to switch to manual numbering

##### 0.7.5.0.5.7 (g) Allow the operation to be cancelled

##### 0.7.5.0.5.8 (h) Detect roadmap numbers that do not match their parent hierarchy

##### 0.7.5.0.5.9 (i) Explain the expected number when a hierarchy mismatch is found

# 0.8 Command-Line Experience

## 0.8.1 GitMap Commands

Provide a simple command-line interface for the complete GitMap workflow.

#### 0.8.1.0.1 Create Main GitMap Command

Create the primary command used to launch GitMap.

**End Goal:**
- Create the primary command used to launch GitMap.

##### 0.8.1.0.1.1 (a) Provide a `gitmap` command

##### 0.8.1.0.1.2 (b) Display useful help

##### 0.8.1.0.1.3 (c) Display the installed version

##### 0.8.1.0.1.4 (d) Exit cleanly when requested

#### 0.8.1.0.2 Create Roadmap Command

Provide a command for creating or working with a roadmap.

**End Goal:**
- Provide a command for creating or working with a roadmap.

##### 0.8.1.0.2.1 (a) Start the interactive roadmap builder

##### 0.8.1.0.2.2 (b) Allow an existing roadmap to be opened

##### 0.8.1.0.2.3 (c) Validate the roadmap before completing

##### 0.8.1.0.2.4 (d) Save changes to `roadmap.md`

#### 0.8.1.0.3 Create Preview Command

Provide a command for previewing how GitMap interprets a roadmap.

**End Goal:**
- Provide a command for previewing how GitMap interprets a roadmap.

##### 0.8.1.0.3.1 (a) Parse the selected roadmap

##### 0.8.1.0.3.2 (b) Display its hierarchy

##### 0.8.1.0.3.3 (c) Report validation problems

##### 0.8.1.0.3.4 (d) Make no GitHub changes

#### 0.8.1.0.4 Create Setup Command

Guide the user through connecting a roadmap to a GitHub repository.

**End Goal:**
- Guide the user through connecting a roadmap to a GitHub repository.

##### 0.8.1.0.4.1 (a) Ask for the GitHub username

##### 0.8.1.0.4.2 (b) Ask for the repository name

##### 0.8.1.0.4.3 (c) Configure authentication

##### 0.8.1.0.4.4 (d) Verify repository access

##### 0.8.1.0.4.5 (e) Save non-sensitive repository configuration

#### 0.8.1.0.5 Create Sync Command

Provide a command for synchronizing the roadmap with GitHub.

**End Goal:**
- Provide a command for synchronizing the roadmap with GitHub.

##### 0.8.1.0.5.1 (a) Validate before synchronization

##### 0.8.1.0.5.2 (b) Verify repository access

##### 0.8.1.0.5.3 (c) Support dry-run mode

##### 0.8.1.0.5.4 (d) Display planned changes

##### 0.8.1.0.5.5 (e) Display a synchronization summary

## 0.8.2 Errors and Guidance

Make GitMap understandable when something goes wrong.

#### 0.8.2.0.1 Add User-Friendly Errors

Replace technical failures with useful messages when possible.

**End Goal:**
- Replace technical failures with useful messages when possible.

##### 0.8.2.0.1.1 (a) Explain missing roadmap files

##### 0.8.2.0.1.2 (b) Explain malformed roadmaps

##### 0.8.2.0.1.3 (c) Explain authentication failures

##### 0.8.2.0.1.4 (d) Explain repository access failures

##### 0.8.2.0.1.5 (e) Avoid unnecessary Python tracebacks during normal use

#### 0.8.2.0.2 Add Next-Step Guidance

Tell users what they can do after each major operation.

**End Goal:**
- Tell users what they can do after each major operation.

##### 0.8.2.0.2.1 (a) Provide guidance after roadmap creation

##### 0.8.2.0.2.2 (b) Provide guidance after repository setup

##### 0.8.2.0.2.3 (c) Provide guidance after preview

##### 0.8.2.0.2.4 (d) Provide guidance after synchronization

# 0.9 Graphical User Interface

Create a graphical GitMap workspace for building, editing, reviewing, validating, and synchronizing roadmaps without requiring the user to work directly with Markdown or the command line.

The graphical interface should use the same underlying roadmap, validation, numbering, GitHub, and synchronization logic as the command-line workflow rather than creating a separate implementation.

## 0.9.1 GUI Foundation

Create the application foundation for the GitMap graphical interface.

#### 0.9.1.0.1 Create GUI Application

Create the primary graphical GitMap application.

**End Goal:**
- Provide a graphical application that can launch independently and use GitMap's existing core functionality.

##### 0.9.1.0.1.1 (a) Create the main GUI application entry point

##### 0.9.1.0.1.2 (b) Create the main application window

##### 0.9.1.0.1.3 (c) Set the application title and GitMap identity

##### 0.9.1.0.1.4 (d) Allow the application to close cleanly

##### 0.9.1.0.1.5 (e) Keep GUI code separate from core roadmap logic

##### 0.9.1.0.1.6 (f) Reuse existing GitMap builder, parser, validator, and GitHub functionality where appropriate

#### 0.9.1.0.2 Create Main Workspace

Create the primary workspace used while working with a roadmap.

**End Goal:**
- Provide a consistent workspace for navigating, editing, and previewing a roadmap.

##### 0.9.1.0.2.1 (a) Create a roadmap navigation area

##### 0.9.1.0.2.2 (b) Create an item editor area

##### 0.9.1.0.2.3 (c) Create a live preview area

##### 0.9.1.0.2.4 (d) Create an application status area

##### 0.9.1.0.2.5 (e) Keep the selected roadmap item synchronized between workspace areas

##### 0.9.1.0.2.6 (f) Allow workspace areas to remain usable with large roadmaps

#### 0.9.1.0.3 Create Project Start Screen

Provide clear ways to begin working in GitMap.

**End Goal:**
- Allow the user to create a new project or continue working with an existing roadmap.

##### 0.9.1.0.3.1 (a) Provide a New Roadmap option

##### 0.9.1.0.3.2 (b) Provide an Open Roadmap option

##### 0.9.1.0.3.3 (c) Allow an existing `roadmap.md` file to be selected

##### 0.9.1.0.3.4 (d) Parse an opened roadmap into the GitMap data model

##### 0.9.1.0.3.5 (e) Report roadmap loading errors clearly

##### 0.9.1.0.3.6 (f) Open a successfully loaded roadmap in the main workspace

#### 0.9.1.0.4 Track Roadmap State

Track whether the roadmap has changed while it is open.

**End Goal:**
- Prevent changes made in the GUI from being accidentally lost.

##### 0.9.1.0.4.1 (a) Detect changes made in the editor

##### 0.9.1.0.4.2 (b) Mark the roadmap as modified when appropriate

##### 0.9.1.0.4.3 (c) Clear the modified state after saving

##### 0.9.1.0.4.4 (d) Warn before closing a roadmap with unsaved changes

##### 0.9.1.0.4.5 (e) Allow the user to save, discard, or cancel when unsaved changes exist


## 0.9.2 Roadmap Navigation

Allow users to move quickly through roadmaps of any practical size.

#### 0.9.2.0.1 Create Roadmap Tree

Display the roadmap as an expandable hierarchy.

**End Goal:**
- Make the complete roadmap structure understandable and navigable without displaying the entire roadmap at once.

##### 0.9.2.0.1.1 (a) Display milestones

##### 0.9.2.0.1.2 (b) Display Sections beneath milestones

##### 0.9.2.0.1.3 (c) Display features beneath Sections

##### 0.9.2.0.1.4 (d) Display issues beneath their actual parents

##### 0.9.2.0.1.5 (e) Display Work Steps beneath issues

##### 0.9.2.0.1.6 (f) Display nested Work Steps recursively

##### 0.9.2.0.1.7 (g) Allow branches to be expanded and collapsed

##### 0.9.2.0.1.8 (h) Clearly indicate the currently selected item

##### 0.9.2.0.1.9 (i) Preserve the roadmap's actual hierarchy when optional levels are absent

#### 0.9.2.0.2 Select Roadmap Items

Allow an item in the roadmap tree to be opened for editing.

**End Goal:**
- Make navigating to any roadmap item a direct operation.

##### 0.9.2.0.2.1 (a) Select an item from the roadmap tree

##### 0.9.2.0.2.2 (b) Load the selected item into the editor

##### 0.9.2.0.2.3 (c) Update the live preview for the selected item

##### 0.9.2.0.2.4 (d) Keep tree, editor, and preview selection synchronized

#### 0.9.2.0.3 Add Go To Navigation

Allow users to jump directly to a roadmap item.

**End Goal:**
- Make individual items easy to locate even in very large roadmaps.

##### 0.9.2.0.3.1 (a) Provide a Go To control

##### 0.9.2.0.3.2 (b) Search by roadmap number

##### 0.9.2.0.3.3 (c) Search by item title

##### 0.9.2.0.3.4 (d) Display matching roadmap items while searching

##### 0.9.2.0.3.5 (e) Distinguish similar titles using their roadmap numbers and hierarchy

##### 0.9.2.0.3.6 (f) Select the chosen item in the roadmap tree

##### 0.9.2.0.3.7 (g) Expand collapsed parents when jumping to an item

##### 0.9.2.0.3.8 (h) Open the selected item in the editor

##### 0.9.2.0.3.9 (i) Move the live preview to the selected context

#### 0.9.2.0.4 Preserve Navigation Context

Avoid forcing the user to repeatedly find their place.

**End Goal:**
- Keep navigation predictable while the roadmap is being edited.

##### 0.9.2.0.4.1 (a) Preserve expanded and collapsed tree branches during normal editing

##### 0.9.2.0.4.2 (b) Preserve the selected item after edits

##### 0.9.2.0.4.3 (c) Move selection appropriately after an item is added

##### 0.9.2.0.4.4 (d) Move selection to an appropriate parent or sibling after an item is removed

##### 0.9.2.0.4.5 (e) Preserve useful navigation context after renumbering


## 0.9.3 Roadmap Editor

Allow the roadmap to be changed directly through graphical controls.

#### 0.9.3.0.1 Display Item Editor

Display fields appropriate to the selected roadmap item.

**End Goal:**
- Provide a clear editing interface based on the type of item being edited.

##### 0.9.3.0.1.1 (a) Display the item type

##### 0.9.3.0.1.2 (b) Display the roadmap number

##### 0.9.3.0.1.3 (c) Display the title

##### 0.9.3.0.1.4 (d) Display descriptions or overviews where supported

##### 0.9.3.0.1.5 (e) Display requirements where supported

##### 0.9.3.0.1.6 (f) Display the item's parent relationship

##### 0.9.3.0.1.7 (g) Hide fields that do not apply to the selected item type

#### 0.9.3.0.2 Edit Roadmap Items

Allow roadmap content to be changed directly.

**End Goal:**
- Allow normal roadmap editing without requiring Markdown editing.

##### 0.9.3.0.2.1 (a) Rename items

##### 0.9.3.0.2.2 (b) Edit descriptions and overviews

##### 0.9.3.0.2.3 (c) Add requirements

##### 0.9.3.0.2.4 (d) Edit requirements

##### 0.9.3.0.2.5 (e) Remove requirements

##### 0.9.3.0.2.6 (f) Preserve multiline content

##### 0.9.3.0.2.7 (g) Update the roadmap data model when changes are accepted

#### 0.9.3.0.3 Add Roadmap Items

Allow new items to be added from anywhere appropriate in the roadmap.

**End Goal:**
- Make it easy to add newly discovered work to an existing roadmap.

##### 0.9.3.0.3.1 (a) Add milestones

##### 0.9.3.0.3.2 (b) Add Sections to milestones

##### 0.9.3.0.3.3 (c) Add features to Sections

##### 0.9.3.0.3.4 (d) Add issues to milestones

##### 0.9.3.0.3.5 (e) Add issues to Sections

##### 0.9.3.0.3.6 (f) Add issues to features

##### 0.9.3.0.3.7 (g) Add Work Steps to issues

##### 0.9.3.0.3.8 (h) Add nested Work Steps

##### 0.9.3.0.3.9 (i) Select the newly added item for editing

#### 0.9.3.0.4 Insert Roadmap Items

Allow new work to be inserted at a specific location in the roadmap.

**End Goal:**
- Allow newly discovered roadmap items to be placed where they logically belong rather than only appended.

##### 0.9.3.0.4.1 (a) Insert an item before a sibling

##### 0.9.3.0.4.2 (b) Insert an item after a sibling

##### 0.9.3.0.4.3 (c) Preserve the selected parent relationship

##### 0.9.3.0.4.4 (d) Detect when insertion creates a numbering conflict

##### 0.9.3.0.4.5 (e) Use the Roadmap Numbering workflow to resolve numbering conflicts

##### 0.9.3.0.4.6 (f) Never silently renumber existing roadmap items

#### 0.9.3.0.5 Remove Roadmap Items

Allow items to be removed safely.

**End Goal:**
- Allow unwanted roadmap content to be removed without accidentally deleting additional work.

##### 0.9.3.0.5.1 (a) Remove individual roadmap items

##### 0.9.3.0.5.2 (b) Warn when an item contains children

##### 0.9.3.0.5.3 (c) Show which descendants would also be removed

##### 0.9.3.0.5.4 (d) Require confirmation before removing an item with descendants

##### 0.9.3.0.5.5 (e) Allow removal to be cancelled

##### 0.9.3.0.5.6 (f) Revalidate the roadmap after removal


## 0.9.4 Graphical Numbering

Expose GitMap's roadmap-numbering system through the GUI.

#### 0.9.4.0.1 Select Numbering Mode

Allow the user to control how roadmap numbers are assigned.

**End Goal:**
- Make automatic numbering easy to use while retaining complete manual control.

##### 0.9.4.0.1.1 (a) Provide an Auto numbering option

##### 0.9.4.0.1.2 (b) Provide a Manual numbering option

##### 0.9.4.0.1.3 (c) Clearly display the current numbering mode

##### 0.9.4.0.1.4 (d) Allow manual numbering for an individual item when appropriate

#### 0.9.4.0.2 Display Automatic Numbers

Show numbers GitMap will assign before an item is created.

**End Goal:**
- Let users understand automatic numbering without needing to calculate numbers themselves.

##### 0.9.4.0.2.1 (a) Display the next automatically generated number

##### 0.9.4.0.2.2 (b) Update the proposed number when the parent changes

##### 0.9.4.0.2.3 (c) Account for optional Section and feature levels

##### 0.9.4.0.2.4 (d) Account for nested Work Steps

##### 0.9.4.0.2.5 (e) Display generated letter sequences where applicable

#### 0.9.4.0.3 Handle Numbering Conflicts

Provide a graphical workflow when an automatic or manual number conflicts with the roadmap.

**End Goal:**
- Prevent duplicate numbers without making unusual roadmap structures impossible.

##### 0.9.4.0.3.1 (a) Clearly identify the conflicting number

##### 0.9.4.0.3.2 (b) Identify the existing item using the number

##### 0.9.4.0.3.3 (c) Offer to renumber affected items

##### 0.9.4.0.3.4 (d) Offer to switch the new item to manual numbering

##### 0.9.4.0.3.5 (e) Allow the operation to be cancelled

#### 0.9.4.0.4 Preview Renumbering

Show the impact of renumbering before changing the roadmap.

**End Goal:**
- Ensure the user understands every existing roadmap number that will change.

##### 0.9.4.0.4.1 (a) List affected roadmap items

##### 0.9.4.0.4.2 (b) Display each old number

##### 0.9.4.0.4.3 (c) Display each proposed new number

##### 0.9.4.0.4.4 (d) Include affected descendants

##### 0.9.4.0.4.5 (e) Require explicit confirmation

##### 0.9.4.0.4.6 (f) Apply the renumbering only after confirmation

##### 0.9.4.0.4.7 (g) Refresh navigation and preview after renumbering


## 0.9.5 Live Roadmap Preview

Provide a useful live representation of the roadmap without overwhelming the user with the complete document.

#### 0.9.5.0.1 Create Contextual Live Preview

Display the part of the roadmap relevant to the item currently being edited.

**End Goal:**
- Let users see the effect of their work immediately while keeping the preview manageable.

##### 0.9.5.0.1.1 (a) Show the currently selected item

##### 0.9.5.0.1.2 (b) Show enough parent hierarchy to establish context

##### 0.9.5.0.1.3 (c) Show immediate children where useful

##### 0.9.5.0.1.4 (d) Avoid displaying the entire roadmap by default

##### 0.9.5.0.1.5 (e) Update the preview when selection changes

#### 0.9.5.0.2 Update Preview While Editing

Refresh the contextual preview as roadmap content changes.

**End Goal:**
- Make the preview reflect what the user is currently creating or editing.

##### 0.9.5.0.2.1 (a) Update titles while they are edited

##### 0.9.5.0.2.2 (b) Update descriptions and overviews while they are edited

##### 0.9.5.0.2.3 (c) Update requirements while they are edited

##### 0.9.5.0.2.4 (d) Update hierarchy after items are added or removed

##### 0.9.5.0.2.5 (e) Update displayed numbers after numbering changes

##### 0.9.5.0.2.6 (f) Avoid unnecessary full-roadmap rendering during normal editing

#### 0.9.5.0.3 Navigate From Preview

Allow the preview itself to act as a roadmap navigation tool.

**End Goal:**
- Let users move directly from something they see in the preview to editing that item.

##### 0.9.5.0.3.1 (a) Make roadmap items in the preview selectable

##### 0.9.5.0.3.2 (b) Select the corresponding item in the roadmap tree

##### 0.9.5.0.3.3 (c) Open the corresponding item in the editor

##### 0.9.5.0.3.4 (d) Update preview context around the newly selected item

#### 0.9.5.0.4 View Full Roadmap

Allow the complete roadmap to be inspected when requested.

**End Goal:**
- Provide full-roadmap review without making it the default editing view.

##### 0.9.5.0.4.1 (a) Provide a View Full Roadmap action

##### 0.9.5.0.4.2 (b) Display the complete hierarchy

##### 0.9.5.0.4.3 (c) Display descriptions and requirements

##### 0.9.5.0.4.4 (d) Display Work Steps and nested Work Steps

##### 0.9.5.0.4.5 (e) Allow the user to return to contextual preview

#### 0.9.5.0.5 Provide Preview Formats

Allow users to inspect both the readable roadmap and the Markdown GitMap will save.

**End Goal:**
- Make the roadmap understandable while still allowing the generated Markdown to be inspected.

##### 0.9.5.0.5.1 (a) Provide a rendered roadmap preview

##### 0.9.5.0.5.2 (b) Provide a Markdown preview

##### 0.9.5.0.5.3 (c) Use GitMap's roadmap Markdown renderer for Markdown preview

##### 0.9.5.0.5.4 (d) Keep rendered and Markdown previews synchronized


## 0.9.6 Validation and Feedback

Make roadmap problems visible while the user is working.

#### 0.9.6.0.1 Validate During Editing

Run appropriate validation as roadmap content changes.

**End Goal:**
- Identify problems before the user reaches save or synchronization.

##### 0.9.6.0.1.1 (a) Detect missing required values

##### 0.9.6.0.1.2 (b) Detect duplicate numbers

##### 0.9.6.0.1.3 (c) Detect malformed hierarchy

##### 0.9.6.0.1.4 (d) Detect invalid parent relationships

##### 0.9.6.0.1.5 (e) Reuse the core GitMap validator

#### 0.9.6.0.2 Display Validation Status

Show whether the current roadmap is valid.

**End Goal:**
- Make roadmap health visible without requiring a separate validation command.

##### 0.9.6.0.2.1 (a) Display a valid roadmap status

##### 0.9.6.0.2.2 (b) Display a warning or error status when problems exist

##### 0.9.6.0.2.3 (c) Display the number of validation problems

##### 0.9.6.0.2.4 (d) Avoid interrupting normal typing for non-critical validation feedback

#### 0.9.6.0.3 Navigate Validation Problems

Allow validation errors to be used as navigation.

**End Goal:**
- Make detected roadmap problems quick to locate and repair.

##### 0.9.6.0.3.1 (a) Display a list of validation problems

##### 0.9.6.0.3.2 (b) Identify the affected roadmap item

##### 0.9.6.0.3.3 (c) Select a validation problem to navigate to the affected item

##### 0.9.6.0.3.4 (d) Open the affected item in the editor

##### 0.9.6.0.3.5 (e) Revalidate after the problem is corrected


## 0.9.7 Roadmap File Operations

Allow roadmaps to be safely opened and saved from the GUI.

#### 0.9.7.0.1 Save Roadmap

Save changes to the roadmap file.

**End Goal:**
- Produce valid GitMap Markdown from the graphical editor.

##### 0.9.7.0.1.1 (a) Render the current roadmap as GitMap Markdown

##### 0.9.7.0.1.2 (b) Save to `roadmap.md`

##### 0.9.7.0.1.3 (c) Preserve the complete hierarchy

##### 0.9.7.0.1.4 (d) Preserve descriptions and requirements

##### 0.9.7.0.1.5 (e) Preserve Work Steps and nested Work Steps

##### 0.9.7.0.1.6 (f) Confirm successful saving

#### 0.9.7.0.2 Save Roadmap As

Allow the roadmap to be saved to another location when appropriate.

**End Goal:**
- Give the user control over where a roadmap is stored.

##### 0.9.7.0.2.1 (a) Provide Save As

##### 0.9.7.0.2.2 (b) Allow a destination to be selected

##### 0.9.7.0.2.3 (c) Use an appropriate default filename

##### 0.9.7.0.2.4 (d) Update the active roadmap path after Save As

#### 0.9.7.0.3 Protect Existing Files

Avoid accidentally destroying valid roadmap data.

**End Goal:**
- Make roadmap file operations safe and predictable.

##### 0.9.7.0.3.1 (a) Validate before saving when appropriate

##### 0.9.7.0.3.2 (b) Report file-writing failures

##### 0.9.7.0.3.3 (c) Avoid replacing a valid roadmap with incomplete output after a failed save

##### 0.9.7.0.3.4 (d) Preserve unsaved GUI state when saving fails


## 0.9.8 GitHub Repository Integration

Allow GitHub repository setup to be performed from the graphical workflow.

#### 0.9.8.0.1 Display Repository Status

Show the GitHub repository associated with the current roadmap.

**End Goal:**
- Make it immediately clear whether and where the roadmap is connected.

##### 0.9.8.0.1.1 (a) Display when no repository is connected

##### 0.9.8.0.1.2 (b) Display the connected repository when available

##### 0.9.8.0.1.3 (c) Display repository access status

##### 0.9.8.0.1.4 (d) Provide access to repository setup

#### 0.9.8.0.2 Connect Existing Repository

Allow an existing GitHub repository to be selected.

**End Goal:**
- Connect the current roadmap to an existing repository without leaving the GUI.

##### 0.9.8.0.2.1 (a) Enter or select a GitHub repository

##### 0.9.8.0.2.2 (b) Verify repository access

##### 0.9.8.0.2.3 (c) Report authentication or access problems

##### 0.9.8.0.2.4 (d) Store non-sensitive repository configuration

##### 0.9.8.0.2.5 (e) Update repository status after connection

#### 0.9.8.0.3 Create GitHub Repository

Expose GitMap's repository-creation workflow through the GUI.

**End Goal:**
- Allow a new GitHub project to be created directly from the roadmap workspace.

##### 0.9.8.0.3.1 (a) Enter a repository name

##### 0.9.8.0.3.2 (b) Enter a repository description

##### 0.9.8.0.3.3 (c) Choose public or private visibility

##### 0.9.8.0.3.4 (d) Validate repository settings before creation

##### 0.9.8.0.3.5 (e) Require confirmation before creating the repository

##### 0.9.8.0.3.6 (f) Create the repository through GitMap's GitHub integration

##### 0.9.8.0.3.7 (g) Connect the roadmap to the newly created repository

##### 0.9.8.0.3.8 (h) Report successful repository creation


## 0.9.9 GitHub Synchronization

Provide the existing GitMap synchronization workflow through the GUI.

#### 0.9.9.0.1 Prepare Synchronization

Verify that the roadmap is ready to synchronize.

**End Goal:**
- Prevent synchronization when required roadmap or repository conditions are not satisfied.

##### 0.9.9.0.1.1 (a) Validate the roadmap

##### 0.9.9.0.1.2 (b) Verify repository configuration

##### 0.9.9.0.1.3 (c) Verify repository access

##### 0.9.9.0.1.4 (d) Report anything preventing synchronization

#### 0.9.9.0.2 Preview GitHub Changes

Show what GitMap intends to change before synchronization.

**End Goal:**
- Preserve GitMap's safe preview-before-sync workflow in the graphical interface.

##### 0.9.9.0.2.1 (a) Display newly added items

##### 0.9.9.0.2.2 (b) Display changed items

##### 0.9.9.0.2.3 (c) Display unchanged items

##### 0.9.9.0.2.4 (d) Display removed roadmap items

##### 0.9.9.0.2.5 (e) Display a summary of planned changes

##### 0.9.9.0.2.6 (f) Distinguish roadmap preview from GitHub change preview

#### 0.9.9.0.3 Review Planned Changes

Allow the synchronization preview to be inspected before proceeding.

**End Goal:**
- Make significant GitHub changes understandable before they occur.

##### 0.9.9.0.3.1 (a) Inspect added items

##### 0.9.9.0.3.2 (b) Inspect changed items

##### 0.9.9.0.3.3 (c) Inspect removed roadmap items

##### 0.9.9.0.3.4 (d) Navigate from a planned change to the corresponding roadmap item where possible

##### 0.9.9.0.3.5 (e) Return to roadmap editing without synchronizing

#### 0.9.9.0.4 Confirm Synchronization

Require explicit approval before changing GitHub.

**End Goal:**
- Ensure synchronization never begins merely because the user opened a preview.

##### 0.9.9.0.4.1 (a) Provide an explicit synchronization action

##### 0.9.9.0.4.2 (b) Clearly identify the target repository

##### 0.9.9.0.4.3 (c) Summarize the planned changes

##### 0.9.9.0.4.4 (d) Require confirmation before applying changes

##### 0.9.9.0.4.5 (e) Allow synchronization to be cancelled

#### 0.9.9.0.5 Display Synchronization Progress

Provide useful feedback while synchronization is running.

**End Goal:**
- Keep the user informed without exposing unnecessary implementation details.

##### 0.9.9.0.5.1 (a) Indicate that synchronization is in progress

##### 0.9.9.0.5.2 (b) Display the current synchronization operation where useful

##### 0.9.9.0.5.3 (c) Keep the interface responsive during synchronization

##### 0.9.9.0.5.4 (d) Prevent conflicting synchronization operations from starting simultaneously

#### 0.9.9.0.6 Display Synchronization Results

Show what happened after synchronization completes.

**End Goal:**
- Make the final state of the GitHub synchronization clear.

##### 0.9.9.0.6.1 (a) Report successful synchronization

##### 0.9.9.0.6.2 (b) Report the number of created items

##### 0.9.9.0.6.3 (c) Report the number of updated items

##### 0.9.9.0.6.4 (d) Report unchanged items where useful

##### 0.9.9.0.6.5 (e) Report failures clearly

##### 0.9.9.0.6.6 (f) Preserve useful error information for troubleshooting


## 0.9.10 GUI Usability

Make the graphical interface practical for regular use rather than only functionally complete.

#### 0.9.10.0.1 Add Keyboard Navigation

Support efficient keyboard use throughout the roadmap workspace.

**End Goal:**
- Allow common GitMap operations without requiring constant mouse use.

##### 0.9.10.0.1.1 (a) Support normal keyboard traversal between controls

##### 0.9.10.0.1.2 (b) Provide a shortcut for saving

##### 0.9.10.0.1.3 (c) Provide a shortcut for Go To

##### 0.9.10.0.1.4 (d) Provide a shortcut for finding roadmap items

##### 0.9.10.0.1.5 (e) Avoid shortcuts that interfere with normal text editing

#### 0.9.10.0.2 Preserve Editing Focus

Avoid unnecessary disruption while the user is entering roadmap content.

**End Goal:**
- Keep live updates and validation from making editing frustrating.

##### 0.9.10.0.2.1 (a) Keep keyboard focus in the active editor while preview updates

##### 0.9.10.0.2.2 (b) Avoid moving the cursor while content is being edited

##### 0.9.10.0.2.3 (c) Avoid unnecessary dialogs during normal editing

##### 0.9.10.0.2.4 (d) Reserve blocking dialogs for destructive or significant operations

#### 0.9.10.0.3 Handle Large Roadmaps

Keep the interface practical as roadmap size increases.

**End Goal:**
- Allow GitMap roadmaps with many milestones and issues to remain manageable.

##### 0.9.10.0.3.1 (a) Avoid rendering the entire roadmap during every edit

##### 0.9.10.0.3.2 (b) Keep tree navigation responsive

##### 0.9.10.0.3.3 (c) Keep Go To search responsive

##### 0.9.10.0.3.4 (d) Keep contextual preview updates responsive

##### 0.9.10.0.3.5 (e) Avoid losing the user's current location during refreshes

#### 0.9.10.0.4 Add Clear User Feedback

Provide useful confirmation for important operations.

**End Goal:**
- Make it clear what GitMap has done without filling the interface with unnecessary messages.

##### 0.9.10.0.4.1 (a) Confirm successful saves

##### 0.9.10.0.4.2 (b) Confirm repository connection

##### 0.9.10.0.4.3 (c) Confirm repository creation

##### 0.9.10.0.4.4 (d) Confirm completed synchronization

##### 0.9.10.0.4.5 (e) Clearly report failed operations

##### 0.9.10.0.4.6 (f) Keep routine feedback unobtrusive


## 0.9.11 GUI Testing

Protect the graphical workflow from regressions.

#### 0.9.11.0.1 Test GUI Roadmap Operations

Test roadmap operations invoked through the graphical interface.

**End Goal:**
- Verify that GUI operations produce the same valid roadmap structures as the core GitMap workflow.

##### 0.9.11.0.1.1 (a) Test opening a roadmap

##### 0.9.11.0.1.2 (b) Test selecting roadmap items

##### 0.9.11.0.1.3 (c) Test editing roadmap items

##### 0.9.11.0.1.4 (d) Test adding roadmap items

##### 0.9.11.0.1.5 (e) Test inserting roadmap items

##### 0.9.11.0.1.6 (f) Test removing roadmap items

##### 0.9.11.0.1.7 (g) Test nested Work Steps

#### 0.9.11.0.2 Test GUI Numbering

Test numbering behavior exposed through the graphical interface.

**End Goal:**
- Verify that graphical numbering controls use the same numbering rules as the core roadmap workflow.

##### 0.9.11.0.2.1 (a) Test automatic numbering

##### 0.9.11.0.2.2 (b) Test manual numbering

##### 0.9.11.0.2.3 (c) Test numbering conflicts

##### 0.9.11.0.2.4 (d) Test renumber previews

##### 0.9.11.0.2.5 (e) Test cancellation before renumbering

#### 0.9.11.0.3 Test Live Preview

Verify that roadmap preview remains synchronized with editing.

**End Goal:**
- Ensure the preview accurately represents the roadmap without changing roadmap data itself.

##### 0.9.11.0.3.1 (a) Test preview after selection changes

##### 0.9.11.0.3.2 (b) Test preview after title changes

##### 0.9.11.0.3.3 (c) Test preview after description changes

##### 0.9.11.0.3.4 (d) Test preview after hierarchy changes

##### 0.9.11.0.3.5 (e) Test preview after renumbering

#### 0.9.11.0.4 Test Navigation

Test navigation across representative large roadmaps.

**End Goal:**
- Verify that users can reliably locate and open roadmap items.

##### 0.9.11.0.4.1 (a) Test tree navigation

##### 0.9.11.0.4.2 (b) Test Go To by number

##### 0.9.11.0.4.3 (c) Test Go To by title

##### 0.9.11.0.4.4 (d) Test navigation from live preview

##### 0.9.11.0.4.5 (e) Test navigation from validation problems

#### 0.9.11.0.5 Test GUI GitHub Workflow

Test GitHub operations without depending on a user's production repository.

**End Goal:**
- Verify that the GUI correctly drives GitMap's existing GitHub workflow.

##### 0.9.11.0.5.1 (a) Test repository connection workflow

##### 0.9.11.0.5.2 (b) Test repository creation workflow

##### 0.9.11.0.5.3 (c) Test synchronization preview

##### 0.9.11.0.5.4 (d) Test synchronization confirmation

##### 0.9.11.0.5.5 (e) Test synchronization result handling

##### 0.9.11.0.5.6 (f) Mock GitHub operations where appropriate

# 0.10 Testing and Reliability

## 0.10.1 Automated Testing

Build a test suite that protects GitMap's roadmap and synchronization behavior.

#### 0.10.1.0.1 Test Roadmap Parsing

Test conversion of Markdown roadmaps into GitMap project data.

**End Goal:**
- Test conversion of Markdown roadmaps into GitMap project data.

##### 0.10.1.0.1.1 (a) Test milestones

##### 0.10.1.0.1.2 (b) Test Sections

##### 0.10.1.0.1.3 (c) Test issues

##### 0.10.1.0.1.4 (d) Test sub-issues

##### 0.10.1.0.1.5 (e) Test descriptions and requirements

#### 0.10.1.0.2 Test Roadmap Validation

Test detection of invalid roadmap structures.

**End Goal:**
- Test detection of invalid roadmap structures.

##### 0.10.1.0.2.1 (a) Test malformed hierarchy

##### 0.10.1.0.2.2 (b) Test duplicate numbering

##### 0.10.1.0.2.3 (c) Test invalid parent relationships

##### 0.10.1.0.2.4 (d) Test useful validation messages

#### 0.10.1.0.3 Test GitHub Mapping

Test conversion of roadmap data into GitHub structures.

**End Goal:**
- Test conversion of roadmap data into GitHub structures.

##### 0.10.1.0.3.1 (a) Test milestone mapping

##### 0.10.1.0.3.2 (b) Test label mapping

##### 0.10.1.0.3.3 (c) Test Section mapping

##### 0.10.1.0.3.4 (d) Test issue mapping

##### 0.10.1.0.3.5 (e) Test sub-issue relationships

#### 0.10.1.0.4 Test Duplicate Prevention

Verify that synchronization can safely run more than once.

**End Goal:**
- Verify that synchronization can safely run more than once.

##### 0.10.1.0.4.1 (a) Test existing labels

##### 0.10.1.0.4.2 (b) Test existing milestones

##### 0.10.1.0.4.3 (c) Test existing issues

##### 0.10.1.0.4.4 (d) Confirm repeated synchronization does not create duplicates

#### 0.10.1.0.5 Test Roadmap Updates

Test synchronization after a roadmap has changed.

**End Goal:**
- Test synchronization after a roadmap has changed.

##### 0.10.1.0.5.1 (a) Test newly added items

##### 0.10.1.0.5.2 (b) Test changed items

##### 0.10.1.0.5.3 (c) Test unchanged items

##### 0.10.1.0.5.4 (d) Test removed roadmap items

##### 0.10.1.0.5.5 (e) Confirm destructive changes are not automatic

## 0.10.2 Failure Protection

Prevent partial or failed synchronization from leaving a project in a confusing state.

#### 0.10.2.0.1 Handle GitHub API Failures

Handle failures while communicating with GitHub.

**End Goal:**
- Handle failures while communicating with GitHub.

##### 0.10.2.0.1.1 (a) Detect API errors

##### 0.10.2.0.1.2 (b) Report which operation failed

##### 0.10.2.0.1.3 (c) Preserve useful error details

##### 0.10.2.0.1.4 (d) Stop safely when synchronization cannot continue

#### 0.10.2.0.2 Test Dry Run Safety

Verify that dry-run mode never changes GitHub.

**End Goal:**
- Verify that dry-run mode never changes GitHub.

##### 0.10.2.0.2.1 (a) Exercise the complete synchronization path

##### 0.10.2.0.2.2 (b) Confirm no create operations occur

##### 0.10.2.0.2.3 (c) Confirm no update operations occur

##### 0.10.2.0.2.4 (d) Confirm planned changes are still reported

#### 0.10.2.0.3 Add Integration Tests

Test complete GitMap workflows using representative roadmap data.

**End Goal:**
- Test complete GitMap workflows using representative roadmap data.

##### 0.10.2.0.3.1 (a) Test roadmap creation through parsing

##### 0.10.2.0.3.2 (b) Test parsing through synchronization planning

##### 0.10.2.0.3.3 (c) Test existing-project update workflows

##### 0.10.2.0.3.4 (d) Keep tests independent of a user's real GitHub repository where possible

# 0.11 Release Preparation

## 0.11.1 Documentation

Prepare GitMap for people other than its developers to install and use.

#### 0.11.1.0.1 Complete README

Create the main user-facing GitMap documentation.

**End Goal:**
- Create the main user-facing GitMap documentation.

##### 0.11.1.0.1.1 (a) Explain what GitMap does

##### 0.11.1.0.1.2 (b) Explain the roadmap-first workflow

##### 0.11.1.0.1.3 (c) Explain installation

##### 0.11.1.0.1.4 (d) Explain basic commands

##### 0.11.1.0.1.5 (e) Provide a simple first-use example

#### 0.11.1.0.2 Create Roadmap Format Guide

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

Document how to prepare a GitHub repository for GitMap.

**End Goal:**
- Document how to prepare a GitHub repository for GitMap.

##### 0.11.1.0.3.1 (a) Explain that the user creates the repository

##### 0.11.1.0.3.2 (b) Explain authentication setup

##### 0.11.1.0.3.3 (c) Explain required repository permissions

##### 0.11.1.0.3.4 (d) Explain how GitMap connects to the repository

##### 0.11.1.0.3.5 (e) Include troubleshooting guidance

## 0.11.2 Release

Prepare the first usable GitMap release.

#### 0.11.2.0.1 Add Version Information

Provide consistent GitMap version information.

**End Goal:**
- Provide consistent GitMap version information.

##### 0.11.2.0.1.1 (a) Define the application version

##### 0.11.2.0.1.2 (b) Make the version available from the command line

##### 0.11.2.0.1.3 (c) Keep package and application versions consistent

#### 0.11.2.0.2 Run Release Test

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

Publish the first stable GitMap release.

**End Goal:**
- Publish the first stable GitMap release.

##### 0.11.2.0.3.1 (a) Complete all required tests

##### 0.11.2.0.3.2 (b) Complete user documentation

##### 0.11.2.0.3.3 (c) Confirm the roadmap-first workflow works end to end

##### 0.11.2.0.3.4 (d) Tag the release as `v1.0.0`
