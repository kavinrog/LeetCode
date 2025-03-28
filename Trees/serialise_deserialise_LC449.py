from collections import deque
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 
        
def serialise(root):
    q = deque()
    if root:
        q.append(root)
    res = []
    
    while q:
        node = q.popleft()
        
        if node:
            res.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        else:
            res.append("null")
    return ",".join(res)

def deserialise(data):
    if not data:
        return None
    nodes = data.split(",")
    root = TreeNode(int(nodes[0]))
    q = deque()
    q.append(root)
    i = 1
    while q:
        node = q.popleft()
        if nodes[i] != "null":
            node.left = TreeNode(int(nodes[i]))
            q.append(node.left)
        i+=1
        if nodes[i] != "null":
            node.right = TreeNode(int(nodes[i]))
            q.append(node.right)
        i+=1
    return root

# Build a test tree manually:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

s = serialise(root)
print("Serialized:", s)

new_root = deserialise(s)

print("Serialized Again:", serialise(new_root))