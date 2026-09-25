Title: GitMap Roadmap

Sub-Title: GitMap turns a project roadmap into a structured GitHub project.

Hierarchy-Issue-Title-Style: type-prefix

# 0.7 Changes to make

## 0.7.1 Synchronization Workflow Improvements
<!-- GitMap-ID: zuredsie -->

#### 0.7.1.0.1 Improve Change Preview Flow (DONE)
<!-- GitMap-ID: cpredsnb -->

Avoid displaying detailed change lists before the user asks to review them.

**Requirements:**
- Present a concise synchronization summary first and allow the user to choose which details to inspect.

**Work Steps:**
- [ ] 0.7.1.0.1.1 (a) Display change counts before detailed change lists
- [ ] 0.7.1.0.1.2 (b) Do not automatically display the complete added-item list
- [ ] 0.7.1.0.1.3 (c) Allow added items to be reviewed on request
- [ ] 0.7.1.0.1.4 (d) Allow changed items to be reviewed on request
- [ ] 0.7.1.0.1.5 (e) Allow unchanged items to be reviewed on request
- [ ] 0.7.1.0.1.6 (f) Allow removed items to be reviewed on request
- [ ] 0.7.1.0.1.7 (g) Return to the synchronization prompt after reviewing a list

## 0.7.2 Synchronization Safety and Recovery
<!-- GitMap-ID: auredsid -->

#### 0.7.2.0.1 Validate Synchronization Plan
<!-- GitMap-ID: hqredsmw -->

**Requirements:**
- Do I need something?

**Work Steps:**
- [ ] 0.7.2.0.1.1 (a) Detect duplicate GitMap identifiers
- [ ] 0.7.2.0.1.2 (b) Detect duplicate milestone mappings
- [ ] 0.7.2.0.1.3 (c) Detect ambiguous identity matches
- [ ] 0.7.2.0.1.4 (d) Refuse to guess when identity cannot be determined safely
- [ ] 0.7.2.0.1.5 (e) Explain conflicts before synchronization
- [ ] 0.7.2.0.1.6 (f) Allow conflicts to be resolved before retrying

#### 0.7.2.0.2 Protect Partial Synchronization
<!-- GitMap-ID: iqredsmv -->

**Work Steps:**
- [ ] 0.7.2.0.2.1 (a) Track completed synchronization operations
- [ ] 0.7.2.0.2.2 (b) Identify the operation that failed
- [ ] 0.7.2.0.2.3 (c) Report operations completed before failure
- [ ] 0.7.2.0.2.4 (d) Report operations that remain incomplete
- [ ] 0.7.2.0.2.5 (e) Stop safely when synchronization cannot continue
- [ ] 0.7.2.0.2.6 (f) Preserve enough state for a safe retry

#### 0.7.2.0.3 Verify Synchronization Results
<!-- GitMap-ID: jqredsmu -->

**Work Steps:**
- [ ] 0.7.2.0.3.1 (a) Re-read affected GitHub items after synchronization
- [ ] 0.7.2.0.3.2 (b) Confirm expected items were created
- [ ] 0.7.2.0.3.3 (c) Confirm expected items were updated
- [ ] 0.7.2.0.3.4 (d) Confirm expected roadmap identities were preserved
- [ ] 0.7.2.0.3.5 (e) Detect unexpected duplicate identifiers
- [ ] 0.7.2.0.3.6 (f) Report differences between planned and actual results

#### 0.7.2.0.4 Support Safe Synchronization Retry
<!-- GitMap-ID: kqredsmt -->

**Work Steps:**
- [ ] 0.7.2.0.4.1 (a) Re-read GitHub state before retrying
- [ ] 0.7.2.0.4.2 (b) Recognize operations already completed
- [ ] 0.7.2.0.4.3 (c) Avoid recreating successfully created items
- [ ] 0.7.2.0.4.4 (d) Avoid reapplying unnecessary updates
- [ ] 0.7.2.0.4.5 (e) Continue remaining synchronization work safely
- [ ] 0.7.2.0.4.6 (f) Report final retry results

#### 0.7.2.0.5 Prevent Concurrent Synchronization
<!-- GitMap-ID: lqredsms -->

Prevent multiple GitMap synchronization operations from modifying the same repository at the same time.

**Requirements:**
- Prevent concurrent synchronization from creating duplicate or conflicting GitHub changes.

**Work Steps:**
- [ ] 0.7.2.0.5.1 (a) Detect when synchronization is already in progress
- [ ] 0.7.2.0.5.2 (b) Prevent a second synchronization from starting against the same repository
- [ ] 0.7.2.0.5.3 (c) Explain why the second synchronization was blocked
- [ ] 0.7.2.0.5.4 (d) Allow synchronization after the active operation completes
- [ ] 0.7.2.0.5.5 (e) Clear synchronization state after successful completion
- [ ] 0.7.2.0.5.6 (f) Clear synchronization state safely after failure
- [ ] 0.7.2.0.5.7 (g) Avoid leaving a stale synchronization lock after GitMap exits unexpectedly

## 0.7.3 Synchronization Performance
<!-- GitMap-ID: buredsic -->

#### 0.7.3.0.1 Skip Unchanged Items During Synchronization
<!-- GitMap-ID: mqredsmr -->

Avoid unnecessary GitHub operations for roadmap items that have already been determined to be unchanged.

**Requirements:**
- Reduce synchronization time by processing only items that require GitHub changes.

**Work Steps:**
- [ ] 0.7.3.0.1.1 (a) Identify unchanged items during synchronization planning
- [ ] 0.7.3.0.1.2 (b) Exclude unchanged items from synchronization operations
- [ ] 0.7.3.0.1.3 (c) Avoid unnecessary GitHub API calls for unchanged items
- [ ] 0.7.3.0.1.4 (d) Preserve unchanged items in the synchronization summary
- [ ] 0.7.3.0.1.5 (e) Count only actionable items in synchronization progress
- [ ] 0.7.3.0.1.6 (f) Report the number of unchanged items skipped

#### 0.7.3.0.2 Reuse Synchronization Plan
<!-- GitMap-ID: nqredsmq -->

Use the already-reviewed synchronization plan when applying changes.

**Requirements:**
- Avoid repeating work that was already completed while determining the synchronization preview.

**Work Steps:**
- [ ] 0.7.3.0.2.1 (a) Preserve the synchronization plan after preview
- [ ] 0.7.3.0.2.2 (b) Use the approved plan when synchronization begins
- [ ] 0.7.3.0.2.3 (c) Process only planned create and update operations
- [ ] 0.7.3.0.2.4 (d) Avoid recalculating unchanged items unnecessarily
- [ ] 0.7.3.0.2.5 (e) Ensure the applied plan matches the plan the user approved

## 0.7.4 GitHub Repository Setup
<!-- GitMap-ID: curedsib -->

#### 0.7.4.0.1 Choose Repository
<!-- GitMap-ID: sqredsml -->

Allow the user to choose where the roadmap will be synchronized.

**Requirements:**
- Connect the completed roadmap to the appropriate GitHub repository.

**Work Steps:**
- [ ] 0.7.4.0.1.1 (a) Use an existing repository
- [ ] 0.7.4.0.1.2 (b) Create a new repository

#### 0.7.4.0.2 Create Repository
<!-- GitMap-ID: tqredsmk -->

Create a GitHub repository directly from GitMap.

**Requirements:**
- Create the repository without requiring the user to leave GitMap.

**Work Steps:**
- [ ] 0.7.4.0.2.1 (a) Ask for the repository name
- [ ] 0.7.4.0.2.2 (b) Ask for a repository description
- [ ] 0.7.4.0.2.3 (c) Allow public or private visibility
- [ ] 0.7.4.0.2.4 (d) Create the repository through GitHub
- [ ] 0.7.4.0.2.5 (e) Confirm successful repository creation

#### 0.7.4.0.3 Connect Repository
<!-- GitMap-ID: uqredsmj -->

Connect the roadmap to the selected repository.

**Requirements:**
- Make the selected repository the synchronization target for the roadmap.

**Work Steps:**
- [ ] 0.7.4.0.3.1 (a) Verify repository access
- [ ] 0.7.4.0.3.2 (b) Store the repository association
- [ ] 0.7.4.0.3.3 (c) Prepare the repository for synchronization

#### 0.7.4.0.4 Initial Synchronization
<!-- GitMap-ID: vqredsmi -->

Allow the completed roadmap to proceed directly into GitMap's existing synchronization workflow.

**Requirements:**
- Move from roadmap creation to GitHub synchronization without restarting GitMap.

**Work Steps:**
- [ ] 0.7.4.0.4.1 (a) Preview the initial synchronization
- [ ] 0.7.4.0.4.2 (b) Require confirmation before synchronization
- [ ] 0.7.4.0.4.3 (c) Synchronize the roadmap to the repository
- [ ] 0.7.4.0.4.4 (d) Report synchronization results

## 0.7.5 Roadmap Numbering
<!-- GitMap-ID: duredsia -->

#### 0.7.5.0.1 Explain Roadmap Numbering
<!-- GitMap-ID: wqredsmh -->

Explain GitMap's numbering system when the user begins building a roadmap.

**Requirements:**
- Make the roadmap hierarchy and numbering rules clear before the user begins creating items.

**Work Steps:**
- [ ] 0.7.5.0.1.1 (a) Explain the milestone numbering format
- [ ] 0.7.5.0.1.2 (b) Explain how child numbers extend their parent number
- [ ] 0.7.5.0.1.3 (c) Show an example hierarchy
- [ ] 0.7.5.0.1.4 (d) Explain automatic numbering
- [ ] 0.7.5.0.1.5 (e) Explain manual numbering

#### 0.7.5.0.2 Choose Numbering Mode
<!-- GitMap-ID: mtredsjr -->

