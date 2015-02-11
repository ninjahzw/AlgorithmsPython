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
    def combinationSum_old(self, candidates, target):
        return self.rec(0, sorted(candidates), target)

    def rec_old(self, start, candidates, target):
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

    # NOTE much better solution!
    # always use this way to solve this kind of problem
    def combinationSum(self, candidates, target):
        result = []
        current = []
        self.rec(current, result, 0, sorted(candidates), target)
        return result

    def rec(self, current, result, start, candidates, target):
        # NOTE judge target here instead of in the for loop!
        if target == 0:
            # NOTE, must append a copy!!!
            result.append(current[:])
        if target < 0:
            return
        for i in xrange(start, len(candidates)):
            # NOTE to eliminate dups
            if i > start and candidates[i] == candidates[i-1]:
                continue
            x = candidates[i]
            current.append(x)
            self.rec(current, result, i, candidates, target - x)
            current.pop()

print Solution().combinationSum([2,3,6,7], 7)
print Solution().combinationSum([2,2,2,1,3], 5)
