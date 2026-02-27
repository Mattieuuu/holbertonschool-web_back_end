#!/usr/bin/env python3
"""
Module for filtering and obfuscating PII fields in log messages.
"""
import re
import logging
from typing import List, Tuple


PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields: List of strings representing fields to obfuscate
        redaction: String to replace field values with
        message: Log line string to process
        separator: Character separating fields in the log line

    Returns:
        The log message with specified fields obfuscated
    """
    pattern = f"({'|'.join(fields)})=([^{separator}]*)"
    return re.sub(pattern, f"\\1={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the formatter with fields to redact."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format log record and redact sensitive fields."""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger for user data.

    Returns:
        A logging.Logger object configured to log user data with PII redaction
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=list(PII_FIELDS)))

    logger.addHandler(stream_handler)

    return logger
