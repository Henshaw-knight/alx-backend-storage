#!/usr/bin/env python3
"""Cache class module"""
import redis
import uuid
from typing import Union


class Cache:
    """Writes strings to Redis"""
    def __init__(self):
        """Stores an instance of the Redis client as a private variable"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key and stores the input `data` in Redis
        Returns:
          the random key
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key, fn=None):
        """Takes in a `key` string argument and an optional Callable args `fn`.
        The callable will be used to convert the data back to the desired
        format. If key does not exist, the original Redis.get method is used
        """
        value = self._redis.get(key)
        if (value is not None) and (fn is not None):
            try:
                int_repr = int(value.decode("utf-8"))
                return fn(int_repr)
            except ValueError:
                return fn(value)
        else:
            return value

    def get_str(self, string_value):
        """Returns the converted string data value format"""
        return string_value

    def get_int(self, int_value):
        """Returns the converted integer data value format"""
        return int_value
