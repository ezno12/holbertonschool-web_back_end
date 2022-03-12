#!/usr/bin/env python3
"""
LIFO cache modul
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    class lifo cache
    """

    def __init__(self):
        """
        inilize
        """
        super().__init__()

    def put(self, key, item):
        """
        add value to dict key
        """
        if key is None or item is None:
            return
        self.cache_data.update({key: item})
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = list(self.cache_data)[-2]
            print('DISCARD:', last)
            self.cache_data.pop(last)

    def get(self, key):
        """
        get value of dict key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
