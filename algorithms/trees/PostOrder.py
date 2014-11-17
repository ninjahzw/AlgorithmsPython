"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].
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
            node = stack[-1]

            # if leaf node:
            if not node.left and not node.right:
                result.append(stack.pop().val)
                pre = node
            
            # first add right, then add left
            if node.right:
                # means its child (children) has been processed
                if pre == node.right:
                    result.append(stack.pop().val)
                    pre = node
                    continue
                stack.append(node.right)
            if node.left:
                # means its child (children) has been processed
                if pre == node.left:
                    result.append(stack.pop().val)
                    pre = node
                    continue
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
