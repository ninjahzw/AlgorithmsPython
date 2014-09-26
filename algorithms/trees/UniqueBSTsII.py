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
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class UniqueBSTs:
    # @return a list of tree node
    def generateTrees(self, n):
        tmp = [[None for i in xrange(n+1)] for j in xrange(n+1)]
        return self.rec(tmp,1,n)

    def rec(self,tmp,start,end):
        if start > end:
            return []
        if start == end:
            return [TreeNode(start)]
        posibilities = []
        for j in range(start,end+1):
            print start,end,j
            root = TreeNode(j)
            if j + 1 > end:
                continue
            lefts = self.rec(tmp,start,j-1) if tmp[start][j-1] is None else tmp[start][j-1]
            rights = self.rec(tmp,j+1,end) if tmp[j+1][end] is None else tmp[j+1][end]
            if len(lefts) == 0:
                for right in rights:
                    root.right = right
                    posibilities.append(root)
                    continue
            if len(rights) == 0:
                for left in lefts:
                    root.left = left
                    posibilities.append(root)
                    continue
            for left in lefts:
                for right in rights:
                    root.left = left
                    root.right = right
                    posibilities.append(root)
        tmp[start][end] = posibilities                         
        return posibilities

list = UniqueBSTs().generateTrees(3)
print list
for one in list:
    print one.val
