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
