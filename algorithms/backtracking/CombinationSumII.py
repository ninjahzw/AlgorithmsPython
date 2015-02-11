"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie,a1 <= a2 <= ... <=ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 

Idea:

"""
__author__ = 'HouZhaowei'
class Solution:

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
            # NOTE NOTE!!! leave the first one and ignore following dups.
            # e.g. have to do this in the case ([1,1],1) 
            if start < i and candidates[i] == candidates[i-1]:
                continue
            x = candidates[i]
            current.append(x)
            self.rec(current, result, i+1, candidates, target - x)
            current.pop()

print Solution().combinationSum([2,3,6,7], 7)
print Solution().combinationSum([3,4,7,8], 11)
print Solution().combinationSum([1,1],1)
print Solution().combinationSum([13,23,25,11,7,26,14,11,27,27,26,12,8,20,22,34,27,17,5,26,31,11,16,27,13,20,29,18,7,14,13,15,25,25,21,27,16,22,33,8,15,25,16,18,10,25,9,24,7,32,15,26,30,19], 25)
