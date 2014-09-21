# Problem:
# Given a linked list, determine if it has a cycle in it.
# 
# Follow up:
# Can you solve it without using extra space?
#
# Idea:
# Maintain two pointers, slow and fast all start form head.
# each time slow move one step and fast move two steps.
# if there is no cycle, then fast will reach the end
# if there is a cycle, then fast and slow will go infinite loop and they will meet!
# see detail on:
# http://www.cnblogs.com/hiddenfox/p/3408931.html (in Chinese)
# 
# Extention:
# Length of the cycle?
# Solution:
# start from the first position the two pointers met,
# the fast pointer stop at that position
# the slow one continue to move, until the met again,
# the steps of this pointer is the length of the cycle.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        fast = head
        slow = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            # here compair the object not the value, becuase there may have dup value.
            if slow == fast:
                return True
        return False
