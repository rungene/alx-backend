#!/usr/bin/python3
"""
1-fifo_cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
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
        self.cache_data[key] = item
        first_key = list(self.cache_data.keys())[0]
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[first_key]
            print('DISCARD: {}'.format(first_key))

    def get(self, key):
        """
        Get data linked to the key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
