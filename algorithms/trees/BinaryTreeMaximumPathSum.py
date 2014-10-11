# problem:
# Given a binary tree, find the maximum path sum.
# 
# The path may start and end at any node in the tree.
# 
# For example:
# Given the below binary tree,
# 
#        1
#       / \
#      2   3
# Return 6.
#   
# Intuition:
# Each path must have a root node
# how to decide the maximum length of path rooted at this node?
# it must be Max(node.left.maxval,0) + Max(node.right.maxval,0) + node.val
# where compare to 0 means if the max val of child node is negative, then abandon this child node.
#
# Idea:
# Recursively Solve this problem
# Each node calculate : path = Max(max path from left, max path from right) and
# value = Max(max value from left + max value from right )
# Any node should return ether current maximum value or 0 if current max is negative.
# return 0 if negative means restart from its parent.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class BinaryTreeMaximumPathSum:
    maxmum = -float("inf") 
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if root is None:
            return 0
        self.rec(root)
        return self.maxmum
    def rec(self,root):
        if root is None:
            return 0
        leftLength= self.rec(root.left)
        rightLength= self.rec(root.right)
    
        maxlength = max(leftLength,rightLength) 
        value = leftLength + rightLength + root.val
        if value > self.maxmum:
            self.maxmum = value
        
        # !!! IMP !!!
        # if current subtree only result in negative value, then return 0
        # means restart from parent 
        return max(maxlength + root.val, 0)

a = TreeNode(2)
b = TreeNode(-1)
c = TreeNode(3)
a.left = b
#a.right = c
print BinaryTreeMaximumPathSum().maxPathSum(a)
