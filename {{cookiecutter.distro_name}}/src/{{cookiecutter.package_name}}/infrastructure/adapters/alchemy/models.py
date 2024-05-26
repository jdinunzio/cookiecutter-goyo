# pylint: disable=too-few-public-methods
import uuid
from datetime import datetime

from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from {{cookiecutter.package_name}}.infrastructure.adapters.alchemy.sqlitedatetimedecorator import TZDateTime


class BaseSQLRecord(DeclarativeBase):
    """Base class for all SQLAlchemy models."""


class TodoListRecord(BaseSQLRecord):
    """SQLAlchemy model for TO-DO List entities."""

    __tablename__ = "todolists"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(120))
    todos: Mapped[list["TodoRecord"]] = relationship(
        back_populates="todolist", cascade="all, delete-orphan"
    )
    created_at: Mapped[datetime] = mapped_column(
        TZDateTime(timezone=True), server_default=func.now()  # pylint: disable=E1102
    )
    completed_at: Mapped[datetime | None] = mapped_column(TZDateTime(timezone=True), nullable=True)
    deleted_at: Mapped[datetime | None] = mapped_column(TZDateTime(timezone=True), nullable=True)


class TodoRecord(BaseSQLRecord):
    """SQLAlchemy model for TO-DO entities."""

    __tablename__ = "todos"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    todolist_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("todolists.id"))
    todolist: Mapped["TodoListRecord"] = relationship(back_populates="todos")
    description: Mapped[str] = mapped_column(String(120))
    created_at: Mapped[datetime] = mapped_column(
        TZDateTime(timezone=True), server_default=func.now()  # pylint: disable=E1102
    )
    completed_at: Mapped[datetime | None] = mapped_column(TZDateTime(timezone=True), nullable=True)
    deleted_at: Mapped[datetime | None] = mapped_column(TZDateTime(timezone=True), nullable=True)
