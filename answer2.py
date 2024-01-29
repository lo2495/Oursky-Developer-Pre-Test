import math
import time


class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.priority_queue = []

    def get(self, key):
        if key in self.cache:
            value, weight, last_accessed_time = self.cache[key]
            score = weight / (math.log(time.time() - last_accessed_time + 1) + 1)
            self.priority_queue.remove((key, score))
            self.priority_queue.append((key, score))
            return value
        else:
            return -1

    def put(self, key, value, weight):
        if key in self.cache:
            self.cache[key] = (value, weight, time.time())
        else:
            if len(self.cache) >= self.capacity:
                least_recently_accessed_key, _ = min(self.priority_queue, key=lambda x: x[1])
                del self.cache[least_recently_accessed_key]
                self.priority_queue.remove((least_recently_accessed_key, _))
            self.cache[key] = (value, weight, time.time())
            score = weight / (math.log(time.time() - self.cache[key][2] + 1) + 1)
            self.priority_queue.append((key, score))

# get(key):

# 1. Time Complexity: O(n)
# - The get(key) operation has a time complexity of O(n), where n is the number of key-value pairs in the cache. It causes the key is not found in the cache.
            
# - When the key is present in the cache, the time complexity of get(key) is reduced to O(1).
            
# 2. Space Complexity: O(1)
            
# - The space complexity is O(1) because the get(key) operation does not require any additional space.
            
# put(key, value, weight):

# 1. Time Complexity: O(n)
# - The put(key, value, weight) operation has a time complexity of O(n), where n is the number of key-value pairs in the cache. It causes the cache is already at its capacity.
            
# - When the cache is not at its capacity, the time complexity of put(key, value, weight) is reduced to O(1).
            
# 2. Space Complexity: O(1)
            
# - The put(key, value, weight) operation does not require any additional space. Thus, the space complexity is O(1).