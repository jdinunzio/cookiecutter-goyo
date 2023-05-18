import abc
{%- if cookiecutter.add_repository_and_sqlalchemy | fix_boolean %}
from {{cookiecutter.package_name}}.application.interfaces.repository import UOWService
{%- endif %}


class Factory(abc.ABC):  # pylint: disable=too-few-public-methods
    """Abstract factory for Payment Gateway."""

{%- if cookiecutter.add_repository_and_sqlalchemy | fix_boolean %}
    @abc.abstractmethod
    def make_uow_service(self) -> UOWService:
        """Create an instance of UOWService.

        Returns:
            UOWService.
        """
{% endif %}
