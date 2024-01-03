#!/usr/bin/python3
""" MRUCaching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and
    is a caching system using MRU algorithm
    """

    def __init__(self):
        """ Initialize the MRU cache
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Discard the most recently used item (MRU)
                mru_key = max(self.cache_data, key=self.cache_data.get)
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))

            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
