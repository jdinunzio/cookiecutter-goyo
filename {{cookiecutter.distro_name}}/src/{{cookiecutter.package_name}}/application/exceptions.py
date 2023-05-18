from typing import Any


class AppException(Exception):
    """Base class for all application exceptions."""

    def __init__(self, message, *args: Any) -> None:
        """Constructor."""
        super().__init__(*args)
        self.message = message


class UseCaseException(AppException):
    """Base class for all Use Case related exceptions."""
