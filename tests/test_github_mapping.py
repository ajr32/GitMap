from types import SimpleNamespace

from gitmap.github_mapping import (
    detect_removed_roadmap_items,
    summarize_roadmap_differences,
)
from gitmap.mapping_mod.issues import sync_issue


def test_summarize_roadmap_differences():
    issue_new = SimpleNamespace(
        number="0.1.1",
        title="New Issue",
        description="New description",
        requirements=[],
        work_steps=[],
        gitmap_id="newissue",
    )

    issue_matching = SimpleNamespace(
        number="0.1.2",
        title="Matching Issue",
        description="Matching description",
        requirements=[],
        work_steps=[],
        gitmap_id="matching1",
    )

    issue_changed = SimpleNamespace(
        number="0.1.3",
        title="Changed Issue",
        description="Changed description",
        requirements=[],
        work_steps=[],
        gitmap_id="changed1",
    )

    section = SimpleNamespace(
        title="Test Section",
        issues=[issue_new, issue_matching, issue_changed],
        gitmap_id="",
    )

    milestone = SimpleNamespace(
        number="0.1",
        title="Test Milestone",
        sections=[section],
        gitmap_id="",
    )

    roadmap = SimpleNamespace(
        milestones=[milestone],
        gitmap_id="",
    )

    existing_issues = [
        SimpleNamespace(
            title="0.1.2 Matching Issue",
            body=(
                "Matching description\n"
                "GitMap-ID: matching1\n"
                "GitMap: 0.1.2"
            ),
            state="open",
        ),
        SimpleNamespace(
            title="0.1.3 Changed Issue",
            body=(
                "Old description\n"
                "GitMap-ID: changed1\n"
                "GitMap: 0.1.3"
            ),
            state="open",
        ),
    ]

    differences = summarize_roadmap_differences(
        roadmap,
        existing_issues,
    )

    assert [issue.number for issue in differences["new"]] == ["0.1.1"]
    assert [issue.number for issue in differences["changed"]] == ["0.1.3"]
    assert [issue.number for issue in differences["matching"]] == ["0.1.2"]


def test_sync_issue_updates_existing_issue_without_recreating(monkeypatch):
    class FakeIssue:
        def __init__(self):
            self.number = 42
            self.body = "Old body\nGitMap: 0.1.1"
            self.title = "Old Title"
            self.edited = False

        def edit(self, **kwargs):
            self.edited = True
            self.title = kwargs["title"]
            self.body = kwargs["body"]

    existing_issue = FakeIssue()

    class FakeRepository:
        def get_issues(self, state="all"):
            return [existing_issue]

        def get_milestones(self):
            return []

        def get_labels(self):
            return []

    mapping = SimpleNamespace(
        number="0.1.1",
        title="Updated Title",
        description="Updated description",
        requirements=[],
        milestone="0.1 Test",
        labels=[],
        work_steps=[],
        gitmap_id="",
    )

    monkeypatch.setattr(
        "gitmap.mapping_mod.issues.resolve_issue_targets",
        lambda repository, mapping: (None, []),
    )

    result, created = sync_issue(FakeRepository(), mapping)

    assert created is False
    assert result.number == 42
    assert result.edited is True
    assert result.title == "Updated Title"
    assert "Updated description" in result.body


def test_detect_removed_roadmap_items():
    roadmap_issue = SimpleNamespace(
        number="0.1.1",
        gitmap_id="still-here",
    )

    section = SimpleNamespace(
        issues=[roadmap_issue],
        gitmap_id="",
    )

    milestone = SimpleNamespace(
        sections=[section],
        gitmap_id="",
    )

    roadmap = SimpleNamespace(
        milestones=[milestone],
        gitmap_id="",
    )

    existing_issue = SimpleNamespace(
        number=42,
        title="Removed Issue",
        body="Old description\nGitMap-ID: removed-id\nGitMap: 0.1.2",
        state="open",
    )

    removed = detect_removed_roadmap_items(
        roadmap,
        [existing_issue],
    )

    assert removed == [existing_issue]
