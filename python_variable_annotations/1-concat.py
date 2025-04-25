#!/usr/bin/env python3
"""
This module defines a function to concatenate two strings using type annotations.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the result
    Args:
        str1 (str): first string
        str2 (str): second string
    Returns:
        str: Concatenated string of str1 and str2
    """
    return str1 + str2
