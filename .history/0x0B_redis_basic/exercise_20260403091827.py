#!/usr/bin/env python3
"""Redis basic cache module.

This module defines a Cache class that stores values in Redis
using randomly generated keys.
"""
import uuid
from typing import Union

import redis


class Cache:
    """Cache class for storing typed values in Redis."""

    def __init__(self) -> None:
        """Initialize a Redis client and clear the current database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis under a random key and return the key.

        Args:
            data (Union[str, bytes, int, float]): Input value to cache.

        Returns:
            str: Generated key used to store the value.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