Allow the user to choose between automatic and manual numbering.

**Requirements:**
- Let users control whether GitMap assigns roadmap numbers or they enter them manually.

**Work Steps:**
- [ ] 0.7.5.0.2.1 (a) Offer automatic numbering
- [ ] 0.7.5.0.2.2 (b) Offer manual numbering
- [ ] 0.7.5.0.2.3 (c) Allow manual numbering when automatic numbering cannot be used

#### 0.7.5.0.3 Choose Starting Series
<!-- GitMap-ID: ntredsjq -->

Allow automatic numbering to reflect the project's development stage.

**Requirements:**
- Start roadmap numbering in the appropriate version series.

**Work Steps:**
- [ ] 0.7.5.0.3.1 (a) Offer pre-production numbering beginning with 0.x
- [ ] 0.7.5.0.3.2 (b) Offer production numbering beginning with 1.x

#### 0.7.5.0.4 Generate Hierarchical Numbers
<!-- GitMap-ID: otredsjp -->

Generate roadmap numbers based on the hierarchy the user actually creates.

**Requirements:**
- Automatically assign valid numbers without requiring every hierarchy level to be present.

**Work Steps:**
- [ ] 0.7.5.0.4.1 (a) Number milestones automatically
- [ ] 0.7.5.0.4.2 (b) Number Sections automatically
- [ ] 0.7.5.0.4.3 (c) Number features automatically
- [ ] 0.7.5.0.4.4 (d) Number issues automatically
- [ ] 0.7.5.0.4.5 (e) Number Work Steps automatically
- [ ] 0.7.5.0.4.6 (f) Increment sibling numbers automatically
- [ ] 0.7.5.0.4.7 (g) Support letter sequences such as (a), (b), and (c) where used

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
- [ ] 0.7.7.0.1.1 (a) Detect when Section or Feature Issues are enabled for an existing roadmap
- [ ] 0.7.7.0.1.2 (b) Determine whether the corresponding hierarchy Issues already exist
- [ ] 0.7.7.0.1.3 (c) Inform the user how many Section and Feature Issues will be created
- [ ] 0.7.7.0.1.4 (d) Ask the user whether to create the missing hierarchy Issues
- [ ] 0.7.7.0.1.5 (e) Create hierarchy Issues only after confirmation

#### 0.7.7.0.2 Require Approval Before Modifying Existing GitHub Items
<!-- GitMap-ID: kuredsit -->

Once a GitHub item already exists, GitMap must not update, close, or otherwise modify it unless the change appears in
the synchronization preview and has been approved by the user. Existing GitHub items are never modified without first
being shown to the user and explicitly approved.

**Work Steps:**
- [ ] 0.7.7.0.2.1 (a) Detect modifications to existing GitHub items
- [ ] 0.7.7.0.2.2 (b) Include all modifications in the synchronization preview
- [ ] 0.7.7.0.2.3 (c) Prevent updates that were not included in the approved synchronization plan
- [ ] 0.7.7.0.2.4 (d) Ensure updates and closures require user approval
- [ ] 0.7.7.0.2.5 (e) Verify only approved changes are applied

## 0.7.8 Finish 0.7.6
<!-- GitMap-ID: gvredshx -->

#### 0.7.8.0.1 Customize Hierarchy Issue Titles
<!-- GitMap-ID: quredsin -->

Allow users to choose how Section and Feature GitHub Issues are titled so they are easy to distinguish from normal
roadmap Issues. Users can easily distinguish hierarchy Issues from normal roadmap Issues while preserving a consistent
appearance across GitHub.

**Work Steps:**
- [ ] 0.7.8.0.1.1 (a) Add a hierarchy Issue title style option during roadmap creation.
- [ ] 0.7.8.0.1.2 (b) Store the selected title style in the roadmap.
- [ ] 0.7.8.0.1.3 (c) Update Section Issue title generation.
- [ ] 0.7.8.0.1.4 (d) Update Feature Issue title generation.
- [ ] 0.7.8.0.1.5 (e) Preserve title style during synchronization.
- [ ] 0.7.8.0.1.6 (f) Show the selected title style in synchronization preview.

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
- [ ] 0.7.10.0.1.1 (a) Use an existing repository
- [ ] 0.7.10.0.1.2 (b) Create a new repository

#### 0.7.10.0.2 Create Repository
<!-- GitMap-ID: pqredsmo -->

Create a GitHub repository directly from GitMap.

**Requirements:**
- Create the repository without requiring the user to leave GitMap.

**Work Steps:**
- [ ] 0.7.10.0.2.1 (a) Ask for the repository name
- [ ] 0.7.10.0.2.2 (b) Ask for a repository description
- [ ] 0.7.10.0.2.3 (c) Allow public or private visibility
- [ ] 0.7.10.0.2.4 (d) Create the repository through GitHub
- [ ] 0.7.10.0.2.5 (e) Confirm successful repository creation

#### 0.7.10.0.3 Connect Repository
<!-- GitMap-ID: qqredsmn -->

Connect the roadmap to the selected repository.

**Requirements:**
- Make the selected repository the synchronization target for the roadmap.

**Work Steps:**
- [ ] 0.7.10.0.3.1 (a) Verify repository access
- [ ] 0.7.10.0.3.2 (b) Store the repository association
- [ ] 0.7.10.0.3.3 (c) Prepare the repository for synchronization

#### 0.7.10.0.4 Initial Synchronization
<!-- GitMap-ID: rqredsmm -->

Allow the completed roadmap to proceed directly into GitMap's existing synchronization workflow.

**Requirements:**
- Move from roadmap creation to GitHub synchronization without restarting GitMap.

**Work Steps:**
- [ ] 0.7.10.0.4.1 (a) Preview the initial synchronization
- [ ] 0.7.10.0.4.2 (b) Require confirmation before synchronization
- [ ] 0.7.10.0.4.3 (c) Synchronize the roadmap to the repository
- [ ] 0.7.10.0.4.4 (d) Report synchronization results

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
- [ ] 0.8.1.0.1.1 (a) Provide a `gitmap` command
- [ ] 0.8.1.0.1.2 (b) Display useful help
- [ ] 0.8.1.0.1.3 (c) Display the installed version
- [ ] 0.8.1.0.1.4 (d) Exit cleanly when requested

#### 0.8.1.0.2 Create Roadmap Command
<!-- GitMap-ID: yqredsmf -->

Provide a command for creating or working with a roadmap.

**Requirements:**
- Provide a command for creating or working with a roadmap.

**Work Steps:**
- [ ] 0.8.1.0.2.1 (a) Start the interactive roadmap builder
- [ ] 0.8.1.0.2.2 (b) Allow an existing roadmap to be opened
- [ ] 0.8.1.0.2.3 (c) Validate the roadmap before completing
- [ ] 0.8.1.0.2.4 (d) Save changes to `roadmap.md`

#### 0.8.1.0.3 Create Preview Command
<!-- GitMap-ID: zqredsme -->

Provide a command for previewing how GitMap interprets a roadmap.

**Requirements:**
- Provide a command for previewing how GitMap interprets a roadmap.

**Work Steps:**
- [ ] 0.8.1.0.3.1 (a) Parse the selected roadmap
- [ ] 0.8.1.0.3.2 (b) Display its hierarchy
- [ ] 0.8.1.0.3.3 (c) Report validation problems
- [ ] 0.8.1.0.3.4 (d) Make no GitHub changes

#### 0.8.1.0.4 Create Setup Command
<!-- GitMap-ID: aqredsmd -->

Guide the user through connecting a roadmap to a GitHub repository.

**Requirements:**
- Guide the user through connecting a roadmap to a GitHub repository.

**Work Steps:**
- [ ] 0.8.1.0.4.1 (a) Ask for the GitHub username
- [ ] 0.8.1.0.4.2 (b) Ask for the repository name
- [ ] 0.8.1.0.4.3 (c) Configure authentication
- [ ] 0.8.1.0.4.4 (d) Verify repository access
- [ ] 0.8.1.0.4.5 (e) Save non-sensitive repository configuration

#### 0.8.1.0.5 Create Sync Command
<!-- GitMap-ID: bqredsmc -->

Provide a command for synchronizing the roadmap with GitHub.

**Requirements:**
- Provide a command for synchronizing the roadmap with GitHub.

**Work Steps:**
- [ ] 0.8.1.0.5.1 (a) Validate before synchronization
- [ ] 0.8.1.0.5.2 (b) Verify repository access
- [ ] 0.8.1.0.5.3 (c) Support dry-run mode
- [ ] 0.8.1.0.5.4 (d) Display planned changes
- [ ] 0.8.1.0.5.5 (e) Display a synchronization summary

## 0.8.2 Errors and Guidance
<!-- GitMap-ID: lvredshs -->

#### 0.8.2.0.1 Add User-Friendly Errors
<!-- GitMap-ID: cqredsmb -->

Replace technical failures with useful messages when possible.

**Requirements:**
- Replace technical failures with useful messages when possible.

**Work Steps:**
- [ ] 0.8.2.0.1.1 (a) Explain missing roadmap files
- [ ] 0.8.2.0.1.2 (b) Explain malformed roadmaps
- [ ] 0.8.2.0.1.3 (c) Explain authentication failures
- [ ] 0.8.2.0.1.4 (d) Explain repository access failures
- [ ] 0.8.2.0.1.5 (e) Avoid unnecessary Python tracebacks during normal use

#### 0.8.2.0.2 Add Next-Step Guidance
<!-- GitMap-ID: dqredsma -->

Tell users what they can do after each major operation.

**Requirements:**
- Tell users what they can do after each major operation.

**Work Steps:**
- [ ] 0.8.2.0.2.1 (a) Provide guidance after roadmap creation
- [ ] 0.8.2.0.2.2 (b) Provide guidance after repository setup
- [ ] 0.8.2.0.2.3 (c) Provide guidance after preview
- [ ] 0.8.2.0.2.4 (d) Provide guidance after synchronization

