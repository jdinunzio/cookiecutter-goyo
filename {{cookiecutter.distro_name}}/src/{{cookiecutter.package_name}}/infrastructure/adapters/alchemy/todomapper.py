from uuid import UUID

from {{cookiecutter.package_name}}.domain import Todo
from {{cookiecutter.package_name}}.infrastructure.adapters.alchemy.models import TodoRecord


class TodoMapper:
    """Map between TO-DO domain models and SQLAlchemy records."""

    @staticmethod
    def record_from_model(model: Todo, todolist_id: UUID) -> TodoRecord:
        """Convert Todo domain model into SQLAlchemy Record."""
        return TodoRecord(todolist_id=todolist_id, **model.dict())

    @staticmethod
    def model_from_record(record: TodoRecord) -> Todo:
        """Convert SQLAlchemy TodoRecord into TO-DO domain model."""
        model = Todo.model_validate(record)
        return model
