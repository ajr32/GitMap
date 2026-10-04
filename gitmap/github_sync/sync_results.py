from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(frozen=True)
class SyncResult:
    status: str
    item_type: str
    description: str
    detail: str | None = None


class SyncResultCollector:
    """Collect the outcome of one GitHub synchronization session."""

    VALID_STATUSES = {
        "created",
        "updated",
        "closed",
        "skipped",
        "failed",
    }

    def __init__(self, roadmap_name, repository_name):
        self.roadmap_name = roadmap_name
        self.repository_name = repository_name
        self.started_at = datetime.now()
        self.results = []

    def add(self, status, item_type, description, detail=None):
        if status not in self.VALID_STATUSES:
            raise ValueError(f"Unknown synchronization result status: {status}")

        result = SyncResult(
            status=status,
            item_type=item_type,
            description=description,
            detail=detail,
        )

        self.results.append(result)
        return result

    def created(self, item_type, description, detail=None):
        return self.add("created", item_type, description, detail)

    def updated(self, item_type, description, detail=None):
        return self.add("updated", item_type, description, detail)

    def closed(self, item_type, description, detail=None):
        return self.add("closed", item_type, description, detail)

    def skipped(self, item_type, description, detail=None):
        return self.add("skipped", item_type, description, detail)

    def failed(self, item_type, description, detail=None):
        return self.add("failed", item_type, description, detail)

    def count(self, status):
        return sum(1 for result in self.results if result.status == status)

    def render(self):
        lines = [
            "GitMap Synchronization Log",
            f"Date: {self.started_at.strftime('%B %d, %Y')}",
            f"Time: {self.started_at.strftime('%I:%M:%S %p')}",
            f"Roadmap: {self.roadmap_name}",
            f"Repository: {self.repository_name}",
            "",
        ]

        sections = (
            ("created", "CREATED"),
            ("updated", "UPDATED"),
            ("closed", "CLOSED"),
            ("skipped", "SKIPPED"),
            ("failed", "FAILED"),
        )

        for status, heading in sections:
            lines.append(heading)

            matches = [result for result in self.results if result.status == status]

            if not matches:
                lines.append("  None")
            else:
                for result in matches:
                    line = f"  {result.item_type}: {result.description}"

                    if result.detail:
                        line += f" — {result.detail}"

                    lines.append(line)

            lines.append("")

        lines.extend(
            [
                "SUMMARY",
                f"  Created: {self.count('created')}",
                f"  Updated: {self.count('updated')}",
                f"  Closed: {self.count('closed')}",
                f"  Skipped: {self.count('skipped')}",
                f"  Failed: {self.count('failed')}",
            ]
        )

        return "\n".join(lines)

    def save(self, directory):
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)

        timestamp = self.started_at.strftime("%Y-%m-%d_%H%M%S")
        path = directory / f"sync_{timestamp}.log"

        path.write_text(
            self.render(),
            encoding="utf-8",
        )

        return path