# 0.9 GitMap Desktop GUI

## 0.9.1 Main GitMap Workspace
<!-- GitMap-ID: crredslb -->

#### 0.9.1.0.1 Load the Designer-Based Main Window
<!-- GitMap-ID: eqredsmz -->

Load the GitMap desktop interface from the Qt Designer file while keeping application behavior in Python.

**Requirements:**
- Load the GitMap GUI from a Qt Designer interface while keeping application behavior in Python.

**Work Steps:**
- [ ] 0.9.1.0.1.1 (a) Create `gitmap/gui/app_old.py`
- [ ] 0.9.1.0.1.2 (b) Create `gitmap/gui/main_window.ui`
- [ ] 0.9.1.0.1.3 (c) Create the GUI module entry point
- [ ] 0.9.1.0.1.4 (d) Create the `QApplication`
- [ ] 0.9.1.0.1.5 (e) Locate `main_window.ui` relative to `app_old.py`
- [ ] 0.9.1.0.1.6 (f) Open the `.ui` file using `QFile`
- [ ] 0.9.1.0.1.7 (g) Load the interface using `QUiLoader`
- [ ] 0.9.1.0.1.8 (h) Display the loaded main window
- [ ] 0.9.1.0.1.9 (i) Verify GitMap launches without UI loading errors

#### 0.9.1.0.2 Create the Main Workspace Layout
<!-- GitMap-ID: fqredsmy -->

Create the main two-part application layout with a large roadmap workspace and a smaller navigation and action area.
application window.

**Requirements:**
- Provide a large roadmap workspace with a smaller navigation and action area that resizes correctly with the

**Work Steps:**
- [ ] 0.9.1.0.2.1 (a) Create the main central widget in Qt Designer
- [ ] 0.9.1.0.2.2 (b) Create the roadmap workspace area
- [ ] 0.9.1.0.2.3 (c) Create the navigation and action area
- [ ] 0.9.1.0.2.4 (d) Place the two areas inside a splitter
- [ ] 0.9.1.0.2.5 (e) Give the roadmap area the larger initial share of the window
- [ ] 0.9.1.0.2.6 (f) Configure layouts so controls resize with the window
- [ ] 0.9.1.0.2.7 (g) Test the interface at its normal startup size
- [ ] 0.9.1.0.2.8 (h) Test the interface maximized
- [ ] 0.9.1.0.2.9 (i) Verify the roadmap tree fills the available workspace

#### 0.9.1.0.3 Create the Empty Workspace State
<!-- GitMap-ID: grredslx -->

Define what GitMap displays before a roadmap is opened or created and how the interface changes after a roadmap becomes
active.
when one becomes active.

**Requirements:**
- Clearly provide Create Roadmap and Open Roadmap when no roadmap is active and transition to roadmap-specific controls

**Work Steps:**
- [ ] 0.9.1.0.3.1 (a) Add the Create Roadmap button
- [ ] 0.9.1.0.3.2 (b) Add the Open Roadmap button
- [ ] 0.9.1.0.3.3 (c) Assign stable Designer object names to both buttons
- [ ] 0.9.1.0.3.4 (d) Locate both buttons from Python using `findChild`
- [ ] 0.9.1.0.3.5 (e) Define the empty-workspace state
- [ ] 0.9.1.0.3.6 (f) Define the active-roadmap state
- [ ] 0.9.1.0.3.7 (g) Switch between the states when appropriate

#### 0.9.1.0.4 Create the Roadmap Tree
<!-- GitMap-ID: hrredslw -->

Create the expandable and scrollable tree used to display the active roadmap.

**Requirements:**
- Display the active roadmap in a large expandable and scrollable tree without an unnecessary column heading.

**Work Steps:**
- [ ] 0.9.1.0.4.1 (a) Add the roadmap tree in Qt Designer
- [ ] 0.9.1.0.4.2 (b) Assign the roadmap tree a stable object name
- [ ] 0.9.1.0.4.3 (c) Locate the tree using `findChild`
- [ ] 0.9.1.0.4.4 (d) Hide the tree header
- [ ] 0.9.1.0.4.5 (e) Verify vertical scrolling
- [ ] 0.9.1.0.4.6 (f) Verify long roadmap items remain usable
- [ ] 0.9.1.0.4.7 (g) Verify the tree resizes with the workspace

#### 0.9.1.0.5 Display the Roadmap Name
<!-- GitMap-ID: irredslv -->

Show the name of the active roadmap in the main workspace.

**Requirements:**
- Display the active Roadmap model's name and keep it updated when the active roadmap or its name changes.

**Work Steps:**
- [ ] 0.9.1.0.5.1 (a) Read the roadmap name from the Roadmap model
- [ ] 0.9.1.0.5.2 (b) Display the roadmap name in the workspace
- [ ] 0.9.1.0.5.3 (c) Update the displayed name when another roadmap is opened
- [ ] 0.9.1.0.5.4 (d) Update the displayed name when the roadmap is renamed
- [ ] 0.9.1.0.5.5 (e) Support displaying the name of an unsaved roadmap

#### 0.9.1.0.6 Display Milestones
<!-- GitMap-ID: jrredslu -->

Add every Milestone in the active Roadmap model to the graphical hierarchy.

**Requirements:**
- Display every Milestone beneath the roadmap root using its roadmap number and title.

**Work Steps:**
- [ ] 0.9.1.0.6.1 (a) Iterate through `roadmap.milestones`
- [ ] 0.9.1.0.6.2 (b) Create a tree item for each Milestone
- [ ] 0.9.1.0.6.3 (c) Display the Milestone number
- [ ] 0.9.1.0.6.4 (d) Display the Milestone title
- [ ] 0.9.1.0.6.5 (e) Attach each Milestone beneath the roadmap root

#### 0.9.1.0.7 Display Sections
<!-- GitMap-ID: krredslt -->

Add Sections beneath their parent Milestones when the active roadmap uses Sections.

**Requirements:**
- Display Sections in their correct hierarchy while continuing to support roadmaps that do not use Sections.

**Work Steps:**
- [ ] 0.9.1.0.7.1 (a) Iterate through each Milestone's Sections
- [ ] 0.9.1.0.7.2 (b) Create a tree item for each Section
- [ ] 0.9.1.0.7.3 (c) Display the Section number and title
- [ ] 0.9.1.0.7.4 (d) Attach each Section beneath its parent Milestone
- [ ] 0.9.1.0.7.5 (e) Verify roadmaps without Sections remain supported

#### 0.9.1.0.8 Display Features
<!-- GitMap-ID: lrredsls -->

Add Features beneath their parent Sections when the active roadmap uses Features.

**Requirements:**
- Display Features in their correct hierarchy while continuing to support featureless roadmaps.

**Work Steps:**
- [ ] 0.9.1.0.8.1 (a) Iterate through each Section's Features
- [ ] 0.9.1.0.8.2 (b) Create a tree item for each Feature
- [ ] 0.9.1.0.8.3 (c) Display the Feature number and title
- [ ] 0.9.1.0.8.4 (d) Attach each Feature beneath its parent Section
- [ ] 0.9.1.0.8.5 (e) Verify featureless roadmaps remain supported

#### 0.9.1.0.9 Display Issues
<!-- GitMap-ID: mrredslr -->

Add Issues at each hierarchy location supported by the active roadmap.

**Requirements:**
- Display Issues correctly whether they belong to Features, Sections or directly to Milestones.

**Work Steps:**
- [ ] 0.9.1.0.9.1 (a) Display Issues beneath Features
- [ ] 0.9.1.0.9.2 (b) Display Issues directly beneath Sections
- [ ] 0.9.1.0.9.3 (c) Display Issues directly beneath Milestones
- [ ] 0.9.1.0.9.4 (d) Display each Issue number and title
- [ ] 0.9.1.0.9.5 (e) Reuse a common Issue tree helper
- [ ] 0.9.1.0.9.6 (f) Verify each Issue appears beneath the correct parent

#### 0.9.1.0.10 Display Requirements
<!-- GitMap-ID: nrredslq -->

Display each Issue's Requirement separately from its actionable Work Steps.

**Requirements:**
- Display Requirements as italicized non-checkbox text beneath their parent Issue.

**Work Steps:**
- [ ] 0.9.1.0.10.1 (a) Read the Requirement from `issue.requirements`
- [ ] 0.9.1.0.10.2 (b) Create a tree item for the Requirement
- [ ] 0.9.1.0.10.3 (c) Remove Markdown checkbox syntax if encountered in legacy content
- [ ] 0.9.1.0.10.4 (d) Display the Requirement without a GUI checkbox
- [ ] 0.9.1.0.10.5 (e) Apply an italic font to the Requirement
- [ ] 0.9.1.0.10.6 (f) Verify the Requirement is visually distinct from Work Steps

#### 0.9.1.0.11 Display Work Steps
<!-- GitMap-ID: orredslp -->

Display an Issue's actionable Work Steps beneath the Issue and preserve their markers and completion state.

**Requirements:**
- Display Work Steps separately from Requirements with their marker, text and completion state.

**Work Steps:**
- [ ] 0.9.1.0.11.1 (a) Iterate through `issue.work_steps`
- [ ] 0.9.1.0.11.2 (b) Create a tree item for each Work Step
- [ ] 0.9.1.0.11.3 (c) Display each Work Step marker
- [ ] 0.9.1.0.11.4 (d) Display each Work Step title
- [ ] 0.9.1.0.11.5 (e) Represent the Work Step completion state
- [ ] 0.9.1.0.11.6 (f) Verify Work Steps appear beneath the correct Issue

