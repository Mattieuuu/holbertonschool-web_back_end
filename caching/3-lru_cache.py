#!/usr/bin/env python3
""" LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines:
      - A caching system using LRU algorithm
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
                # Remove least recently used item (first in order)
                lru_key = self.order[0]
                del self.cache_data[lru_key]
                self.order.remove(lru_key)
                print("DISCARD: {}".format(lru_key))

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
