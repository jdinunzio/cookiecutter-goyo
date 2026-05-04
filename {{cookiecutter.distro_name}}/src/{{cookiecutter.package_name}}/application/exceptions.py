class AppError(Exception):
    """Base class for all application exceptions."""

    def __init__(self, message: str, *args: object) -> None:
        """Create an AppError with a given message."""
        super().__init__(*args)
        self.message = message


{%- if cookiecutter.add_repository_and_sqlalchemy %}


class RepoError(AppError):
    """Base class for all repository exceptions."""


class RecordNotFoundError(RepoError):
    """Record not found."""

{%- endif %}


class UseCaseError(AppError):
    """Base class for all Use Case related exceptions."""
