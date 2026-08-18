Title: GitMap Roadmap

Sub-Title: GitMap turns a project roadmap into a structured GitHub project.

# 0.1 Foundations (DONE)

## 0.1.1 Project Setup (DONE)

Set up the basic GitMap project so it can be installed, run, tested, and developed safely.

#### 0.1.1.0.1 Create Python Project (DONE)

Create the basic Python project structure for GitMap.

**Requirements:**
- Create the `gitmap` package.
- Create `../pyproject.toml`.
- Create a `tests` directory.
- Create a `../.gitignore`.
-
#### 0.1.1.0.2 Install Dependencies (DONE)

Set up the dependencies needed to develop and test GitMap.

**Requirements:**
- Support editable installation.
- Add `pytest` as a development dependency.
- Confirm the development environment installs successfully.
#### 0.1.1.0.3 Create Command-Line Entry Point (DONE)

Create the basic command-line entry point for GitMap.

**Requirements:**
- Allow GitMap to be started from the command line.
- Display a simple welcome message.
- Exit cleanly.

#### 0.1.1.0.4 Add Initial Tests (DONE)

Create the first automated tests for GitMap.

**Requirements:**
- Confirm GitMap can be imported.
- Confirm the command-line entry point runs.
- Confirm the test suite can be run with `pytest`.

#### 0.1.1.0.5 Add Project Documentation (DONE)

Create the basic documentation needed to understand and develop GitMap.

**Requirements:**
- Explain what GitMap does.
- Explain how to install GitMap for development.
- Explain how to run GitMap.
- Explain how to run the tests.

## 0.1.2 Roadmap Format (DONE)

Define the Markdown structure GitMap will use to describe projects before they are synchronized with GitHub.

#### 0.1.2.0.1 Define Roadmap Structure (DONE)

Define the hierarchy used in a GitMap roadmap.

**Requirements:**
- Support milestones.
- Support Sections.
- Support issues.
- Support sub-issues.
- Support descriptions and requirements.
- Use Markdown headings to represent hierarchy.

#### 0.1.2.0.2 Create Example Roadmap (DONE)

Create a complete example roadmap that can be used for development and testing.

**Requirements:**
- Include at least one milestone.
- Include at least one Section.
- Include multiple issues.
- Include at least one sub-issue.
- Include descriptions and requirements.

#### 0.1.2.0.3 Document Roadmap Format (DONE)

Document how users should write a GitMap roadmap.

**Requirements:**
- Explain each heading level.
- Show how milestones, Sections, issues, and sub-issues are represented.
- Provide a copyable example.

# 0.2 Roadmap Parser (DONE)

## 0.2.1 Markdown Parsing (DONE)

Teach GitMap to read a roadmap and turn its Markdown structure into project data.

#### 0.2.1.0.1 Read Roadmap File (DONE)

Load a roadmap from a Markdown file.

**Requirements:**
- Accept a roadmap file path.
- Read the Markdown contents.
- Report a clear error if the file cannot be read.

#### 0.2.1.0.2 Parse Milestones (DONE)

Identify milestone headings in the roadmap.

**Requirements:**
- Recognize milestone headings.
- Capture the milestone number and title.
- Preserve the order of milestones.

#### 0.2.1.0.3 Parse Sections (DONE)

Identify Sections within each milestone.

**Requirements:**
- Associate each Section with its milestone.
- Capture the Section title.
- Capture the Section description.
- Recognize the Section type marker.

#### 0.2.1.0.4 Parse Issues (DONE)

Identify issues within each Section.

**Requirements:**
- Associate each issue with its Section.
- Capture the issue number and title.
- Capture the issue description.
- Capture requirements.

#### 0.2.1.0.5 Parse Work Steps (DONE)

Support issues nested beneath other issues.

**Requirements:**
- Associate each sub-issue with its parent issue.
- Preserve the roadmap hierarchy.
- Support numbering such as `0.2.4.1`.

## 0.2.2 Roadmap Validation (DONE)

Detect roadmap problems before anything is sent to GitHub.

#### 0.2.2.0.1 Validate Roadmap Structure (DONE)

Check that the roadmap follows GitMap's expected hierarchy.

