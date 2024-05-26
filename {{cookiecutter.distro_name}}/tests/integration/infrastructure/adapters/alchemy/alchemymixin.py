import uuid
from pathlib import Path
from random import randint

from {{cookiecutter.package_name}}.application.interfaces import UOWService
from {{cookiecutter.package_name}}.domain import TodoList
from {{cookiecutter.package_name}}.infrastructure.adapters import config
from {{cookiecutter.package_name}}.infrastructure.adapters.factory import SimpleEnvFactory


class AlchemyMixin:
    """Mixin class for SQLAlchemy related integration tests."""

    service: UOWService
    db_file_name = config.SQLITE_DB_FILE_NAME

    @classmethod
    def init_service(cls) -> None:
        """Initialise service and db."""
        cls.service = SimpleEnvFactory().make_uow_service()
        cls.service.init_db()

    @classmethod
    def delete_db(cls) -> None:
        """Delete db if exits."""
        cls.service.terminate()
        db_path = Path(cls.db_file_name)
        if db_path.exists():
            db_path.unlink()

    def create_and_persist_todolist(self, **kwargs: object) -> tuple[TodoList, TodoList]:
        """Create a new TodoList and persist it in the repository.

        Args:
            kwargs: Properties to set on the TodoList.

        Returns:
            tuple with the entity sent to the repository for creation, and the returned one.
        """
        todo_list = self.new_todolist(**kwargs)
        with self.service.get_uow() as uow:
            repo = uow.todolist_repo
            created = repo.create(todo_list)
            uow.commit()
        return todo_list, created

    @staticmethod
    def new_todolist(**kwargs: object) -> TodoList:
        """Return a newly created TodoList."""
        random_int = randint(0, 100)  # noqa: S311
        return TodoList(
            id=uuid.uuid4(),
            description=f"some description {random_int}",
            **kwargs,  # type: ignore
        )
