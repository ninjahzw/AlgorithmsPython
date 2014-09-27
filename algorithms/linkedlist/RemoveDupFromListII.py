# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# 
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
#
# Idea:
# LinkedList operation always more complicated than thought!
# NOTE! NOTE! the head need to be changed if head elements will be deleted!

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class RemoveDupSortedList:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        headPre = ListNode(0)
        headPre.next = head
        pre = headPre
        cur = pre.next
        
        while cur:
            # check equality of cur and cur.next 
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            # cur need to be deleted
            # NOTE if head changes, headPre moves with pre.
            if cur is not pre.next:
                pre.next = cur.next
            # cur does not need to be deleted.
            else:
                pre = pre.next
            cur = pre.next

        return headPre.next


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
