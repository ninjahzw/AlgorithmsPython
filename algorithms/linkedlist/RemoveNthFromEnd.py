# Problem:
# Given a linked list, remove the nth node from the end of list and return its head.
# 
# For example,
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# 
# Note:
# Given n will always be valid.
# Try to do this in one pass.
#
# Idea:
# Maintain two main pointers (actually 3) the cursor pointer traverse through the list.
# NOTE the start pointer starts from head when the cursor reach to the n-th emelent.
# when the cursor reaches the end, the position of the start pointer is the element to remove.
# Also need to maintain another pointer right before the start pointer to perform the remove.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class RemoveNthFromEnd:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        pre = ListNode(0)
        pre.next = head 
        start = None 
        cursor = head
        counter = 0
        while cursor is not None:
            counter += 1
            if counter >= n:
                if counter == n :start = head;cursor = cursor.next;continue
                start = start.next
                pre = pre.next
            cursor = cursor.next
        if counter >=n:
            # NOTE special case! then the length of the list is n, remove head.
            if pre.next is head : return  head.next
            pre.next = start.next
        return head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
b = RemoveNthFromEnd().removeNthFromEnd(a,1)
while b is not None:
    print b.val
    b = b.next