#### 0.9.1.0.12 Apply GitMap GUI Colors
<!-- GitMap-ID: prredslo -->

Carry GitMap's established command-line color conventions into the graphical roadmap display.
the italic Requirement distinction.

**Requirements:**
- Use the established CLI semantic colors in the GUI where practical while keeping the roadmap readable and preserving

**Work Steps:**
- [ ] 0.9.1.0.12.1 (a) Identify the semantic colors used by the GitMap CLI
- [ ] 0.9.1.0.12.2 (b) Map the CLI colors to GUI hierarchy types
- [ ] 0.9.1.0.12.3 (c) Apply the Milestone color
- [ ] 0.9.1.0.12.4 (d) Apply the Section color
- [ ] 0.9.1.0.12.5 (e) Apply the Feature color
- [ ] 0.9.1.0.12.6 (f) Apply the Issue color
- [ ] 0.9.1.0.12.7 (g) Apply appropriate Requirement and Work Step styling
- [ ] 0.9.1.0.12.8 (h) Verify the complete tree remains easy to read

## 0.9.2 Open Existing Roadmaps
<!-- GitMap-ID: hwredsgw -->

#### 0.9.2.0.1 Open a Roadmap File
<!-- GitMap-ID: qrredsln -->

Allow the user to select an existing roadmap using the desktop interface.

**Requirements:**
- Provide a graphical Open Roadmap workflow for selecting an existing GitMap roadmap file.

**Work Steps:**
- [ ] 0.9.2.0.1.1 (a) Connect the Open Roadmap button
- [ ] 0.9.2.0.1.2 (b) Display a `QFileDialog`
- [ ] 0.9.2.0.1.3 (c) Allow Markdown roadmap files to be selected
- [ ] 0.9.2.0.1.4 (d) Return without changing the active roadmap when the dialog is cancelled
- [ ] 0.9.2.0.1.5 (e) Preserve the selected roadmap path

#### 0.9.2.0.2 Parse an Opened Roadmap
<!-- GitMap-ID: rrredslm -->

Pass the selected roadmap through GitMap's existing parser rather than implementing separate GUI parsing logic.

**Requirements:**
- Parse roadmaps opened by the GUI using the existing `parse_roadmap` behavior.

**Work Steps:**
- [ ] 0.9.2.0.2.1 (a) Pass the selected path to `parse_roadmap`
- [ ] 0.9.2.0.2.2 (b) Receive the populated Roadmap model
- [ ] 0.9.2.0.2.3 (c) Preserve hierarchy configuration
- [ ] 0.9.2.0.2.4 (d) Preserve permanent GitMap IDs
- [ ] 0.9.2.0.2.5 (e) Make the parsed Roadmap the active GUI model

#### 0.9.2.0.3 Populate the Workspace
<!-- GitMap-ID: srredsll -->

Display a successfully parsed Roadmap model in the main workspace.

**Requirements:**
- Populate the same main workspace with successfully opened and newly created roadmaps.

**Work Steps:**
- [ ] 0.9.2.0.3.1 (a) Clear the previous roadmap tree
- [ ] 0.9.2.0.3.2 (b) Display the opened roadmap name
- [ ] 0.9.2.0.3.3 (c) Populate the roadmap hierarchy
- [ ] 0.9.2.0.3.4 (d) Display Requirements and Work Steps
- [ ] 0.9.2.0.3.5 (e) Expand the initial tree
- [ ] 0.9.2.0.3.6 (f) Transition to the active-roadmap state

#### 0.9.2.0.4 Handle Roadmap Opening Errors
<!-- GitMap-ID: trredslk -->

Handle inaccessible, malformed or otherwise invalid roadmap files without crashing the desktop application.

**Requirements:**
- Report roadmap opening failures graphically while leaving the currently active roadmap unchanged.

**Work Steps:**
- [ ] 0.9.2.0.4.1 (a) Catch file opening failures
- [ ] 0.9.2.0.4.2 (b) Catch parser failures
- [ ] 0.9.2.0.4.3 (c) Display a Qt error dialog
- [ ] 0.9.2.0.4.4 (d) Include useful error information
- [ ] 0.9.2.0.4.5 (e) Leave the existing roadmap intact after a failed open
- [ ] 0.9.2.0.4.6 (f) Preserve diagnostic information for development

## 0.9.3 Create New Roadmaps
<!-- GitMap-ID: iwredsgv -->

#### 0.9.3.0.1 Create the Structure Dialog
<!-- GitMap-ID: urredslj -->

Create a separate Qt Designer dialog for configuring the structure of a new roadmap.

**Requirements:**
- Open a graphical structure configuration dialog before creating a new in-memory roadmap.

**Work Steps:**
- [ ] 0.9.3.0.1.1 (a) Create `structure_dialog.ui`
- [ ] 0.9.3.0.1.2 (b) Load the structure dialog from Python
- [ ] 0.9.3.0.1.3 (c) Connect Create Roadmap to the structure dialog
- [ ] 0.9.3.0.1.4 (d) Add structure controls
- [ ] 0.9.3.0.1.5 (e) Add the live example area
- [ ] 0.9.3.0.1.6 (f) Add Create and Cancel actions

#### 0.9.3.0.2 Configure Sections
<!-- GitMap-ID: vrredsli -->

Allow Sections to be enabled or disabled when creating a new roadmap.

**Requirements:**
- Allow new roadmaps to use or omit Sections and disable Section-dependent options when Sections are unavailable.

**Work Steps:**
- [ ] 0.9.3.0.2.1 (a) Add Use Sections
- [ ] 0.9.3.0.2.2 (b) Enable Section-dependent controls when Sections are selected
- [ ] 0.9.3.0.2.3 (c) Disable and grey Section-dependent controls when Sections are not selected
- [ ] 0.9.3.0.2.4 (d) Update the live structure example

#### 0.9.3.0.3 Configure Features
<!-- GitMap-ID: wrredslh -->

Allow Features to be enabled or disabled where the selected hierarchy supports them.

**Requirements:**
- Allow new roadmaps to use or omit Features while keeping unavailable Feature controls visible but disabled.

**Work Steps:**
- [ ] 0.9.3.0.3.1 (a) Add Use Features
- [ ] 0.9.3.0.3.2 (b) Enable Feature-dependent controls when Features are selected
- [ ] 0.9.3.0.3.3 (c) Disable and grey Feature-dependent controls when Features are unavailable
- [ ] 0.9.3.0.3.4 (d) Update the live structure example

#### 0.9.3.0.4 Configure Issue Placement
<!-- GitMap-ID: xrredslg -->

Control which enabled hierarchy levels may directly contain Issues.

**Requirements:**
- Allow only valid Issue placement choices based on the hierarchy selected for the new roadmap.

**Work Steps:**
- [ ] 0.9.3.0.4.1 (a) Add Allow Issues under Sections
- [ ] 0.9.3.0.4.2 (b) Add Allow Issues under Features
- [ ] 0.9.3.0.4.3 (c) Disable Section Issue placement when Sections are disabled
- [ ] 0.9.3.0.4.4 (d) Disable Feature Issue placement when Features are disabled
- [ ] 0.9.3.0.4.5 (e) Validate the final configuration
- [ ] 0.9.3.0.4.6 (f) Update the live example after each change

#### 0.9.3.0.5 Create the Baseball Parks Example
<!-- GitMap-ID: yrredslf -->

Show a live example of how the selected hierarchy organizes roadmap content.

**Requirements:**
- Display a rendered Baseball Parks example that updates to demonstrate the currently selected roadmap structure.

**Work Steps:**
- [ ] 0.9.3.0.5.1 (a) Add MLB Parks as the primary example Milestone
- [ ] 0.9.3.0.5.2 (b) Add American League and National League examples
- [ ] 0.9.3.0.5.3 (c) Add AL East and NL East when Features are enabled
- [ ] 0.9.3.0.5.4 (d) Add Camden Yards and Nationals Park Issues
- [ ] 0.9.3.0.5.5 (e) Add example Requirements and Work Steps
- [ ] 0.9.3.0.5.6 (f) Add a small NFL Stadiums example
- [ ] 0.9.3.0.5.7 (g) Update example numbering when the hierarchy changes

#### 0.9.3.0.6 Explain GitMap Hierarchy Levels
<!-- GitMap-ID: zrredsle -->

Explain how each GitMap hierarchy level can be used without prescribing a particular project structure.
mandatory project meanings.
structure

**Requirements:**
- Explain Milestones, Sections, Features, Issues, Requirements and Work Steps as organizational concepts rather than

**Work Steps:**
- [ ] 0.9.3.0.6.1 (a) Explain Milestone as a major phase
- [ ] 0.9.3.0.6.2 (b) Explain Section as an area or subsystem
- [ ] 0.9.3.0.6.3 (c) Explain Feature as a feature or capability
- [ ] 0.9.3.0.6.4 (d) Explain Issue as a specific task
- [ ] 0.9.3.0.6.5 (e) Explain Requirements as what should be done
- [ ] 0.9.3.0.6.6 (f) Explain Work Steps as steps for doing it
- [ ] 0.9.3.0.6.7 (g) Explain that the Baseball Parks example demonstrates organization rather than a prescribed

#### 0.9.3.0.7 Create an Unsaved Roadmap Workspace
<!-- GitMap-ID: arredsld -->

Create the Roadmap model after structure selection without forcing the user to choose a file location.

**Requirements:**
- Create a usable in-memory roadmap immediately after structure setup without automatically creating a file.

**Work Steps:**
- [ ] 0.9.3.0.7.1 (a) Create the Roadmap model
- [ ] 0.9.3.0.7.2 (b) Apply the selected structure settings
- [ ] 0.9.3.0.7.3 (c) Populate the main workspace
- [ ] 0.9.3.0.7.4 (d) Mark the roadmap as unsaved
- [ ] 0.9.3.0.7.5 (e) Enable roadmap editing controls
- [ ] 0.9.3.0.7.6 (f) Verify no file is created automatically

