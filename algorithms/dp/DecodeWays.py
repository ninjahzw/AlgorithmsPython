"""
Problem:
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

Idea:

"""
__author__ = 'Hou Zhaowei'
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        # directly decide the result if the length of the string is 0 or 1
        if s is None or len(s) == 0:
            return 0
        if len(s) == 1:
            if s[0] == '0':
                return 0
            return 1
        # the string must not start with '0'
        if s[0] == '0': 
            return 0

        # NOTE in DP, we usually apply one more space
        # in 2-D array, apply one more row and col
        tmp = [0 for x in xrange(0, len(s) + 1)]
        tmp[0] = 1
        tmp[1] = 1
        # use DP to determin if length is >= 2
        for i in xrange(2, len(s) + 1):
            # the i-th index in the tmp denotes i-1 th index in the original string
            index = i - 1 
            # if substring like 30 or 40 or 50 .... exists, 
            # then the string does not have a solution.
            if s[index] == '0' and (s[index-1] == 0 or s[index-1] > '2'):
                return 0
            if s[index] > '0':
                tmp[i] = tmp[i-1]
            if '0' < s[index-1] < '2' or (s[index-1] == '2' and s[index] < '7'):
                tmp[i] += tmp[i-2]
        return tmp[-1]

print Solution().numDecodings("01")
