#!/usr/bin/env python3
"""Cache Module: provides a simple caching mechanism using Redis."""
import redis
from typing import Union, Optional, Callable, Any
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> any:
        """Wrap the original method, increment the call count
        return the method's result."""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """Decorator to store history of inputs and outputs."""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        
        self._redis.rpush(input_key, str(args))
        
        result = method(self, *args, **kwargs)
        
        self._redis.rpush(output_key, str(result))
        
        return result
    
    return wrapper


class Cache:
    """class for interacting with Redis to store data with random keys."""
    def __init__(self) -> None:
        """Initialize the Cache instance with a Redis client
        and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis using a randomly generated key.

        Args: data (Union[str, bytes, int, float]):
            The data to be stored in Redis.

        Returns:
            str: The randomly generated key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """Retrieve data from Redis and automatically convert it to a string.
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Retrieve data from Redis and automatically convert it to an integer.
        """
        return self.get(key, lambda x: int(x))
