"""
Problem:
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.=
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Return the sum = 12 + 13 = 25.

Idea:
DFS, value_of_each_node = previous_value * 10 + current_value
if leaf node, then add result.
"""
__author__ = 'Zhaowei'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.result = 0
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root is not None:
            self.dfs(root, 0)
        return self.result
    def dfs(self, root, num):
        value = num * 10 + root.val
        # leaf node
        if root.left is None and root.right is None:
            self.result += value
        if root.left is not None:
            self.dfs(root.left, value)
        if root.right is not None:
            self.dfs(root.right, value)