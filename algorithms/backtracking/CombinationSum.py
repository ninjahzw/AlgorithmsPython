"""
Given a set of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie,a1 <= a2 <= ... <=ak).
The solution set must not contain duplicate combinations.

For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]

Idea:
Tag: Backtracking DFS
first sort.
NOTE, to eliminate duplicates, for each element, only check itself and bigger ones.
"""
__author__ = 'HouZhaowei'
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        return self.rec(0, sorted(candidates), target)

    def rec(self, start, candidates, target):
        current = []
        for i in xrange(start, len(candidates)):
            x = candidates[i]
            if x > target:
                continue
            if x == target:
                current.append([x])
                continue
            # NOTE: to eliminate duplicate, recur on items greater or equal to current element.
            tmp = self.rec(i, candidates, target - x)
            for one in tmp:
                current.append([x] + one)
        return current

print Solution().combinationSum([2,3,6,7], 7)
print Solution().combinationSum([8,7,4,3], 11)