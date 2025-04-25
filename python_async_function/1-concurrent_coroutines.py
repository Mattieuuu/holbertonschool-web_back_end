#!/usr/bin/env python3
"""
Module that contains an asynchronous coroutine that spawns wait_random n times
with the specified max_delay and returns the list of all delays.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with the specified max_delay.
    Returns the list of all delays in ascending order.

    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay in seconds

    Returns:
        List[float]: List of delays in ascending order
    """
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
