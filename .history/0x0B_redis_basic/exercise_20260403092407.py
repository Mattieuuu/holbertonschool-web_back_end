#!/usr/bin/env python3
"""Redis basic cache module.

This module defines a Cache class that stores values in Redis
using randomly generated keys.
"""
import uuid
from typing import Callable, Optional, TypeVar, Union

import redis


T = TypeVar("T")


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

    def get(
        self,
        key: str,
        fn: Optional[Callable[[bytes], T]] = None,
    ) -> Optional[Union[bytes, T]]:
        """Retrieve data from Redis and optionally convert it.

        Args:
            key (str): Redis key to retrieve.
            fn (Optional[Callable[[bytes], T]]): Optional conversion callable.

        Returns:
            Optional[Union[bytes, T]]: Raw bytes, converted value, or None.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is None:
            return data
        return fn(data)

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a UTF-8 string value from Redis.

        Args:
            key (str): Redis key to retrieve.

        Returns:
            Optional[str]: Decoded string value, or None.
        """
        return self.get(key, fn=lambda data: data.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer value from Redis.

        Args:
            key (str): Redis key to retrieve.

        Returns:
            Optional[int]: Integer value, or None.
        """
        return self.get(key, fn=int)
