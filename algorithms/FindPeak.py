"""
Problem:
 peak element is an element that is greater than its neighbors.
 Given an input array where num[i] != num[i+1], find a peak element and return its index.
 The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

 You may imagine that num[-1] = num[n] = -inf.
 For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
 click to show spoilers.

 Note:
 Your solution should be in logarithmic complexity.

Idea:
TRICK: add -inf to the head and tail of the array to eliminate boundary issues.
NOTE: the basic idea is compair middle element to its neighbors:
Do a binary search for a peak.
For any mid element: 
if it is bigger than its neighbors then peak found,
if it is in a up slop, then the peak will be in the right part (mid, end),
if it is in a down slop, then the peak will be in the left part (start, mid)
if it is in a pit, then either left or right (my algorithm always choose left part in this case)
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        num = [-float('inf')] + num + [-float('inf')]
        return self.rec(0, len(num)-1, num)
        
    def rec(self, start, end, num):
        print start, end
        if end > start:
            mid = (end + start)/2
            if num[mid-1] < num[mid] and  num[mid+1] < num[mid]:
                return mid - 1
            if num[mid-1] < num[mid] < num[mid+1]:
                # NOTE, not mid + 1 and mid - 1 just mid.
                return self.rec(mid, end, num)
            else:
                return self.rec(start, mid, num)
        else:
            return start - 1
                    
print Solution().findPeakElement([3, 2, 1, 2, 3, 2, 1])

