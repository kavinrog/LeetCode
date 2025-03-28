#Import OrderedDict from collections for maintaining key order
from collections import OrderedDict

# Define the LRUCache class
class LRUCache:
    def __init__(self, capacity):
        # Initialize an ordered dictionary to store cache entries
        self.cache = OrderedDict()
        self.capacity = capacity  # Set the max capacity of the cache

    def get(self, key):
        # If key is not in cache, return -1
        if key not in self.cache:
            return -1
        # Move the accessed key to the end to mark it as recently used
        self.cache.move_to_end(key)
        return self.cache[key]  # Return the value

    def put(self, key, value):
        # If key already exists, mark it as recently used
        if key in self.cache:
            self.cache.move_to_end(key)
        # Insert or update the key with the new value
        self.cache[key] = value
        # If capacity is exceeded, remove the least recently used item (from the front)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

''' Uncomment the Testing code for testing the Class'''

# # Commands to simulate the input sequence
# commands = ["LRUCache", "put", "get", "put", "put", "get", "get"]
# inputs   = [[2],        [1, 10], [1],   [2, 20], [3, 30], [2],   [1]]

# # List to store the results of each command
# output = []

# lru = None  # Placeholder for the LRUCache instance

# # Loop through each command and run the appropriate method
# for cmd, inp in zip(commands, inputs):
#     if cmd == "LRUCache":
#         lru = LRUCache(*inp)  # Create the cache with given capacity
#         output.append(None)   # Constructor returns nothing
#     elif cmd == "put":
#         lru.put(*inp)         # Call the put method
#         output.append(None)   # put returns nothing
#     elif cmd == "get":
#         res = lru.get(*inp)   # Call the get method and store the result
#         output.append(res)

# # Print the final output list
# print("Output:", output)  # Expected: [None, None, 10, None, None, 20, -1]