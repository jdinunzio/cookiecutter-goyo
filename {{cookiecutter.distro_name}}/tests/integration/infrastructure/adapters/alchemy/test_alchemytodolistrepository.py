import uuid
from datetime import datetime
from unittest import TestCase

import pytz

from {{cookiecutter.package_name}}.application.exceptions import RecordNotFoundError
from {{cookiecutter.package_name}}.domain import TodoList, TodoListPartial
from tests.integration.infrastructure.adapters.alchemy.alchemymixin import AlchemyMixin


class TestAlchemyTodoListRepository(TestCase, AlchemyMixin):
    """Test TodoListRepository."""

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

    def test_instance_creation_and_get_ok(self) -> None:
        """Instance can be created and gotten."""
        # given a successful instance creation
        todo_list, created = self.create_and_persist_todolist()
        self.assertEqual(todo_list, created)

        # when attempting to retrieve the persisted instance
        retrieved = self.get_todo_list(todo_list.id)

        # then, it is found and it's equal to the previously created one
        self.assertEqual(created, retrieved)

    def test_instance_creation_rollback(self) -> None:
        """Rollback during creation doesn't persist the instance."""
        # given the creation of a todo_list has been rolled back
        todo_list = self.new_todolist()
        with self.uow as uow:
            repo = uow.todolist_repo
            repo.create(todo_list)
            uow.rollback()

        # when attempting to retrieve the instance
        retrieved = self.get_todo_list(todo_list.id)

        # then nothing is found
        self.assertIsNone(retrieved)

    def test_retrieval_ok(self) -> None:
        """Retrieval should not include deleted lists."""
        # given we've persisted some todo_lists
        list_dicts = [{}, {"deleted_at": datetime.now(pytz.UTC)}, {}]
        _ = [self.new_todolist(**dct) for dct in list_dicts]

        # when we retrieve todo_lists
        with self.service.get_uow() as uow:
            repo = uow.todolist_repo
            retrieved_todo_lists = repo.retrieve()
            uow.commit()

        # then we don't get deleted lists
        self.assertTrue(all(x.deleted_at is None for x in retrieved_todo_lists))

    def test_delete_non_existent_raises(self) -> None:
        """Trying to delete a non-existent entity raises."""
        # given an uuid for a non-existent todo-list
        todolist_id = uuid.uuid4()

        # when trying to delete it
        with self.uow as uow, self.assertRaises(RecordNotFoundError):
            uow.todolist_repo.delete(todolist_id)

    def test_delete_ok(self) -> None:
        """Deleting a record sets its deleted_at datetime."""
        # given a todolist exists
        todo_list, _ = self.create_and_persist_todolist()

        # when it's deleted
        with self.service.get_uow() as uow:
            repo = uow.todolist_repo
            repo.delete(todo_list.id)
            uow.commit()

        # then it's `deleted_at` has been set
        with self.service.get_uow() as uow:
            repo = uow.todolist_repo
            retrieved = repo.get(todo_list.id)
            uow.commit()

        assert retrieved is not None  # makes mypy happy
        self.assertIsNotNone(retrieved.deleted_at)

    def test_update_non_existent_raises(self) -> None:
        """Trying to update a non-existent entity raises."""
        # given an uuid for a non-existent todo-list
        todolist_id = uuid.uuid4()
        fake_update = TodoListPartial(**self.new_todolist().model_dump())

        # when trying to delete it
        with self.service.get_uow() as uow, self.assertRaises(RecordNotFoundError):
            uow.todolist_repo.update(todolist_id, fake_update)

    def test_update_ok(self) -> None:
        """Instance can be updated."""
        # given an existing instance
        todo_list, _ = self.create_and_persist_todolist()

        # when attempting to retrieve the persisted instance
        patch = TodoListPartial(description="this description was updated")
        with self.service.get_uow() as uow:
            updated_todo_list = uow.todolist_repo.update(todo_list.id, patch)

        # then the resulting TodoList has the patched fields updated
        patch_dict = patch.model_dump(exclude_unset=True)
        updated_dict = updated_todo_list.model_dump(include=patch_dict)
        self.assertEqual(updated_dict, patch_dict)
        # and the remaining fields were not modified
        original_unchanged = todo_list.model_dump(exclude=set(patch_dict.keys()))
        updated_unchanged = updated_todo_list.model_dump(exclude=set(patch_dict.keys()))
        self.assertEqual(updated_unchanged, original_unchanged)

    # Support methods

    def get_todo_list(self, todo_list_id: uuid.UUID) -> TodoList | None:
        """Return a TodoList or None gathered from the repository.

        Args:
            todo_list_id: Id of the TodoList to return.

        Returns:
            The TodoList, if exists, None in other case.
        """
        with self.service.get_uow() as uow:
            repo = uow.todolist_repo
            retrieved = repo.get(todo_list_id)
            uow.commit()
        return retrieved
