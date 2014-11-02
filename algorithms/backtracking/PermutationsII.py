"""
Problem:
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].

Idea:
Basically same as 'Permutations' problem in this directory.
only for each recursion, add a dict to make sure (FOR EACH LEVEL)same value will be ignored.
"""
__author__ = 'HouZhaowei'
class PermutationsII:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute_unique(self, num):
        memory = dict()
        if len(num) == 1:
            return [num]
        result = []
        for i, x in enumerate(num):
            if x in memory:
                continue
            else:
                memory[x] = 1
            sub = self.permute_unique(num[0:i] + num[i+1:len(num)])
            for y in sub:
                result.append([x] + y)
        return result

print PermutationsII().permute_unique([1,1])
