"""
IMPORTANT!
Problem:
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

Idea:
Tags: DFS
NOTE that an in-order traversal of a BST yields the sorted array.
So we can solve this problem by in-order approach using bottom-up manner.

NOTE: THINK: what about the linked-list is in descending order?
idea: will be first right, then node, then left order ?
"""
__author__ = 'HouZhaowei'
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head is None:
            return None
        start = 0
        # length of the listL
        length = 0
        self.node = head
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        # NOTE: here must from 0 to length-1
        # Or from 1 to length
        return self.dfs(0, length-1)

    def dfs(self, start, end):
        print(self.node)
        if start > end:
            return None
        mid = (start + end)/2
        # same as in-order traversal.
        left = self.dfs(start, mid-1)
        root = TreeNode(self.node.val)
        self.node = self.node.next
        right = self.dfs(mid + 1, end)

        root.left = left
        root.right = right
        return root

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
Solution().sortedListToBST(a)