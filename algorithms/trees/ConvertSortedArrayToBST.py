# Problem:
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# Idea:
# Do a binary traversal.
# NOTE the boundary condition: start > end return None, start = end return the node.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Convert:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num or len(num) == 0:
            return None 
        return self.rec(num, 0, len(num)-1)
    
    def rec(self, num, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(num[start])
        rootIndex = (start + end)/2
        root = TreeNode(num[rootIndex])
        root.left = self.rec(num, start, rootIndex-1)
        root.right = self.rec(num, rootIndex+1, end)
        return root 
root = Convert().sortedArrayToBST([1,3])                    
print root.val
print root.right.val
