from datetime import datetime
from typing import cast
from uuid import UUID

import pytz
from sqlalchemy import select
from sqlalchemy.orm import Session

from {{cookiecutter.package_name}}.application.exceptions import RecordNotFoundError
from {{cookiecutter.package_name}}.application.interfaces import TodoRepository
from {{cookiecutter.package_name}}.domain import Todo, TodoPartial
from {{cookiecutter.package_name}}.infrastructure.adapters.alchemy.models import TodoRecord
from {{cookiecutter.package_name}}.infrastructure.adapters.alchemy.todomapper import TodoMapper


class AlchemyTodoRepository(TodoRepository):
    """Concrete implementation of TodoRepository for SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        """Create AlchemyTodoRepository.

        Args:
            session: SQLAlchemy session.
        """
        self.session = session
        self.mapper = TodoMapper()

    def create(self, todolist_id: UUID, to_do: Todo) -> Todo:
        """Create and persist an instance of TO-DO.

        Args:
            todolist_id: Id of the TodoList to add this TO-DO.
            to_do: Instance to create in the repository.

        Returns:
            TO-DO persisted in the repository, optionally with some fields updated.
        """
        original_record = self.mapper.record_from_model(to_do, todolist_id)
        self.session.add(original_record)
        self.session.flush()
        return self.mapper.model_from_record(original_record)

    def update(self, todo_id: UUID, todo_update: TodoPartial) -> Todo:
        """Update an instance of TO-DO.

        Args:
            todo_id: Id of the TO-DO to update.
            todo_update: Instance with the update information.

        Returns:
            TO-DO updated in the repository.
        """
        record = self.session.get(TodoRecord, todo_id)
        if record is None:
            msg = f"can't update todo: ${todo_id} not found"
            raise RecordNotFoundError(msg)

        for key, val in todo_update.dict(exclude_unset=True).items():
            setattr(record, key, val)

        self.session.flush()
        return self.mapper.model_from_record(cast(TodoRecord, record))

    def get(self, todo_id: UUID) -> Todo | None:
        """Get an instance of TO-DO, given its id.

        Args:
            todo_id: Id of the instance to retrieve.

        Returns:
            TO-DO for the given id, or None.
        """
        record = self.session.get(TodoRecord, todo_id)
        if record is None:
            return None

        model = self.mapper.model_from_record(cast(TodoRecord, record))
        return model

    def retrieve(self, todolist_id: UUID) -> list[Todo]:
        """Get all non-deleted Todos.

        To be extended in the future to allow queries.

        Args:
            todolist_id: Id of the TodoList to add this TO-DO.

        Returns:
            List of Todos.
        """
        stmt = (
            select(TodoRecord)
            .where(TodoRecord.deleted_at == None)  # pylint: disable=C0121  # noqa: E711
            .where(TodoRecord.todolist_id == todolist_id)
        )
        records = self.session.scalars(stmt).all()
        models = [self.mapper.model_from_record(record) for record in records]
        return models

    def delete(self, todo_id: UUID, when: datetime | None = None) -> None:
        """Delete an instance of TO-DO, given its id.

        Args:
            todo_id: Id of the instance to delete.
            when: Datetime of deletion, if not specified, now is assumed.
        """
        when = when if when is not None else datetime.now(tz=pytz.UTC)
        record = self.session.get(TodoRecord, todo_id)
        if record is None:
            msg = f"can't delete todo: ${todo_id} not found"
            raise RecordNotFoundError(msg)
        record.deleted_at = when
        self.session.add(record)
        self.session.flush()
