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
    """Track structured synchronization progress."""

    def __init__(self, overall_total=None, callback=None):
        self.overall_total = overall_total
        self.overall_current = 0
        self.history = []
        self.callback = callback
        self.last_event = None
        self._stage_positions = {}

    def report(self, stage, current, total, message):
        """Record a stage update and emit a structured progress event."""

        previous = self._stage_positions.get(stage, 0)
        delta = max(0, current - previous)

        self._stage_positions[stage] = max(previous, current)
        self.overall_current += delta

        if (
            self.overall_total is not None
            and self.overall_current > self.overall_total
        ):
            self.overall_current = self.overall_total

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