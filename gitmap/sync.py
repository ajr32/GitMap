"""Synchronization tools for GitMap."""

from dataclasses import dataclass, field

from gitmap.models import Roadmap


@dataclass
class SyncResult:
    """Summary of a synchronization operation."""

    created: list[str] = field(default_factory=list)
    existing: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def successful(self) -> bool:
        """Return whether synchronization completed without errors."""

        return not self.errors


class SyncEngine:
    """Synchronize a roadmap with GitHub."""

    def __init__(self, roadmap: Roadmap):
        self.roadmap = roadmap

    def plan(self) -> SyncResult:
        """Create a synchronization plan without changing GitHub."""

        result = SyncResult()

        for milestone in self.roadmap.milestones:
            result.created.append(f"Milestone: {milestone.number} {milestone.title}")

            for epic in milestone.epics:
                result.created.append(f"Epic: {epic.title}")

                for issue in epic.issues:
                    result.created.append(f"Issue: {issue.number} {issue.title}")

        return result
