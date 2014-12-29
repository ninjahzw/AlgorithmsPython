"""
Problem
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 

Idea:
NOTE, IMPORTANT:
This is base 26, but start from 1!
"""
class Solution:
    # @return a string
    def convertToTitle(self, num):
        result = ""
        remainder = 1
        while num > 0:
            num = num - 1
            remainder = num % 26 + 1
            result = chr(remainder + ord('A') - 1) + result
            num = num / 26
        return result

print Solution().convertToTitle(25)
