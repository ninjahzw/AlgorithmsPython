# Given a linked list, return the node where the cycle begins.
# If there is no cycle, return null.
#
# Follow up:
# Can you solve it without using extra space?
#
# Idea:
# Basic idea see LinkedListCycle.py
# 0 -> 0 -> 0 -> 0 -> 0
#                 \   |
#                    0   <- kth element
# suppose there is a cycle, '\' (direction : bottom -> up) and  '|' (up -> down) denotes several times linking
# the fast and slow meet at the kth element in the cycle (must be in the cycle)
# let L = length before the cycle
# R = length of the cycle
# then at the time they meet we have:
# steps(slow) = L + nR + k  (slow may also go some cycles before they meet)
# steps(fast) = L + mR + k  
# We know fast is 2 times faster, so:
# L + mR + k = 2(L + nR + k)
# => mR = L + k + 2nR
# => L + k = (m+2n)R where (m+2n) is Positive Integer
# which means L and k are complementary based on Y, So start fron K, with L steps can reach the start point.
# Or explan like this: L = R-k + (m+2n-1)R
# R-k is the start point, and (m+2n-1)R means goes serveral Cycles.
#
# see detail on:
# http://fisherlei.blogspot.com/2013/11/leetcode-linked-list-cycle-ii-solution.html 
# http://www.cnblogs.com/hiddenfox/p/3408931.html 

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
        hasCycle = False
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            # here compair the object not the value, becuase there may have dup value.
            if slow == fast:
                hasCycle = True
                break 
        if hasCycle:
            slow2 = head
            while slow != slow2:
                slow2 = slow2.next
                slow = slow.next
        else:
            return None
        return slow
