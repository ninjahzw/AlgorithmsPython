# Problem:
# Given a singly linked list L: L0 ->L1->...Ln-1->Ln,
# reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->...
# 
# You must do this in-place without altering the nodes' values.
# 
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
#
# Idea:
# break list into two parts (!! use slow and fast pointers !!)
# reverse the 2nd part
# Join use the former roles

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ReorderList:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None or head.next is None:
            return head 

        # find the middle point
        slow = head
        fast = head
        while fast != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            
        # devide two parts
        newHead = slow.next
        slow.next = None 
        newHead = self.reverseList(newHead)

        # IMP Join two LL one another
        helper = ListNode(0)
        traverser = ListNode(0)
        traverser.next = head
        while newHead and traverser.next:
            helper.next = newHead.next
            newHead.next = traverser.next.next
            traverser.next.next = newHead
            traverser = traverser.next.next
            newHead = helper.next 
    
    # IMP: To reverse a Linked List.      
    # @return : head of new list 
    def reverseList(self,head):
        helper = ListNode(0) 
        reverseHead = head
        while head.next:
            helper.next = head.next
            head.next = head.next.next
            helper.next.next = reverseHead
            reverseHead = helper.next 

        return reverseHead

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
ReorderList().reorderList(a)

while a:
    print a.val
    a = a.next
