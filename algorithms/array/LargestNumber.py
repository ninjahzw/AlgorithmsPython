"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
Note: The result may be very large, so you need to return a string instead of an integer.

Idea:
a + b > b + a then the a is prior to b in the result.
NOTE super important!!!!!
"""

class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        # NOTE useage of sorted function, using self-defined compare function!
        num = sorted([str(x) for x in num], cmp = self.compare)
        # make result as a string and eliminate heading 0s.
        ans = ''.join(num).lstrip('0')
        return ans or '0'

    def compare(self, a, b):
        ## NOTE!NOTE! 
        # >>> [1, -1][2>1]
        # -1
        # NOT 1 !
        # here when a + b > b + a is true, return -1, means a < b means a prior to b
        return [1, -1][a + b > b + a]
