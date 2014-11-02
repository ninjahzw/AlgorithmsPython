# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# 
# For example, this binary tree is symmetric:
# 
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#   \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class SymmetricTree:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root): 
        if root is None:
            return True 
        return self.rec(root.left,root.right)
        
    def rec(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            return self.rec(left.left,right.right) and\
            self.rec(left.right,right.left)         
        return False

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c
print SymmetricTree().isSymmetric(a)
