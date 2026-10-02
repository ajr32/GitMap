# def get_existing_issues(repository, roadmap=None):
#     """Retrieve GitMap-managed issues from a GitHub repository."""
#
#     issues = [
#         issue
#         for issue in repository.get_issues(state="all")
#         if is_gitmap_managed_issue(issue)
#     ]
#
#     if roadmap is None:
#         return issues
#
#     roadmap_label = f"GitMap: {roadmap.name}"
#
#     return [
#         issue
#         for issue in issues
#         if any(
#             label.name.casefold() == roadmap_label.casefold() for label in issue.labels
#         )
#     ]
#
# def has_existing_gitmap_issues(repository):
#     """Return whether the repository already contains synchronized GitMap issues."""
#
#     return bool(get_existing_issues(repository))
#
# def get_gitmap_id_from_github_issue(issue) -> str:
#     """Return the permanent GitMap ID stored in a GitHub issue body."""
#
#     body = issue.body or ""
#
#     for line in body.splitlines():
#         if line.startswith("GitMap-ID:"):
#             return line.removeprefix("GitMap-ID:").strip()
#
#     return ""
#
# def find_all_existing_issue_matches(mapping, existing_issues):
#     """Return all GitHub issues that could represent a GitMap mapping."""
#
#     matches = []
#
#     for issue in existing_issues:
#         body = issue.body or ""
#
#         gitmap_id = get_gitmap_id_from_github_issue(issue)
#
#         id_matches = mapping.gitmap_id and gitmap_id == mapping.gitmap_id
#
#         number_matches = any(
#             line.strip() == f"GitMap: {mapping.number}" for line in body.splitlines()
#         )
#
#         if id_matches or number_matches:
#             matches.append(issue)
#
#     return matches
#
# def classify_existing_issue(mapping, existing_issues):
#     """Classify a GitMap mapping as existing, missing, or conflicting."""
#
#     matches = find_all_existing_issue_matches(
#         mapping,
#         existing_issues,
#     )
#
#     if not matches:
#         return "missing", []
#
#     if len(matches) == 1:
#         return "existing", matches
#
#     return "conflict", matches
#
# def find_existing_issue_by_gitmap_id(mapping, existing_issues):
#     """Find an existing GitHub issue by permanent GitMap ID."""
#
#     if not mapping.gitmap_id:
#         return None
#
#     for issue in existing_issues:
#         if get_gitmap_id_from_github_issue(issue) == mapping.gitmap_id:
#             return issue
#
#     return None
#
# def find_existing_issue(mapping, existing_issues):
#     """Find an existing GitHub issue by permanent ID or roadmap number."""
#
#     existing = find_existing_issue_by_gitmap_id(
#         mapping,
#         existing_issues,
#     )
#
#     if existing is not None:
#         return existing
#
#     # Backward-compatible fallback for roadmaps that have not
#     # yet been migrated to permanent GitMap IDs.
#     marker = f"GitMap: {mapping.number}"
#
#     for issue in existing_issues:
#         for line in (issue.body or "").splitlines():
#             if line.strip() == marker:
#                 return issue
#     return None
#
# ---
#
# def build_hierarchy_issue_body(mapping):
#     """Build the body for a Section or Feature GitHub Issue."""
#
#     body = mapping.description.strip()
#
#     if mapping.gitmap_id:
#         body += f"\n\nGitMap-ID: {mapping.gitmap_id}"
#
#     body += f"\nGitMap: {mapping.number}"
#     body += f"\nGitMap-Type: {mapping.hierarchy_type}"
#
#     return body
#
#
# def create_hierarchy_issue(repository, mapping, milestone, labels=None):
#     """Create a GitHub Issue representing a Section or Feature."""
#
#     return repository.create_issue(
#         title=mapping.title,
#         body=build_hierarchy_issue_body(mapping),
#         milestone=milestone,
#         labels=labels or [],
#     )
#
#
# def sync_hierarchy_issue(
#     repository,
#     mapping,
#     expected_operation=None,
#     roadmap=None,
# ):
#     """Create or update a Section or Feature GitHub Issue."""
#
#     existing_issues = get_existing_issues(repository)
#     existing = find_existing_issue(mapping, existing_issues)
#
#     if expected_operation == "update" and existing is None:
#         raise RuntimeError(
#             f"Approved hierarchy update no longer exists: {mapping.title}"
#         )
#
#     if expected_operation == "create" and existing is not None:
#         raise RuntimeError(
#             f"Approved hierarchy create became an update: {mapping.title}"
#         )
#
#     milestones = get_existing_milestones(repository)
#
#     milestone_mapping = MilestoneMapping(
#         number=mapping.number,
#         title=mapping.milestone,
#     )
#
#     milestone = find_existing_milestone(
#         milestone_mapping,
#         milestones,
#     )
#
#     labels = []
#
#     if roadmap is not None:
#         labels.append(f"GitMap: {roadmap.name}")
#
#     if existing:
#         existing.edit(
#             title=mapping.title,
#             body=build_hierarchy_issue_body(mapping),
#             milestone=milestone,
#             labels=labels,
#         )
#         return existing, False
#
#     issue = create_hierarchy_issue(
#         repository,
#         mapping,
#         milestone,
#         labels=labels,
#     )
#
#     return issue, True
#
#
# def sync_hierarchy_issues(
#     repository,
#     roadmap,
#     mappings=None,
#     expected_operation=None,
#     progress_start=0,
#     progress_total=None,
#     progress_callback=None,
# ):
#     """Synchronize Section and Feature hierarchy issues."""
#
#     if mappings is None:
#         mappings = collect_hierarchy_issue_mappings(roadmap)
#
#     if progress_total is None:
#         progress_total = progress_start + len(mappings)
#
#     progress = progress_start
#
#     results = []
#
#     for mapping in mappings:
#         progress += 1
#
#         action = (
#             "Updating"
#             if expected_operation == "update"
#             else "Creating"
#             if expected_operation == "create"
#             else "Synchronizing"
#         )
#
#         if progress_callback is not None:
#             progress_callback(
#                 "Hierarchy Issues",
#                 progress - progress_start,
#                 progress_total - progress_start,
#                 f"{action} {mapping.title}",
#             )
#
#         result, created = sync_hierarchy_issue(
#             repository,
#             mapping,
#             expected_operation=expected_operation,
#             roadmap=roadmap,
#         )
#         results.append((result, created))
#
#     return results
#
#
#
# def collect_hierarchy_issue_mappings(roadmap):
#     """Collect Section and Feature hierarchy issues."""
#
#     mappings = []
#
#     use_sections = should_use_section_issue(roadmap)
#     use_features = should_use_feature_issue(roadmap)
#
#     for milestone in roadmap.milestones:
#         for section in milestone.sections:
#             if use_sections:
#                 mappings.append(
#                     map_section_issue(
#                         section,
#                         milestone,
#                         roadmap.hierarchy_issue_title_style,
#                     )
#                 )
#
#             if use_features:
#                 for feature in section.features:
#                     mappings.append(
#                         map_feature_issue(
#                             feature,
#                             milestone,
#                             section,
#                             roadmap.hierarchy_issue_title_style,
#                         )
#                     )
#
#     return mappings
#
# def classify_hierarchy_issues(roadmap, existing_issues):
#     """Classify requested hierarchy issues as existing, missing, or conflicting."""
#
#     results = {
#         "existing": [],
#         "missing": [],
#         "conflicts": [],
#     }
#
#     for mapping in collect_hierarchy_issue_mappings(roadmap):
#         status, matches = classify_existing_issue(
#             mapping,
#             existing_issues,
#         )
#
#         entry = {
#             "mapping": mapping,
#             "matches": matches,
#         }
#
#         if status == "conflict":
#             results["conflicts"].append(entry)
#         else:
#             results[status].append(entry)
#
#     return results
#
# def sync_existing_roadmap_hierarchy_issues(
#     repository,
#     roadmap,
#     roadmap_path=None,
# ):
#     """Handle hierarchy Issues safely for an existing synchronized roadmap."""
#
#     if not has_explicit_github_representation(roadmap):
#         roadmap_structure = getattr(
#             roadmap,
#             "structure",
#             "sections_and_features",
#         )
#
#         roadmap.github_representation = choose_github_representation(roadmap_structure)
#
#         if roadmap_path is not None:
#             write_github_representation_to_roadmap(
#                 roadmap_path,
#                 roadmap,
#             )
#
#     existing_issues = get_existing_issues(repository)
#
#     classifications = classify_hierarchy_issues(
#         roadmap,
#         existing_issues,
#     )
#
#     counts = count_hierarchy_classifications(
#         classifications,
#     )
#
#     display_hierarchy_classifications(counts)
#
#     if not confirm_missing_hierarchy_issues(counts):
#         return []
#
#     missing_mappings = [entry["mapping"] for entry in classifications["missing"]]
#
#     return sync_hierarchy_issues(
#         repository,
#         roadmap,
#         mappings=missing_mappings,
#         expected_operation="create",
#     )
#
from gitmap.github_sync import state_reconstruction

