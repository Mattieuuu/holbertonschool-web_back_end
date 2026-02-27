#!/usr/bin/env python3
"""
Module for filtering and obfuscating PII fields in log messages.
"""
import re
import logging
from typing import List


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
