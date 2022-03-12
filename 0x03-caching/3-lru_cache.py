#!/usr/bin/python3
"""
LRU cache modul
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    class lru cache
    """

    def __init__(self):
        """
        inilize
        """
        super().__init__()
        self.lst = []

    def put(self, key, item):
        """
        add value to dict key
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.lst.remove(key)
        self.cache_data[key] = item
        self.lst.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = self.lst.pop(0)
            print('DISCARD:', last)
            del self.cache_data[last]

    def get(self, key):
        """
        get value of dict key
        """
        if key in self.cache_data:
            self.lst.remove(key)
            self.lst.append(key)
        if key in self.cache_data:
            return self.cache_data[key]
