from pathlib import Path
from unittest import TestCase

from {{cookiecutter.package_name}}.application.interfaces import UnitOfWork
from tests.integration.infrastructure.adapters.alchemy.alchemymixin import AlchemyMixin


class TestAlchemyUOWService(TestCase, AlchemyMixin):
    """Test AlchemyUOWService."""

    @classmethod
    def setUpClass(cls) -> None:
        """Class set up: create service and init db."""
        cls.init_service()

    @classmethod
    def tearDownClass(cls) -> None:
        """Class tear down: delete db."""
        cls.delete_db()

    def test_database_created(self) -> None:
        """Database was created."""
        db_path = Path(self.db_file_name)
        self.assertTrue(db_path.exists())

    def test_get_uow(self) -> None:
        """Service can return a unit of work."""
        uow = self.service.get_uow()
        self.assertIsInstance(uow, UnitOfWork)