## 0.9.4 Roadmap Navigation
<!-- GitMap-ID: jwredsgu -->

#### 0.9.4.0.1 Associate Tree Items With Model Objects
<!-- GitMap-ID: drredsla -->

Maintain a connection between displayed tree items and their underlying GitMap model objects.

**Requirements:**
- Resolve each editable graphical roadmap item back to the model object it represents.

**Work Steps:**
- [ ] 0.9.4.0.1.1 (a) Choose a safe model association mechanism
- [ ] 0.9.4.0.1.2 (b) Associate Milestone tree items
- [ ] 0.9.4.0.1.3 (c) Associate Section tree items
- [ ] 0.9.4.0.1.4 (d) Associate Feature tree items
- [ ] 0.9.4.0.1.5 (e) Associate Issue tree items
- [ ] 0.9.4.0.1.6 (f) Verify associations remain correct after tree refreshes

#### 0.9.4.0.2 Select Roadmap Items
<!-- GitMap-ID: erredslz -->

Allow users to select items in the graphical hierarchy for further actions.

**Requirements:**
- Track the selected roadmap object and enable only actions valid for its type and location.

**Work Steps:**
- [ ] 0.9.4.0.2.1 (a) Detect tree selection changes
- [ ] 0.9.4.0.2.2 (b) Resolve the selected model object
- [ ] 0.9.4.0.2.3 (c) Determine actions valid for the selected object
- [ ] 0.9.4.0.2.4 (d) Enable valid actions
- [ ] 0.9.4.0.2.5 (e) Disable invalid actions

#### 0.9.4.0.3 Open Items From the Tree
<!-- GitMap-ID: frredsly -->

Open editable roadmap items directly from the graphical roadmap hierarchy.
workspace.

**Requirements:**
- Open the appropriate pop-out Item Editor when an editable roadmap item is double-clicked without replacing the main

**Work Steps:**
- [ ] 0.9.4.0.3.1 (a) Detect tree double-clicks
- [ ] 0.9.4.0.3.2 (b) Resolve the clicked model object
- [ ] 0.9.4.0.3.3 (c) Determine whether the object is editable
- [ ] 0.9.4.0.3.4 (d) Open the appropriate Item Editor
- [ ] 0.9.4.0.3.5 (e) Leave the main workspace open

## 0.9.5 Item Editors
<!-- GitMap-ID: kwredsgt -->

#### 0.9.5.0.1 Create the Item Editor Window
<!-- GitMap-ID: gsredskx -->

Create a reusable graphical window for editing roadmap items.
open.

**Requirements:**
- Provide a pop-out Item Editor that operates on the selected in-memory roadmap object while leaving the main workspace

**Work Steps:**
- [ ] 0.9.5.0.1.1 (a) Create `item_editor.ui`
- [ ] 0.9.5.0.1.2 (b) Load the Item Editor from Python
- [ ] 0.9.5.0.1.3 (c) Associate the editor with a model object
- [ ] 0.9.5.0.1.4 (d) Add controls for applying changes
- [ ] 0.9.5.0.1.5 (e) Add Cancel or Close behavior

#### 0.9.5.0.2 Adapt the Editor to Item Type
<!-- GitMap-ID: hsredskw -->

Configure the Item Editor according to the type of roadmap object being edited.

**Requirements:**
- Show only editing controls that are valid for the selected Milestone, Section, Feature or Issue.

**Work Steps:**
- [ ] 0.9.5.0.2.1 (a) Detect the selected item type
- [ ] 0.9.5.0.2.2 (b) Configure the editor for Milestones
- [ ] 0.9.5.0.2.3 (c) Configure the editor for Sections
- [ ] 0.9.5.0.2.4 (d) Configure the editor for Features
- [ ] 0.9.5.0.2.5 (e) Configure the editor for Issues

#### 0.9.5.0.3 Edit Item Content
<!-- GitMap-ID: isredskv -->

Edit supported roadmap titles and descriptions.
synchronizing GitHub.

**Requirements:**
- Apply valid title and description edits to the in-memory model and refresh the workspace without automatically

**Work Steps:**
- [ ] 0.9.5.0.3.1 (a) Populate the title control
- [ ] 0.9.5.0.3.2 (b) Populate the description control
- [ ] 0.9.5.0.3.3 (c) Validate edited values
- [ ] 0.9.5.0.3.4 (d) Apply approved changes to the model
- [ ] 0.9.5.0.3.5 (e) Refresh the roadmap tree
- [ ] 0.9.5.0.3.6 (f) Mark the roadmap as modified

#### 0.9.5.0.4 Edit Requirements
<!-- GitMap-ID: jsredsku -->

Manage an Issue's Requirements graphically.

**Requirements:**
- Allow Requirements to be viewed, added, edited and removed independently from Work Steps.

**Work Steps:**
- [ ] 0.9.5.0.4.1 (a) Display the existing Requirement
- [ ] 0.9.5.0.4.2 (b) Add a Requirement
- [ ] 0.9.5.0.4.3 (c) Edit Requirement text
- [ ] 0.9.5.0.4.4 (d) Remove a Requirement
- [ ] 0.9.5.0.4.5 (e) Refresh the roadmap tree

#### 0.9.5.0.5 Edit Work Steps
<!-- GitMap-ID: ksredskt -->

Manage an Issue's Work Steps graphically.

**Requirements:**
- Allow Work Steps to be added, edited, completed and removed while maintaining correct numbering and markers.

**Work Steps:**
- [ ] 0.9.5.0.5.1 (a) Display existing Work Steps
- [ ] 0.9.5.0.5.2 (b) Add a Work Step
- [ ] 0.9.5.0.5.3 (c) Assign the next Work Step marker
- [ ] 0.9.5.0.5.4 (d) Edit Work Step text
- [ ] 0.9.5.0.5.5 (e) Change Work Step completion state
- [ ] 0.9.5.0.5.6 (f) Remove a Work Step
- [ ] 0.9.5.0.5.7 (g) Renumber Work Step markers when required
- [ ] 0.9.5.0.5.8 (h) Refresh the roadmap tree

## 0.9.6 Add Insert and Delete Roadmap Items
<!-- GitMap-ID: lwredsgs -->

#### 0.9.6.0.1 Add Valid Child Items
<!-- GitMap-ID: lsredsks -->

Add new roadmap items beneath compatible parent items.

**Requirements:**
- Offer only child item types permitted by the selected parent and the active roadmap's hierarchy configuration.

**Work Steps:**
- [ ] 0.9.6.0.1.1 (a) Determine the selected parent type
- [ ] 0.9.6.0.1.2 (b) Read the roadmap hierarchy configuration
- [ ] 0.9.6.0.1.3 (c) Determine valid child types
- [ ] 0.9.6.0.1.4 (d) Present only valid choices
- [ ] 0.9.6.0.1.5 (e) Create the selected child using automatic numbering
- [ ] 0.9.6.0.1.6 (f) Refresh the roadmap tree

#### 0.9.6.0.2 Insert Items Between Existing Siblings
<!-- GitMap-ID: msredskr -->

Use GitMap's automatic numbering logic to insert items at a selected sibling position.

**Requirements:**
- Insert items between existing siblings without requiring the user to manually calculate or repair roadmap numbers.

**Work Steps:**
- [ ] 0.9.6.0.2.1 (a) Display valid insertion positions
- [ ] 0.9.6.0.2.2 (b) Let the user choose a position
- [ ] 0.9.6.0.2.3 (c) Use GitMap's sibling numbering logic
- [ ] 0.9.6.0.2.4 (d) Determine affected descendants
- [ ] 0.9.6.0.2.5 (e) Generate the numbering preview
- [ ] 0.9.6.0.2.6 (f) Apply the insertion only after approval

#### 0.9.6.0.3 Delete Roadmap Items Safely
<!-- GitMap-ID: nsredskq -->

Delete roadmap items while previewing any hierarchy or numbering consequences.

**Requirements:**
- Require confirmation of the item, descendant and numbering effects before applying a destructive roadmap deletion.

**Work Steps:**
- [ ] 0.9.6.0.3.1 (a) Select the item to delete
- [ ] 0.9.6.0.3.2 (b) Determine its descendants
- [ ] 0.9.6.0.3.3 (c) Determine resulting numbering changes
- [ ] 0.9.6.0.3.4 (d) Display the proposed deletion
- [ ] 0.9.6.0.3.5 (e) Display numbering changes
- [ ] 0.9.6.0.3.6 (f) Allow approval or cancellation
- [ ] 0.9.6.0.3.7 (g) Apply only the approved deletion
- [ ] 0.9.6.0.3.8 (h) Refresh the roadmap tree

## 0.9.7 Graphical Change Preview
<!-- GitMap-ID: mwredsgr -->

#### 0.9.7.0.1 Create the Roadmap Preview Window
<!-- GitMap-ID: osredskp -->

Create a separate graphical window for reviewing proposed roadmap changes.

**Requirements:**
- Display proposed changes in a scrollable pop-out preview while leaving the main roadmap workspace available.

**Work Steps:**
- [ ] 0.9.7.0.1.1 (a) Create `preview_dialog.ui`
- [ ] 0.9.7.0.1.2 (b) Load the preview interface from Python
- [ ] 0.9.7.0.1.3 (c) Add a scrollable change area
- [ ] 0.9.7.0.1.4 (d) Add Approve and Cancel actions
- [ ] 0.9.7.0.1.5 (e) Keep the main workspace available

#### 0.9.7.0.2 Display Before and After Changes
<!-- GitMap-ID: psredsko -->

Show the original and proposed state of affected roadmap items.

