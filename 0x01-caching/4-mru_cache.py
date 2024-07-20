#!/usr/bin/python3
""" MRUCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the MRUCache
        """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache using MRU algorithm
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update the item and move it to the end of the OrderedDict
                self.cache_data[key] = item
                self.order.move_to_end(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    most_recent_key, _ = self.order.popitem(last=True)
                    self.cache_data.pop(most_recent_key)
                    print(f"DISCARD: {most_recent_key}")

                # Add the new item to cache_data and order
                self.cache_data[key] = item
                self.order[key] = None

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        if key in self.cache_data:
            self.order.move_to_end(key)
            return self.cache_data[key]
        return None
