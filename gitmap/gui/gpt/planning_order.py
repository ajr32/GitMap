"""UI-independent planning preferences for GitMap GPT."""
from dataclasses import asdict, dataclass
import json
from pathlib import Path


@dataclass
class PlanningOrder:
    project_name: str = ""
    suggest_name: bool = True
    project_description: str = ""
    operation: str = "new"
    autonomy: int = 8
    hierarchy: str = "recommend"
    detail: str = "comprehensive"
    questions: str = "important"
    existing_roadmap_path: str = ""

    def save(self, path: str | Path) -> None:
        Path(path).write_text(json.dumps(asdict(self), indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: str | Path) -> "PlanningOrder":
        return cls(**json.loads(Path(path).read_text(encoding="utf-8")))