**Requirements:**
- Detect issues outside a Section.
- Detect Sections outside a milestone.
- Detect malformed hierarchy.
- Provide useful error messages.

#### 0.2.2.0.2 Validate Numbering (DONE)

Check roadmap numbering for obvious errors.

**Requirements:**
- Detect duplicate numbers.
- Detect invalid parent relationships.
- Identify the location of the problem.

#### 0.2.2.0.3 Preview Parsed Roadmap (DONE)

Allow users to see what GitMap understood before synchronization.

**Requirements:**
- Display milestones.
- Display Sections.
- Display issues and sub-issues.
- Preserve hierarchy in the preview.

# 0.3 GitHub Setup

## 0.3.1 Repository Connection (DONE)

Connect a completed GitMap roadmap to a GitHub repository chosen by the user.

#### 0.3.1.0.1 Collect Repository Information (DONE)
[ ] (a) First example sub-issue
[ ] (b) Second example sub-issue

Ask the user which GitHub repository should receive the roadmap.

**Requirements:**
- Ask for the GitHub username.
- Ask for the repository name.
- Do not create the repository automatically.
- Allow roadmap creation to be completed before GitHub setup begins.

#### 0.3.1.0.2 Configure GitHub Authentication (DONE)

Set up authentication required to work with the selected repository.

**Requirements:**
- Keep credentials outside source control.
- Provide clear setup instructions.
- Detect missing authentication.
- Never store authentication tokens in the roadmap.

#### 0.3.1.0.3 Verify Repository (DONE)

Confirm that GitMap can access the repository before synchronization.

**Requirements:**
- Verify that the repository exists.
- Verify that authentication works.
- Verify that the user has appropriate access.
- Stop synchronization if verification fails.

## 0.3.2 GitHub Project Structure

Translate GitMap's roadmap concepts into the GitHub structures needed for synchronization.

#### 0.3.2.0.1 Define Milestone Mapping

Define how roadmap milestones map to GitHub milestones.

**Requirements:**
- Preserve milestone titles.
- Avoid creating duplicate milestones.
- Allow existing milestones to be recognized.

#### 0.3.2.0.2 Define Label Mapping

Define the labels GitMap uses when creating GitHub items.

**Requirements:**
- Support labels for Sections.
- Support labels for issues when defined by the roadmap.
- Avoid creating duplicate labels.
- Allow labels to be created before issues are synchronized.

#### 0.3.2.0.3 Define Issue Mapping

Define how roadmap items become GitHub issues.

**Requirements:**
- Preserve issue titles.
- Preserve descriptions.
- Preserve requirements.
- Associate issues with their milestone.
- Apply appropriate labels.

#### 0.3.2.0.4 Define Work Step Mapping

Define how roadmap hierarchy is represented in GitHub.

**Requirements:**
- Preserve parent-child relationships when supported.
- Keep sub-issues associated with their parent.
- Preserve roadmap numbering.

# 0.4 GitHub Synchronization

## 0.4.1 Synchronization Engine

Synchronize the validated roadmap with the selected GitHub repository.

#### 0.4.1.0.1 Create Labels

Create the labels required by the roadmap before synchronizing other items.

**Requirements:**
- Read required labels from the parsed roadmap.
- Detect labels that already exist.
- Create only missing labels.
- Do not create duplicates.

#### 0.4.1.0.2 Create Milestones

Create roadmap milestones in GitHub.

**Requirements:**
- Detect milestones that already exist.
- Create only missing milestones.
- Preserve milestone titles.
- Do not create duplicates.

#### 0.4.1.0.3 Create Sections

Create GitHub issues representing roadmap Sections.

**Requirements:**
- Create the Section before its child issues.
- Include the Section description.
- Apply the Section label.
- Associate the Section with its milestone.
- Detect an existing matching Section before creating another.

#### 0.4.1.0.4 Create Issues

Create GitHub issues from roadmap issues.

**Requirements:**
- Preserve the issue title.
- Include the description.
- Include requirements using GitHub Markdown.
- Associate the issue with its milestone.
- Apply defined labels.
- Detect existing matching issues before creating another.

