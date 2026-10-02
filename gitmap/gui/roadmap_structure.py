# =============================================================================
# GITMAP roadmap_structure.py ROAD MAP
# =============================================================================
# Stable navigation labels:
#
#   Part A   - Restore/infer structure settings for an existing parsed Roadmap
#     A1     - Detect Sections
#     A2     - Restore/infer Issues directly under Sections
#     A3     - Detect Features
#     A4     - Restore/infer Issues directly under Features
#
# Existing Part labels are STABLE. If code is inserted later, use A5, A2A,
# etc. Do not renumber/reletter existing Parts unless we explicitly decide to
# refactor this navigation scheme.
#
# WHY THIS FILE EXISTS:
# A brand-new Roadmap gets its structure settings from the Structure Dialog.
# An EXISTING Markdown roadmap needs those settings reconstructed after parsing.
#
# GitMap already persists Section/Feature tracking choices in
# roadmap.github_representation. Those explicit settings are authoritative when
# present. Content inference is retained only as a compatibility fallback for
# older roadmaps that do not contain the representation metadata.
# =============================================================================


def _representation_allows_issues(representation, hierarchy_type):
    """Return whether explicit representation permits child Issues.

    None means there is no explicit setting for this hierarchy type and the
    caller should fall back to inference from existing content.
    """

    if not isinstance(representation, dict):
        return None

    if hierarchy_type not in representation:
        return None

    return representation.get(hierarchy_type) in ("issue", "both")


# =============================================================================
# PART A — RESTORE/INFER STRUCTURE SETTINGS FROM AN EXISTING ROADMAP
# =============================================================================
def infer_roadmap_structure(roadmap):
    """Restore explicit structure settings, falling back to content inference."""

    representation = getattr(roadmap, "github_representation", None)

    # -------------------------------------------------------------------------
    # PART A1 — DETECT SECTIONS
    # -------------------------------------------------------------------------
    roadmap.use_sections = any(
        milestone.sections
        for milestone in roadmap.milestones
    )

    # -------------------------------------------------------------------------
    # PART A2 — RESTORE/INFER ISSUES DIRECTLY UNDER SECTIONS
    # -------------------------------------------------------------------------
    section_permission = _representation_allows_issues(
        representation,
        "section",
    )

    if section_permission is None:
        # Compatibility fallback for older roadmaps without persisted settings.
        section_permission = any(
            section.issues
            for milestone in roadmap.milestones
            for section in milestone.sections
        )

    roadmap.allow_issues_under_sections = (
        roadmap.use_sections and section_permission
    )

    # -------------------------------------------------------------------------
    # PART A3 — DETECT FEATURES
    # -------------------------------------------------------------------------
    roadmap.use_features = any(
        section.features
        for milestone in roadmap.milestones
        for section in milestone.sections
    )

    # -------------------------------------------------------------------------
    # PART A4 — RESTORE/INFER ISSUES DIRECTLY UNDER FEATURES
    # -------------------------------------------------------------------------
    feature_permission = _representation_allows_issues(
        representation,
        "feature",
    )

    if feature_permission is None:
        # Compatibility fallback for older roadmaps without persisted settings.
        feature_permission = any(
            feature.issues
            for milestone in roadmap.milestones
            for section in milestone.sections
            for feature in section.features
        )

    roadmap.allow_issues_under_features = (
        roadmap.use_features and feature_permission
    )
