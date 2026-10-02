from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class SyncProgressEvent:
    """One structured synchronization progress update."""

    stage: str
    stage_current: int
    stage_total: int | None
    overall_current: int
    overall_total: int | None
    message: str


class SyncProgressReporter:
    """Collect structured sync progress and a short recent-activity history."""

    def __init__(self, overall_total=None, history_limit=8, callback=None):
        self.overall_total = overall_total
        self.overall_current = 0
        self.history = deque(maxlen=history_limit)
        self.callback = callback
        self.last_event = None
        self._stage_positions = {}

    def report(self, stage, current, total, message):
        """Record a stage update and emit a structured progress event."""

        previous = self._stage_positions.get(stage, 0)
        delta = max(0, current - previous)
        self._stage_positions[stage] = max(previous, current)
        self.overall_current += delta

        event = SyncProgressEvent(
            stage=stage,
            stage_current=current,
            stage_total=total,
            overall_current=self.overall_current,
            overall_total=self.overall_total,
            message=message,
        )

        self.last_event = event
        self.history.append(message)

        if self.callback is not None:
            self.callback(event, tuple(self.history))

        return event
