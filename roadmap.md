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

#### 0.2.1.0.5 Parse Sub-Issues (DONE)

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

# 0.3 GitHub Setup

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

## 0.3.2 GitHub Project Structure

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

#### 0.3.2.0.4 Define Sub-Issue Mapping (DONE)

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

#### 0.4.1.0.5 Create Sub-Issues (DONE)

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

# 0.5 Roadmap Updates

## 0.5.1 Existing Project Import

Allow GitMap to understand what already exists in a connected GitHub repository.

#### 0.5.1.0.1 Read Existing Milestones

Retrieve existing milestones from the repository.

**End Goal:**
- Retrieve existing milestones from the repository.

##### 0.5.1.0.1.1 (a) Read open milestones

##### 0.5.1.0.1.2 (b) Recognize milestones already represented in the roadmap

##### 0.5.1.0.1.3 (c) Preserve GitHub milestone identifiers for later updates

#### 0.5.1.0.2 Read Existing Labels

Retrieve existing repository labels.

**End Goal:**
- Retrieve existing repository labels.

##### 0.5.1.0.2.1 (a) Read current labels

##### 0.5.1.0.2.2 (b) Match existing labels to roadmap labels

##### 0.5.1.0.2.3 (c) Avoid recreating labels that already exist

#### 0.5.1.0.3 Read Existing Issues

Retrieve existing GitHub issues that correspond to roadmap items.

**End Goal:**
- Retrieve existing GitHub issues that correspond to roadmap items.

##### 0.5.1.0.3.1 (a) Read existing issues

##### 0.5.1.0.3.2 (b) Match issues to roadmap items

##### 0.5.1.0.3.3 (c) Preserve GitHub issue numbers

##### 0.5.1.0.3.4 (d) Distinguish GitMap-managed items from unrelated repository issues

#### 0.5.1.0.4 Rebuild Roadmap State

Use GitHub data to reconstruct the current state of a GitMap-managed project.

**End Goal:**
- Use GitHub data to reconstruct the current state of a GitMap-managed project.

##### 0.5.1.0.4.1 (a) Associate existing issues with milestones

##### 0.5.1.0.4.2 (b) Restore Section and issue relationships

##### 0.5.1.0.4.3 (c) Restore sub-issue relationships when available

##### 0.5.1.0.4.4 (d) Identify roadmap items that cannot be matched safely

## 0.5.2 Roadmap Changes

Allow a user to modify the roadmap after the initial synchronization and safely apply those changes to GitHub.

#### 0.5.2.0.1 Detect Roadmap Changes

Compare the local roadmap with the current GitHub project.

**End Goal:**
- Compare the local roadmap with the current GitHub project.

##### 0.5.2.0.1.1 (a) Detect new roadmap items

##### 0.5.2.0.1.2 (b) Detect changed roadmap items

##### 0.5.2.0.1.3 (c) Detect items that already match GitHub

##### 0.5.2.0.1.4 (d) Present differences before synchronization

#### 0.5.2.0.2 Update Existing Items

Update GitHub items when their corresponding roadmap entries change.

**End Goal:**
- Update GitHub items when their corresponding roadmap entries change.

##### 0.5.2.0.2.1 (a) Update titles when changed

##### 0.5.2.0.2.2 (b) Update descriptions when changed

##### 0.5.2.0.2.3 (c) Update requirements when changed

##### 0.5.2.0.2.4 (d) Preserve GitHub issue numbers

##### 0.5.2.0.2.5 (e) Avoid recreating existing items

#### 0.5.2.0.3 Handle Removed Roadmap Items

Safely identify items that exist in GitHub but have been removed from the roadmap.

**End Goal:**
- Safely identify items that exist in GitHub but have been removed from the roadmap.

##### 0.5.2.0.3.1 (a) Never delete GitHub items automatically

##### 0.5.2.0.3.2 (b) Report removed roadmap items

##### 0.5.2.0.3.3 (c) Require an explicit user decision before destructive changes

##### 0.5.2.0.3.4 (d) Preserve historical GitHub data by default

