"""
Problem:
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Idea:
Almost same as merge k sorted array.
"""

import heapq

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            heap.append((node.val, node))
        # NOTE this works as long as no duplicates, otherwise, it will start to campair objects.
        heapq.heapify(heap)
        dummy_head = ListNode(0)
        curr = dummy_head
        while heap:
            node = heapq.heappop(heap)
            curr.next = ListNode(node[0])
            curr = curr.next
            if node[1].next:
                heapq.heappush(heap, (node[1].next.val, node[1].next))
        return dummy_head.next
        
