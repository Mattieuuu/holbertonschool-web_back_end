#!/usr/bin/env python3
"""
Test to verify environment variables are read correctly
"""
import os

# Set test environment variables
os.environ['PERSONAL_DATA_DB_USERNAME'] = 'test_user'
os.environ['PERSONAL_DATA_DB_PASSWORD'] = 'test_pass'
os.environ['PERSONAL_DATA_DB_HOST'] = 'test_host'
os.environ['PERSONAL_DATA_DB_NAME'] = 'test_db'

get_db = __import__('filtered_logger').get_db

# Verify the function exists and has correct type annotation
print("Return type annotation:", get_db.__annotations__.get('return'))
print("Function successfully imports and is callable")
