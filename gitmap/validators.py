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
                ValidationError(f"Milestone {milestone.number} title cannot be blank.")
            )

        for Section in milestone.Sections:
            if not Section.title.strip():
                errors.append(
                    ValidationError(
                        f"Section in milestone {milestone.number} cannot have a blank title."
                    )
                )

            for issue in Section.issues:
                if not issue.number.strip():
                    errors.append(
                        ValidationError(
                            f"Issue in Section '{Section.title}' cannot have a blank number."
                        )
                    )

                if not issue.title.strip():
                    errors.append(
                        ValidationError(
                            f"Issue {issue.number} cannot have a blank title."
                        )
                    )

    return errors
