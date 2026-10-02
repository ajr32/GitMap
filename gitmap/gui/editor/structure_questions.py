QUESTIONS = [
    {
        "id": "numbering",
        "subject": "Roadmap Numbering",
        "question": "How should GitMap number your roadmap?",
        "options": [
            {
                "text": "Automatic numbering",
                "value": "automatic",
                "example": """# Exampel Roadmap

## 0.1 First Milestone

### 0.1.1 First Section

#### 0.1.1.1 First Item""",
                "explanation": (
                    "GitMap assigns the next available number automatically "
                    "based on the item's parent. This is definitely the easier option."
                ),
            },
            {
                "text": "Manual numbering",
                "value": "manual",
                "example": """# Example Roadmap

## 2.4 First Milestone

### 2.4.7 First Section

#### 2.4.7.3 First Item""",
                "explanation": (
                    "You would be responsible for entering roadmap numbers yourself. "
                    "However, child numbers must extend their parent's number."
                ),
            },
        ],
    },
    {
        "id": "structure",
        "subject": "Roadmap Structure",
        "question": "How would you like to organize your roadmap?",
        "options": [
            {
                "text": "Sections only",
                "value": "sections",
                "example": "",
                "explanation": "",
            },
            {
                "text": "Sections and Features",
                "value": "sections_and_features",
                "example": "",
                "explanation": "",
            },
            {
                "text": "Neither",
                "value": "neither",
                "example": "",
                "explanation": "",
            },
        ],
    },
    {
        "id": "section_tracking",
        "subject": "Tracking - Sections",
        "question": "How would you like to track and organize the sections in your project?",
        "options": [
            {
                "text": "Issues only",
                "value": "issues",
                "example": "",
                "explanation": "",
            },
            {
                "text": "Labels only",
                "value": "labeling",
                "example": "",
                "explanation": "",
            },
            {
                "text": "Both Issues and Labels",
                "value": "issues_and_labels",
                "example": "",
                "explanation": "",
            },
            {
                "text": "Neither Issues or Labels",
                "value": "blank",
                "example": "",
                "explanation": "",
            },
        ],
    },
    {
        "id": "feature_tracking",
        "subject": "Tracking - Features",
        "question": "How would you like to track and organize the features in your project?",
        "options": [
            {
                "text": "Issues only",
                "value": "issues",
                "example": "",
                "explanation": "",
            },
            {
                "text": "Labels only",
                "value": "labeling",
                "example": "",
                "explanation": "",
            },
            {
                "text": "Both Issues and Labels",
                "value": "issues_and_labels",
                "example": "",
                "explanation": "",
            },
            {
                "text": "Neither Issues or Labels",
                "value": "blank",
                "example": "",
                "explanation": "",
            },
        ],
    },
    {
        "id": "hierarchy",
        "subject": "Hierarchy Issue Titles",
        "question": "Once made, how do you want your Sections and Features to be titled?",
        "options": [
            {
                "text": "Plain",
                "value": "plain",
                "example": "",
                "explanation": "",
            },
            {
                "text": "By type prefix",
                "value": "labeling",
                "example": "",
                "explanation": "",
            },
        ],
    },
    {
        "id": "starting_point",
        "subject": "Roadmap Numbering - Starting Series",
        "question": "What do you want the first number in your roadmap to be?",
        "options": [
            {
                "text": "0 - Pre-production",
                "value": "pre-production",
                "example": "",
                "explanation": "",
            },
            {
                "text": "1 - First run of production",
                "value": "production",
                "example": "",
                "explanation": "",
            },
            {
                "text": "Production, but a number greater than 1",
                "value": "re-production",
                "example": "",
                "explanation": "",
            },
        ],
    },
    {
        "id": "project_name",
        "subject": "Roadmap Name",
        "question": "What is the name of your project?",
        "options": [],
    },
]
