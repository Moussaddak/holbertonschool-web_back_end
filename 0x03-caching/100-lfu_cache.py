#!/usr/bin/python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ a caching system
    """
    hitRate = {}

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            itemKeys = self.cache_data.keys()
            numberOfItem = len(itemKeys)
            if key not in self.hitRate:
                self.hitRate[key] = self.hitRate.get(key, -1)
            self.hitRate[key] = self.hitRate.get(key) + 1
            if numberOfItem == BaseCaching.MAX_ITEMS and key not in itemKeys:
                droppedKey = min(self.hitRate, key=self.hitRate.get)
                if droppedKey == key:
                    self.hitRate.pop(droppedKey)
                    droppedKey = min(self.hitRate, key=self.hitRate.get)
                    self.hitRate[key] = 0
                print("DISCARD: {}".format(droppedKey))
                self.cache_data.pop(droppedKey)
                self.hitRate.pop(droppedKey)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        itemKeys = self.cache_data.keys()
        if key in itemKeys:
            self.hitRate[key] += 1
        return self.cache_data.get(key, None)
