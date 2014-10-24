"""
NOTE! FAMOUS PROBLEM!!
Problem:
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
Detail : https://oj.leetcode.com/problems/trapping-rain-water/

Idea:
IMPORTANT, NOTE! the trick to solve this problem is awesome.
An O(n) solution is to consider each bar at a time, we can see that, for each bar,
the water itself can trap depends on the max height on its left and right,
e.g.  if current bar is of height 2, the max height on its left is 4, max height on its right is 3,
then water can be trapped in this bar is min(4,3)-2 = 1.

Thus, To find the trapped water at position i,
we need to find the maximum value of the left elements of i and right elements of i.
Assuming they are maxLeft[i] and maxRight[i].
The trapped water is min (maxLeft[i], maxRight[i]) - A[i] (if this value is larger than 0).

To find maxLeft and maxRight, we need to scan the array from left to right and from right to left.
You can check the details in the code below.
"""
__author__ = 'Zhaowei'
class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if A is None or len(A) == 0:
            return 0
        max_left = [0 for x in xrange(len(A))]
        max_right = [0 for x in xrange(len(A))]
        max_height = A[0]
        # scan form left to right, for every element set its left maximum
        for i, x in enumerate(A):
            max_left[i] = max_height
            if x > max_height:
                max_height = x
        max_height = A[-1]
        # scan from right to left, do the same thing as before.
        for i in xrange(len(A)-1, -1, -1):
            max_right[i] = max_height
            if A[i] > max_height:
                max_height = A[i]
        result = 0
        # compare max_left ot max_right find the minimum and minus current value
        # will be the amount of water that current value can contain.
        for i in xrange(len(A)):
            current = min(max_left[i], max_right[i]) - A[i]
            # NOTE, current could <=0.
            if current > 0:
                result += current
        return result