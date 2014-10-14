"""
Problem:
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

Idea:
first go deep for each level, then assemble result when reach the bottom and returns back!
NOTE: is this backtracking?

"""

__author__ = 'HouZhaowei'
#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    NOTE!
    if define self.result as:
    result = []
    then error occurs!(on leetcode)
    so must define it as self.result!!
    """
    def __init__(self):
        self.result = []
    # @param root, a tree node
    # @return a list of lists of integers
    def level_order_bottom(self, root):
        if root is None:
            return self.result
        self.rec([root])
        return self.result

    def rec(self, nodes):
        next = []
        current = []
        for node in nodes:
            current.append(node.val)
            if node.left is not None : next.append(node.left)
            if node.right is not None : next.append(node.right)
        if len(next) > 0:
            self.rec(next)
        # append result here will make sure the order is bottom up!
        self.result.append(current)

a = TreeNode(1)
b = TreeNode(2)
a.left = b
print Solution().level_order_bottom(a)