"""
NOTE! FAMOUS PROBLEM!
Problem:
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

Idea:
We can solve this use O(n^2) time which compare each pair of heights.
But we can use some information to greatly reduce the time complexity to O(n)
The feature of this problem is: the water can not be higher than the lower height.
We maintain two pointers (i and j) from head and tail (NOTE: must from both side!)
compare the two heights of the indices, here we have three conditions:
1. if height[i] > height[j]:
which means the maximum container with index j has been found, we can directly reduce j by 1.
2. if height[i] < height[j]:
same
3. if they equals:
reduce both.

"""

__author__ = 'HouZhaowei'

class Solution:
    # @return an integer
    def max_area(self, height):
        i, j = 0, len(height)-1
        max_area = 0
        while i < j:
            area = 0
            if height[i] > height[j]:
                area = (j - i) * height[j]
                j -= 1
            elif height[i] < height[j]:
                area = (j - i) * height[i]
                i += 1
            else:
                area = (j - i) * height[i]
                j -= 1
                i += 1
            if area > max_area:
                max_area = area

        return max_area