# Given a binary tree, return the zigzag level order traversal of its nodes' values. 
# (ie, from left to right, then right to left for the next level and alternate between).
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
# [20,9],
# [15,7]
# ]
#
# Idea:
# Basically same to normal order one 
# NOTE only need to know current line is even line or odd line.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class BinaryTreeLevelZigzagTrav:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        result = []
        if root is None:
            return []
        level = [root]
        # NOTE add a index variable
        index = 0
        while len(level) > 0:
            currentLevelValues = []
            nextLevel = []
            for x in level:
                # NOTE only this two line main difference from the normal order trav.
                if index % 2 == 0: currentLevelValues += [x.val]
                # for odd number lines, add reversely.
                else: currentLevelValues = [x.val] + currentLevelValues
                if x.left is not None: nextLevel.append(x.left) 
                if x.right is not None: nextLevel.append(x.right) 
            level = nextLevel
            result.append(currentLevelValues)
            index += 1
        return result
