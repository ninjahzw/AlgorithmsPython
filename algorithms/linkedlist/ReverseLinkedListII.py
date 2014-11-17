"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.
For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 <= m <= n <= length of list.
"""
__author__ = 'HouZhaowei'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        index = 0
        start = ListNode(0)
        end = ListNode(0)
        # NOTE add a node pointing to head can cover the case that m = 1
        # (in this case head will change)
        before_head = ListNode(0)
        before_head.next = head
        cursor = before_head
        # node before start of the rotation
        pre = head
        # node after end of the rotation
        after = None
        determined = False
        while cursor:
            if index == m:
                start.next = cursor
                determined = True
            if index == n:
                end.next = cursor
            if not determined:
                pre = cursor
            cursor = cursor.next
            # NOTE, because start from before head, so index starts from 0
            index += 1

        after = end.next.next
        end.next.next = None
        (start, end) = self.reverseList(start.next)
        pre.next = start
        end.next = after
        return before_head.next

    # NOTE, IMP: To reverse a Linked List.
    # @return : head of new list
    # the process for input "1234" is : 1234, 2134, 3214, 4321
    def reverseList(self,head):
        helper = ListNode(0)
        reverseTail = head
        reverseHead = head
        while head.next:
            helper.next = head.next
            head.next = head.next.next
            # guarantee the point will points to reverse head 
            helper.next.next = reverseHead
            reverseHead = helper.next
        return reverseHead, reverseTail

    def reverseListRec(self, head):
        reverse_head = head
        while reverse_head.next:
            reverse_head = reverse_head.next
        self.rec(head)
        return reverse_head

    def rec(self, head):
        if not head:
            return None
        node = self.rec(head.next)
        if node:
            node.next = head
        head.next = None
        return head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
node = Solution().reverseBetween(a, 1, 1)
#while node:
#    print node.val
#    node = node.next

# Test reverse LL
head = Solution().reverseListRec(a)
while head:
    print head.val
    head = head.next

