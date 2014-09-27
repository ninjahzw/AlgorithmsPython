# Problem:
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
#
# Idea:
# NOTE the critical part if to find the random TARGET of the new LinkedList.
# if we just copy the old random pointer to the new, then it's not deep copy
# because if the target node of the random pointer is deleted in the original list,
# the pointer is the new list will also point to None.
#
# Solution:
# apply three loops:
# 1. insert and copy node : e.g. a->b->c  ==>  a->a->b->b->c->c
# 2. copy random pointer: cur.next.random = cur.random.next
# 3. separate the new and the old: break one to two lists.
#
# see also:
# http://fisherlei.blogspot.com/2013/11/leetcode-copy-list-with-random-pointer.html

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class CopyLLRandomPointer:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        cur = head
        # dup and insert
        while cur:
            node = RandomListNode(cur.label)
            node.next = cur.next
            cur.next = node
            cur = node.next

        cur = head
        # copy random pointer
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
       
        # sperate the two LL 
        cur = head
        dup = cur.next if cur else None
        while cur:
            dupCur = cur.next
            cur.next = dupCur.next
            if cur.next:
                dupCur.next = cur.next.next
            cur = cur.next
        return dup