# def is_gitmap_managed_issue(issue):
#     """Return True if the GitHub issue is managed by GitMap."""
#
#     body = issue.body or ""
#
#     return "GitMap-ID:" in body or "GitMap:" in body

# def count_hierarchy_classifications(classifications):
#     """Count Section and Feature hierarchy issue classifications."""
#
#     counts = {
#         "existing": {
#             "section": 0,
#             "feature": 0,
#         },
#         "missing": {
#             "section": 0,
#             "feature": 0,
#         },
#         "conflicts": {
#             "section": 0,
#             "feature": 0,
#         },
#     }
#
#     for status, entries in classifications.items():
#         for entry in entries:
#             mapping = entry["mapping"]
#             issue_type = mapping.hierarchy_type
#
#             if issue_type in ("section", "feature"):
#                 counts[status][issue_type] += 1
#
#     return counts


# def display_hierarchy_classifications(counts):
#     """Display hierarchy Issue status for an existing roadmap."""
#
#     print()
#     print("Hierarchy Issues")
#     print()
#
#     print("Existing:")
#     print(f"  Sections: {counts['existing']['section']}")
#     print(f"  Features: {counts['existing']['feature']}")
#     print()
#
#     print("Missing:")
#     print(f"  Sections: {counts['missing']['section']}")
#     print(f"  Features: {counts['missing']['feature']}")
#     print()
#
#     print("Conflicts:")
#     print(f"  Sections: {counts['conflicts']['section']}")
#     print(f"  Features: {counts['conflicts']['feature']}")
#
#
# def confirm_missing_hierarchy_issues(counts):
#     """Ask whether missing hierarchy Issues should be created."""
#
#     missing_sections = counts["missing"]["section"]
#     missing_features = counts["missing"]["feature"]
#
#     total_missing = missing_sections + missing_features
#
#     if total_missing == 0:
#         return False
#
#     print()
#     response = (
#         input(f"Create the {total_missing} missing hierarchy Issues? [(y)es/(n)o]: ")
#         .strip()
#         .lower()
#     )
#
#     return response in ("y", "yes")
#
#
# def detect_changed_hierarchy_issues(roadmap, existing_issues):
#     """Return existing Section and Feature issues that differ from the roadmap."""
#
#     changed = []
#
#     for mapping in collect_hierarchy_issue_mappings(roadmap):
#         existing = find_existing_issue(mapping, existing_issues)
#
#         if existing is None:
#             continue
#
#         expected_body = build_hierarchy_issue_body(mapping)
#
#         changes = []
#
#         if existing.title != mapping.title:
#             changes.append("title")
#
#         if (existing.body or "").strip() != expected_body.strip():
#             changes.append("body")
#
#         if changes:
#             changed.append(
#                 {
#                     "mapping": mapping,
#                     "github_issue": existing,
#                     "changes": changes,
#                 }
#             )
#
#     return changed


