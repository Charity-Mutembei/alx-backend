#!/usr/bin/python3
"""
creating a class BasicCache that inherits from
BaseCaching and is caching system. And it inherit
from base_caching.py
"""

BasicCaching = __import__('base_caching').BaseCaching


class BasicCache(BasicCaching):
    """
    that inherits the BasicCaching classs
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
