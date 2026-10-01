"""Validation tools for GitMap roadmaps."""

from gitmap.models import Issue, Roadmap


class ValidationError:
    """A problem found while validating a roadmap."""

    def __init__(self, message: str):
        self.message = message

    def __str__(self) -> str:
        return self.message


def _validate_issue(
    issue: Issue,
    location: str,
    seen_numbers: set[str],
) -> list[ValidationError]:
    """Validate an issue."""

    errors = []

    if not issue.number.strip():
        errors.append(
            ValidationError(f"Issue in {location} cannot have a blank number.")
        )

    if issue.number in seen_numbers:
        errors.append(ValidationError(f"Duplicate number: {issue.number}"))
    else:
        seen_numbers.add(issue.number)

    if not issue.title.strip():
        errors.append(
            ValidationError(f"Issue {issue.number} cannot have a blank title.")
        )

    for work_step in issue.work_steps:
        if work_step.number in seen_numbers:
            errors.append(ValidationError(f"Duplicate number: {work_step.number}"))
        else:
            seen_numbers.add(work_step.number)

        if not work_step.number.strip():
            errors.append(
                ValidationError(
                    f"Work step of {issue.number} cannot have a blank number."
                )
            )

        if not work_step.title.strip():
            errors.append(
                ValidationError(
                    f"Work step {work_step.number} cannot have a blank title."
                )
            )

    return errors


def validate_roadmap(roadmap: Roadmap) -> list[ValidationError]:
    """Validate the basic structure of a roadmap."""

    errors: list[ValidationError] = []
    seen_numbers: set[str] = set()

    if not roadmap.name.strip():
        errors.append(ValidationError("Roadmap name cannot be blank."))

    for milestone in roadmap.milestones:
        if not milestone.number.strip():
            errors.append(ValidationError("Milestone number cannot be blank."))

        if not milestone.title.strip():
            errors.append(
                ValidationError(f"Milestone {milestone.number} title cannot be blank.")
            )

        if milestone.number in seen_numbers:
            errors.append(ValidationError(f"Duplicate number: {milestone.number}"))
        else:
            seen_numbers.add(milestone.number)

        for issue in milestone.issues:
            errors.extend(
                _validate_issue(
                    issue,
                    f"milestone {milestone.number}",
                    seen_numbers,
                )
            )

        for section in milestone.sections:
            if section.number in seen_numbers:
                errors.append(ValidationError(f"Duplicate number: {section.number}"))
            else:
                seen_numbers.add(section.number)

            if not section.title.strip():
                errors.append(
                    ValidationError(
                        f"Section in milestone {milestone.number} cannot have a blank title."
                    )
                )

            for feature in section.features:
                if feature.number in seen_numbers:
                    errors.append(
                        ValidationError(f"Duplicate number: {feature.number}")
                    )
                else:
                    seen_numbers.add(feature.number)

                if not feature.number.strip():
                    errors.append(
                        ValidationError(
                            f"Feature in section '{section.title}' "
                            "cannot have a blank number."
                        )
                    )

                if not feature.title.strip():
                    errors.append(
                        ValidationError(
                            f"Feature {feature.number} cannot have a blank title."
                        )
                    )

                for issue in feature.issues:
                    errors.extend(
                        _validate_issue(
                            issue,
                            f"feature '{feature.title}'",
                            seen_numbers,
                        )
                    )

            for issue in section.issues:
                errors.extend(
                    _validate_issue(
                        issue,
                        f"section '{section.title}'",
                        seen_numbers,
                    )
                )

    return errors
