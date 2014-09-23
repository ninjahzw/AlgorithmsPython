# Problem:
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# 
# For example:
# Given the below binary tree and sum = 22,
#          5
#         / \
#        4   8
#       /   / \
#      11  13  4
#     /  \      \
#    7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
#
# Idea:
# Use pre-order traversal
# NOTE a leaf node must have no children!

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class PathSum:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
           return False
        return self.preOrder(root,sum,0)

    def preOrder(self,root,sum,pathsum):
        if root is None:
            return False
        value = pathsum + root.val
        if root.left is None and root.right is None:
            if value == sum:
                return True
            return False
            
        if self.preOrder(root.left,sum,pathsum + root.val)\
             or self.preOrder(root.right,sum,pathsum + root.val):
            return True
        return False

a = TreeNode(1)
b = TreeNode(1)
c = TreeNode(2)
a.left = b

print PathSum().hasPathSum(a,1) 
