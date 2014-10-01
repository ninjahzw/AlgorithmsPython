# Problem:
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Idea:
# This is simple but also Typical !!!
# NOTE Use backtracking 
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class MaxDepthBinaryTree:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        return self.rec(root)
    
    def rec(self, root):
        if not root:
            return 0
        left = self.rec(root.left)
        right = self.rec(root.right)
        # NOTE do not forget +1 (current node)
        return left+1 if left > right else right+1
