class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    
    def is_valid_bst(self, root):
        self.rec(root, -2147483648, 2147483647)
        
    def rec(self, node, minimum, maximum):
        if node is None:
            return True
        if node.val <= minimum or node.val >= maximum:
            return False
        return self.rec(node.left, minimum, node.val) and self.rec(node.right, node.val, maximum)
