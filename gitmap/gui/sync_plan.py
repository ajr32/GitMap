from gitmap.mapping_mod.mapping_issues import collect_hierarchy_issue_mappings
from gitmap.roadmap_traversal import (
    iter_roadmap_features,
    iter_roadmap_issues,
    iter_roadmap_sections,
)


def collect_roadmap_items(roadmap):
    """Collect GitMap-managed roadmap items for change comparison."""

    items = {}

    for section, milestone in iter_roadmap_sections(roadmap):
        milestone_parent_id = f"milestone:{milestone.number}:{milestone.title}"

        if section.gitmap_id:
            items[section.gitmap_id] = {
                "type": "section",
                "number": section.number,
                "title": section.title,
                "parent_id": milestone_parent_id,
            }

    for feature, _, section in iter_roadmap_features(roadmap):
        if feature.gitmap_id:
            items[feature.gitmap_id] = {
                "type": "feature",
                "number": feature.number,
                "title": feature.title,
                "parent_id": section.gitmap_id,
            }

    for issue, milestone, section, feature in iter_roadmap_issues(roadmap):
        if not issue.gitmap_id:
            continue

        if feature is not None:
            parent_id = feature.gitmap_id
        elif section is not None:
            parent_id = section.gitmap_id
        else:
            parent_id = f"milestone:{milestone.number}:{milestone.title}"

        items[issue.gitmap_id] = {
            "type": "issue",
            "number": issue.number,
            "title": issue.title,
            "parent_id": parent_id,
        }

    return items


def compare_roadmaps(before_roadmap, after_roadmap):
    """Compare two roadmap states using permanent GitMap IDs."""

    before_items = collect_roadmap_items(before_roadmap)
    after_items = collect_roadmap_items(after_roadmap)

    added_ids = set(after_items) - set(before_items)
    removed_ids = set(before_items) - set(after_items)
    common_ids = set(before_items) & set(after_items)

    renumbered_ids = {
        item_id
        for item_id in common_ids
        if before_items[item_id]["number"] != after_items[item_id]["number"]
    }

    retitled_ids = {
        item_id
        for item_id in common_ids
        if before_items[item_id]["title"] != after_items[item_id]["title"]
    }

    hierarchy_ids = {
        item_id
        for item_id in common_ids
        if before_items[item_id]["parent_id"] != after_items[item_id]["parent_id"]
    }

    unchanged_ids = {
        item_id
        for item_id in common_ids
        if before_items[item_id]["number"] == after_items[item_id]["number"]
        and before_items[item_id]["title"] == after_items[item_id]["title"]
        and before_items[item_id]["parent_id"] == after_items[item_id]["parent_id"]
    }

    return {
        "before_items": before_items,
        "after_items": after_items,
        "added": added_ids,
        "removed": removed_ids,
        "renumbered": renumbered_ids,
        "retitled": retitled_ids,
        "hierarchy": hierarchy_ids,
        "unchanged": unchanged_ids,
    }


def find_roadmap_item_by_id(roadmap, gitmap_id):
    """Find a roadmap object by its permanent GitMap ID."""

    for issue, _, _, _ in iter_roadmap_issues(roadmap):
        if issue.gitmap_id == gitmap_id:
            return issue

    for section, _ in iter_roadmap_sections(roadmap):
        if section.gitmap_id == gitmap_id:
            return section

    for feature, _, _ in iter_roadmap_features(roadmap):
        if feature.gitmap_id == gitmap_id:
            return feature

    return None


def build_sync_plan(before_roadmap, after_roadmap):
    """Build the roadmap-object plan needed for GitHub synchronization."""

    comparison = compare_roadmaps(
        before_roadmap,
        after_roadmap,
    )

    changed_ids = (
        comparison["renumbered"] | comparison["retitled"] | comparison["hierarchy"]
    )

    added_issues = []
    changed_issues = []

    added_hierarchy = []
    changed_hierarchy = []

    for item_id in comparison["added"]:
        item = find_roadmap_item_by_id(
            after_roadmap,
            item_id,
        )

        if item is None:
            continue

        item_type = comparison["after_items"][item_id]["type"]

        if item_type == "issue":
            added_issues.append(item)
        elif item_type in ("section", "feature"):
            added_hierarchy.append(item)

    for item_id in changed_ids:
        item = find_roadmap_item_by_id(
            after_roadmap,
            item_id,
        )

        if item is None:
            continue

        item_type = comparison["after_items"][item_id]["type"]

        if item_type == "issue":
            changed_issues.append(item)
        elif item_type in ("section", "feature"):
            changed_hierarchy.append(item)

    return {
        "added_issues": added_issues,
        "changed_issues": changed_issues,
        "added_hierarchy": added_hierarchy,
        "changed_hierarchy": changed_hierarchy,
        "removed_ids": comparison["removed"],
    }


def get_hierarchy_mappings(roadmap, hierarchy_items):
    """Return GitHub hierarchy mappings for selected roadmap items."""

    if not hierarchy_items:
        return []

    item_ids = {item.gitmap_id for item in hierarchy_items if item.gitmap_id}

    mappings = collect_hierarchy_issue_mappings(roadmap)

    return [mapping for mapping in mappings if mapping.gitmap_id in item_ids]
