#!/usr/bin/python3
""" BaseCaching module
"""


BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """functions like a basic cache"""
    def put(self, key, item):
        """functions like a basic cache"""
        self.cache_data[key] = item

    def get(self, key):
        """functions like a basic cache"""
        if key and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
