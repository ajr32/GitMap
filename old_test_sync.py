"""Tests for GitMap synchronization planning."""

from gitmap.models import Issue, Milestone, Roadmap, Section
from gitmap.sync import SyncEngine


def test_sync_plan_lists_roadmap_items():
    """The sync plan identifies milestones, Sections, and issues."""

    roadmap = Roadmap(
        name="GitMap",
        milestones=[
            Milestone(
                number="0.1",
                title="Foundations",
                Sections=[
                    Section(
                        title="Project Setup",
                        issues=[
                            Issue(
                                number="0.1.1",
                                title="Create Python Project",
                            )
                        ],
                    )
                ],
            )
        ],
    )

    result = SyncEngine(roadmap).plan()

    assert result.successful
    assert "Milestone: 0.1 Foundations" in result.created
    assert "Section: Project Setup" in result.created
    assert "Issue: 0.1.1 Create Python Project" in result.created


def test_sync_plan_starts_empty_for_empty_roadmap():
    """An empty roadmap produces an empty synchronization plan."""

    roadmap = Roadmap(name="GitMap")

    result = SyncEngine(roadmap).plan()

    assert result.successful
    assert result.created == []
