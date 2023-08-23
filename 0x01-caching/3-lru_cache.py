#!/usr/bin/python3
"""
3-lru_cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """
        Initialisation"""
        super().__init__()
        self.key_dict = {}

    def put(self, key, item):
        """
        Add item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_key = min(self.key_dict, key=self.key_dict.get)
            del self.cache_data[min_key]
            del self.key_dict[min_key]
            print('DISCARD: {}'.format(min_key))

        self.cache_data[key] = item
        if key in self.key_dict:
            self.key_dict[key] += 1
        else:
            self.key_dict[key] = max(self.key_dict.values(), default=-1) + 1

    def get(self, key):
        """
        Get data linked to the key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
