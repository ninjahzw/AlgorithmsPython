# Problem:
# Two elements of a binary search tree (BST) are swapped by mistake.
# 
# Recover the tree without changing its structure.
# 
# Note:
# A solution using O(n) space is pretty straight forward. 
# Could you devise a constant space solution?
#
# Idea:
# NOTE Treat the tree as a sorted array by in-order traversal
# how do you deal with the condition that two elements in a sorted array swaped?
# NOTE Question: if Duplicate?
# Ref:
# http://yucoding.blogspot.com/2013/03/leetcode-question-75-recover-binary.html
# http://huntfor.iteye.com/blog/2077665
# 
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class RecoverBST:
    first,second,pre = None,None,None
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        self.rec(root)
        self.swap(self.first,self.second)
        return root

    def rec(self, root):
        if not root:
            return
        self.rec(root.left)
        if self.pre and root.val < self.pre.val:
            if not self.first:
                self.first = self.pre
            self.second = root
        self.pre = root
        self.rec(root.right)
    
    def swap(self, node1, node2):
        tmp = node1.val
        node1.val = node2.val
        node2.val = tmp
