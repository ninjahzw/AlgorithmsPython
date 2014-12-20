"""
Problem
Given two strings S and T, determine if they are both one edit distance apart.

Idea:
Just string operation!
NOTE: Pay attention to boundary conditions!
"""
class Solution:
    # @param s, a string
    # @param t, a string
    # @return a boolean
    def isOneEditDistance(self, s, t):
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                if i < len(s) - 1 and j < len(t) - 1:
                    return s[i+1:] == t[j+1:] or s[i+1:] == t[j:] or s[i:] == t[j+1:]
                if i < len(s) - 1:
                    return  s[i+1:] == t[j]
                if j < len(t) - 1:
                    return s[i] == t[j+1:]
                # in case that they both reach the end of the string
                return True
            i+=1
            j+=1
        return abs(len(s) - len(t)) == 1 

print Solution().isOneEditDistance("ab","ba")