**Requirements:**
- Make hierarchy, numbering, additions, changes and removals understandable before a proposed operation is approved.

**Work Steps:**
- [ ] 0.9.7.0.2.1 (a) Collect the original state
- [ ] 0.9.7.0.2.2 (b) Collect the proposed state
- [ ] 0.9.7.0.2.3 (c) Display before values
- [ ] 0.9.7.0.2.4 (d) Display after values
- [ ] 0.9.7.0.2.5 (e) Highlight added items
- [ ] 0.9.7.0.2.6 (f) Highlight changed items
- [ ] 0.9.7.0.2.7 (g) Highlight removed items

#### 0.9.7.0.3 Cancel Previewed Changes
<!-- GitMap-ID: qsredskn -->

Restore the original roadmap state when the user cancels a proposed operation.

**Requirements:**
- Leave the roadmap exactly as it was before the proposed operation when a preview is cancelled.

**Work Steps:**
- [ ] 0.9.7.0.3.1 (a) Preserve the original state before generating changes
- [ ] 0.9.7.0.3.2 (b) Detect cancellation
- [ ] 0.9.7.0.3.3 (c) Restore original numbering
- [ ] 0.9.7.0.3.4 (d) Restore original hierarchy
- [ ] 0.9.7.0.3.5 (e) Refresh the roadmap tree
- [ ] 0.9.7.0.3.6 (f) Verify cancellation produces no saved changes

## 0.9.8 Save Roadmaps
<!-- GitMap-ID: nwredsgq -->

#### 0.9.8.0.1 Save an Existing Roadmap
<!-- GitMap-ID: rsredskm -->

Write changes to the active roadmap file.

**Requirements:**
- Save an existing roadmap to its current path while preserving valid GitMap Markdown and permanent identities.

**Work Steps:**
- [ ] 0.9.8.0.1.1 (a) Determine the active roadmap path
- [ ] 0.9.8.0.1.2 (b) Serialize the in-memory Roadmap
- [ ] 0.9.8.0.1.3 (c) Write the roadmap file
- [ ] 0.9.8.0.1.4 (d) Mark the roadmap as saved
- [ ] 0.9.8.0.1.5 (e) Update GUI status

#### 0.9.8.0.2 Save a New Roadmap
<!-- GitMap-ID: ssredskl -->

Choose a file location the first time an unsaved roadmap is saved.

**Requirements:**
- Prompt for a destination when saving an unsaved roadmap and make the successful destination its active file.

**Work Steps:**
- [ ] 0.9.8.0.2.1 (a) Detect that the roadmap has no active path
- [ ] 0.9.8.0.2.2 (b) Open a save dialog
- [ ] 0.9.8.0.2.3 (c) Write the roadmap to the selected path
- [ ] 0.9.8.0.2.4 (d) Store the selected path
- [ ] 0.9.8.0.2.5 (e) Change the roadmap from unsaved to saved

#### 0.9.8.0.3 Save As
<!-- GitMap-ID: tsredskk -->

Write the active roadmap to a user-selected new file.

**Requirements:**
- Save the current roadmap to a different path and make that path active after the operation succeeds.

**Work Steps:**
- [ ] 0.9.8.0.3.1 (a) Add Save As
- [ ] 0.9.8.0.3.2 (b) Open the Save As dialog
- [ ] 0.9.8.0.3.3 (c) Write the current roadmap to the selected path
- [ ] 0.9.8.0.3.4 (d) Update the active roadmap path
- [ ] 0.9.8.0.3.5 (e) Update the window state

#### 0.9.8.0.4 Track Modified Roadmaps
<!-- GitMap-ID: usredskj -->

Track whether the in-memory roadmap differs from its last saved state.

**Requirements:**
- Maintain and display an accurate modified state for the active roadmap.

**Work Steps:**
- [ ] 0.9.8.0.4.1 (a) Establish a modified-state flag
- [ ] 0.9.8.0.4.2 (b) Mark content edits as modified
- [ ] 0.9.8.0.4.3 (c) Mark structural changes as modified
- [ ] 0.9.8.0.4.4 (d) Clear modified state after a successful save
- [ ] 0.9.8.0.4.5 (e) Indicate modified state in the GUI

#### 0.9.8.0.5 Protect Unsaved Work
<!-- GitMap-ID: vsredski -->

Prevent unsaved changes from being silently discarded.

**Requirements:**
- Prompt before closing or replacing an active roadmap that contains unsaved changes.

**Work Steps:**
- [ ] 0.9.8.0.5.1 (a) Detect unsaved changes before replacement
- [ ] 0.9.8.0.5.2 (b) Offer Save
- [ ] 0.9.8.0.5.3 (c) Offer Discard
- [ ] 0.9.8.0.5.4 (d) Offer Cancel
- [ ] 0.9.8.0.5.5 (e) Stop the requested operation when Cancel is selected
- [ ] 0.9.8.0.5.6 (f) Verify application closing also protects unsaved work

## 0.9.9 Roadmap Settings
<!-- GitMap-ID: owredsgp -->

#### 0.9.9.0.1 Create Roadmap Settings
<!-- GitMap-ID: wsredskh -->

Create a graphical settings interface for viewing the active roadmap's configuration.

**Requirements:**
- Display supported configuration values from the active Roadmap model in a dedicated settings interface.

**Work Steps:**
- [ ] 0.9.9.0.1.1 (a) Create the settings interface
- [ ] 0.9.9.0.1.2 (b) Load settings from the active Roadmap
- [ ] 0.9.9.0.1.3 (c) Display numbering configuration
- [ ] 0.9.9.0.1.4 (d) Display hierarchy configuration
- [ ] 0.9.9.0.1.5 (e) Display hierarchy Issue title style

#### 0.9.9.0.2 Safely Modify Roadmap Settings
<!-- GitMap-ID: xsredskg -->

Allow supported settings to change without bypassing validation or preview protections.

**Requirements:**
- Validate settings changes and preview any changes that would alter existing roadmap numbering or hierarchy.

**Work Steps:**
- [ ] 0.9.9.0.2.1 (a) Determine editable settings
- [ ] 0.9.9.0.2.2 (b) Validate proposed settings
- [ ] 0.9.9.0.2.3 (c) Determine whether existing items are affected
- [ ] 0.9.9.0.2.4 (d) Generate a preview when required
- [ ] 0.9.9.0.2.5 (e) Apply only approved changes
- [ ] 0.9.9.0.2.6 (f) Refresh the workspace

## 0.9.10 GitHub Synchronization
<!-- GitMap-ID: pwredsgo -->

#### 0.9.10.0.1 Start Synchronization From the GUI
<!-- GitMap-ID: luredsis -->

Begin synchronization using a graphical action in the main workspace.
validation or preview behavior.

**Requirements:**
- Start synchronization through the existing GitMap synchronization system without bypassing discovery, mapping,

**Work Steps:**
- [ ] 0.9.10.0.1.1 (a) Add the synchronization action
- [ ] 0.9.10.0.1.2 (b) Validate the active roadmap
- [ ] 0.9.10.0.1.3 (c) Start existing GitHub discovery
- [ ] 0.9.10.0.1.4 (d) Build the synchronization plan
- [ ] 0.9.10.0.1.5 (e) Pass the plan to graphical preview

#### 0.9.10.0.2 Display the Synchronization Preview
<!-- GitMap-ID: mvredshr -->

Display the existing GitMap synchronization preview graphically.

**Requirements:**
- Clearly distinguish added, changed, unchanged and removed GitHub items before synchronization approval.

**Work Steps:**
- [ ] 0.9.10.0.2.1 (a) Display summary counts
- [ ] 0.9.10.0.2.2 (b) Display added items
- [ ] 0.9.10.0.2.3 (c) Display changed items
- [ ] 0.9.10.0.2.4 (d) Display unchanged items when requested
- [ ] 0.9.10.0.2.5 (e) Display removed items
- [ ] 0.9.10.0.2.6 (f) Provide approval and cancellation

#### 0.9.10.0.3 Apply Only Approved GitHub Changes
<!-- GitMap-ID: nvredshq -->

Preserve GitMap's approval boundary when synchronization is controlled through the GUI.

**Requirements:**
- Allow only GitHub operations contained in the approved synchronization plan to modify existing GitHub state.

**Work Steps:**
- [ ] 0.9.10.0.3.1 (a) Preserve the approved synchronization plan
- [ ] 0.9.10.0.3.2 (b) Reject operations absent from the approved plan
- [ ] 0.9.10.0.3.3 (c) Apply approved creations
- [ ] 0.9.10.0.3.4 (d) Apply approved updates
- [ ] 0.9.10.0.3.5 (e) Apply approved closures
- [ ] 0.9.10.0.3.6 (f) Verify cancellation modifies nothing

#### 0.9.10.0.4 Display Synchronization Results
<!-- GitMap-ID: ovredshp -->

Show the outcome of synchronization inside the graphical interface.
console.

**Requirements:**
- Display created, updated, closed, skipped and failed synchronization operations without requiring the development

**Work Steps:**
- [ ] 0.9.10.0.4.1 (a) Collect synchronization results
- [ ] 0.9.10.0.4.2 (b) Display created items
- [ ] 0.9.10.0.4.3 (c) Display updated items
- [ ] 0.9.10.0.4.4 (d) Display closed items
- [ ] 0.9.10.0.4.5 (e) Display skipped operations
- [ ] 0.9.10.0.4.6 (f) Display failures
- [ ] 0.9.10.0.4.7 (g) Refresh the roadmap workspace after synchronization

## 0.9.11 User Feedback and Error Handling
<!-- GitMap-ID: qwredsgn -->

#### 0.9.11.0.1 Use the Status Bar
<!-- GitMap-ID: pvredsho -->

Use the main window status bar for lightweight feedback.

**Requirements:**
- Report routine application status without unnecessarily interrupting the user's workflow.

