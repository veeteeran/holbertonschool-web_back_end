#!/usr/bin/env python3
"""Redis Cache module"""
import redis
from typing import Union
from uuid import uuid4


class Cache():
    """Redis cache object"""
    def __init__(self):
        """Initialize a Cache object"""
        self._redis = redis.Redis()
        self._redis.flushdb()

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
