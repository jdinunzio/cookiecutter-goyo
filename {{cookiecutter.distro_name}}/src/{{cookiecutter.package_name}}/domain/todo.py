import uuid
from datetime import datetime

import pytz
from pydantic import BaseModel, ConfigDict, Field


class TodoOptional(BaseModel):
    """Model for TO-DO optional field."""

    created_at: datetime | None = None
    completed_at: datetime | None = None
    deleted_at: datetime | None = None


class TodoRequired(BaseModel):
    """Model for TO-DO required fields.

    Keep in sync with TodoRequiredOptional.
    """

    description: str


class TodoRequiredOptional(BaseModel):
    """Model for TO-DO required fields made optional.

    This model replaces TodoRequired for describing the model for patch operations.
    Keep in sync with TodoRequired.
    """

    description: str | None = None


class TodoPartial(TodoRequiredOptional, TodoOptional):
    """Model representing TO-DO Update Operations.

    This model contains all TO-DO attributes except for `id`, and all of them are
    optional.
    """


class TodoCreate(TodoRequired, TodoOptional):
    """Model representing TO-DO Creation Operations.

    This model contains all required and optionals fields of TO-DO, except for `id`,
    which shouldn't be specified on creation.
    """


class Todo(TodoRequired, TodoOptional):
    """A TO-DO entry in a TO-DO list."""

    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=lambda: datetime.now(pytz.UTC))
