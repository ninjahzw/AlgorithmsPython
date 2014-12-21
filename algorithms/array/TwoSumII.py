"""
Problem:
Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. 
Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

Solution:

"""
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        if num is None or len(num) < 2:
            return None
        start = 0
        end = len(num) - 1
        while start < end:
            cur_sum = num[start] + num[end]
            if cur_sum == target:
                return (start + 1, end + 1)
            if cur_sum < target:
                start += 1
                continue
            if cur_sum > target:
                end -= 1
                continue

print Solution().twoSum([2, 7, 11, 15], 9)
                         
