#!/usr/bin/env python3
"""
Module for filtering and obfuscating PII fields in log messages.
"""
import re
import logging
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection
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


def get_db() -> MySQLConnection:
    """
    Connects to a secure MySQL database using environment variables.

    Returns:
        A MySQLConnection object connected to the database
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME')

    connection = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )

    return connection


def main() -> None:
    """
    Main function to retrieve and display filtered user data from database.

    Obtains a database connection, retrieves all rows from the users table,
    and displays each row with PII fields filtered.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")

    logger = get_logger()

    column_names = [desc[0] for desc in cursor.description]

    for row in cursor:
        message = "; ".join(f"{column_names[i]}={row[i]}"
                           for i in range(len(row))) + ";"
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
