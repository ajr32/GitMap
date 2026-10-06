from dataclasses import dataclass, field
from typing import Any

from gitmap.github_sync.issues.github_representation import map_issue
from gitmap.github_sync.issues.hierarchy_sync import collect_hierarchy_issue_mappings
from gitmap.github_sync.issues.issue_comparison import (
    hierarchy_issue_has_changes,
    issue_has_changes,
)
from gitmap.github_sync.issues.issue_lookup import find_existing_issue
from gitmap.roadmap.model.traversal import find_roadmap_item_by_id, iter_roadmap_issues
from gitmap.roadmap.structure.comparison import compare_roadmaps


@dataclass
class SyncPlan:
    """Structured description of the work intended for one GitHub sync."""

    added_issues: list[Any] = field(default_factory=list)
    changed_issues: list[Any] = field(default_factory=list)
    removed_issues: list[str] = field(default_factory=list)

    added_hierarchy: list[Any] = field(default_factory=list)
    changed_hierarchy: list[Any] = field(default_factory=list)
    removed_hierarchy: list[str] = field(default_factory=list)

    added_hierarchy_mappings: list[Any] = field(default_factory=list)
    changed_hierarchy_mappings: list[Any] = field(default_factory=list)

    relationship_additions: list[Any] = field(default_factory=list)
    relationship_removals: list[Any] = field(default_factory=list)
    relationship_reparents: list[Any] = field(default_factory=list)

    labels_to_create: list[Any] = field(default_factory=list)
    milestones_to_create: list[Any] = field(default_factory=list)

    def __getitem__(self, key):
        """Keep existing callers working while they migrate to attributes."""
        return getattr(self, key)

    def get(self, key, default=None):
        """Provide dict-like access during the SyncPlan migration."""
        return getattr(self, key, default)

    @property
    def total_operations(self):
        """Return the number of concrete operations currently represented."""
        return sum(
            len(items)
            for items in (
                self.added_issues,
                self.changed_issues,
                self.removed_issues,
                self.added_hierarchy_mappings,
                self.changed_hierarchy_mappings,
                self.removed_hierarchy,
                self.relationship_additions,
                self.relationship_removals,
                self.relationship_reparents,
                self.labels_to_create,
                self.milestones_to_create,
            )
        )


def build_sync_plan(before_roadmap, after_roadmap):
    """Build the structured roadmap plan needed for GitHub synchronization.

    This phase describes changes that can be determined from the two roadmap
    states. GitHub-state-dependent work (relationship reconciliation, labels,
    and milestones) has explicit places on SyncPlan and can be populated by
    later planning phases without changing the plan's public shape.
    """

    comparison = compare_roadmaps(
        before_roadmap,
        after_roadmap,
    )

    changed_ids = (
        comparison["renumbered"] | comparison["retitled"] | comparison["hierarchy"]
    )

    plan = SyncPlan()

    for item_id in comparison["added"]:
        item = find_roadmap_item_by_id(
            after_roadmap,
            item_id,
        )

        if item is None:
            continue

        item_type = comparison["after_items"][item_id]["type"]

        if item_type == "issue":
            plan.added_issues.append(item)
        elif item_type in ("section", "feature"):
            plan.added_hierarchy.append(item)

    for item_id in changed_ids:
        item = find_roadmap_item_by_id(
            after_roadmap,
            item_id,
        )

        if item is None:
            continue

        item_type = comparison["after_items"][item_id]["type"]

        if item_type == "issue":
            plan.changed_issues.append(item)
        elif item_type in ("section", "feature"):
            plan.changed_hierarchy.append(item)

    for item_id in comparison["removed"]:
        before_item = comparison["before_items"].get(item_id)

        if before_item is None:
            continue

        item_type = before_item["type"]

        if item_type == "issue":
            plan.removed_issues.append(item_id)
        elif item_type in ("section", "feature"):
            plan.removed_hierarchy.append(item_id)

    plan.added_hierarchy_mappings = get_hierarchy_mappings(
        after_roadmap,
        plan.added_hierarchy,
    )
    plan.changed_hierarchy_mappings = get_hierarchy_mappings(
        after_roadmap,
        plan.changed_hierarchy,
    )

    return plan


def get_hierarchy_mappings(roadmap, hierarchy_items):
    """Return GitHub hierarchy mappings for selected roadmap items."""

    if not hierarchy_items:
        return []

    item_ids = {item.gitmap_id for item in hierarchy_items if item.gitmap_id}

    mappings = collect_hierarchy_issue_mappings(roadmap)

    return [mapping for mapping in mappings if mapping.gitmap_id in item_ids]


def build_remote_sync_plan(roadmap, existing_issues):
    """Build a synchronization plan from the roadmap and actual GitHub state."""

    plan = SyncPlan()

    roadmap_ids = set()

    # Ordinary roadmap issues.
    for issue, milestone, section, feature in iter_roadmap_issues(roadmap):
        if issue.gitmap_id:
            roadmap_ids.add(issue.gitmap_id)

        mapping = map_issue(
            issue,
            milestone,
            section,
            feature,
            roadmap=roadmap,
        )

        existing = find_existing_issue(
            mapping,
            existing_issues,
        )

        if existing is None:
            plan.added_issues.append(issue)
        elif issue_has_changes(mapping, existing):
            plan.changed_issues.append(issue)

    # Section / Feature hierarchy issues.
    hierarchy_mappings = collect_hierarchy_issue_mappings(roadmap)

    for mapping in hierarchy_mappings:
        if mapping.gitmap_id:
            roadmap_ids.add(mapping.gitmap_id)

        existing = find_existing_issue(
            mapping,
            existing_issues,
        )

        if existing is None:
            plan.added_hierarchy_mappings.append(mapping)
        elif hierarchy_issue_has_changes(mapping, existing, roadmap):
            plan.changed_hierarchy_mappings.append(mapping)

    # Anything GitMap manages remotely that no longer exists in the roadmap
    # is a removal candidate.
    for github_issue in existing_issues:
        body = github_issue.body or ""

        gitmap_id = ""

        for line in body.splitlines():
            if line.startswith("GitMap-ID:"):
                gitmap_id = line.removeprefix("GitMap-ID:").strip()
                break

        if not gitmap_id or gitmap_id in roadmap_ids:
            continue

        if "GitMap-Type: section" in body or "GitMap-Type: feature" in body:
            plan.removed_hierarchy.append(gitmap_id)
        else:
            plan.removed_issues.append(gitmap_id)

    return plan


def build_initial_sync_plan(roadmap):
    """Build a SyncPlan for a roadmap with no existing managed GitHub Issues."""

    plan = SyncPlan()

    for milestone in roadmap.milestones:
        plan.added_issues.extend(milestone.issues)

        for section in milestone.sections:
            plan.added_issues.extend(section.issues)

            for feature in section.features:
                plan.added_issues.extend(feature.issues)

    plan.added_hierarchy_mappings = collect_hierarchy_issue_mappings(roadmap)

    return plan