**Work Steps:**
- [ ] 0.9.11.0.1.1 (a) Locate the Designer status bar
- [ ] 0.9.11.0.1.2 (b) Display roadmap-open status
- [ ] 0.9.11.0.1.3 (c) Display save status
- [ ] 0.9.11.0.1.4 (d) Display validation status
- [ ] 0.9.11.0.1.5 (e) Display synchronization status

#### 0.9.11.0.2 Display User-Friendly Errors
<!-- GitMap-ID: qvredshn -->

Present expected application failures as understandable graphical messages.

**Requirements:**
- Display useful graphical error messages while preserving more detailed diagnostic information for development.

**Work Steps:**
- [ ] 0.9.11.0.2.1 (a) Create a common GUI error-display helper
- [ ] 0.9.11.0.2.2 (b) Handle roadmap file errors
- [ ] 0.9.11.0.2.3 (c) Handle parser errors
- [ ] 0.9.11.0.2.4 (d) Handle validation errors
- [ ] 0.9.11.0.2.5 (e) Handle save errors
- [ ] 0.9.11.0.2.6 (f) Handle GitHub errors
- [ ] 0.9.11.0.2.7 (g) Preserve useful diagnostic logging

## 0.9.12 Desktop Application Behavior
<!-- GitMap-ID: rwredsgm -->

#### 0.9.12.0.1 Add Standard Keyboard Shortcuts
<!-- GitMap-ID: rvredshm -->

Provide familiar keyboard shortcuts for common desktop actions.

**Requirements:**
- Use standard desktop shortcuts for common GitMap actions where they do not conflict with application behavior.

**Work Steps:**
- [ ] 0.9.12.0.1.1 (a) Add Ctrl+O for Open
- [ ] 0.9.12.0.1.2 (b) Add Ctrl+S for Save
- [ ] 0.9.12.0.1.3 (c) Add a Save As shortcut
- [ ] 0.9.12.0.1.4 (d) Add appropriate new-roadmap navigation
- [ ] 0.9.12.0.1.5 (e) Verify shortcuts do not conflict with Item Editors

#### 0.9.12.0.2 Support Normal Desktop Window Behavior
<!-- GitMap-ID: svredshl -->

Manage the relationship between the main workspace and GitMap's pop-out windows.
main workspace.

**Requirements:**
- Allow editors, previews and dialogs to behave as normal child windows without unexpectedly closing or replacing the

**Work Steps:**
- [ ] 0.9.12.0.2.1 (a) Establish ownership for dialogs
- [ ] 0.9.12.0.2.2 (b) Establish ownership for Item Editors
- [ ] 0.9.12.0.2.3 (c) Establish ownership for Preview windows
- [ ] 0.9.12.0.2.4 (d) Test multiple simultaneous Item Editors
- [ ] 0.9.12.0.2.5 (e) Test closing individual child windows
- [ ] 0.9.12.0.2.6 (f) Test closing the main application

## 0.9.13 Preserve the GitMap Core Architecture
<!-- GitMap-ID: swredsgl -->

#### 0.9.13.0.1 Reuse the Existing Parser
<!-- GitMap-ID: tvredshk -->

Use GitMap's established parser for GUI roadmap loading.

**Requirements:**
- Use the existing GitMap parser as the authoritative parser for roadmaps opened by the desktop interface.

**Work Steps:**
- [ ] 0.9.13.0.1.1 (a) Route GUI file loading through `parse_roadmap`
- [ ] 0.9.13.0.1.2 (b) Preserve parser behavior shared with the CLI
- [ ] 0.9.13.0.1.3 (c) Verify representative existing roadmaps

#### 0.9.13.0.2 Reuse the Existing Model
<!-- GitMap-ID: uvredshj -->

Use the existing GitMap model as the application's roadmap state.

**Requirements:**
- Keep the existing Roadmap model and its hierarchy objects authoritative for GUI state and editing.

**Work Steps:**
- [ ] 0.9.13.0.2.1 (a) Store the active Roadmap model
- [ ] 0.9.13.0.2.2 (b) Read hierarchy data from existing model classes
- [ ] 0.9.13.0.2.3 (c) Apply GUI edits to existing model classes
- [ ] 0.9.13.0.2.4 (d) Avoid introducing duplicate GUI-only roadmap models

#### 0.9.13.0.3 Reuse Automatic Numbering
<!-- GitMap-ID: vvredshi -->

Use GitMap's existing automatic numbering system for graphical roadmap changes.

**Requirements:**
- Route GUI creation, insertion and renumbering operations through the existing automatic numbering behavior.

**Work Steps:**
- [ ] 0.9.13.0.3.1 (a) Reuse sibling-number calculation
- [ ] 0.9.13.0.3.2 (b) Reuse insertion numbering
- [ ] 0.9.13.0.3.3 (c) Reuse descendant renumbering
- [ ] 0.9.13.0.3.4 (d) Preserve Work Step marker behavior
- [ ] 0.9.13.0.3.5 (e) Verify numbering results match CLI behavior

#### 0.9.13.0.4 Reuse Validation
<!-- GitMap-ID: wvredshh -->

Use existing GitMap validation before applying graphical roadmap changes.

**Requirements:**
- Apply the existing roadmap validation rules to GUI operations rather than creating weaker GUI-specific rules.

**Work Steps:**
- [ ] 0.9.13.0.4.1 (a) Validate edited roadmaps
- [ ] 0.9.13.0.4.2 (b) Validate hierarchy changes
- [ ] 0.9.13.0.4.3 (c) Detect duplicate numbers
- [ ] 0.9.13.0.4.4 (d) Detect invalid structures
- [ ] 0.9.13.0.4.5 (e) Display validation failures graphically

#### 0.9.13.0.5 Reuse GitHub Mapping
<!-- GitMap-ID: bvredshc -->

Use GitMap's existing identity, mapping and synchronization protections from the desktop GUI.
when synchronizing through the GUI.

**Requirements:**
- Preserve existing GitHub mapping, permanent identity, roadmap-specific searching, hierarchy and approval protections

**Work Steps:**
- [ ] 0.9.13.0.5.1 (a) Route GUI synchronization through existing GitHub mapping
- [ ] 0.9.13.0.5.2 (b) Preserve permanent GitMap IDs
- [ ] 0.9.13.0.5.3 (c) Preserve roadmap-specific searching
- [ ] 0.9.13.0.5.4 (d) Preserve parent and child GitHub relationships
- [ ] 0.9.13.0.5.5 (e) Preserve Issue identity during renumbering
- [ ] 0.9.13.0.5.6 (f) Preserve approval before modifying existing GitHub items

## 0.9.14 GUI Integration Testing
<!-- GitMap-ID: twredsgk -->

### Special Test Case of Features
<!-- GitMap-ID: goredsox -->

#### 0.9.14.0.1 Test Existing Roadmaps
<!-- GitMap-ID: cvredshb -->

Verify that existing roadmap files work correctly in the desktop interface.

**Requirements:**
- Open and display representative existing GitMap roadmaps without changing their intended hierarchy or content.

**Work Steps:**
- [ ] 0.9.14.0.1.1 (a) Test a roadmap using Sections and Features
- [ ] 0.9.14.0.1.2 (b) Test a featureless roadmap
- [ ] 0.9.14.0.1.3 (c) Test Issues directly beneath Sections
- [ ] 0.9.14.0.1.4 (d) Test Issues directly beneath Milestones
- [ ] 0.9.14.0.1.5 (e) Verify Requirements
- [ ] 0.9.14.0.1.6 (f) Verify Work Steps

#### 0.9.14.0.2 Test New Roadmap Creation
<!-- GitMap-ID: dvredsha -->

Verify each supported new-roadmap structure configuration.

**Requirements:**
- Create valid in-memory roadmaps for every hierarchy configuration offered by the structure dialog.

**Work Steps:**
- [ ] 0.9.14.0.2.1 (a) Test Sections with Features
- [ ] 0.9.14.0.2.2 (b) Test Sections without Features
- [ ] 0.9.14.0.2.3 (c) Test supported no-Section structures
- [ ] 0.9.14.0.2.4 (d) Test Issue placement choices
- [ ] 0.9.14.0.2.5 (e) Verify the resulting roadmap model

#### 0.9.14.0.3 Test Editing and Numbering
<!-- GitMap-ID: evredshz -->

Verify graphical editing preserves GitMap's automatic numbering rules.
logic.

**Requirements:**
- Produce the same valid hierarchy and numbering results through GUI editing that GitMap produces through its existing

**Work Steps:**
- [ ] 0.9.14.0.3.1 (a) Add roadmap items
- [ ] 0.9.14.0.3.2 (b) Insert between siblings
- [ ] 0.9.14.0.3.3 (c) Delete roadmap items
- [ ] 0.9.14.0.3.4 (d) Verify descendant renumbering
- [ ] 0.9.14.0.3.5 (e) Verify Work Step numbering and markers
- [ ] 0.9.14.0.3.6 (f) Cancel a numbering preview and verify rollback

#### 0.9.14.0.4 Test Saving and Unsaved Changes
<!-- GitMap-ID: fvredshy -->

Verify roadmap files can be safely created and modified through the GUI.

**Requirements:**
- Preserve roadmap content through Save, Save As, reopening and unsaved-change protection.

**Work Steps:**
- [ ] 0.9.14.0.4.1 (a) Save a new roadmap
- [ ] 0.9.14.0.4.2 (b) Save changes to an existing roadmap
- [ ] 0.9.14.0.4.3 (c) Test Save As
- [ ] 0.9.14.0.4.4 (d) Reopen each saved roadmap
- [ ] 0.9.14.0.4.5 (e) Verify permanent GitMap IDs
- [ ] 0.9.14.0.4.6 (f) Verify unsaved-change protection

