#!/usr/bin/env python3
"""Redis basic cache module.

This module defines a Cache class that stores values in Redis
using randomly generated keys.
"""
import uuid
from functools import wraps
from typing import Any, Callable, Optional, TypeVar, Union

import redis


T = TypeVar("T")


def count_calls(method: Callable) -> Callable:
    """Count and store the number of times a Cache method is called.

    Args:
        method (Callable): Cache instance method to wrap.

    Returns:
        Callable: Wrapped method that increments call count in Redis.
    """

    @wraps(method)
    def wrapper(self, *args: Any, **kwargs: Any) -> Any:
        """Increment Redis counter and execute wrapped method."""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Store history of inputs and outputs for a Cache method.

    Args:
        method (Callable): Cache instance method to wrap.

    Returns:
        Callable: Wrapped method that records inputs and outputs in Redis.
    """

    @wraps(method)
    def wrapper(self, *args: Any, **kwargs: Any) -> Any:
        """Record method call arguments and output in Redis lists."""
        inputs_key = "{}:inputs".format(method.__qualname__)
        outputs_key = "{}:outputs".format(method.__qualname__)
        self._redis.rpush(inputs_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, output)
        return output

    return wrapper


class Cache:
    """Cache class for storing typed values in Redis."""

    def __init__(self) -> None:
        """Initialize a Redis client and clear the current database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
