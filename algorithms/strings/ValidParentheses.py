"""
CLASSIC!  Tag: Stack!
Problem:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Idea:
Use stack!
"""
__author__ = 'Zhaowei'
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for i, x in enumerate(s):
            # if the current stack is empty
            # or there is no corresponding other half at the top of the stack, push current in.
            if len(stack) == 0 or self.pair(x) != stack[-1]:
                stack.append(x)
            else:
                stack.pop()
        if len(stack) == 0:
            return True
        return False

    # given right part of parentheses return the corresponding left part
    # NOTE if the input is the left part then it's valid.
    def pair(self, half):
        if half == '(' or half == "[" or half == "{":
            return None
        if half == ')':
            return '('
        if half == ']':
            return '['
        if half == '}':
            return '{'

print Solution().isValid('()')