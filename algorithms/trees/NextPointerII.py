# Problem:
# what if the binary can be any binary tree?
# 
# Follow up for problem "Populating Next Right Pointers in Each Node".
# 
# What if the given tree could be any binary tree? 
# Would your previous solution still work?
# 
# Note:
# 
# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#         /  \
#        2    3
#       / \    \
#      4   5    7
# After calling your function, the tree should look like:
#         1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL
#
# Idea:
# Try breadth first ..
# FAILED!!
# Still use depth first:
# Make full use of the previous relation, 
# for each node, it is already connected to all of its right neighbors (if have)
# NOTE! the recursion must from right to left!

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
        
class NextPointer:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return None

        # find neighbor for children
        node = root.next
        neighbor = None
        while node is not None:
            if node.left is not None:
                neighbor = node.left
                break
            if node.right is not None:
                neighbor = node.right
                break
            node = node.next

        if root.right is not None:
            root.right.next = neighbor
        if root.left is not None:
            root.left.next = neighbor if root.right is None else root.right      
        
        # !!! VERY IMPORTANT
        # MUST right first, then left.
        # because links are from left to right so we need to fill up right part first.
        self.connect(root.right)
        self.connect(root.left) 

    # FAILED!
    def connectBreadth(self, root):
        if root is None:
            return None
        queue = list()
        queue.append(root)
        pre = None
        while len(queue) > 0:
            node = queue.pop(0)
            if pre is not None:
                pre.next = node
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            pre = node
        self.remove(root)
    
    # remove all pointers on the right most.
    # THIS will NOT work 
    def remove(self,root):
        root.next = None
        if root.right is not None:
            self.remove(root.right)
        elif root.left is not None:
            self.remove(root.left)


a = TreeNode(2)
b = TreeNode(-1)
c = TreeNode(3)
d = TreeNode(6)
e = TreeNode(7)
f = TreeNode(9)
g = TreeNode(1)
a.left = b
a.right = c
c.left = d
c.right = e
e.left = f
d.left = g
NextPointer().connect(a)
print g.next
print e.next
print f.next
print c.next
print a.next
print d.next
print b.next
