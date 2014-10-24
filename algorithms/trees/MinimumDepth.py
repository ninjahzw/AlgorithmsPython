"""
Problem:
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Idea:
Simple DFS
NOTE: leaf node condition.
"""
__author__ = 'HouZhaowei'
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.mini_dep = float('inf')
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        self.dfs(root, 0)
        return self.mini_dep

    def dfs(self, root, total):
        total += 1
        if root.left is None and root.right is None:
            if total < self.mini_dep:
                self.mini_dep = total
        if root.left is not None:
            self.dfs(root.left, total)
        if root.right is not None:
            self.dfs(root.right, total)
