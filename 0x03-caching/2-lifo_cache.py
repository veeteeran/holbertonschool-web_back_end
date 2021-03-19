#!/usr/bin/env python3
"""FIFO caching module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
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
        keyList = list(self.cache_data)[0:]
        if key and item:
            if keyList:
                lastItem = keyList[-1]

            if key in keyList:
                del self.cache_data[key]
                keyList.remove(key)

            self.cache_data.update({key: item})

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                del self.cache_data[lastItem]
                print(f"DISCARD: {lastItem}")

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
