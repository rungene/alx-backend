#!/usr/bin/python3
"""
0-basic_cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """subclass of BaseCaching that implements the put() and get() methods."""

    def put(self, key, item):
        """Add an item into cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
