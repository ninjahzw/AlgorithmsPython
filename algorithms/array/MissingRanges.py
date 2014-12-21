"""
Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

Idea:

IMPORTANT: add lower - 1 and upper + 1 to the original array.
"""

class Solution:
    # @param A, a list of integers
    # @param lower, an integer
    # @param upper, an integer
    # @return a list of strings
    def findMissingRanges(self, A, lower, upper):
        result = []
        # no need add lower-1 just assign it to pre
        A = A + [upper + 1]
        pre = lower-1
        for i, k in enumerate(A):
            if k - pre > 1:
                result.append(self.getRange(pre + 1, k - 1))
            pre = k
        return result

    def getRange(self, start, end):
        return str(start) + "->" + str(end) if end > start else str(start)

print Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99)
