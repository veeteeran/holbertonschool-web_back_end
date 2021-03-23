#!/usr/bin/env python3
"""LFU caching module"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
        LFU Caching, Inherits from BaseCaching
    """

    def __init__(self):
        """Initialize LRU Class"""
        self.accessedDict = OrderedDict()
        self.unaccessedDict = OrderedDict()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
            Assign key: item to self.cache_data
            If key or item is None do nothing
                Parameters:
                        key: key for item in self.cache_data dict
                        item: contains value for key
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data.pop(key)
                self.cache_data.update({key: item})
                self.unaccessedDict.pop(key)
                self.unaccessedDict.update({key: item})
            else:
                self.cache_data.update({key: item})
                self.unaccessedDict.update({key: item})

            if len(self.cache_data) > self.MAX_ITEMS:
                discarded = self.__updateDicts(key, item)
                print(f"DISCARD: {discarded}")

    def get(self, key):
        """
            Returns the value of self.cache_data of given key
                Parameters:
                        key: key where vaule is returned
                Returns:
                        value of given key
                        if key is None or doesn't exist returns None
        """
        if key in self.cache_data:
            self.accessedDict.update({key: self.cache_data[key]})
            self.cache_data.move_to_end(key)

        if key in self.unaccessedDict:
            self.unaccessedDict.pop(key)

        return self.cache_data.get(key)

    def __updateDicts(self, key, item):
        """Update cache_data Dict"""
        if len(self.accessedDict) == 4:
            accessedKeys = list(self.accessedDict)[0:]
            discarded = accessedKeys.pop(0)
            self.accessedDict.pop(discarded)

        else:
            unaccessedKeys = list(self.unaccessedDict)[0:]
            discarded = unaccessedKeys.pop(0)
            self.unaccessedDict.pop(discarded)

        self.unaccessedDict.update({key: item})

        self.cache_data.clear()

        for k, v in self.unaccessedDict.items():
            self.cache_data[k] = v

        for k, v in self.accessedDict.items():
            self.cache_data[k] = v

        return discarded
