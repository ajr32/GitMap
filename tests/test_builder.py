from gitmap.builder import start_new_roadmap


def test_start_new_roadmap(monkeypatch):
    answers = iter(
        [
            "Test Project",
            "A test project overview.",
            "",  # finished overview
            "0.1",
            "Foundations",
            "s",  # add section
            "0.1.1",
            "Project Setup",
            "Set up the initial project.",
            "",  # finished section overview
            "f",  # add feature
            "0.1.1.1",
            "Project Structure",
            "Set up the project structure.",
            "",  # finished feature description
            "0.1.1.1.1",
            "Create Python Project",
            "Create the initial Python project structure.",
            "",  # finished issue description
            "r",
            "Python 3.14",
            "w",
            "0.1.1.1.1.1",
            "Set up package structure",
            "Create the package folders.",
            "",  # finished work-step description
            "Use src layout",
            "",  # finished work-step requirements
            "d",  # done with issue
            "",  # finished issues in feature
            "",  # finished features
            "d",  # done with section
            "",  # finished sections
            "d",  # done with milestone
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
            "issues": [],
            "sections": [
                {
                    "number": "0.1.1",
                    "title": "Project Setup",
                    "overview": "Set up the initial project.",
                    "milestone": "0.1",
                    "issues": [],
                    "features": [
                        {
                            "number": "0.1.1.1",
                            "title": "Project Structure",
                            "description": "Set up the project structure.",
                            "section": "Project Setup",
                            "issues": [
                                {
                                    "number": "0.1.1.1.1",
                                    "title": "Create Python Project",
                                    "description": "Create the initial Python project structure.",
                                    "requirements": ["Python 3.14"],
                                    "parent": "Project Structure",
                                    "work_steps": [
                                        {
                                            "number": "0.1.1.1.1.1",
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
            ],
        }
    ]