#### 0.5.2.0.4 Preview Updates

Show the user exactly what an update synchronization will do.

**End Goal:**
- Show the user exactly what an update synchronization will do.

##### 0.5.2.0.4.1 (a) Show new items

##### 0.5.2.0.4.2 (b) Show changed items

##### 0.5.2.0.4.3 (c) Show unchanged items

##### 0.5.2.0.4.4 (d) Show roadmap items that were removed

##### 0.5.2.0.4.5 (e) Require confirmation before applying changes

# 0.6 User Workflow

## 0.6.1 Interactive Roadmap Builder

Guide users through creating a roadmap without requiring them to know GitMap's Markdown format.

#### 0.6.1.0.1 Start New Roadmap

Begin an interactive roadmap-building session.

**End Goal:**
- Begin an interactive roadmap-building session.

##### 0.6.1.0.1.1 (a) Ask for the project name

##### 0.6.1.0.1.2 (b) Ask for a project overview

##### 0.6.1.0.1.3 (c) Create the initial roadmap structure

##### 0.6.1.0.1.4 (d) Do not require GitHub information yet

#### 0.6.1.0.2 Collect Milestones

Guide the user through defining project milestones.

**End Goal:**
- Guide the user through defining project milestones.

##### 0.6.1.0.2.1 (a) Ask for the milestone number

##### 0.6.1.0.2.2 (b) Ask for the milestone title

##### 0.6.1.0.2.3 (c) Allow multiple milestones

##### 0.6.1.0.2.4 (d) Allow the user to indicate when they are finished

#### 0.6.1.0.3 Collect Sections

Guide the user through defining Sections within each milestone.

**End Goal:**
- Guide the user through defining Sections within each milestone.

##### 0.6.1.0.3.1 (a) Ask for the Section title

##### 0.6.1.0.3.2 (b) Ask for a Section overview

##### 0.6.1.0.3.3 (c) Associate the Section with its milestone

##### 0.6.1.0.3.4 (d) Allow multiple Sections

#### 0.6.1.0.4 Collect Issues

Guide the user through defining issues within a Section.

**End Goal:**
- Guide the user through defining issues within a Section.

##### 0.6.1.0.4.1 (a) Ask for the issue title

##### 0.6.1.0.4.2 (b) Ask for the issue description

##### 0.6.1.0.4.3 (c) Ask for requirements

##### 0.6.1.0.4.4 (d) Allow requirements to be entered individually

##### 0.6.1.0.4.5 (e) Treat a blank entry as finished

#### 0.6.1.0.5 Collect Sub-Issues

Allow an issue to contain smaller sub-issues.

**End Goal:**
- Allow an issue to contain smaller sub-issues.

##### 0.6.1.0.5.1 (a) Ask whether an issue needs sub-issues

##### 0.6.1.0.5.2 (b) Collect sub-issue titles

##### 0.6.1.0.5.3 (c) Collect descriptions and requirements

##### 0.6.1.0.5.4 (d) Preserve the parent-child relationship

##### 0.6.1.0.5.5 (e) Support additional nesting when appropriate

#### 0.6.1.0.6 Support Pasted Content

Allow users to paste existing project information instead of answering every question individually.

**End Goal:**
- Allow users to paste existing project information instead of answering every question individually.

##### 0.6.1.0.6.1 (a) Accept pasted overview text

##### 0.6.1.0.6.2 (b) Accept pasted descriptions

##### 0.6.1.0.6.3 (c) Accept pasted requirements

##### 0.6.1.0.6.4 (d) Preserve multiline content

##### 0.6.1.0.6.5 (e) Allow interactive questions and pasted content to be mixed

## 0.6.2 Roadmap Review

Let the user review and revise the roadmap before connecting it to GitHub.

#### 0.6.2.0.1 Display Completed Roadmap

Show the complete generated roadmap.

**End Goal:**
- Show the complete generated roadmap.

##### 0.6.2.0.1.1 (a) Preserve Markdown hierarchy

##### 0.6.2.0.1.2 (b) Make milestone, Section, issue, and sub-issue relationships clear

