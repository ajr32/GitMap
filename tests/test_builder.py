from gitmap.builder import start_new_roadmap


def test_start_new_roadmap(monkeypatch):
    answers = iter(
        [
            "Test Project",
            "A test project overview.",
            "",  # finished overview
            "0.1",
            "Foundations",
            "Project Setup",
            "Set up the initial project.",
            "Create Python Project",
            "Create the initial Python project structure.",
            "",  # finished issue description

            "r",
            "Python 3.14",

            "w",
            "Set up package structure",
            "Create the package folders.",
            "",  # finished work-step description
            "Use src layout",
            "",  # finished work-step requirements

            "d",

            "",  # finished issues
            "",  # finished sections
            "",  # finished milestones
        ]
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(answers),
    )

    roadmap = start_new_roadmap()

    assert roadmap["name"] == "Test Project"
    assert roadmap["overview"] == "A test project overview."
    assert roadmap["milestones"] == [
        {
            "number": "0.1",
            "title": "Foundations",
            "sections": [
    {
        "title": "Project Setup",
        "overview": "Set up the initial project.",
        "milestone": "0.1",
        "issues": [
            {
                "title": "Create Python Project",
                "description": "Create the initial Python project structure.",
                "requirements": ["Python 3.14"],
                "section": "Project Setup",
                "work_steps": [
                    {
                        "title": "Set up package structure",
                        "description": "Create the package folders.",
                        "requirements": ["Use src layout"],
                        "parent": "Create Python Project",
                    }
                ],
            }
        ],
    }
],
        }
    ]