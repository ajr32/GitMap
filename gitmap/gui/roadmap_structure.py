# =============================================================================
# GITMAP roadmap_structure.py ROAD MAP
# =============================================================================
# Stable navigation labels:
#
#   Part A   - Infer structure settings for an existing parsed Roadmap
#     A1     - Detect Sections
#     A2     - Detect Issues directly under Sections
#     A3     - Detect Features
#     A4     - Detect Issues directly under Features
#
# Existing Part labels are STABLE. If code is inserted later, use A5, A2A,
# etc. Do not renumber/reletter existing Parts unless we explicitly decide to
# refactor this navigation scheme.
#
# WHY THIS FILE EXISTS:
# A brand-new Roadmap gets its structure settings from the Structure Dialog.
# An EXISTING Markdown roadmap may not have those questionnaire answers
# available, so GitMap examines the hierarchy that the parser actually found
# and reconstructs the relevant structure flags.
#
# IMPORTANT LIMITATION:
# This is inference from EXISTING CONTENT. If a structure is allowed but has
# never actually been used in the Markdown yet, this function cannot discover
# that permission from absence alone. Persistent metadata could solve that in
# the future if needed.
# =============================================================================

# =============================================================================
# PART A — INFER STRUCTURE SETTINGS FROM AN EXISTING ROADMAP
# =============================================================================
# Called after parse_roadmap() opens an existing Markdown roadmap.
#
# This function updates four Roadmap flags:
#   use_sections
#   allow_issues_under_sections
#   use_features
#   allow_issues_under_features
#
# `any(...)` means: scan the relevant hierarchy and set the flag True as soon
# as at least one matching child collection contains something.
# =============================================================================
def infer_roadmap_structure(roadmap):
    """Infer structure settings from an existing parsed roadmap."""

    # -------------------------------------------------------------------------
    # PART A1 — DETECT SECTIONS
    # -------------------------------------------------------------------------
    # If ANY Milestone contains at least one Section, this roadmap uses the
    # Section level.
    # -------------------------------------------------------------------------
    roadmap.use_sections = any(milestone.sections for milestone in roadmap.milestones)

    # -------------------------------------------------------------------------
    # PART A2 — DETECT ISSUES DIRECTLY UNDER SECTIONS
    # -------------------------------------------------------------------------
    # Walk every Section under every Milestone. If at least one Section has an
    # Issue directly attached to it, remember that this hierarchy is in use.
    #
    # This is different from Issues underneath Features.
    # -------------------------------------------------------------------------
    roadmap.allow_issues_under_sections = any(
        section.issues
        for milestone in roadmap.milestones
        for section in milestone.sections
    )

    # -------------------------------------------------------------------------
    # PART A3 — DETECT FEATURES
    # -------------------------------------------------------------------------
    # Walk every Section. If any Section contains Features, the Roadmap uses
    # the Feature hierarchy level.
    # -------------------------------------------------------------------------
    roadmap.use_features = any(
        section.features
        for milestone in roadmap.milestones
        for section in milestone.sections
    )

    # -------------------------------------------------------------------------
    # PART A4 — DETECT ISSUES DIRECTLY UNDER FEATURES
    # -------------------------------------------------------------------------
    # Walk every Feature under every Section/Milestone. If at least one
    # Feature contains Issues, remember that Feature -> Issue hierarchy is in
    # use.
    #
    # The Add UI later consults these inferred flags when deciding which item
    # types should be offered for an existing roadmap.
    # -------------------------------------------------------------------------
    roadmap.allow_issues_under_features = any(
        feature.issues
        for milestone in roadmap.milestones
        for section in milestone.sections
        for feature in section.features
    )