#### 0.4.1.0.5 Create Work Steps

Create roadmap sub-issues and associate them with their parent issues.

**Requirements:**
- Create the parent before its sub-issues.
- Preserve the parent-child hierarchy.
- Include descriptions and requirements.
- Associate sub-issues with the correct milestone.

## 0.4.2 Safe Synchronization

Make synchronization predictable and safe to run more than once.

#### 0.4.2.0.1 Add Dry Run

Allow users to preview what synchronization would change without changing GitHub.

**Requirements:**
- Show items that would be created.
- Show items that already exist.
- Make no GitHub changes during a dry run.
- Clearly identify dry-run output.

#### 0.4.2.0.2 Prevent Duplicate Items

Make repeated synchronization safe.

**Requirements:**
- Check GitHub before creating an item.
- Reuse existing matching items.
- Prevent duplicate labels.
- Prevent duplicate milestones.
- Prevent duplicate issues.

#### 0.4.2.0.3 Add Synchronization Summary

Display the result of synchronization.

**Requirements:**
- Report items created.
- Report items already present.
- Report skipped items.
- Report errors.
# 0.5 Roadmap Updates

## 0.5.1 Existing Project Import

Allow GitMap to understand what already exists in a connected GitHub repository.

#### 0.5.1.0.1 Read Existing Milestones

Retrieve existing milestones from the repository.

**Requirements:**
- Read open milestones.
- Recognize milestones already represented in the roadmap.
- Preserve GitHub milestone identifiers for later updates.

#### 0.5.1.0.2 Read Existing Labels

Retrieve existing repository labels.

**Requirements:**
- Read current labels.
- Match existing labels to roadmap labels.
- Avoid recreating labels that already exist.

#### 0.5.1.0.3 Read Existing Issues

Retrieve existing GitHub issues that correspond to roadmap items.

**Requirements:**
- Read existing issues.
- Match issues to roadmap items.
- Preserve GitHub issue numbers.
- Distinguish GitMap-managed items from unrelated repository issues.

#### 0.5.1.0.4 Rebuild Roadmap State

Use GitHub data to reconstruct the current state of a GitMap-managed project.

**Requirements:**
- Associate existing issues with milestones.
- Restore Section and issue relationships.
- Restore sub-issue relationships when available.
- Identify roadmap items that cannot be matched safely.

## 0.5.2 Roadmap Changes

Allow a user to modify the roadmap after the initial synchronization and safely apply those changes to GitHub.

#### 0.5.2.0.1 Detect Roadmap Changes

Compare the local roadmap with the current GitHub project.

**Requirements:**
- Detect new roadmap items.
- Detect changed roadmap items.
- Detect items that already match GitHub.
- Present differences before synchronization.

#### 0.5.2.0.2 Update Existing Items

Update GitHub items when their corresponding roadmap entries change.

**Requirements:**
- Update titles when changed.
- Update descriptions when changed.
- Update requirements when changed.
- Preserve GitHub issue numbers.
- Avoid recreating existing items.

#### 0.5.2.0.3 Handle Removed Roadmap Items

Safely identify items that exist in GitHub but have been removed from the roadmap.

**Requirements:**
- Never delete GitHub items automatically.
- Report removed roadmap items.
- Require an explicit user decision before destructive changes.
- Preserve historical GitHub data by default.

#### 0.5.2.0.4 Preview Updates

Show the user exactly what an update synchronization will do.

**Requirements:**
- Show new items.
- Show changed items.
- Show unchanged items.
- Show roadmap items that were removed.
- Require confirmation before applying changes.
# 0.6 User Workflow

## 0.6.1 Interactive Roadmap Builder

Guide users through creating a roadmap without requiring them to know GitMap's Markdown format.

#### 0.6.1.0.1 Start New Roadmap

Begin an interactive roadmap-building session.

**Requirements:**
- Ask for the project name.
- Ask for a project overview.
- Create the initial roadmap structure.
- Do not require GitHub information yet.

#### 0.6.1.0.2 Collect Milestones

Guide the user through defining project milestones.

**Requirements:**
- Ask for the milestone number.
- Ask for the milestone title.
- Allow multiple milestones.
- Allow the user to indicate when they are finished.

