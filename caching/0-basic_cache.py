#!/usr/bin/python3
""" BasicCache module
"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class. Inherits from BaseCaching.
    """

    def put(self, key, item):
        """ Add an item to the cache_data dictionary
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key from the cache_data dictionary.
        """
        return self.cache_data.get(key, None)
