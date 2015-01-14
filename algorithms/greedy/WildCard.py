"""
Problem:
Implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "*") -> true
isMatch("aa", "a*") -> true
isMatch("ab", "?*") -> true
isMatch("aab", "c*a*b") -> false

Idea:
NOTE use greedy algorithm.
-- if there is not a match, see if you have previously stars.
-- still don't know why use mark.
"""


class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        index_s = 0
        index_p = 0
        star = -1
        mark = -1
        while index_s < len(s):
            if index_p < len(p) and (s[index_s] == p[index_p] or p[index_p] == '?'):
                index_s += 1
                index_p +=1
            elif index_p < len(p) and p[index_p] == '*':
                star = index_p
                index_p += 1
                mark = index_s
            else:
                if star != -1:
                    index_p = star + 1
                    mark += 1
                    index_s = mark
                else:
                    return False
        while index_p < len(p):
            if p[index_p] == '*':
                index_p += 1
            else:
                return False
        return index_p == len(p)


print Solution().isMatch("ac", "*?")
print Solution().isMatch("abcdefga", "a*a")

