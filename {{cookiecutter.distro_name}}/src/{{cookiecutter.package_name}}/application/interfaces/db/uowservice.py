import abc

from {{cookiecutter.package_name}}.application.interfaces.db.uow import UnitOfWork


class UOWService(abc.ABC):  # pylint: disable=R0903
    """Abstract Unit Of Work Service.

    It provides a mechanism to create a unit of work, basically a transaction.
    """

    @abc.abstractmethod
    def get_uow(self) -> UnitOfWork:
        """Return a unit of work.

        The intended use is:

            uow_service = SomeConcreteUOWService()
            with uow_service.get_uow() as uow:
                foo_instance = Foo(...)
                uow.foo_repo.create(foo_instance)
                uow.commit()

        Returns:
            UnitOfWork
        """

    @abc.abstractmethod
    def init_db(self) -> None:
        """Initialises the database.

        This is a convenience method. Strictly speaking this doesn't belong to UOWService, but for
        a small project, it's better to have it here rather than creating another service. Once
        the project has growth to require migrations, this method can be removed.
        """

    @abc.abstractmethod
    def terminate(self) -> None:
        """Terminate Unit of Work Service.

        DB resources are freed, and after this, no more UOW can be retrieved.
        """
