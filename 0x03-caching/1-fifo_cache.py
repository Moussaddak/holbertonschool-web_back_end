#!/usr/bin/python3
""" 1. FIFO caching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
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
            if numberOfItem >= self.MAX_ITEMS and key not in itemKeys:
                ListKeys = list(itemKeys)
                firstItem = ListKeys[0]
                self.cache_data.pop(firstItem)
                print("DISCARD: {}".format(firstItem))
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
