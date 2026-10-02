def iter_roadmap_issues(roadmap):
    """Yield every roadmap issue with its structural context."""

    for milestone in roadmap.milestones:
        for issue in getattr(milestone, "issues", []):
            yield issue, milestone, None, None

        for section in getattr(milestone, "sections", []):
            for issue in getattr(section, "issues", []):
                yield issue, milestone, section, None

            for feature in getattr(section, "features", []):
                for issue in getattr(feature, "issues", []):
                    yield issue, milestone, section, feature


def iter_roadmap_sections(roadmap):
    """Yield every section with its parent milestone."""

    for milestone in roadmap.milestones:
        for section in milestone.sections:
            yield section, milestone


def iter_roadmap_features(roadmap):
    """Yield every feature with its parent milestone and section."""

    for milestone in roadmap.milestones:
        for section in milestone.sections:
            for feature in section.features:
                yield feature, milestone, section


def iter_work_steps(work_steps):
    """Yield every work step, including nested work steps."""

    for work_step in work_steps:
        yield work_step
        yield from iter_work_steps(work_step.work_steps)


def iter_roadmap_work_steps(roadmap):
    """Yield every work step with its issue and structural context."""

    for issue, milestone, section, feature in iter_roadmap_issues(roadmap):
        for work_step in iter_work_steps(issue.work_steps):
            yield work_step, issue, milestone, section, feature


def find_roadmap_item_by_id(roadmap, gitmap_id):
    """Return the roadmap item with the given permanent GitMap ID."""

    if not gitmap_id:
        return None

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
