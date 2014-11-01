"""
Problem:
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.
The array may contain duplicates.

Idea:
Compare to previous problem, NOT only need to add:
if num[mid] == num[start]:
    start += 1
Also need to add :
if num[end] > num[start]:
    return num[start]
in the for loop!!
Because if start element equal to mid element, then start += 1 means skip the start element and reprocess
the sub-problem, for each sub-problem, if the last element is greater than first element, then return firs0t.
"""
__author__ = 'Zhaowei'
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        start = 0
        end = len(num) - 1
        # if last > first, then no rotate.
        if num[end] > num[start]:
            return num[start]
        # NOTE, here is end - 1
        # when the loop ends, start and end will be on the two side of the 'crack'
        while start < end - 1:
            # NOTE! NOTE!
            # if last > first, then no rotate on this sub-problem.
            if num[end] > num[start]:
                return num[start]
            mid = (end + start)/2
            if num[mid] > num[start]:
                start = mid
            # NOTE: only difference to the previous problem
            elif num[mid] == num[start]:
                start += 1
            else:
                end = mid
        # the right hand side of the 'crack' is the smallest.
        return num[end]

print Solution().findMin([3, 3, 0, 1, 2, 2, 2])
print Solution().findMin([1, 2])
print Solution().findMin([0,0,1,1,2,0])
print Solution().findMin([10,1,10,10,10])
