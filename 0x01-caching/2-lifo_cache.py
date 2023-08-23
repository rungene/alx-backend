#!/usr/bin/python3
"""
2-lifo_cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """
        Initialisation"""
        super().__init__()

    def put(self, key, item):
        """
        Add item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print('DISCARD: {}'.format(last_key))

        self.cache_data[key] = item

    def get(self, key):
        """
        Get data linked to the key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
