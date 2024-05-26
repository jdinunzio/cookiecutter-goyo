from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker

from {{cookiecutter.package_name}}.application.interfaces import UnitOfWork, UOWService
from {{cookiecutter.package_name}}.infrastructure.adapters.alchemy.alchemyuow import AlchemyUnitOfWork
from {{cookiecutter.package_name}}.infrastructure.adapters.alchemy.models import BaseSQLRecord


class AlchemyUOWService(UOWService):  # pylint: disable=R0903
    """Concrete implementation of Unit Of Work Service using SQLAlchemy.

    It abstracts a unit of work, basically a transaction.
    """

    def __init__(self, engine: Engine, session_factory: sessionmaker) -> None:
        """Create UOWService for SQLAlchemy.

        Args:
            engine: SQLAlchemy engine to use.
            session_factory: SQLAlchemy session factory. Used to create session/transactions for
                UOW
        """
        self.engine: Engine = engine
        self.session_factory: sessionmaker = session_factory

    def get_uow(self) -> UnitOfWork:
        """Return a unit of work.

        The intended use is:

            uow_service = SomeConcreteUOWService()
            with uow_service.get_uow() as uow:
                foo_instance = Foo(...)
                uow.foo_repo.create(foo_instance)
                uow.commit()

        Returns:
            UnitOfWork
        """
        session = self.session_factory(autoflush=False)
        return AlchemyUnitOfWork(session)

    def init_db(self) -> None:
        """Initialise the database.

        This is a convenience method. Strictly speaking this doesn't belong to UOWService, but for
        a small project, it's better to have it here rather than creating another service. Once
        the project has growth to require migrations, this method can be removed.
        """
        BaseSQLRecord.metadata.create_all(self.engine)

    def terminate(self) -> None:
        """Terminate Unit of Work Service."""
        self.engine.dispose()