#### 0.6.1.0.3 Collect Sections

Guide the user through defining Sections within each milestone.

**Requirements:**
- Ask for the Section title.
- Ask for a Section overview.
- Associate the Section with its milestone.
- Allow multiple Sections.

#### 0.6.1.0.4 Collect Issues

Guide the user through defining issues within a Section.

**Requirements:**
- Ask for the issue title.
- Ask for the issue description.
- Ask for requirements.
- Allow requirements to be entered individually.
- Treat a blank entry as finished.

#### 0.6.1.0.5 Collect Work Steps

Allow an issue to contain smaller sub-issues.

**Requirements:**
- Ask whether an issue needs sub-issues.
- Collect sub-issue titles.
- Collect descriptions and requirements.
- Preserve the parent-child relationship.
- Support additional nesting when appropriate.

#### 0.6.1.0.6 Support Pasted Content

Allow users to paste existing project information instead of answering every question individually.

**Requirements:**
- Accept pasted overview text.
- Accept pasted descriptions.
- Accept pasted requirements.
- Preserve multiline content.
- Allow interactive questions and pasted content to be mixed.

## 0.6.2 Roadmap Review

Let the user review and revise the roadmap before connecting it to GitHub.

#### 0.6.2.0.1 Display Completed Roadmap

Show the complete generated roadmap.

**Requirements:**
- Preserve Markdown hierarchy.
- Make milestone, Section, issue, and sub-issue relationships clear.
- Show descriptions and requirements.

#### 0.6.2.0.2 Edit Roadmap Before Sync

Allow changes before GitHub synchronization begins.

**Requirements:**
- Allow items to be renamed.
- Allow descriptions and requirements to be changed.
- Allow items to be added.
- Allow items to be removed.
- Revalidate the roadmap after changes.

#### 0.6.2.0.3 Save Roadmap

Save the completed roadmap to `roadmap.md`.

**Requirements:**
- Produce valid GitMap Markdown.
- Preserve the complete hierarchy.
- Confirm where the roadmap was saved.

# 0.7 Command-Line Experience

## 0.7.1 GitMap Commands

Provide a simple command-line interface for the complete GitMap workflow.

#### 0.7.1.0.1 Create Main GitMap Command

Create the primary command used to launch GitMap.

**Requirements:**
- Provide a `gitmap` command.
- Display useful help.
- Display the installed version.
- Exit cleanly when requested.

#### 0.7.1.0.2 Create Roadmap Command

Provide a command for creating or working with a roadmap.

**Requirements:**
- Start the interactive roadmap builder.
- Allow an existing roadmap to be opened.
- Validate the roadmap before completing.
- Save changes to `roadmap.md`.

#### 0.7.1.0.3 Create Preview Command

Provide a command for previewing how GitMap interprets a roadmap.

**Requirements:**
- Parse the selected roadmap.
- Display its hierarchy.
- Report validation problems.
- Make no GitHub changes.

#### 0.7.1.0.4 Create Setup Command

Guide the user through connecting a roadmap to a GitHub repository.

**Requirements:**
- Ask for the GitHub username.
- Ask for the repository name.
- Configure authentication.
- Verify repository access.
- Save non-sensitive repository configuration.

#### 0.7.1.0.5 Create Sync Command

Provide a command for synchronizing the roadmap with GitHub.

**Requirements:**
- Validate before synchronization.
- Verify repository access.
- Support dry-run mode.
- Display planned changes.
- Display a synchronization summary.

## 0.7.2 Errors and Guidance

Make GitMap understandable when something goes wrong.

#### 0.7.2.0.1 Add User-Friendly Errors

Replace technical failures with useful messages when possible.

**Requirements:**
- Explain missing roadmap files.
- Explain malformed roadmaps.
- Explain authentication failures.
- Explain repository access failures.
- Avoid unnecessary Python tracebacks during normal use.

#### 0.7.2.0.2 Add Next-Step Guidance

Tell users what they can do after each major operation.

**Requirements:**
- Provide guidance after roadmap creation.
- Provide guidance after repository setup.
- Provide guidance after preview.
- Provide guidance after synchronization.

