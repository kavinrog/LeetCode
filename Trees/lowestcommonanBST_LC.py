class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        
def lowestCommonAncestor(root, p, q):
    if root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)
    elif root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    else:
        return root

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)


p = root.left            
q = root.left.right      

lca = lowestCommonAncestor(root, p, q)
print("Lowest Common Ancestor:", lca.val)  # Expected Output: 2