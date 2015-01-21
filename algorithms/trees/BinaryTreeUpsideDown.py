"""
Problem:
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.
For example:
Given a binary tree {1,2,3,4,5},
    1
   / \
  2   3
 / \
4   5
return the root of the binary tree [4,5,2,#,#,3,1].
    4
   / \
  5   2
     / \
    3   1  

Idea:
Ref : http://www.meetqun.com/thread-2219-1-1.html
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return root of the upside down tree
    def upsideDownBinaryTree(self, root):
        if not root: return
        new_root = self.rec(self, root)
        root.left = None
        root.right = None
        return new_root

    def rec(self, root):
        cur_root = None
        real_root = None
        if root.left is not None:
            real_root = self.upsideDownBinaryTree(root.left)
            cur_root = root.left
            cur_root.right = root
            cur_root.left = root.right
        else:
            return root
        return real_root

    def upsideDownBinaryTree_loop(self, root):
        cur = root
        while cur:
            left = cur.left
            left.left = root.right
            left.right = root
            cur = cur.left

node1 = TreeNode(1)
node2 = TreeNode(2)

node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
#node1.right = node3
#node2.left = node4
#node2.right = node5
node = Solution().upsideDownBinaryTree(node1)
print node.val, node.right.val
#print node.val, node.left.val, node.right.val, node.right.left.val, node.right.right.val