# 0.8 Testing and Reliability

## 0.8.1 Automated Testing

Build a test suite that protects GitMap's roadmap and synchronization behavior.

#### 0.8.1.0.1 Test Roadmap Parsing

Test conversion of Markdown roadmaps into GitMap project data.

**Requirements:**
- Test milestones.
- Test Sections.
- Test issues.
- Test sub-issues.
- Test descriptions and requirements.

#### 0.8.1.0.2 Test Roadmap Validation

Test detection of invalid roadmap structures.

**Requirements:**
- Test malformed hierarchy.
- Test duplicate numbering.
- Test invalid parent relationships.
- Test useful validation messages.

#### 0.8.1.0.3 Test GitHub Mapping

Test conversion of roadmap data into GitHub structures.

**Requirements:**
- Test milestone mapping.
- Test label mapping.
- Test Section mapping.
- Test issue mapping.
- Test sub-issue relationships.

#### 0.8.1.0.4 Test Duplicate Prevention

Verify that synchronization can safely run more than once.

**Requirements:**
- Test existing labels.
- Test existing milestones.
- Test existing issues.
- Confirm repeated synchronization does not create duplicates.

#### 0.8.1.0.5 Test Roadmap Updates

Test synchronization after a roadmap has changed.

**Requirements:**
- Test newly added items.
- Test changed items.
- Test unchanged items.
- Test removed roadmap items.
- Confirm destructive changes are not automatic.

## 0.8.2 Failure Protection

Prevent partial or failed synchronization from leaving a project in a confusing state.

#### 0.8.2.0.1 Handle GitHub API Failures

Handle failures while communicating with GitHub.

**Requirements:**
- Detect API errors.
- Report which operation failed.
- Preserve useful error details.
- Stop safely when synchronization cannot continue.

#### 0.8.2.0.2 Test Dry Run Safety

Verify that dry-run mode never changes GitHub.

**Requirements:**
- Exercise the complete synchronization path.
- Confirm no create operations occur.
- Confirm no update operations occur.
- Confirm planned changes are still reported.

#### 0.8.2.0.3 Add Integration Tests

Test complete GitMap workflows using representative roadmap data.

**Requirements:**
- Test roadmap creation through parsing.
- Test parsing through synchronization planning.
- Test existing-project update workflows.
- Keep tests independent of a user's real GitHub repository where possible.

# 0.9 Release Preparation

## 0.9.1 Documentation

Prepare GitMap for people other than its developers to install and use.

#### 0.9.1.0.1 Complete README

Create the main user-facing GitMap documentation.

**Requirements:**
- Explain what GitMap does.
- Explain the roadmap-first workflow.
- Explain installation.
- Explain basic commands.
- Provide a simple first-use example.

#### 0.9.1.0.2 Create Roadmap Format Guide

Create detailed documentation for writing GitMap roadmaps manually.

**Requirements:**
- Explain milestones.
- Explain Sections.
- Explain issues.
- Explain sub-issues.
- Explain descriptions and requirements.
- Provide complete examples.

#### 0.9.1.0.3 Create GitHub Setup Guide

Document how to prepare a GitHub repository for GitMap.

**Requirements:**
- Explain that the user creates the repository.
- Explain authentication setup.
- Explain required repository permissions.
- Explain how GitMap connects to the repository.
- Include troubleshooting guidance.

## 0.9.2 Release

Prepare the first usable GitMap release.

#### 0.9.2.0.1 Add Version Information

Provide consistent GitMap version information.

**Requirements:**
- Define the application version.
- Make the version available from the command line.
- Keep package and application versions consistent.

#### 0.9.2.0.2 Run Release Test

Test GitMap from a clean environment before release.

**Requirements:**
- Install GitMap from scratch.
- Create a new roadmap.
- Connect to a test repository.
- Preview synchronization.
- Perform synchronization.
- Run synchronization again to verify duplicate prevention.

#### 0.9.2.0.3 Create Version 1.0 Release

Publish the first stable GitMap release.

**Requirements:**
- Complete all required tests.
- Complete user documentation.
- Confirm the roadmap-first workflow works end to end.
- Tag the release as `v1.0.0`.
