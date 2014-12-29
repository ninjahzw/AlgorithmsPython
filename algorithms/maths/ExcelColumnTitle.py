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
            # NOTE num has to be minus one, because starts from 1
            num = num - 1
            result = chr(num % 26 + ord('A')) + result
            num = num / 26
        return result

print Solution().convertToTitle(25)
