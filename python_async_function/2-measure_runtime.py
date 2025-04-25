#!/usr/bin/env python3
"""
Module that measures the runtime of the wait_n coroutine
"""

import time
import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n

    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): maximum delay in seconds

    Returns:
        float: average time per execution
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
