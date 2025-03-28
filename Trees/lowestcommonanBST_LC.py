# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

# Function to find the Lowest Common Ancestor (LCA) in a Binary Search Tree
def lowestCommonAncestor(root, p, q):
    # If both nodes are greater than root, LCA lies in the right subtree
    if root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)
    # If both nodes are smaller than root, LCA lies in the left subtree
    elif root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    # If the nodes are on either side or one is the root, current root is the LCA
    else:
        return root

# Building the Binary Search Tree
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

# Defining the nodes for which we want to find the LCA
p = root.left            # Node with value 2
q = root.left.right      # Node with value 4

# Calling the function
lca = lowestCommonAncestor(root, p, q)

# Printing the result
print("Lowest Common Ancestor:", lca.val)  # Expected Output: 2