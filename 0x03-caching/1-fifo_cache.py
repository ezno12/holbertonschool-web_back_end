#!/usr/bin/python3
"""
FIFO cache modul
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    class fifo cache
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
            for k, v in self.cache_data.items():
                print('DISCARD:', list(self.cache_data.keys())[0])
                break
            self.cache_data.pop(k)

    def get(self, key):
        """
        get value of dict key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
