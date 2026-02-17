#!/usr/bin/env python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - A caching system using FIFO algorithm
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
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Remove the first item added (FIFO)
                    first_key = self.order[0]
                    del self.cache_data[first_key]
                    self.order.remove(first_key)
                    print("DISCARD: {}".format(first_key))

                self.order.append(key)
            else:
                # If key already exists, don't add to order again
                pass

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
