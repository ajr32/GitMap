from gitmap.roadmap.model.traversal import (
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
