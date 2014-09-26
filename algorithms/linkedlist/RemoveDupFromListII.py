# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# 
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
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
       # while head.next and  head.val == head.next.val:
       #     head = head.next
       # if not head.next:

       #     return None
       # head = head.next
       # if head is None or head.next is None:
       #     return head
        pre = ListNode(0);pre.next = head
        a = head 
        b = head.next
        while b:
            haveDup = False
            while b and a.val == b.val:
                haveDup = True
                a.next = b.next
                b = b.next 
            # if dup the also remove the start element of the dup seg.
            # also consider the end boundary condition, if b is None then b do not have a next. 
            if haveDup: a = b; pre.next = b;b = b.next if b else b;continue
            pre = pre.next
            a = a.next
            b = b.next
        return head

a = ListNode(1)
b = ListNode(1)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
x = RemoveDupSortedList().deleteDuplicates(a)
while x:
    print x.val
    x = x.next
