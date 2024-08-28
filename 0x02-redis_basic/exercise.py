#!/usr/bin/env python3
"""Cache Module: provides a simple caching mechanism using Redis."""
import redis
from typing import Union
import uuid


class Cache:
    """class for interacting with Redis to store data with random keys."""
    def __init__(self) -> None:
        """Initialize the Cache instance with a Redis client
        and flush the database."""
        self.__redis = redis.Redis()
        self.__redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis using a randomly generated key.

        Args: data (Union[str, bytes, int, float]):
            The data to be stored in Redis.

        Returns:
            str: The randomly generated key used to store the data.
        """
        key = str(uuid.uuid4())
        self.__redis.set(key, data)
        return key
