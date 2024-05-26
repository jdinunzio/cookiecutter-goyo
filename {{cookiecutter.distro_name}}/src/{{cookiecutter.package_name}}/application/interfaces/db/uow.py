import abc
from typing import Self

from {{cookiecutter.package_name}}.application.interfaces.db.todolistrepository import TodoListRepository
from {{cookiecutter.package_name}}.application.interfaces.db.todorepository import TodoRepository


class UnitOfWork(abc.ABC):
    """Abstract Unit of Work.

    A Unit of Work is a generalisation of the concept of transactions. They provide a context on
    which certain set of operations either all succeed or if one fail, the effects of all is
    rolled back.

    This Unit of Work interface requires implementations with python's context manager interface.

    Example of use:

        uow = someConcreteUOWService.get_uow()
        with uow:
            # repos are only valid inside a context
            uow.todolist_repo.create(some_todolist)
            uow.commit()
    """

    todo_repo: TodoRepository
    todolist_repo: TodoListRepository

    @abc.abstractmethod
    def commit(self) -> None:
        """Commit changes made in this unit of work, persisting them."""
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self) -> None:
        """Rollback changes made in this unit of work, undoing them."""
        raise NotImplementedError

    @abc.abstractmethod
    def __enter__(self) -> Self:
        """Enter a unit of work context."""
        raise NotImplementedError

    def __exit__(self, *args: object) -> None:
        """Exit the unit of work context.

        Exiting a context invokes a rollback. In this way, developers are required to explicitly
        commit the unit of work before the context ends.
        """
        self.rollback()
