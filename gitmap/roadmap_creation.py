from gitmap.roadmap_menus import (
    choose_numbering_mode,
    choose_roadmap_structure,
    choose_starting_series,
    explain_roadmap_numbering,
)

from gitmap.roadmap_preparation import (
    ask_project_name,
    ask_project_overview,
    collect_features,
    collect_issue_details,
    collect_issues,
    collect_milestones,
    collect_sections,
)



def start_new_roadmap():
    """Start an interactive roadmap-building session."""

    # Choose how the roadmap will be organized and numbered.
    explain_roadmap_numbering()
    numbering_mode = choose_numbering_mode()
    roadmap_structure = choose_roadmap_structure()

    starting_series = None

    if numbering_mode == "automatic":
        starting_series = choose_starting_series()

    # Collect the project name and overview.
    project_name = ask_project_name()
    project_overview = ask_project_overview()

    # Round 1: Create all milestones.
    milestones = collect_milestones(
        numbering_mode,
        starting_series,
        roadmap_structure,
    )

    # Build each milestone before moving to the next milestone.
    for milestone in milestones:
        # If Sections are used, collect them for this milestone.
        if roadmap_structure != "neither":
            milestone["sections"] = collect_sections(
                milestone,
                numbering_mode,
                roadmap_structure,
            )

            # Build each section before moving to the next section.
            for section in milestone["sections"]:
                # If Features are used, collect them for this section.
                if roadmap_structure == "sections_and_features":
                    section["features"] = collect_features(
                        section,
                        numbering_mode,
                    )

                    # Complete the Issues for each feature.
                    for feature in section["features"]:
                        feature["issues"] = collect_issues(
                            feature,
                            numbering_mode,
                        )

                # Without Features, Issues belong directly to the Section.
                else:
                    section["issues"] = collect_issues(
                        section,
                        numbering_mode,
                    )

        # Without Sections, Issues belong directly to the Milestone.
        else:
            milestone["issues"] = collect_issues(
                milestone,
                numbering_mode,
            )

    # Build and return the completed roadmap.
    return {
        "name": project_name,
        "overview": project_overview,
        "numbering_mode": numbering_mode,
        "starting_series": starting_series,
        "structure": roadmap_structure,
        "milestones": milestones,
    }