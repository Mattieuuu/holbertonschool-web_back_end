#!/usr/bin/env python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
      - A caching system using LIFO algorithm
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
                    # Remove the last item added (LIFO)
                    last_key = self.order[-1]
                    del self.cache_data[last_key]
                    self.order.remove(last_key)
                    print("DISCARD: {}".format(last_key))

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
