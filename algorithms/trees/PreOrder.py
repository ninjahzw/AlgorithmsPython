"""
Given a binary tree, return the preorder traversal of its nodes' values.
Note: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        result = []
        if root is None:
            return result
        stack = []
        stack.append(root)
        pre = None
        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)

a.left = b
#a.right = c
b.left = d
#b.right = e

print Solution().postorderTraversal(a)
