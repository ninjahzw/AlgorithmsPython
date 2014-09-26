# Problem
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# 
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
#
# Idea:
# Maintain two pointers, Notice the boundary conditions.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class RemoveDupSortedList:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        pre = head
        cursor = head.next
        while cursor:
            while cursor and pre.val == cursor.val:
                pre.next = cursor.next
                cursor = cursor.next 
            pre = pre.next
            if cursor:cursor = cursor.next
        return head

a = ListNode(1)
b = ListNode(1)
a.next = b
c = RemoveDupSortedList().deleteDuplicates(a)
while c:
    print c.val
    c = c.next
