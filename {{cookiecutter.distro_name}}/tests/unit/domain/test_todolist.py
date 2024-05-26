import uuid
from datetime import datetime, timedelta
from unittest import TestCase

import pytz

from {{cookiecutter.package_name}}.domain.todolist import TodoList


class TestTodoList(TestCase):
    """Unit test for To-do List domain object."""

    def test_default_values(self) -> None:
        """Instance is created with default values."""
        # when an instance has been created only with required fields
        desc = "some description"
        model = TodoList(description=desc)
        # then optional fields have proper values too
        self.assertIsInstance(model.id, uuid.UUID)
        now = datetime.now(pytz.UTC)
        self.assertLess(now - model.created_at, timedelta(seconds=1))
        self.assertEqual(model.todos, [])
        self.assertIsNone(model.completed_at)
        self.assertIsNone(model.deleted_at)
