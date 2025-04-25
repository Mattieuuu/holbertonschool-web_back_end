#!/usr/bin/env python3
"""
This module defines a function that returns list of tuples containing 
sequence and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains a sequence and its length
    Args:
        lst (Iterable[Sequence]): iterable containing sequences
    Returns:
        List[Tuple[Sequence, int]]: list of tuples (sequence, length)
    """
    return [(i, len(i)) for i in lst]
