#!/usr/bin/env python3
"""
This module defines a function that sums a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floating point numbers
    Args:
        input_list (List[float]): list of floats to sum
    Returns:
        float: Sum of all numbers in input_list
    """
    return sum(input_list)