##### 0.6.2.0.1.3 (c) Show descriptions and requirements

#### 0.6.2.0.2 Edit Roadmap Before Sync

Allow changes before GitHub synchronization begins.

**End Goal:**
- Allow changes before GitHub synchronization begins.

##### 0.6.2.0.2.1 (a) Allow items to be renamed

##### 0.6.2.0.2.2 (b) Allow descriptions and requirements to be changed

##### 0.6.2.0.2.3 (c) Allow items to be added

##### 0.6.2.0.2.4 (d) Allow items to be removed

##### 0.6.2.0.2.5 (e) Revalidate the roadmap after changes

#### 0.6.2.0.3 Save Roadmap

Save the completed roadmap to `roadmap.md`.

**End Goal:**
- Save the completed roadmap to `roadmap.md`.

##### 0.6.2.0.3.1 (a) Produce valid GitMap Markdown

##### 0.6.2.0.3.2 (b) Preserve the complete hierarchy

##### 0.6.2.0.3.3 (c) Confirm where the roadmap was saved

# 0.7 Command-Line Experience

## 0.7.1 GitMap Commands

Provide a simple command-line interface for the complete GitMap workflow.

#### 0.7.1.0.1 Create Main GitMap Command

Create the primary command used to launch GitMap.

**End Goal:**
- Create the primary command used to launch GitMap.

##### 0.7.1.0.1.1 (a) Provide a `gitmap` command

##### 0.7.1.0.1.2 (b) Display useful help

##### 0.7.1.0.1.3 (c) Display the installed version

##### 0.7.1.0.1.4 (d) Exit cleanly when requested

#### 0.7.1.0.2 Create Roadmap Command

Provide a command for creating or working with a roadmap.

**End Goal:**
- Provide a command for creating or working with a roadmap.

##### 0.7.1.0.2.1 (a) Start the interactive roadmap builder

##### 0.7.1.0.2.2 (b) Allow an existing roadmap to be opened

##### 0.7.1.0.2.3 (c) Validate the roadmap before completing

##### 0.7.1.0.2.4 (d) Save changes to `roadmap.md`

#### 0.7.1.0.3 Create Preview Command

Provide a command for previewing how GitMap interprets a roadmap.

**End Goal:**
- Provide a command for previewing how GitMap interprets a roadmap.

##### 0.7.1.0.3.1 (a) Parse the selected roadmap

##### 0.7.1.0.3.2 (b) Display its hierarchy

##### 0.7.1.0.3.3 (c) Report validation problems

##### 0.7.1.0.3.4 (d) Make no GitHub changes

#### 0.7.1.0.4 Create Setup Command

Guide the user through connecting a roadmap to a GitHub repository.

**End Goal:**
- Guide the user through connecting a roadmap to a GitHub repository.

##### 0.7.1.0.4.1 (a) Ask for the GitHub username

##### 0.7.1.0.4.2 (b) Ask for the repository name

##### 0.7.1.0.4.3 (c) Configure authentication

##### 0.7.1.0.4.4 (d) Verify repository access

##### 0.7.1.0.4.5 (e) Save non-sensitive repository configuration

#### 0.7.1.0.5 Create Sync Command

Provide a command for synchronizing the roadmap with GitHub.

**End Goal:**
- Provide a command for synchronizing the roadmap with GitHub.

##### 0.7.1.0.5.1 (a) Validate before synchronization

##### 0.7.1.0.5.2 (b) Verify repository access

##### 0.7.1.0.5.3 (c) Support dry-run mode

##### 0.7.1.0.5.4 (d) Display planned changes

##### 0.7.1.0.5.5 (e) Display a synchronization summary

## 0.7.2 Errors and Guidance

Make GitMap understandable when something goes wrong.

#### 0.7.2.0.1 Add User-Friendly Errors

Replace technical failures with useful messages when possible.

**End Goal:**
- Replace technical failures with useful messages when possible.

##### 0.7.2.0.1.1 (a) Explain missing roadmap files

##### 0.7.2.0.1.2 (b) Explain malformed roadmaps

