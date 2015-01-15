"""
Problem:
Given a list of non negative integers, arrange them such that they form the largest number.
For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
Note: The result may be very large, so you need to return a string instead of an integer.

Idea:
this is a sorting problem, how to compare two elements is the most important and fundamental part.

NOTE this answer is copied from:
http://bookshadow.com/weblog/2015/01/13/leetcode-largest-number/
A very elegant solution!!!!!
"""

class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = sorted([str(x) for x in num], cmp = self.compare)
        ans = ''.join(num).lstrip('0')
        return ans or '0'

    def compare(self, a, b):
        return [1, -1][a + b > b + a]
