#!/usr/bin/env python3
"""
This module defines a function that returns a multiplication function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float by multiplier
    Args:
        multiplier (float): number to multiply by
    Returns:
        Callable[[float], float]: Function that takes a float and returns a float
    """
    def multiplier_function(n: float) -> float:
        return n * multiplier
    return multiplier_function
