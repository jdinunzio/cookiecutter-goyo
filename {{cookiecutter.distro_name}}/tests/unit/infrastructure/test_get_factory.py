from unittest import TestCase

from {{cookiecutter.package_name}}.infrastructure.adapters.factory import get_factory


class TestGetFactory(TestCase):
    """Test `get_factory` factory method."""

    def test_unknown_env_error(self) -> None:
        """`get_factory` should raise when given unknown env."""
        with self.assertRaises(RuntimeError):
            get_factory("this-env-doesn't-exist")
