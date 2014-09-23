# Problem:
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# 
# For example:
# Given the below binary tree and sum = 22,
#        5
#       / \
#      4   8
#     /   / \
#    11  13  4
#   /  \    / \
#  7    2  5   1
# return
# [
# [5,4,11,2],
# [5,8,4,5]
# ]

# Idea:
# We can actually construct the path array for each Path
# if we found that Path not valid, then,discard
# but this approach will take much space since we need to keep track of all paths.
# 
# Better Solution? YES!
# NOTE BACKTRACKING !
# if we found a valid path, then backtrack to assemble the result!
# NOTE each recurssion will return a 2D array because,
# for a node, it need to add all valid paths though it. 

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class PathSumII:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root is None:
           return [] 
        return self.preOrder(root,sum,0)

    def preOrder(self,root,sum,pathsum):
        # here [] means invalid value.
        if root is None:
            return [] 
        value = pathsum + root.val
        if root.left is None and root.right is None:
            if value == sum:
                return [[root.val]]
            return []
            
        newResult = []
        leftResult =  self.preOrder(root.left,sum,pathsum + root.val)
        # only assemble valid values
        if len(leftResult)>0:
            for one in leftResult:
                newResult.append([root.val]+one)
                
        rightResult = self.preOrder(root.right,sum,pathsum + root.val)
        if len(rightResult)>0:
            for one in rightResult:
                newResult.append([root.val]+one)
        return newResult 

a = TreeNode(1)
b = TreeNode(1)
c = TreeNode(2)
a.left = b

print PathSumII().pathSum(a,2) 
