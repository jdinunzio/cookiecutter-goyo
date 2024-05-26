from unittest import TestCase

from tests.integration.infrastructure.adapters.alchemy.alchemymixin import AlchemyMixin


class TestAlchemyUnitOfWork(TestCase, AlchemyMixin):
    """Test AlchemyUnitOfWork."""

    @classmethod
    def setUpClass(cls) -> None:
        """Class set up: create service and init db."""
        cls.init_service()

    @classmethod
    def tearDownClass(cls) -> None:
        """Class tear down: delete db."""
        cls.delete_db()

    def setUp(self) -> None:
        """Get a fresh unit of work."""
        self.uow = self.service.get_uow()

    def test_context_commit(self) -> None:
        """A unit of work should be a context manager and allow commits."""
        with self.uow:
            # look into repository tests for more complex interactions
            self.uow.commit()

    def test_context_rollback(self) -> None:
        """A unit of work should be a context manager and allow rollbacks."""
        with self.uow:
            # look into repository tests for more complex interactions
            self.uow.rollback()
