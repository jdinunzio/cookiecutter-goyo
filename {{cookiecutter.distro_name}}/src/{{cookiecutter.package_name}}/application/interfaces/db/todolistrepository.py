# pylint: disable=R0801
import abc
from datetime import datetime
from uuid import UUID

from {{cookiecutter.package_name}}.domain import TodoList, TodoListPartial


class TodoListRepository(abc.ABC):
    """Abstract class for TodoListRepository."""

    @abc.abstractmethod
    def create(self, todolist: TodoList) -> TodoList:
        """Create and persist an instance of TodoList.

        Args:
            todolist: Instance to create in the repository.

        Returns:
            TodoList persisted in the repository, optionally with some fields updated.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, todolist_id: UUID, todolist_update: TodoListPartial) -> TodoList:
        """Update an instance of TodoList.

        Args:
            todolist_id: Id of the TodoList to update.
            todolist_update: Instance with the update information.

        Returns:
            TodoList updated in the repository.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, todolist_id: UUID) -> TodoList | None:
        """Get an instance of TodoList, given its id.

        Args:
            todolist_id: Id of the instance to retrieve.

        Returns:
            TodoList for the given id, or None.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def retrieve(self) -> list[TodoList]:
        """Get all non-deleted TodoLists.

        To be extended in the future to allow queries.

        Returns:
            List of TodoLists.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, todolist_id: UUID, when: datetime | None = None) -> None:
        """Delete an instance of TodoList, given its id.

        Args:
            todolist_id: Id of the instance to delete.
            when: Datetime of deletion, if not specified, now is assumed.
        """
        raise NotImplementedError()
