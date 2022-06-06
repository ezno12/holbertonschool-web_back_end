#!/usr/bin/env python3
"""
modul for Redis tasks
"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """
    cache class
    """
    def __init__(self) -> None:
        """init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
