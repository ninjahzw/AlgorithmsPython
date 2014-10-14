"""
Problem:
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.

Idea:
NOTE!IMPORTANT! this is a good problem to test the understanding of binary search!
compare the target to the two side of "still consecutive half" each time.
intuitive explanation:
http://fisherlei.blogspot.com/2013/01/leetcode-search-in-rotated-sorted-array.html
"""
__author__ = 'Zhaowei'
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
                return mid
            # when the fault is on the right side
            if A[mid] >= A[start]:
                if A[start] <= target <= A[mid]:
                    end = mid
                else:
                    start = mid+1
            # when the fault is on the left side
            else:
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid-1
        return -1