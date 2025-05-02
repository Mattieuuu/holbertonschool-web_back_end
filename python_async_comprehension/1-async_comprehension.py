#!/usr/bin/env python3
"""
Module that collects 10 random numbers using async comprehension.
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension.

    Returns:
        List[float]: List of 10 random float numbers.
    """
    return [number async for number in async_generator()]