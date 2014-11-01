"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.

Idea:
NOTE, Python will process more than one spaces one by one. (so is Java)
"""
__author__ = 'Zhaowei'
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        length = 0
        for i in xrange(len(s)-1, -1, -1):
            if s[i] == ' ':
                # eliminate the spaces in the end
                if length == 0:
                    continue
                break
            length += 1
        return length
print Solution().lengthOfLastWord("Hello    World")