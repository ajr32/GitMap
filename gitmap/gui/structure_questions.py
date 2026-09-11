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
]
