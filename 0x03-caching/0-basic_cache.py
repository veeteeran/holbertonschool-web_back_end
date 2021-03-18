#!/usr/bin/env python3
"""BasicCache module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        Inherits from BaseCaching
    """

    def put(self, key, item):
        """
            Assign key: item to self.cache_data
            If key or item is None do nothing

                Parameters:
                        key: key for item in self.cache_data dict
                        item: contains value for key
        """
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        """
            Returns the value of self.cache_data of given key

                Parameters:
                        key: key where vaule is returned

                Returns:
                        value of given key
                        if key is None or doesn't exist returns None
        """
        return self.cache_data.get(key)
