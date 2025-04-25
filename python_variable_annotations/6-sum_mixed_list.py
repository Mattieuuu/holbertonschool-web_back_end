#!/usr/bin/env python3
"""
This module defines a function that sums a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floating point numbers
    Args:
        mxd_lst (List[Union[int, float]]): list of ints and floats to sum
    Returns:
        float: Sum of all numbers in mxd_lst
    """
    return float(sum(mxd_lst))
