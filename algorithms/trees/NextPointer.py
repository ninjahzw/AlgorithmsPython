# Populate each next pointer to point to its next right node.
#  If there is no next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# Note:
# 
# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# For example,
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL
# 
# Idea:
# Make full use of its feature: a full binary tree.
# for each node if have left child (it must also have right child) 
# then connect its two childres, if it has a next pointer (its parent applied this pointer)
# then connect its right child to its sibling's left child.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class NestPointer:

    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return None
        if root.left is not None:
            root.left.next = root.right
            if root.next is not None:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

                                          
