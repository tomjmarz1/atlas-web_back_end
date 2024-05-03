#!/usr/bin/python3
""" BaseCaching module
"""

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
  """functions like a basic cache"""
  def put(self, key, item):
    self.cache_data[key] = item

  def get(self, key):
    if key and key in self.cache_data:
      return self.cache_data[key]
    else:
      return None
