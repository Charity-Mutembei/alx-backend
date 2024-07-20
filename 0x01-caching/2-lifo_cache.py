#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the LIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache using LIFO algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the last item put in cache (LIFO)
                last_key = next(reversed(self.cache_data))
                self.cache_data.pop(last_key)
                print(f"DISCARD: {last_key}")

            # Add the item to cache_data
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
