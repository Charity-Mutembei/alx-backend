#!/usr/bin/python3
""" LFUCache module
"""
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the LFUCache
        """
        super().__init__()
        self.freq = defaultdict(int)  # Frequency of access for each key
        self.order = OrderedDict()
        self.key_freq_order = defaultdict(OrderedDict)

    def put(self, key, item):
        """ Add an item in the cache using LFU algorithm
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update the item and increase its frequency
                self.cache_data[key] = item
                self.freq[key] += 1
                # Move the key to the end of the order dictionary
                self.order.move_to_end(key)
                self.key_freq_order[self.freq[key]].move_to_end(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Find the least frequently used frequency
                    min_freq = min(self.freq.values())
                    lfu_keys = self.key_freq_order[min_freq]
                    lru_key = next(iter(lfu_keys))
                    self.cache_data.pop(lru_key)
                    self.freq.pop(lru_key)
                    lfu_keys.pop(lru_key)
                    if not lfu_keys:
                        self.key_freq_order.pop(min_freq)
                    print(f"DISCARD: {lru_key}")

                # Add the new item
                self.cache_data[key] = item
                self.freq[key] = 1
                self.order[key] = None
                self.key_freq_order[1][key] = None

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        if key in self.cache_data:
            # Increase the frequency of the key
            self.freq[key] += 1
            # Move the key to the end of the order dictionary
            self.order.move_to_end(key)
            # Update the frequency order
            freq = self.freq[key]
            self.key_freq_order[freq].move_to_end(key)
            return self.cache_data[key]
        return None
