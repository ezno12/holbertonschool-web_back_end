#!/usr/bin/env python3
"""
MRU cache modul
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    class mru cache
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
        self.cache_data[key] = item
        self.lst.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = self.lst.pop(-2)
            print('DISCARD:', last)
            del self.cache_data[last]

    def get(self, key):
        """
        get value of dict key
        """
        if key in self.cache_data:
            self.lst.append(key)
        if key in self.cache_data:
            return self.cache_data[key]