# def apply_roadmap_label_to_existing_issues(repository, roadmap):
#     """Apply the roadmap-specific label to existing roadmap Issues."""
#
#     existing_issues = get_existing_issues(repository)
#
#     for milestone in roadmap.milestones:
#         issue_locations = [(issue, None, None) for issue in milestone.issues]
#
#         for section in milestone.sections:
#             issue_locations.extend((issue, section, None) for issue in section.issues)
#
#             for feature in section.features:
#                 issue_locations.extend(
#                     (issue, section, feature) for issue in feature.issues
#                 )
#
#         for issue, section, feature in issue_locations:
#             mapping = map_issue(
#                 issue,
#                 milestone,
#                 section,
#                 feature,
#                 roadmap=roadmap,
#             )
#
#             existing = find_existing_issue(
#                 mapping,
#                 existing_issues,
#             )
#
#             if existing is None:
#                 continue
#
#             roadmap_label = f"GitMap: {roadmap.name}"
#
#             if any(
#                 label.name.casefold() == roadmap_label.casefold()
#                 for label in existing.labels
#             ):
#                 continue
#
#             existing.add_to_labels(roadmap_label)
#

#state_reconstruction.py

# def rebuild_roadmap_state(repository, roadmap):
#     """Rebuild GitMap project state from existing GitHub data."""
#
#     existing_issues = get_existing_issues(repository)
#
#     return {
#         "milestones": associate_issues_with_milestones(existing_issues),
#         "sections": associate_issues_with_sections(existing_issues, roadmap),
#         "features": associate_issues_with_features(existing_issues, roadmap),
#         "work_steps": restore_work_step_relationships(existing_issues),
#         "unmatched": find_unmatched_roadmap_items(roadmap, existing_issues),
#     }
