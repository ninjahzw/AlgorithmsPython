"""
Problem:
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.
You may assume no duplicate exists in the array.

Idea:
NOTE: the conditions of the loop and the position of the smallest. See the comments among code.
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
            mid = (end + start)/2
            if num[mid] > num[start]:
                start = mid
            else:
                end = mid
        # the right hand side of the 'crack' is the smallest.
        return num[end]

print Solution().findMin([4, 5, 6, 7, 0, 1, 2])
print Solution().findMin([1, 2])

