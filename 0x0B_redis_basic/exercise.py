#!/usr/bin/env python3
"""
modul for Redis tasks
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method:Callable) -> Callable:
    """
    count each time Cache called decoretor
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    """
    inputKey = method.__qualname__ + ":inputs"
    outputKey = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        """
        self._redis.rpush(inputKey, str(args))
        value = method(self, *args, *kwds)
        return self._redis.rpush(outputKey, value)
    return wrapper


class Cache:
    """
    cache class
    """
    def __init__(self) -> None:
        """init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]: 
        """
        get a key of redis
        """
        if key:
            if fn:
                return fn(self._redis.get(key))
            else:
                return self._redis.get(key)

    def get_str(data: bytes) -> str:
        """
        convert date to string
        """
        return data.decode("utf-8")

    def get_int(data: bytes) -> int:
        """
        convert data to int
        """
        return int(data)
