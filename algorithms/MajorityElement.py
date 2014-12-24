"""
Problem:
Given an array of size n, find the majority element. 
The majority element is the element that appears more than upper[n/2] times.

You may assume that the array is non-empty and the majority element always exist in the array.

Solution:
NOTE:
this problem can be solved in O(nlogn) time O(1) space by sorting, 
and O(n) time O(n) space useing hashing.

IMOPRTANT: this solution is elegant!
Whenever count return to 0, means other elements pf the previous part of the array 
successfully offset the current majority. then candidate current element as new majority,
because every time same number of other elements offset current candidate, and 
the real majority appears more than n/2 times, so at last it will remain.

Reference:
http://www.sysexpand.com/?path=exercises/majority-element
"""


class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        majority_index = 0
        count = 1
        for i in xrange(1, len(num)):
            if num[i] == num[majority_index]:
                count += 1
            else: count -= 1
            if count == 0:
                majority_index = i
                count = 1
        return num[majority_index]

print Solution().majorityElement([2,1,1,3,1]);
