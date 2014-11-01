"""
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

Idea:
Binary Search.
Simple solution which seems like O(n*log(n)) is: binary search find target,
and find left and right boundary simply use left_index -- and right_index ++
but if you look more into this, you will find the actual time complexity is O(n)
e.g. a long list with all elements same.

More efficient approach which is really O(n*log(n)) is when target is find,
then look for the two boundaries by two embedded binary searches.

Or, do two separate binary searches find the two boundaries.s
"""
__author__ = 'HouZhaowei'
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if A is None or len(A) == 0:
            return [-1, -1]
        start = 0
        end = len(A) - 1
        start_index = -1
        end_index = -1
        while start <= end:
            mid = (start + end)/2
            # if find the element, then do other two binary searches on both side.
            # to find the left and right borders.
            if A[mid] == target:
                start1 = 0
                end1 = mid
                while start1 <= end1:
                    mid1 = (start1 + end1)/2
                    if A[mid1] < target:
                        start1 = mid1+1
                    else:
                        end1 = mid1-1
                start_index = start1
                start1 = mid
                end1 = len(A) - 1
                while start1 <= end1:
                    mid1 = (start1 + end1)/2
                    if A[mid1] > target:
                        end1 = mid1-1
                    else:
                        start1 = mid1+1
                end_index = end1
                break
            elif A[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return [start_index, end_index]

print Solution().searchRange([5, 7, 7, 10], 8)
print Solution().searchRange([1, 2], 1)
print Solution().searchRange([1, 1], 1)