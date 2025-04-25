#!/usr/bin/env python3
"""
This module defines a function that creates a tuple from a string and number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple from a string and the square of a number
    Args:
        k (str): string to use as first element
        v (Union[int, float]): number to square for second element
    Returns:
        Tuple[str, float]: Tuple containing k and square of v
    """
    return (k, float(v ** 2))
