#!/usr/bin/env python3
"""
Test the logger with sample data
"""

import logging

get_logger = __import__('filtered_logger').get_logger

logger = get_logger()

# Test logging with PII data
logger.info("name=John Doe;email=john@example.com;phone=123-456-7890;ssn=123-45-6789;password=secret123;age=30;")
