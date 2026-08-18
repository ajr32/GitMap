from types import SimpleNamespace

from gitmap.github_mapping import summarize_roadmap_differences


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