from typing import Self

from sqlalchemy.orm import Session

from {{cookiecutter.package_name}}.application.interfaces import UnitOfWork
from {{cookiecutter.package_name}}.infrastructure.adapters.alchemy.alchemytodolistrepository import (
    AlchemyTodoListRepository,
)
from {{cookiecutter.package_name}}.infrastructure.adapters.alchemy.alchemytodorepository import (
    AlchemyTodoRepository,
)


class AlchemyUnitOfWork(UnitOfWork):
    """Concrete implementation of UnitOfWork using SQLAlchemy.

    Example of use:

        uow = instanceOfAlchemyUOWService.get_uow()
        with uow:
            # repos are only valid inside a context
            uow.todolist_repo.create(some_todolist)
            uow.commit()
    """

    def __init__(self, session: Session) -> None:
        """Create a SQLAlchemy unit of work.

        Args:
            session: SQLAlchemy session.
        """
        self.session: Session = session

    def commit(self) -> None:
        """Commit changes made in this unit of work, persisting them."""
        return self.session.commit()

    def rollback(self) -> None:
        """Rollback changes made in this unit of work, undoing them."""
        return self.session.rollback()

    def __enter__(self) -> Self:
        """Enter a context.

        A new session is created/gotten from the session pool.
        """
        self.todolist_repo = AlchemyTodoListRepository(self.session)
        self.todo_repo = AlchemyTodoRepository(self.session)
        return self

    def __exit__(self, *args: object) -> None:
        """Exit context.

        Exiting a context invokes a rollback. In this way, developers are required to explicitly
        commit the unit of work before the context ends.
        """
        super().__exit__(*args)
        self.session.close()
