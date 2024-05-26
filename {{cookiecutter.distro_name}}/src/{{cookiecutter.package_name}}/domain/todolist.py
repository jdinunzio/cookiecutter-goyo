import uuid
from datetime import datetime

import pytz
from pydantic import BaseModel, ConfigDict, Field

from {{cookiecutter.package_name}}.domain.todo import Todo


class TodoListOptional(BaseModel):
    """Model for TodoList optional field."""

    todos: list[Todo] = Field(default_factory=list)
    created_at: datetime | None = None
    completed_at: datetime | None = None
    deleted_at: datetime | None = None


class TodoListRequired(BaseModel):
    """Model for TodoList required fields.

    Keep in sync with TodoListRequiredOptional.
    """

    description: str


class TodoListRequiredOptional(BaseModel):
    """Model for TodoList required fields made optional.

    This model replaces TodoListRequired for describing the model for patch operations.
    Keep in sync with TodoListRequired.
    """

    description: str | None = None


class TodoListPartial(TodoListRequiredOptional, TodoListOptional):
    """Model representing TodoList Update Operations.

    This model contains all TodoList attributes except for `id`, and all of them are
    optional.
    """


class TodoListCreate(TodoListRequired, TodoListOptional):
    """Model representing TodoList Creation Operations.

    This model contains all required and optionals fields of TodoList, except for `id`,
    which shouldn't be specified on creation.
    """


class TodoList(TodoListRequired, TodoListOptional):
    """A To-DO list."""

    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=lambda: datetime.now(pytz.UTC))
