import abc
from datetime import datetime
from uuid import UUID

from {{cookiecutter.package_name}}.domain import Todo, TodoPartial


class TodoRepository(abc.ABC):
    """Abstract class for TodoRepository."""

    @abc.abstractmethod
    def create(self, todolist_id: UUID, to_do: Todo) -> Todo:
        """Create and persist an instance of TO-DO.

        Args:
            todolist_id: Id of the TodoList to add this TO-DO.
            to_do: Instance to create in the repository.

        Returns:
            TO-DO persisted in the repository, optionally with some fields updated.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, todo_id: UUID, todo_update: TodoPartial) -> Todo:
        """Update an instance of TO-DO.

        Args:
            todo_id: Id of the TO-DO to update.
            todo_update: Instance with the update information.

        Returns:
            TO-DO updated in the repository.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, todo_id: UUID) -> Todo | None:
        """Get an instance of TO-DO, given its id.

        Args:
            todo_id: Id of the instance to retrieve.

        Returns:
            TO-DO for the given id, or None.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def retrieve(self, todolist_id: UUID) -> list[Todo]:
        """Get all non-deleted Todos for the given TodoList Id.

        To be extended in the future to allow queries.

        Args:
            todolist_id: Id of the TodoList to add this TO-DO.

        Returns:
            List of Todos.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, todo_id: UUID, when: datetime | None = None) -> None:
        """Delete an instance of TO-DO, given its id.

        Args:
            todo_id: Id of the instance to delete.
            when: Datetime of deletion, if not specified, now is assumed.
        """
        raise NotImplementedError()