##### 0.7.2.0.1.3 (c) Explain authentication failures

##### 0.7.2.0.1.4 (d) Explain repository access failures

##### 0.7.2.0.1.5 (e) Avoid unnecessary Python tracebacks during normal use

#### 0.7.2.0.2 Add Next-Step Guidance

Tell users what they can do after each major operation.

**End Goal:**
- Tell users what they can do after each major operation.

##### 0.7.2.0.2.1 (a) Provide guidance after roadmap creation

##### 0.7.2.0.2.2 (b) Provide guidance after repository setup

##### 0.7.2.0.2.3 (c) Provide guidance after preview

##### 0.7.2.0.2.4 (d) Provide guidance after synchronization

# 0.8 Testing and Reliability

## 0.8.1 Automated Testing

Build a test suite that protects GitMap's roadmap and synchronization behavior.

#### 0.8.1.0.1 Test Roadmap Parsing

Test conversion of Markdown roadmaps into GitMap project data.

**End Goal:**
- Test conversion of Markdown roadmaps into GitMap project data.

##### 0.8.1.0.1.1 (a) Test milestones

##### 0.8.1.0.1.2 (b) Test Sections

##### 0.8.1.0.1.3 (c) Test issues

##### 0.8.1.0.1.4 (d) Test sub-issues

##### 0.8.1.0.1.5 (e) Test descriptions and requirements

#### 0.8.1.0.2 Test Roadmap Validation

Test detection of invalid roadmap structures.

**End Goal:**
- Test detection of invalid roadmap structures.

##### 0.8.1.0.2.1 (a) Test malformed hierarchy

##### 0.8.1.0.2.2 (b) Test duplicate numbering

##### 0.8.1.0.2.3 (c) Test invalid parent relationships

##### 0.8.1.0.2.4 (d) Test useful validation messages

#### 0.8.1.0.3 Test GitHub Mapping

Test conversion of roadmap data into GitHub structures.

**End Goal:**
- Test conversion of roadmap data into GitHub structures.

##### 0.8.1.0.3.1 (a) Test milestone mapping

##### 0.8.1.0.3.2 (b) Test label mapping

##### 0.8.1.0.3.3 (c) Test Section mapping

##### 0.8.1.0.3.4 (d) Test issue mapping

##### 0.8.1.0.3.5 (e) Test sub-issue relationships

#### 0.8.1.0.4 Test Duplicate Prevention

Verify that synchronization can safely run more than once.

**End Goal:**
- Verify that synchronization can safely run more than once.

##### 0.8.1.0.4.1 (a) Test existing labels

##### 0.8.1.0.4.2 (b) Test existing milestones

##### 0.8.1.0.4.3 (c) Test existing issues

##### 0.8.1.0.4.4 (d) Confirm repeated synchronization does not create duplicates

#### 0.8.1.0.5 Test Roadmap Updates

Test synchronization after a roadmap has changed.

**End Goal:**
- Test synchronization after a roadmap has changed.

##### 0.8.1.0.5.1 (a) Test newly added items

##### 0.8.1.0.5.2 (b) Test changed items

##### 0.8.1.0.5.3 (c) Test unchanged items

##### 0.8.1.0.5.4 (d) Test removed roadmap items

##### 0.8.1.0.5.5 (e) Confirm destructive changes are not automatic

## 0.8.2 Failure Protection

Prevent partial or failed synchronization from leaving a project in a confusing state.

#### 0.8.2.0.1 Handle GitHub API Failures

Handle failures while communicating with GitHub.

**End Goal:**
- Handle failures while communicating with GitHub.

##### 0.8.2.0.1.1 (a) Detect API errors

##### 0.8.2.0.1.2 (b) Report which operation failed

##### 0.8.2.0.1.3 (c) Preserve useful error details

##### 0.8.2.0.1.4 (d) Stop safely when synchronization cannot continue

#### 0.8.2.0.2 Test Dry Run Safety

Verify that dry-run mode never changes GitHub.

**End Goal:**
- Verify that dry-run mode never changes GitHub.

