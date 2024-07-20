#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the FIFOCache
        """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache using FIFO algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get the first item to discard (FIFO)
                oldest_key, _ = self.order.popitem(last=False)
                self.cache_data.pop(oldest_key)
                print(f"DISCARD: {oldest_key}")

            # Add the item to cache_data and order
            self.cache_data[key] = item
            self.order[key] = None

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
