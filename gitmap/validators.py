"""Validation tools for GitMap roadmaps."""

from gitmap.models import Roadmap


class ValidationError:
    """A problem found while validating a roadmap."""

    def __init__(self, message: str):
        self.message = message

    def __str__(self) -> str:
        return self.message


def validate_roadmap(roadmap: Roadmap) -> list[ValidationError]:
    """Validate the basic structure of a roadmap."""

    errors: list[ValidationError] = []

    if not roadmap.name.strip():
        errors.append(ValidationError("Roadmap name cannot be blank."))

    for milestone in roadmap.milestones:
        if not milestone.number.strip():
            errors.append(ValidationError("Milestone number cannot be blank."))

        if not milestone.title.strip():
            errors.append(
                ValidationError(
                    f"Milestone {milestone.number} title cannot be blank."
                )
            )

        for epic in milestone.epics:
            if not epic.title.strip():
                errors.append(
                    ValidationError(
                        f"Epic in milestone {milestone.number} cannot have a blank title."
                    )
                )

            for issue in epic.issues:
                if not issue.number.strip():
                    errors.append(
                        ValidationError(
                            f"Issue in epic '{epic.title}' cannot have a blank number."
                        )
                    )

                if not issue.title.strip():
                    errors.append(
                        ValidationError(
                            f"Issue {issue.number} cannot have a blank title."
                        )
                    )

    return errors