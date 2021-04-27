#!/usr/bin/env python3
"""Redis Cache module"""
from functools import wraps
import redis
from typing import Callable, Optional, Union
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """Decorator to count number of times methods are called"""
    @wraps(method)
    def count_calls_wrapper(self, *args) -> bytes:
        """Counts number of calls wrapped function makes"""
        self._redis.incr(count_calls_wrapper.__qualname__)
        return method(self, *args)

    return count_calls_wrapper


def call_history(method):
    """Decorator to store the history of inputs and outputs for a function"""
    inputs = f"{method.__qualname__}:inputs"
    outputs = f"{method.__qualname__}:outputs"

    @wraps(method)
    def call_history_wrapper(self, *args) -> bytes:
        """Stores the history of inputs and outputs for a function"""
        self._redis.rpush(inputs, str(args))
        out = method(self, *args)
        self._redis.rpush(outputs, out)

        return out

    return call_history_wrapper


class Cache():
    """Redis cache object"""
    def __init__(self):
        """Initialize a Cache object"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate random uuid key, store data in key, return key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """get data based on key, return data as specified type based on fn"""
        if fn:
            value = self._redis.get(key)
            return fn(value)

        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """Typecast the key to a str"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Typecast the key to an int"""
        return self.get(key, int)
