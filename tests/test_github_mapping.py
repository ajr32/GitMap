from types import SimpleNamespace

from gitmap.github_mapping import (
    detect_removed_roadmap_items,
    summarize_roadmap_differences,
    sync_issue,
)


def test_summarize_roadmap_differences():
    issue_new = SimpleNamespace(
        number="0.1.1",
        title="New Issue",
        description="New description",
        requirements=[],
        work_steps=[],
    )

    issue_matching = SimpleNamespace(
        number="0.1.2",
        title="Matching Issue",
        description="Matching description",
        requirements=[],
        work_steps=[],
    )

    issue_changed = SimpleNamespace(
        number="0.1.3",
        title="Changed Issue",
        description="Changed description",
        requirements=[],
        work_steps=[],
    )

    section = SimpleNamespace(
        title="Test Section",
        issues=[issue_new, issue_matching, issue_changed],
    )

    milestone = SimpleNamespace(
        number="0.1",
        title="Test Milestone",
        sections=[section],
    )

    roadmap = SimpleNamespace(
        milestones=[milestone],
    )

    existing_issues = [
        SimpleNamespace(
            title="Matching Issue",
            body="Matching description\nGitMap: 0.1.2",
        ),
        SimpleNamespace(
            title="Changed Issue",
            body="Old description\nGitMap: 0.1.3",
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
    )

    monkeypatch.setattr(
        "gitmap.github_mapping.resolve_issue_targets",
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
    )

    section = SimpleNamespace(
        issues=[roadmap_issue],
    )

    milestone = SimpleNamespace(
        sections=[section],
    )

    roadmap = SimpleNamespace(
        milestones=[milestone],
    )

    existing_issue = SimpleNamespace(
        number=42,
        title="Removed Issue",
        body="Old description\nGitMap: 0.1.2",
    )

    removed = detect_removed_roadmap_items(
        roadmap,
        [existing_issue],
    )

    assert removed == [existing_issue]
