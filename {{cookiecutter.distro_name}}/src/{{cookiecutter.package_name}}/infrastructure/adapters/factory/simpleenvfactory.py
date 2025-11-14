from typing import cast

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

from {{cookiecutter.package_name}}.application.interfaces import Factory, UOWService
from {{cookiecutter.package_name}}.infrastructure.adapters import config
from {{cookiecutter.package_name}}.infrastructure.adapters.alchemy import AlchemyUOWService


class SimpleEnvFactory(Factory):  # pylint: disable=too-few-public-methods
    """Factory for local tests.

    * services are memoised.
    * make_uow_service will return an AlchemyUOWService with SQLite using a file.
    """

    alchemy_engine: Engine | None = None
    uow_service: AlchemyUOWService | None = None

    def make_uow_service(self) -> UOWService:
        """Return an instance of UOWService, using cache by default.

        Returns:
            UOWService.
        """
        if self.uow_service is not None:
            return self.uow_service

        self.make_alchemy_engine()
        assert self.alchemy_engine is not None

        session_maker = sessionmaker(bind=self.alchemy_engine)

        SimpleEnvFactory.uow_service = AlchemyUOWService(self.alchemy_engine, session_maker)
        return cast("UOWService", self.uow_service)

    def make_alchemy_engine(self) -> Engine:
        """Create and return (or use memoised) SQLAlchemy engine.

        Returns:
            SQLAlchemy Engine
        """
        if self.alchemy_engine is not None:
            return self.alchemy_engine

        engine = create_engine(f"sqlite:///{config.SQLITE_DB_FILE_NAME}")
        SimpleEnvFactory.alchemy_engine = engine
        return cast("Engine", self.alchemy_engine)
