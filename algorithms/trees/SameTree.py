# Problem:
# Given two binary trees, write a function to check if they are equal or not.
# 
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
#
# Idea:
# Recur on both trees simultaneously.

class SameTree:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if not p and not q: 
            return True
        if not p or not q:
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)
            
                            
