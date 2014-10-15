"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]
The minimum number of jumps to reach the last index is 2.
(Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Idea:
I came up to the dynamic programming solution which is more intuitive. but it will cost O(n^2) times.
Better Idea?
YES!
NOTE! IMPORTANT! use Greedy algorithm!
Note that we don't need to show the jump path, only the number of jumps is needed,
we can apply some trick here:
for the first step, the farthest it can go is A[0], so if this can reach the end then over.
if not, for the second step, the farthest it can go is max(i + A[i] for each i between index 0 and A[0])
if reach the end, then stop if not, continue with the same approach.
this approach only go through the array once, so the time complexity is O(n)
"""

# @param A, a list of integers
# @return a boolean
__author__ = 'HouZhaowei'
class Solution:
    # DP solution O(n^2)
    # @param A, a list of integers
    # @return an integer
    def jumpDP(self, A):
        tmp = [-1 for x in A]
        tmp[0] = 0
        length = len(A)-1
        for i, x in enumerate(A):
            for j in xrange(1, x + 1):
                index = i + j
                if index > length:
                    continue
                if tmp[index] == -1 or tmp[i] + 1 < tmp[index]:
                    tmp[index] = tmp[i] + 1
        return tmp[-1]

    # NOTE
    # Greedy solution O(n)
    def jump(self, A):
        if A is None or len(A) <= 1:
            return 0
        max_range = A[0]
        step = A[0]
        jump = 1
        for i in xrange(1, len(A)):
            if i == len(A)-1:
                return jump
            if i + A[i] > max_range:
                max_range = i + A[i]
            step -= 1
            if step == 0:
                jump += 1
                step = max_range - i
        return jump

print Solution().jump([1,2])