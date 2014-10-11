# Problem:
# Given a binary tree, return the in-order traversal of its nodes' values.
#
# Idea:
# NOTE Always keep an eye on those simple questions!
class BTInorder:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        result = []
        self.rec(root,result)
        return result
    
    def rec(self, root, result):
        if not root:
            return
        self.rec(root.left, result)
        result.append(root.val)
        self.rec(root.right, result)
