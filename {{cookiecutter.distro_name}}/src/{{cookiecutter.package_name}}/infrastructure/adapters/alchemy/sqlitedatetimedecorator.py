# ruff: noqa: ANN401
import datetime
from typing import Any

from sqlalchemy import DateTime, TypeDecorator
from sqlalchemy.dialects.sqlite.base import SQLiteDialect


class TZDateTime(TypeDecorator):  # pylint: disable=W0223,R0901
    """Type decorator for SQLite to guarantee timezones are preserved.

    SQLite doesn't have a native datetime type, and the timezone is not persisted. When a record
    with datetime is retrieved, it's returned as a naive datetime. To prevent that, we define this
    type decorator that intercept records in the way in, normalise datetimes to UTC, and in their
    way out, UTC timezone is added to the (now naive) datetimes.
    """

    impl = DateTime
    cache_ok = True

    def process_bind_param(self, value: Any | None, dialect: object) -> Any | None:
        """Convert datetime to UTC and strip timezone, only for SQLite."""
        if not isinstance(dialect, SQLiteDialect):
            return value
        if value is not None:
            if not value.tzinfo or value.tzinfo.utcoffset(value) is None:
                raise TypeError("tzinfo is required")
            value = value.astimezone(datetime.timezone.utc).replace(tzinfo=None)
        return value

    def process_result_value(self, value: Any | None, dialect: object) -> Any | None:
        """Add UTC timezone to (naive) datetime to UTC, only for SQLite."""
        if not isinstance(dialect, SQLiteDialect):
            return value
        if value is not None:
            value = value.replace(tzinfo=datetime.timezone.utc)
        return value
