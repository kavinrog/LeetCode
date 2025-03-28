class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = None
        self.right = None
        
def lowestCommonAncestor(root, p, q):
    if root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.left, p, q)
    elif root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root
        