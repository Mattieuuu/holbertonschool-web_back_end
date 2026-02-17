#!/usr/bin/env python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - A caching system with no limit
    """

    def put(self, key, item):
        """ Add an item in the cache
        Args:
            key: Key to assign the item to
            item: Item to be stored with the key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        Args:
            key: Key to retrieve the item for
        Returns:
            The value in self.cache_data linked to key or None
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
