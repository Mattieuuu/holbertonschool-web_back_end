#!/usr/bin/env python3
"""
Module that creates an asyncio.Task from a coroutine
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for the wait_random coroutine

    Args:
        max_delay (int): maximum delay in seconds to wait

    Returns:
        asyncio.Task: Task that will execute the wait_random coroutine
    """
    return asyncio.create_task(wait_random(max_delay))
