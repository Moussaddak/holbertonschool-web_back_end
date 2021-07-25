#!/usr/bin/python3
""""4. MRU Caching
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines:
      - caching system
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        itemKeys = self.cache_data.keys()
        numberOfItem = len(itemKeys)
        if key and item:
            if key in itemKeys:
                self.cache_data.pop(key)
            elif numberOfItem >= self.MAX_ITEMS and key not in itemKeys:
                ListKeys = list(itemKeys)
                firstItem = ListKeys[-1]
                self.cache_data.pop(firstItem)
                print("DISCARD: {}".format(firstItem))
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        itemKeys = self.cache_data.keys()
        if key in itemKeys:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
        return self.cache_data.get(key, None)
