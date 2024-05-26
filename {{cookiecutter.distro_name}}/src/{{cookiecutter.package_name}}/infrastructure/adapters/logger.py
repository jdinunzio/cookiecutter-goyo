import logging
from datetime import datetime

import pytz
from pythonjsonlogger import jsonlogger

# main logger for the application
logger = logging.getLogger("main")


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    """Custom Log Formatter to add datetime and log level."""

    def add_fields(
        self,
        log_record: dict,
        record: logging.LogRecord,
        message_dict: dict,
    ) -> None:
        """Add fields from the logging record to its JSON representation."""
        super().add_fields(log_record, record, message_dict)
        if not log_record.get("timestamp"):
            now = datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            log_record["timestamp"] = now
        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname


def init_logging(log_level: str) -> logging.Logger:
    """Initialise logging with the given log level and using JSON format.

    Args:
        log_level: Log level.

    Returns:
        logger.
    """
    log_level_number = logging.getLevelName(log_level.upper())
    logger.setLevel(log_level_number)
    log_handler = logging.StreamHandler()
    formatter = CustomJsonFormatter("%(timestamp)s %(level)s %(name)s %(pathname)s %(message)s")
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    return logger
