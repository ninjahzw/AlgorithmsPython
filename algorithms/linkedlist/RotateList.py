# Given a list, rotate the list to the right by k places, where k is non-negative.
# 
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
#
# !NOTE! if k is grater than length of the list, then move length-k%length steps from head.
# Idea: 
# do a loop on the ll and count the length 
# then loop again and stop at length-k%length, then do the links.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class RotateList:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head or k < 1 or not head.next:
            return head
        cur = head
        length = 1 # count head
        while cur.next:
            cur = cur.next
            length += 1
        tail = cur
        cur = head
        steps = length - k%length
        if steps == length:
            return head
        while cur.next and steps > 1:
            cur = cur.next
            steps -= 1
        newHead = cur.next
        cur.next = None
        tail.next = head
        return newHead 
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
x = RotateList().rotateRight(a,2)
while x is not None:
    print x.val
    x = x.next
