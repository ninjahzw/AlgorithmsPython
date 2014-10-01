# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MergeTwoSorted:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0) 
        returnHead = head
        while l1 and l2:
            if l1.val>l2.val:
                head.next = l2
                head = head.next
                l2 = l2.next
            else:
                head.next = l1
                head = head.next
                l1 = l1.next
        while l1:
            head.next = l1
            head = head.next
            l1 = l1.next
        while l2:
            head.next = l2
            head = head.next
            l2 = l2.next 

        return returnHead.next


a = ListNode(0)
b = ListNode(2)
c = ListNode(4)
d = ListNode(1)
e = ListNode(3)
a.next = b
b.next = c
d.next = e
node = MergeTwoSorted().mergeTwoLists(a,d)
while node:
    print node.val
    node = node.next
