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
        if (key is not None or item is not None):
            self.cache_data[key] = item
            
        

    def get(self, key):
        """
        Get item from cache
        """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
