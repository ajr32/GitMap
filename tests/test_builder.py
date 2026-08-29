from gitmap.builder.builder import (
    render_roadmap_markdown,
)
from gitmap.builder.builder_add import (
    add_issue,
    add_work_step,
)
from gitmap.builder.builder_edit import (
    edit_issue,
)
from gitmap.builder.builder_rename import (
    rename_feature,
    rename_work_step,
)
from gitmap.roadmap_creation import start_new_roadmap


def test_start_new_roadmap(monkeypatch):
    answers = iter(
        [
            # Numbering / structure setup
            "2",  # manual numbering
            "2",  # sections and features

            # Project
            "Test Project",
            "A test project overview.",
            "",  # finished overview

            # Milestone
            "0.1",
            "Foundations",

            # Section
            "s",
            "0.1.1",
            "Project Setup",
            "Set up the initial project.",
            "",  # finished section overview

            # Feature
            "f",
            "0.1.1.1",
            "Project Structure",
            "Set up the project structure.",
            "",  # finished feature description

            # Issue
            "0.1.1.1.1",
            "Create Python Project",
            "Create the initial Python project structure.",
            "",  # finished issue description

            # Requirement
            "r",
            "Python 3.14",
            "",  # finished issue requirements

            # Work step
            "w",
            "0.1.1.1.1.1",
            "Set up package structure",
            "Create the package folders.",
            "",  # finished work-step description
            "Use src layout",
            "",  # finished work-step requirements
            "n",  # no nested work step

            # Finish issue / feature / section / milestone / roadmap
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
                                    "description": (
                                        "Create the initial Python project structure."
                                    ),
                                    "requirements": ["Python 3.14"],
                                    "parent": "Project Structure",
                                    "work_steps": [
                                        {
                                            "number": "0.1.1.1.1.1",
                                            "title": "Set up package structure",
                                            "description": "Create the package folders.",
                                            "requirements": ["Use src layout"],
                                            "parent": "Create Python Project",
                                            "work_steps": [],
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


def test_render_nested_work_steps():
    roadmap = {
        "name": "Test Project",
        "overview": "",
        "milestones": [
            {
                "number": "0.1",
                "title": "Foundations",
                "issues": [
                    {
                        "number": "0.1.1",
                        "title": "Create Project",
                        "description": "Create the project.",
                        "requirements": ["Use Python 3.14"],
                        "work_steps": [
                            {
                                "number": "0.1.1.1",
                                "title": "Create Structure",
                                "description": "",
                                "requirements": [],
                                "work_steps": [
                                    {
                                        "number": "0.1.1.1.1",
                                        "title": "Create Package",
                                        "description": "",
                                        "requirements": [],
                                        "work_steps": [],
                                    }
                                ],
                            }
                        ],
                    }
                ],
                "sections": [],
            }
        ],
    }

    markdown = render_roadmap_markdown(roadmap)

    assert "- [ ] 0.1.1.1 Create Structure" in markdown
    assert "  - [ ] 0.1.1.1.1 Create Package" in markdown
    assert "Create the project." in markdown
    assert "**Requirements:**" in markdown
    assert "- Use Python 3.14" in markdown


def test_rename_feature(monkeypatch):
    roadmap = {
        "milestones": [
            {
                "issues": [],
                "sections": [
                    {
                        "features": [
                            {
                                "number": "0.1.1.1",
                                "title": "Old Feature",
                                "issues": [],
                            }
                        ],
                        "issues": [],
                    }
                ],
            }
        ]
    }

    answers = iter(
        [
            "0.1.1.1",
            "New Feature",
        ]
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(answers),
    )

    rename_feature(roadmap)

    assert (
        roadmap["milestones"][0]["sections"][0]["features"][0]["title"]
        == "New Feature"
    )


def test_rename_nested_work_step(monkeypatch):
    roadmap = {
        "milestones": [
            {
                "issues": [
                    {
                        "work_steps": [
                            {
                                "number": "0.1.1",
                                "title": "Parent Step",
                                "work_steps": [
                                    {
                                        "number": "0.1.1.1",
                                        "title": "Old Nested Step",
                                        "work_steps": [],
                                    }
                                ],
                            }
                        ],
                    }
                ],
                "sections": [],
            }
        ]
    }

    answers = iter(
        [
            "0.1.1.1",
            "New Nested Step",
        ]
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(answers),
    )

    rename_work_step(roadmap)

    nested_step = roadmap["milestones"][0]["issues"][0]["work_steps"][0][
        "work_steps"
    ][0]

    assert nested_step["title"] == "New Nested Step"


def test_edit_issue_requirements(monkeypatch):
    roadmap = {
        "milestones": [
            {
                "issues": [
                    {
                        "number": "0.1.1",
                        "title": "Test Issue",
                        "description": "Old description",
                        "requirements": ["Old requirement"],
                        "work_steps": [],
                    }
                ],
                "sections": [],
            }
        ]
    }

    answers = iter(
        [
            "0.1.1",
            "r",
            "New requirement",
            "",
        ]
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(answers),
    )

    edit_issue(roadmap)

    assert roadmap["milestones"][0]["issues"][0]["requirements"] == [
        "New requirement"
    ]


def test_add_issue(monkeypatch):
    roadmap = {
        "milestones": [
            {
                "number": "0.1",
                "title": "Foundations",
                "issues": [],
                "sections": [],
            }
        ]
    }

    answers = iter(
        [
            "0.1",  # parent
            "0.1.1",  # issue number
            "New Issue",  # title
            "New description",
            "",  # finished description
            "New requirement",
            "",  # finished requirements
        ]
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(answers),
    )

    add_issue(roadmap)

    issue = roadmap["milestones"][0]["issues"][0]

    assert issue["number"] == "0.1.1"
    assert issue["title"] == "New Issue"
    assert issue["description"] == "New description"
    assert issue["requirements"] == ["New requirement"]


def test_add_nested_work_step(monkeypatch):
    roadmap = {
        "milestones": [
            {
                "issues": [
                    {
                        "number": "0.1.1",
                        "title": "Parent Issue",
                        "work_steps": [
                            {
                                "number": "0.1.1.1",
                                "title": "Parent Work Step",
                                "work_steps": [],
                            }
                        ],
                    }
                ],
                "sections": [],
            }
        ]
    }

    answers = iter(
        [
            "0.1.1.1",  # parent work step
            "0.1.1.1.1",  # new work-step number
            "Nested Work Step",  # title
            "Do nested work.",  # description
            "",  # finished description
            "",  # finished requirements
            "n",  # no further nesting
        ]
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(answers),
    )

    add_work_step(roadmap, "manual")

    nested = roadmap["milestones"][0]["issues"][0]["work_steps"][0][
        "work_steps"
    ][0]

    assert nested["number"] == "0.1.1.1.1"
    assert nested["title"] == "Nested Work Step"
    assert nested["parent"] == "Parent Work Step"