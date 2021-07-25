#!/usr/bin/env python3
"""0. Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - caching system
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if (key or item) is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
