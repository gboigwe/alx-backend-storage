#!/usr/bin/env python3
"""Module for Redis and Python interaction"""
import uuid
from functools import wraps
from typing import Callable, Union
import redis


def count_calls(method: Callable) -> Callable:
    """Decorator to track the number of times a method is invoked"""
    key = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to increment
        the call count and execute the method
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to log input parameters and return values of a function"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to record function calls and their results"""
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        output = method(self, *args, **kwargs)
        self._redis.rpush(input_key, str(args))
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


def replay(fn: Callable):
    """Function to display the call history of a specific function"""
    r = redis.Redis()
    f_name = fn.__qualname__
    n_calls = r.get(f_name)
    try:
        n_calls = n_calls.decode('utf-8')
    except Exception:
        n_calls = 0
    print(f'{f_name} was called {n_calls} times:')
    ins = r.lrange(f_name + ":inputs", 0, -1)
    outs = r.lrange(f_name + ":outputs", 0, -1)
    for i, o in zip(ins, outs):
        try:
            i = i.decode('utf-8')
        except Exception:
            i = ""
        try:
            o = o.decode('utf-8')
        except Exception:
            o = ""
        print(f'{f_name}(*{i}) -> {o}')


class Cache():
    """Class for managing a Redis-based caching system"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method to store data in the cache
        Args:
            data (Union[str, bytes, int, float]): Data to be stored
        Returns:
            str: Unique identifier for the stored data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None)\
            -> Union[str, bytes, int, float]:
        """Retrieve data from the cache and
        optionally apply a conversion function
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Retrieve and convert cached data to a string"""
        variable = self._redis.get(key)
        return variable.decode("UTF-8")

    def get_int(self, key: str) -> int:
        """Retrieve and convert cached data to an integer"""
        variable = self._redis.get(key)
        try:
            variable = int(variable.decode("UTF-8"))
        except Exception:
            variable = 0
        return variable
