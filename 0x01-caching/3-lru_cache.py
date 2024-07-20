#!/usr/bin/python3
""" LRUCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the LRUCache
        """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache using LRU algorithm
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update the item and move it to the end of the OrderedDict
                self.cache_data[key] = item
                self.order.move_to_end(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    oldest_key, _ = self.order.popitem(last=False)
                    self.cache_data.pop(oldest_key)
                    print(f"DISCARD: {oldest_key}")

                # Add the new item to cache_data and order
                self.cache_data[key] = item
                self.order[key] = None

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        if key in self.cache_data:
            # Move the accessed item to the end of the OrderedDict
            self.order.move_to_end(key)
            return self.cache_data[key]
        return None
