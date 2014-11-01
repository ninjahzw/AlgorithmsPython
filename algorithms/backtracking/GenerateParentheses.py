"""
Problem:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
"((()))", "(()())", "(())()", "()(())", "()()()"

Idea:
The result set of this problem is exponential.
most step may have two choices (ether apply left parentheses or right parentheses)
but some the feature of the problem must be taken into consideration:
there must be enough left parentheses before a right one can apply.

NOTE that if we change the position of left rec and right rec,
the result doesn't change, only the order of the result changes.
(the traverse order changes, from left to right.)

TODO:
QUESTION: can this be considered as a "backtracking" solution ?
"""
__author__ = 'HouZhaowei'

class GenerateParentheses:
    # @param an integer
    # @return a list of string
    def generate_parentheses(self, n):
        size = n * 2
        result = []
        self.rec(0, 0, "", result, n)
        return result

    def rec(self, left_num, right_num, current, result, n):
        if left_num == n:
            for i in xrange(right_num, n):
                current += ")"
            result.append(current)
            return

        # choose left parentheses
        self.rec(left_num + 1, right_num, current + "(", result, n)

        # NOTE: only apply right parentheses when have enough left ones.
        if right_num < left_num:
            # choose right parentheses
            self.rec(left_num, right_num + 1, current + ")", result, n)

print GenerateParentheses().generate_parentheses(3)
