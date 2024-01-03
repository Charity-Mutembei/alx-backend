#!/usr/bin/python3
""" LRUCaching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching and
    is a caching system using LRU algorithm
    """

    def __init__(self):
        """ Initialize the LRU cache
        """
        super().__init__()
        self.order_of_access = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Discard the least recently used item (LRU)
                lru_key = self.order_of_access.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD: {}".format(lru_key))

            self.cache_data[key] = item
            self.order_of_access.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            if key in self.cache_data:
                # Update the order of access
                self.order_of_access.remove(key)
                self.order_of_access.append(key)
                return self.cache_data[key]
        return None
