#!/usr/bin/python3
""" LFUCaching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and is a
    caching system using LFU algorithm
    """

    def __init__(self):
        """ Initialize the LFU cache
        """
        super().__init__()
        self.frequency_counter = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Discard the least frequency used item (LFU)
                min_frequency = min(self.frequency_counter.values())
                candidates = [k for k, v
                              in self.frequency_counter.items()
                              if v == min_frequency]

                if len(candidates) > 1:
                    # Use LRU algorithm to break ties
                    lru_key = min(self.cache_data,
                                  key=lambda k:
                                  self.cache_data[k][1])
                    discarded_key = lru_key
                else:
                    discarded_key = candidates[0]

                del self.cache_data[discarded_key]
                del self.frequency_counter[discarded_key]
                print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = (item, 0)  # Frequency initialized to 0
            self.frequency_counter[key] = 0

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            if key in self.cache_data:
                # Update the frequency counter
                self.frequency_counter[key] += 1
                return self.cache_data[key][0]
        return None
