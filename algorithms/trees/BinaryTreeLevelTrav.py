# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
# 
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#  /  \
# 15   7
# return its level order traversal as:
# [
# [3],
# [9,20],
# [15,7]
# ]
#
# Idea:
# Breadth first search.
# NOTE : use level and nextLevel to cooperate.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class BineryTreeLevelTrav:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        result = []
        if root is None:
            return []
        level = [root]
        while len(level) > 0:
            currentLevelValues = []
            nextLevel = []
            for x in level:
                currentLevelValues.append(x.val)
                if x.left is not None: nextLevel.append(x.left) 
                if x.right is not None: nextLevel.append(x.right) 
            level = nextLevel
            result.append(currentLevelValues)
        return result
