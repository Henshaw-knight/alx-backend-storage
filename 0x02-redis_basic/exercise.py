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
