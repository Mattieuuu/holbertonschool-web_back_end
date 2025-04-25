#!/usr/bin/env python3
"""
Module that spawns Tasks n times with a specified delay
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with specified max_delay.
    Returns list of delays in ascending order.

    Args:
        n (int): number of times to spawn task_wait_random
        max_delay (int): maximum delay in seconds

    Returns:
        List[float]: list of delays in ascending order
    """
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
