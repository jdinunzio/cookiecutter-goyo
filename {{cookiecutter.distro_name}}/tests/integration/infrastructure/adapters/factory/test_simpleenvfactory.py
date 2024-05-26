from unittest import TestCase

from {{cookiecutter.package_name}}.application.interfaces import UOWService
from {{cookiecutter.package_name}}.infrastructure.adapters.factory import SimpleEnvFactory


class TestSimpleEnvFactory(TestCase):
    """Integration test for SimpleEnvFactory."""

    factory: SimpleEnvFactory

    @classmethod
    def setUpClass(cls) -> None:
        """Class setup."""
        cls.factory = SimpleEnvFactory()

    def test_make_uow_service(self) -> None:
        """`make_uow_service` should return a valid UOW service."""
        uow_service = self.factory.make_uow_service()
        self.assertIsInstance(uow_service, UOWService)

    def test_uow_service_is_memoised(self) -> None:
        """`make_uow_service` should be memoised."""
        uow_service1 = self.factory.make_uow_service()
        uow_service2 = self.factory.make_uow_service()
        print(uow_service1)
        print(uow_service2)
        self.assertEqual(uow_service1, uow_service2)
