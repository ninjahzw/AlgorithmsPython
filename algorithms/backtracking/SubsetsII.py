# Given a collection of integers that might contain duplicates, S, return all possible subsets.
# 
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,2], a solution is:
# 
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
#
# Idea:
# Solution similiar to SubSet
# This condition 
class SubSetsII:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S): 
        result = [[]]
        S.sort()
        self.dfs(S, 0, result, [])
        return result

    def dfs(self, S, position, result, tmp):
        i = position
        while i < len(S):
            tmp.append(S[i])
            self.dfs(S, i+1, result, tmp)
            result.append(tmp[:])
            tmp.remove(S[i])
            while i < len(S)-1 and S[i] == S[i+1]:
                i=i+1
            i=i+1

class SubSetsIIDP:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        result = [[]]
        for i in xrange(len(S)):
            while i < len(S)-1 and S[i] == S[i+1]:
                print S[i],S[i+1]
                i=i+1
            for j in xrange(len(result)):
                copy = result[j][:]
                copy.append(S[i])
                result.append(copy)
        return result

print SubSetsII().subsetsWithDup([1,2,2,2])
