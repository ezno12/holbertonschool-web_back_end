#!/usr/bin/python3
"""
caching modul
"""
BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """
    basic caching
    """
    def put(self, key, item):
        """
        add item to cache
        """
        if (key is None or item is None):
            return None
        else:
            cache_item = self.cache_data[key] = item
            return cache_item
        

    def get(self, key):
        """
        Get item from cache
        """
        if (key is None):
            return None
        else:
            return self.cache_Data[key]
