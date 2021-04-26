#!/usr/bin/env python3
"""Redis tasks"""
import redis
from typing import Union
from uuid import uuid4


class Cache():
    """Redis cache object"""
    def __init__(self):
        """Initialize a Cache object"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, float, int, str]) -> str:
        """Generate random uuid key, store data in key, return key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
