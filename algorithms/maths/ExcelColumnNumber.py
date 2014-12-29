"""
Problem:
Related to question Excel Sheet Column Title
Given a column title as appear in an Excel sheet, 
return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

Idea:
This is a base 64 calculation

"""
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        result = 0
        factor = 1
        # NOTE reverse loop, no modify nor copy of the original array.
        # safe to use!
        for x in reversed(s):
            # NOTE python ord funciton and chr function
            result += (ord(x) - ord('A') + 1) * factor
            factor = factor * 26
        return result
