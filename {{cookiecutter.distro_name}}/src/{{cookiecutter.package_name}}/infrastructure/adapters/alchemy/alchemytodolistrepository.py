from datetime import datetime
from typing import cast
from uuid import UUID

import pytz
from sqlalchemy import select
from sqlalchemy.orm import Session

from {{cookiecutter.package_name}}.application.exceptions import RecordNotFoundError
from {{cookiecutter.package_name}}.application.interfaces import TodoListRepository
from {{cookiecutter.package_name}}.domain import TodoList, TodoListPartial
from {{cookiecutter.package_name}}.infrastructure.adapters.alchemy.models import TodoListRecord
from {{cookiecutter.package_name}}.infrastructure.adapters.alchemy.todolistmapper import TodoListMapper


class AlchemyTodoListRepository(TodoListRepository):
    """Concrete implementation of TodoListRepository for SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        """Create AlchemyTodoListRepository.

        Args:
            session: SQLAlchemy session.
        """
        self.session = session
        self.mapper = TodoListMapper()

    def create(self, todolist: TodoList) -> TodoList:
        """Create and persist an instance of TodoList.

        Args:
            todolist: Instance to create in the repository.

        Returns:
            TodoList persisted in the repository, optionally with some fields updated.
        """
        original_record = self.mapper.record_from_model(todolist)
        self.session.add(original_record)
        self.session.flush()
        return self.mapper.model_from_record(original_record)

    def update(self, todolist_id: UUID, todolist_update: TodoListPartial) -> TodoList:
        """Update an instance of TodoList.

        Args:
            todolist_id: Id of the TodoList to update.
            todolist_update: Instance with the update information.

        Returns:
            TodoList updated in the repository.
        """
        record = self.session.get(TodoListRecord, todolist_id)
        if record is None:
            msg = f"can't update todolist: ${todolist_id} not found"
            raise RecordNotFoundError(msg)

        for key, val in todolist_update.dict(exclude_unset=True).items():
            setattr(record, key, val)

        self.session.flush()
        return self.mapper.model_from_record(cast(TodoListRecord, record))

    def get(self, todolist_id: UUID) -> TodoList | None:
        """Get an instance of TodoList, given its id.

        Args:
            todolist_id: Id of the instance to retrieve.

        Returns:
            TodoList for the given id, or None.
        """
        record = self.session.get(TodoListRecord, todolist_id)
        if record is None:
            return None

        model = self.mapper.model_from_record(cast(TodoListRecord, record))
        return model

    def retrieve(self) -> list[TodoList]:
        """Get all non-deleted TodoLists.

        To be extended in the future to allow queries.

        Returns:
            List of TodoLists.
        """
        stmt = select(TodoListRecord).where(
            TodoListRecord.deleted_at == None  # pylint: disable=C0121  # noqa: E711
        )
        records = self.session.scalars(stmt).all()
        models = [self.mapper.model_from_record(record) for record in records]
        return models

    def delete(self, todolist_id: UUID, when: datetime | None = None) -> None:
        """Delete an instance of TodoList, given its id.

        Args:
            todolist_id: Id of the instance to delete.
            when: Datetime of deletion, if not specified, now is assumed.
        """
        when = when if when is not None else datetime.now(tz=pytz.UTC)
        record = self.session.get(TodoListRecord, todolist_id)
        if record is None:
            msg = f"can't delete todolist: ${todolist_id} not found"
            raise RecordNotFoundError(msg)
        record.deleted_at = when
        self.session.add(record)
        self.session.flush()
