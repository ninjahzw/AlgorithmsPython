"""
Problem:
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

Idea:
Decompose to sub-problems.
NOTE this is permutation not combination, so the order does matters.
This problem is like Combinations in this folder, only we have to consider every number as the start number
for a specific loop.
One time pass :)
"""
__author__ = 'HouZhaowei'
class Permutations:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) == 1:
            return [num]
        result = []
        for i, x in enumerate(num):
            sub = self.permute(num[0:i] + num[i+1:len(num)])
            for y in sub:
                result.append([x] + y)
        return result

print Permutations().permute([1,2,3])