# Problem:
# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# 
# You may assume no duplicates in the array.
# 
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0
#
# Idea:
# Just pay attention to boundary conditions.
# NOTE there is actually log(n) solution!

class SearchInsertPosition:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if target < A[0]:
            return 0
        if target > A[-1]:
            return len(A)
        for i, x in enumerate(A):
            if x < target:
                continue
            if x >= target:
                return i
        return 0

    # NOTE ! log(n) solution
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        start = 0
        end = len(A)-1
        while start <= end:
            mid = (start + end)/2
            if A[mid] == target:
                return mid
            if A[mid] < target:
                start = mid+1
                continue
            if A[mid] > target:
                end = mid - 1
        # NOTE NOTE NOTE !!! do not return start + 1 or end
        return start
