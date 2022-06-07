#!/usr/bin/env python3
"""
modul for Redis tasks
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
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
    store the history of inputs and outputs for a particular function.
    """
    inputKey = method.__qualname__ + ":inputs"
    outputKey = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        """
        self._redis.rpush(inputKey, str(args))
        value = method(self, *args, *kwds)
        self._redis.rpush(outputKey, str(value))
        return value
    return wrapper


def replay(fn: Callable) -> str:
    """Retrieving lists"""
    method = fn.__qualname__
    inputs = f"{method}:inputs"
    outputs = f"{method}:outputs"
    input_list = fn.__self__._redis.lrange(inputs, 0, -1)
    output_list = fn.__self__._redis.lrange(outputs, 0, -1)
    ValueKey = fn.__self__._redis.get(method).decode('utf-8')
    print(f"{method} was called {ValueKey} times:")
    for inp, out in zip(input_list, output_list):
        print(f"{method}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")


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

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
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
