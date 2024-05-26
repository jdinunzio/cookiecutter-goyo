from {{cookiecutter.package_name}}.domain import TodoList
from {{cookiecutter.package_name}}.infrastructure.adapters.alchemy.models import TodoListRecord


class TodoListMapper:
    """Map between TodoList domain models and SQLAlchemy records."""

    @staticmethod
    def record_from_model(model: TodoList) -> TodoListRecord:
        """Convert TodoList domain model into SQLAlchemy TodoListRecord."""
        return TodoListRecord(**model.dict())

    @staticmethod
    def model_from_record(record: TodoListRecord) -> TodoList:
        """Convert SQLAlchemy TodoListRecord into TodoList domain model."""
        model = TodoList.model_validate(record)
        return model