#### 0.9.14.0.5 Test GitHub Synchronization
<!-- GitMap-ID: gwredsgx -->

Verify that graphical synchronization preserves all existing GitMap protections.
workflow.

**Requirements:**
- Produce the same protected GitHub synchronization results from the GUI as from the established GitMap synchronization

**Work Steps:**
- [ ] 0.9.14.0.5.1 (a) Preview synchronization containing new items
- [ ] 0.9.14.0.5.2 (b) Preview synchronization containing changed items
- [ ] 0.9.14.0.5.3 (c) Preview synchronization containing removed items
- [ ] 0.9.14.0.5.4 (d) Cancel synchronization and verify GitHub remains unchanged
- [ ] 0.9.14.0.5.5 (e) Approve synchronization
- [ ] 0.9.14.0.5.6 (f) Verify only approved operations occurred
- [ ] 0.9.14.0.5.7 (g) Verify GitMap IDs remain associated with the correct GitHub Issues
- [ ] 0.9.14.0.5.8 (h) Verify GitHub parent and child relationships remain correct

# 0.10 Testing and Reliability

## 0.10.1 Automated Testing
<!-- GitMap-ID: xvredshg -->

#### 0.10.1.0.1 Test Roadmap Parsing
<!-- GitMap-ID: ysredskf -->

Test conversion of Markdown roadmaps into GitMap project data.

**Requirements:**
- Test conversion of Markdown roadmaps into GitMap project data.

**Work Steps:**
- [ ] 0.10.1.0.1.1 (a) Test milestones
- [ ] 0.10.1.0.1.2 (b) Test Sections
- [ ] 0.10.1.0.1.3 (c) Test issues
- [ ] 0.10.1.0.1.4 (d) Test sub-issues
- [ ] 0.10.1.0.1.5 (e) Test descriptions and requirements

#### 0.10.1.0.2 Test Roadmap Validation
<!-- GitMap-ID: zsredske -->

Test detection of invalid roadmap structures.

**Requirements:**
- Test detection of invalid roadmap structures.

**Work Steps:**
- [ ] 0.10.1.0.2.1 (a) Test malformed hierarchy
- [ ] 0.10.1.0.2.2 (b) Test duplicate numbering
- [ ] 0.10.1.0.2.3 (c) Test invalid parent relationships
- [ ] 0.10.1.0.2.4 (d) Test useful validation messages

#### 0.10.1.0.3 Test GitHub Mapping
<!-- GitMap-ID: asredskd -->

Test conversion of roadmap data into GitHub structures.

**Requirements:**
- Test conversion of roadmap data into GitHub structures.

**Work Steps:**
- [ ] 0.10.1.0.3.1 (a) Test milestone mapping
- [ ] 0.10.1.0.3.2 (b) Test label mapping
- [ ] 0.10.1.0.3.3 (c) Test Section mapping
- [ ] 0.10.1.0.3.4 (d) Test issue mapping
- [ ] 0.10.1.0.3.5 (e) Test sub-issue relationships

#### 0.10.1.0.4 Test Duplicate Prevention
<!-- GitMap-ID: bsredskc -->

Verify that synchronization can safely run more than once.

**Requirements:**
- Verify that synchronization can safely run more than once.

**Work Steps:**
- [ ] 0.10.1.0.4.1 (a) Test existing labels
- [ ] 0.10.1.0.4.2 (b) Test existing milestones
- [ ] 0.10.1.0.4.3 (c) Test existing issues
- [ ] 0.10.1.0.4.4 (d) Confirm repeated synchronization does not create duplicates

#### 0.10.1.0.5 Test Roadmap Updates
<!-- GitMap-ID: csredskb -->

Test synchronization after a roadmap has changed.

**Requirements:**
- Test synchronization after a roadmap has changed.

**Work Steps:**
- [ ] 0.10.1.0.5.1 (a) Test newly added items
- [ ] 0.10.1.0.5.2 (b) Test changed items
- [ ] 0.10.1.0.5.3 (c) Test unchanged items
- [ ] 0.10.1.0.5.4 (d) Test removed roadmap items
- [ ] 0.10.1.0.5.5 (e) Confirm destructive changes are not automatic

## 0.10.2 Failure Protection
<!-- GitMap-ID: yvredshf -->

#### 0.10.2.0.1 Handle GitHub API Failures
<!-- GitMap-ID: dsredska -->

Handle failures while communicating with GitHub.

**Requirements:**
- Handle failures while communicating with GitHub.

**Work Steps:**
- [ ] 0.10.2.0.1.1 (a) Detect API errors
- [ ] 0.10.2.0.1.2 (b) Report which operation failed
- [ ] 0.10.2.0.1.3 (c) Preserve useful error details
- [ ] 0.10.2.0.1.4 (d) Stop safely when synchronization cannot continue

#### 0.10.2.0.2 Test Dry Run Safety
<!-- GitMap-ID: esredskz -->

Verify that dry-run mode never changes GitHub.

**Requirements:**
- Verify that dry-run mode never changes GitHub.

**Work Steps:**
- [ ] 0.10.2.0.2.1 (a) Exercise the complete synchronization path
- [ ] 0.10.2.0.2.2 (b) Confirm no create operations occur
- [ ] 0.10.2.0.2.3 (c) Confirm no update operations occur
- [ ] 0.10.2.0.2.4 (d) Confirm planned changes are still reported

#### 0.10.2.0.3 Add Integration Tests
<!-- GitMap-ID: fsredsky -->

Test complete GitMap workflows using representative roadmap data.

**Requirements:**
- Test complete GitMap workflows using representative roadmap data.

**Work Steps:**
- [ ] 0.10.2.0.3.1 (a) Test roadmap creation through parsing
- [ ] 0.10.2.0.3.2 (b) Test parsing through synchronization planning
- [ ] 0.10.2.0.3.3 (c) Test existing-project update workflows
- [ ] 0.10.2.0.3.4 (d) Keep tests independent of a user's real GitHub repository where possible

# 0.11 Release Preparation

## 0.11.1 Documentation
<!-- GitMap-ID: zvredshe -->

#### 0.11.1.0.1 Complete README
<!-- GitMap-ID: gtredsjx -->

Create the main user-facing GitMap documentation.

**Requirements:**
- Create the main user-facing GitMap documentation.

**Work Steps:**
- [ ] 0.11.1.0.1.1 (a) Explain what GitMap does
- [ ] 0.11.1.0.1.2 (b) Explain the roadmap-first workflow
- [ ] 0.11.1.0.1.3 (c) Explain installation
- [ ] 0.11.1.0.1.4 (d) Explain basic commands
- [ ] 0.11.1.0.1.5 (e) Provide a simple first-use example

#### 0.11.1.0.2 Create Roadmap Format Guide
<!-- GitMap-ID: htredsjw -->

Create detailed documentation for writing GitMap roadmaps manually.

**Requirements:**
- Create detailed documentation for writing GitMap roadmaps manually.

**Work Steps:**
- [ ] 0.11.1.0.2.1 (a) Explain milestones
- [ ] 0.11.1.0.2.2 (b) Explain Sections
- [ ] 0.11.1.0.2.3 (c) Explain issues
- [ ] 0.11.1.0.2.4 (d) Explain sub-issues
- [ ] 0.11.1.0.2.5 (e) Explain descriptions and requirements
- [ ] 0.11.1.0.2.6 (f) Provide complete examples

#### 0.11.1.0.3 Create GitHub Setup Guide
<!-- GitMap-ID: itredsjv -->

Document how to prepare a GitHub repository for GitMap.

**Requirements:**
- Document how to prepare a GitHub repository for GitMap.

**Work Steps:**
- [ ] 0.11.1.0.3.1 (a) Explain that the user creates the repository
- [ ] 0.11.1.0.3.2 (b) Explain authentication setup
- [ ] 0.11.1.0.3.3 (c) Explain required repository permissions
- [ ] 0.11.1.0.3.4 (d) Explain how GitMap connects to the repository
- [ ] 0.11.1.0.3.5 (e) Include troubleshooting guidance

## 0.11.2 Release
<!-- GitMap-ID: avredshd -->

#### 0.11.2.0.1 Add Version Information
<!-- GitMap-ID: jtredsju -->

Provide consistent GitMap version information.

**Requirements:**
- Provide consistent GitMap version information.

**Work Steps:**
- [ ] 0.11.2.0.1.1 (a) Define the application version
- [ ] 0.11.2.0.1.2 (b) Make the version available from the command line
- [ ] 0.11.2.0.1.3 (c) Keep package and application versions consistent

#### 0.11.2.0.2 Run Release Test
<!-- GitMap-ID: ktredsjt -->

Test GitMap from a clean environment before release.

**Requirements:**
- Test GitMap from a clean environment before release.

**Work Steps:**
- [ ] 0.11.2.0.2.1 (a) Install GitMap from scratch
- [ ] 0.11.2.0.2.2 (b) Create a new roadmap
- [ ] 0.11.2.0.2.3 (c) Connect to a test repository
- [ ] 0.11.2.0.2.4 (d) Preview synchronization
- [ ] 0.11.2.0.2.5 (e) Perform synchronization
- [ ] 0.11.2.0.2.6 (f) Run synchronization again to verify duplicate prevention

#### 0.11.2.0.3 Create Version 1.0 Release
<!-- GitMap-ID: ltredsjs -->

Publish the first stable GitMap release.

**Requirements:**
- Publish the first stable GitMap release.

**Work Steps:**
- [ ] 0.11.2.0.3.1 (a) Complete all required tests
- [ ] 0.11.2.0.3.2 (b) Complete user documentation
- [ ] 0.11.2.0.3.3 (c) Confirm the roadmap-first workflow works end to end
- [ ] 0.11.2.0.3.4 (d) Tag the release as `v1.0.0`