##### 0.8.2.0.2.1 (a) Exercise the complete synchronization path

##### 0.8.2.0.2.2 (b) Confirm no create operations occur

##### 0.8.2.0.2.3 (c) Confirm no update operations occur

##### 0.8.2.0.2.4 (d) Confirm planned changes are still reported

#### 0.8.2.0.3 Add Integration Tests

Test complete GitMap workflows using representative roadmap data.

**End Goal:**
- Test complete GitMap workflows using representative roadmap data.

##### 0.8.2.0.3.1 (a) Test roadmap creation through parsing

##### 0.8.2.0.3.2 (b) Test parsing through synchronization planning

##### 0.8.2.0.3.3 (c) Test existing-project update workflows

##### 0.8.2.0.3.4 (d) Keep tests independent of a user's real GitHub repository where possible

# 0.9 Release Preparation

## 0.9.1 Documentation

Prepare GitMap for people other than its developers to install and use.

#### 0.9.1.0.1 Complete README

Create the main user-facing GitMap documentation.

**End Goal:**
- Create the main user-facing GitMap documentation.

##### 0.9.1.0.1.1 (a) Explain what GitMap does

##### 0.9.1.0.1.2 (b) Explain the roadmap-first workflow

##### 0.9.1.0.1.3 (c) Explain installation

##### 0.9.1.0.1.4 (d) Explain basic commands

##### 0.9.1.0.1.5 (e) Provide a simple first-use example

#### 0.9.1.0.2 Create Roadmap Format Guide

Create detailed documentation for writing GitMap roadmaps manually.

**End Goal:**
- Create detailed documentation for writing GitMap roadmaps manually.

##### 0.9.1.0.2.1 (a) Explain milestones

##### 0.9.1.0.2.2 (b) Explain Sections

##### 0.9.1.0.2.3 (c) Explain issues

##### 0.9.1.0.2.4 (d) Explain sub-issues

##### 0.9.1.0.2.5 (e) Explain descriptions and requirements

##### 0.9.1.0.2.6 (f) Provide complete examples

#### 0.9.1.0.3 Create GitHub Setup Guide

Document how to prepare a GitHub repository for GitMap.

**End Goal:**
- Document how to prepare a GitHub repository for GitMap.

##### 0.9.1.0.3.1 (a) Explain that the user creates the repository

##### 0.9.1.0.3.2 (b) Explain authentication setup

##### 0.9.1.0.3.3 (c) Explain required repository permissions

##### 0.9.1.0.3.4 (d) Explain how GitMap connects to the repository

##### 0.9.1.0.3.5 (e) Include troubleshooting guidance

## 0.9.2 Release

Prepare the first usable GitMap release.

#### 0.9.2.0.1 Add Version Information

Provide consistent GitMap version information.

**End Goal:**
- Provide consistent GitMap version information.

##### 0.9.2.0.1.1 (a) Define the application version

##### 0.9.2.0.1.2 (b) Make the version available from the command line

##### 0.9.2.0.1.3 (c) Keep package and application versions consistent

#### 0.9.2.0.2 Run Release Test

Test GitMap from a clean environment before release.

**End Goal:**
- Test GitMap from a clean environment before release.

##### 0.9.2.0.2.1 (a) Install GitMap from scratch

##### 0.9.2.0.2.2 (b) Create a new roadmap

##### 0.9.2.0.2.3 (c) Connect to a test repository

##### 0.9.2.0.2.4 (d) Preview synchronization

##### 0.9.2.0.2.5 (e) Perform synchronization

##### 0.9.2.0.2.6 (f) Run synchronization again to verify duplicate prevention

#### 0.9.2.0.3 Create Version 1.0 Release

Publish the first stable GitMap release.

**End Goal:**
- Publish the first stable GitMap release.

##### 0.9.2.0.3.1 (a) Complete all required tests

##### 0.9.2.0.3.2 (b) Complete user documentation

##### 0.9.2.0.3.3 (c) Confirm the roadmap-first workflow works end to end

##### 0.9.2.0.3.4 (d) Tag the release as `v1.0.0`
