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