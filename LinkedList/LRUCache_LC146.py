from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
        
    def get(self, key):
        if not key in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put (self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value 
        
        if len(self.cache) > self.capacity:
            return self.cache.popitem(last = False)

commands = ["LRUCache", "put", "get", "put", "put", "get", "get"]
inputs =    [[2],        [1, 10], [1],   [2, 20], [3, 30], [2],   [1]]

output = []

lru = None

for cmd, inp in zip(commands, inputs):
    if cmd == "LRUCache":
        lru = LRUCache(*inp)
        output.append(None)  
    elif cmd == "put":
        lru.put(*inp)
        output.append(None)  
    elif cmd == "get":
        res = lru.get(*inp)
        output.append(res)   

print("Output:", output)