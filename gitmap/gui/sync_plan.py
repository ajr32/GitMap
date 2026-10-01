from gitmap.github_sync.hierarchy_sync import collect_hierarchy_issue_mappings
from gitmap.roadmap.comparison import compare_roadmaps
from gitmap.roadmap.traversal import (
    find_roadmap_item_by_id,
)


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
        "added_hierarchy_mappings": get_hierarchy_mappings(
            after_roadmap,
            added_hierarchy,
        ),
        "changed_hierarchy_mappings": get_hierarchy_mappings(
            after_roadmap,
            changed_hierarchy,
        ),
        "removed_ids": comparison["removed"],
    }


def get_hierarchy_mappings(roadmap, hierarchy_items):
    """Return GitHub hierarchy mappings for selected roadmap items."""

    if not hierarchy_items:
        return []

    item_ids = {item.gitmap_id for item in hierarchy_items if item.gitmap_id}

    mappings = collect_hierarchy_issue_mappings(roadmap)

    return [mapping for mapping in mappings if mapping.gitmap_id in item_ids]
