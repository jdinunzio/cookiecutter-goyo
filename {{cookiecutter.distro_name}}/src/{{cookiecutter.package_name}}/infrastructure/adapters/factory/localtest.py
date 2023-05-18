from {{cookiecutter.package_name}}.application.interfaces.factory import Factory
{%- if cookiecutter.add_repository_and_sqlalchemy | fix_boolean %}
from {{cookiecutter.package_name}}.application.interfaces.repository import UOWService
{%- endif %}


class LocalTestFactory(Factory):  # pylint: disable=too-few-public-methods
    """Factory for local tests."""

{%- if cookiecutter.add_repository_and_sqlalchemy | fix_boolean %}
    def make_uow_service(self) -> UOWService:
        """Create an instance of UOWService.

        Returns:
            UOWService.
        """
        raise NotImplementedError()
{% endif %}
