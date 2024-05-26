class AppError(Exception):
    """Base class for all application exceptions."""

    def __init__(self, message: str, *args: object) -> None:
        """Create an AppError with a given message."""
        super().__init__(*args)
        self.message = message


class RepoError(AppError):
    """Base class for all repository exceptions."""


class RecordNotFoundError(RepoError):
    """Record not found."""


class UseCaseError(AppError):
    """Base class for all Use Case related exceptions."""
