#!/usr/bin/env python3
""" MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines:
      - A caching system using MRU algorithm
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        Args:
            key: Key to assign the item to
            item: Item to be stored with the key
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update existing key - move to end (most recent)
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove most recently used item (last in order)
                mru_key = self.order[-1]
                del self.cache_data[mru_key]
                self.order.remove(mru_key)
                print("DISCARD: {}".format(mru_key))

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key
        Args:
            key: Key to retrieve the item for
        Returns:
            The value in self.cache_data linked to key or None
        """
        if key is not None and key in self.cache_data:
            # Move to end (most recent)
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
