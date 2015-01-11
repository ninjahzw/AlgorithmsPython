"""
NOTE! IMPORTANT PROBLEM!
Problem:
Implement an iterator over a binary search tree (BST). 
Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, 
where h is the height of the tree.

Idea:

Use in-order traversal, with a stack
"""
tion for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.addLeft(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0

    # @return an integer, the next smallest number
    # NOTE this method is important and essential!
    def next(self):
        if self.hasNext():
            node = self.stack.pop()
            self.addLeft(node.right)
            return node.val
        else: return None

    # go all the way down through the left.
    def addLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left
