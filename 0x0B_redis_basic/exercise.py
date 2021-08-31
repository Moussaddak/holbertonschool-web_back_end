#!/usr/bin/env python3
""" Redis Cache File """
import redis
from typing import Union, Callable, Optional, Any
from functools import wraps
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """ Count calls decorator method """
    key = method.__qualname__

    @wraps(method)
    def counter(self, *args) -> bytes:
        self._redis.incr(key)
        return method(self, *args)

    return counter


def call_history(method: Callable) -> Callable:
    """ Stores the history of inputs and outputs """

    key = method.__qualname__

    @wraps(method)
    def history(self, *args) -> bytes:
        self._redis.rpush(f'{key}:inputs', str(args))
        data = method(self, *args)
        self._redis.rpush(f'{key}:outputs', data)
        return data

    return history


def replay(obj: Union[Callable, str]) -> None:
    """ Returns a printed history of inputs and outputs """
    cls = obj.__self__

    call_count = str(cls.get(cls.store.__qualname__), 'UTF-8')
    inputs = cls._redis.lrange(f"{cls.store.__qualname__}:inputs", 0, -1)
    outputs = cls._redis.lrange(f"{cls.store.__qualname__}:outputs", 0, -1)

    print(f'{obj.__qualname__} was called {call_count} times:')

    for input, output in zip(inputs, outputs):
        input, output = str(input, 'UTF-8'), str(output, 'UTF-8')
        print(f'{obj.__qualname__}(*{input}) -> {output}')


class Cache:
    """ Redis Caching class """

    def __init__(self):
        """ Initializes the Cache session """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Adds data to redis database """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """ fetch data from the redis client by key """
        data = self._redis.get(key)
        return data if not callable(fn) else fn(data)

    def get_int(self, key: str) -> int:
        """ returns the key as an int value """
        return int(self._redis.get(key))

    def get_str(self, key: str) -> str:
        """ returns the key as a string value """
        # return str(self._redis.get(key), 'UTF-8')
        return self._redis.get(key).decode('utf-8')


# cache = Cache()
# cache.store("foo")
# cache.store("bar")
# cache.store(42)
# replay(cache.store)
