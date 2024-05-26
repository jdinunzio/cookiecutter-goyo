import uuid
from datetime import datetime
from random import randint
from unittest import TestCase

import pytz

from {{cookiecutter.package_name}}.application.exceptions import RecordNotFoundError
from {{cookiecutter.package_name}}.domain import Todo, TodoPartial
from tests.integration.infrastructure.adapters.alchemy.alchemymixin import AlchemyMixin


class TestAlchemyTodoRepository(TestCase, AlchemyMixin):
    """Test TodoRepository."""

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
        todolist, _ = self.create_and_persist_todolist()
        todo, created = self.create_and_persist_todo(todolist.id)
        self.assertEqual(todo, created)

        # when attempting to retrieve the persisted instance
        retrieved = self.get_todo(todo.id)

        # then, it is found and it's equal to the previously created one
        self.assertEqual(created, retrieved)

    def test_instance_creation_rollback(self) -> None:
        """Rollback during creation doesn't persist the instance."""
        # given the creation of a TO-DO has been rolled back
        todolist, _ = self.create_and_persist_todolist()
        todo = self.new_todo()
        with self.uow as uow:
            repo = uow.todo_repo
            repo.create(todolist.id, todo)
            uow.rollback()

        # when attempting to retrieve the instance
        retrieved = self.get_todo(todo.id)

        # then nothing is found
        self.assertIsNone(retrieved)

    def test_retrieval_ok(self) -> None:
        """Retrieval should not include deleted lists."""
        # given we've persisted some todos
        todolist, _ = self.create_and_persist_todolist()
        list_dicts = [{}, {"deleted_at": datetime.now(pytz.UTC)}, {}]
        _ = [self.new_todo(todolist_id=todolist.id, **dct) for dct in list_dicts]

        # when we retrieve todos
        with self.service.get_uow() as uow:
            repo = uow.todo_repo
            retrieved_todos = repo.retrieve(todolist.id)
            uow.commit()

        # then we don't get deleted lists
        self.assertTrue(all(x.deleted_at is None for x in retrieved_todos))

    def test_delete_non_existent_raises(self) -> None:
        """Trying to delete a non-existent entity raises."""
        # given an uuid for a non-existent TO-DO
        todo_id = uuid.uuid4()

        # when trying to delete it
        with self.uow as uow, self.assertRaises(RecordNotFoundError):
            uow.todo_repo.delete(todo_id)

    def test_delete_ok(self) -> None:
        """Deleting a record sets its deleted_at datetime."""
        # given a TO-DOo exists
        todolist, _ = self.create_and_persist_todolist()
        todo, _ = self.create_and_persist_todo(todolist.id)

        # when it's deleted
        with self.service.get_uow() as uow:
            repo = uow.todo_repo
            repo.delete(todo.id)
            uow.commit()

        # then it's `deleted_at` has been set
        with self.service.get_uow() as uow:
            repo = uow.todo_repo
            retrieved = repo.get(todo.id)
            uow.commit()

        assert retrieved is not None  # makes mypy happy
        self.assertIsNotNone(retrieved.deleted_at)

    def test_update_non_existent_raises(self) -> None:
        """Trying to update a non-existent entity raises."""
        # given an uuid for a non-existent TO-DO
        todo_id = uuid.uuid4()
        fake_update = TodoPartial(**self.new_todo().dict())

        # when trying to delete it
        with self.service.get_uow() as uow, self.assertRaises(RecordNotFoundError):
            uow.todo_repo.update(todo_id, fake_update)

    def test_update_ok(self) -> None:
        """Instance can be updated."""
        # given an existing instance
        todolist, _ = self.create_and_persist_todolist()
        todo, _ = self.create_and_persist_todo(todolist.id)

        # when attempting to retrieve the persisted instance
        patch = TodoPartial(description="this description was updated")
        with self.service.get_uow() as uow:
            updated_todo = uow.todo_repo.update(todo.id, patch)

        # then the resulting TO-DO has the patched fields updated
        patch_dict = patch.dict(exclude_unset=True)
        updated_dict = updated_todo.dict(include=patch_dict)
        self.assertEqual(updated_dict, patch_dict)
        # and the remaining fields were not modified
        original_unchanged = todo.dict(exclude=set(patch_dict.keys()))
        updated_unchanged = updated_todo.dict(exclude=set(patch_dict.keys()))
        self.assertEqual(updated_unchanged, original_unchanged)

    # Support methods

    def create_and_persist_todo(
        self, todolist_id: uuid.UUID, **kwargs: object
    ) -> tuple[Todo, Todo]:
        """Create a new TO-DO and persist it in the repository.

        Args:
            todolist_id: Id of the TodoList on which to persist this To-DO.
            kwargs: Properties to set on the To-DO.

        Returns:
            tuple with the entity sent to the repository for creation, and the returned one.
        """
        todo = self.new_todo(**kwargs)
        with self.service.get_uow() as uow:
            repo = uow.todo_repo
            created = repo.create(todolist_id, todo)
            uow.commit()
        return todo, created

    def get_todo(self, todo_id: uuid.UUID) -> Todo | None:
        """Return a TO-DO or None gathered from the repository.

        Args:
            todo_id: Id of the TO-DO to return.

        Returns:
            The TO-DO, if exists, None in other case.
        """
        with self.service.get_uow() as uow:
            repo = uow.todo_repo
            retrieved = repo.get(todo_id)
            uow.commit()
        return retrieved

    @staticmethod
    def new_todo(**kwargs: object) -> Todo:
        """Return a newly created Todo."""
        random_int = randint(0, 100)  # noqa: S311
        return Todo(
            id=uuid.uuid4(),
            description=f"some description {random_int}",
            **kwargs,  # type: ignore
        )
