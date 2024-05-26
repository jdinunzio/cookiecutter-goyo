from enum import Enum

from {{cookiecutter.package_name}}.application.interfaces.factory import Factory
from {{cookiecutter.package_name}}.infrastructure.adapters.config import ENV_TYPE

from .simpleenvfactory import SimpleEnvFactory


class FactoryType(str, Enum):
    """Enumeration of factories."""

    SIMPLE_ENV = "simple"


def get_factory(env_type: str | None = None) -> Factory:
    """Return concrete implementation of abstract factory, given the factory name.

    Args:
        env_type: Optional name of the factory to return. If none is provided, the default
            factory is used.

    Returns:
        Concrete implementation of Payment Gateway Abstract Factory.
    """
    env_type = env_type if env_type is not None else ENV_TYPE
    if env_type == FactoryType.SIMPLE_ENV:
        return SimpleEnvFactory()

    error_msg = f"Factory for {env_type=!r} unknown."
    raise RuntimeError(error_msg)
