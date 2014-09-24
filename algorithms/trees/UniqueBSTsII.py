# Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
# 
# For example,
# Given n = 3, there are a total of 5 unique BST's.
# 
#        1         3     3      2      1
#         \       /     /      / \      \
#          3     2     1      1   3      2
#         /     /       \                 \
#        2     1         2                 3
#
# Idea:
# NOTE: USE DP!
#
Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class UniqueBSTs:
    # @return an integer
    def numTrees(self, n):
        # NOTE here must be n+1 trees[n] here not means the subscript n.
        tmp = [0 for i in xrange(n+1)]
        tmp[0],tmp[1]= 1,1
        for i in xrange(2,n+1):
            for j in xrange (i):
                tmp[i] += tmp[j] * tmp[i-j-1]
        return tmp[n]

print UniqueBSTs().numTrees(4)
