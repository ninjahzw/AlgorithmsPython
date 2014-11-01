# Problem
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.
#
# Idea:
# NOTE NOTE! the height of sub tree not comparing to each route!
# So for each subtree only need to return it's max height!
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Determin:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root is None:
            True
        if self.rec(root) == -1:
            return False
        return True
        
    def rec(self, root):
        if not root:
            return 0
        left = self.rec(root.left)
        right = self.rec(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(right-left) > 1:
            return -1
        # NOTE, only need to return the maximum!
        return max(left,right)+1



a = TreeNode(0)
b = TreeNode(1)
c = TreeNode(2)
b.left = a
b.right = c
Determin().isBalanced(b)
