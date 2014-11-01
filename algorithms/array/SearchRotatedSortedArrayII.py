"""
Problem:
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?
Would this affect the run-time complexity? How and why?
Write a function to determine if a given target is in the array.

Idea:
Comparing to 'Search in Rotated Sorted Array'
only add two lines at the bottom:
else:
    start += 1
-----------
and thus the time complexity rise up to o(n) why?
e.g. condition 1: A = 1,2,3,3,3,3,3 -> B = 3,1,2,3,3,3,3
or A = 3,3,3,3,3,3,4,5 -> B = 3,3,3,3,3,4,5,3
two different conditions result into the the same consequence B[mid] = B[start]
so if we meet an equal, we have to add start by 1 then check a gain.
"""
__author__ = 'HouZhaowei'
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        start = 0
        end = len(A)-1
        while start <= end:
            mid = (start + end)/2
            if A[mid] == target:
                return True
            # when the fault is on the right side
            if A[mid] > A[start]:
                if A[start] <= target <= A[mid]:
                    end = mid
                else:
                    start = mid+1
            # when the fault is on the left side
            elif A[mid] < A[start]:
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid-1
            else:
                start += 1
        return False