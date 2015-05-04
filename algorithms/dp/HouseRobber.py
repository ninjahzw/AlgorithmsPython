"""
Problem:
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that 
adjacent houses have security system connected and it will automatically 
contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police

Idea:
This is a classic DP problem.
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if num is None or len(num) == 0:
            return 0
        if len(num) == 1:
            return num[0]
        a = num[0]
        b = max(a, num[1])
        for i in xrange(2, len(num)):
            tmp = b
            b = max(a + num[i], b)
            a = tmp
        return b

# print Solution().rob([1,2,3,4,2,3,12,3])
print Solution().rob([1,1,1])
             
