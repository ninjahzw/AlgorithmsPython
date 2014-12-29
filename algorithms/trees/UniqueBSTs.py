# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
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
# In "Unique Binary Search Trees", we are only required to output the number of the trees. 
# We know that all nodes in the left subtree are smaller than the root. 
# And all nodes in the right subtree are larger than the root.
# For a integer n, we have n options to be the root. In these options, assuming i is the value that we choose to be the root. 
# The value in left subtree are from 1 to i - 1, and the values in right subtree are from i+1 to n. 
# If 1 to i-1 can form p different trees, and i+1 to n can form q different trees, 
# then we will have p * q trees when i is the root. In fact, 
# the number of different trees depends on how many number to form the tree.
# trees[n] = trees[n-1]*trees[0]
#           + trees[n-2]*trees[1]
#           + ...
#           + trees[1]*trees[n-2]
#           + trees[0]*trees[n-1]
# We can use an array to save the number of different trees that n integers can form. We fill the array from bottom to up, starting from 0 to n.

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

print UniqueBSTs().numTrees(2)
