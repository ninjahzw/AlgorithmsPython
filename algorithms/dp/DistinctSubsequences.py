"""
!!IMPORTANT!!
Problem:
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions of 
the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

Idea:
The BackTracking Idea is more intuitive but will get "Time limit Exceed."

More Efficient Idea? YES! DP!
Let W(i, j) stand for the number of subsequences of S(0, i) in T(0, j). 
If S.charAt(i) == T.charAt(j), W(i, j) = W(i-1, j-1) + W(i-1,j); Otherwise, W(i, j) = W(i-1,j).
NOTE: Just list the example, we can figure out why this approach could work.
"""
class Solution:
    def __init__(self):
        self.count = 0

    # @return an integer
    def numDistinct(self, S, T):
        self.rec(S, T)
        return self.count

    def rec (self, S, T):
        if len(T) == 0:
            self.count += 1
            return
        if len(S) == 0:
            return
        # NOTE!! if equals, can choose consume a T or not concume!
        if T[0] == S[0]:
            self.rec(S[1:],T[1:])
            self.rec(S[1:],T)
        else:
            # Can only chose not consume otherwise.
            self.rec(S[1:],T)

    # Much more efficient way!
    # NOTE that we only need to compute the maximum count, so we can apply DP!
    # NOTE NOTE index must start from 0 to length, same to Edit Distance
    # Because we must consider 0 length, and length from 1 to Array.length
    # So the iteration starts from 1 and for every iteration, the index should be i-1 and j-1
    def numDistinctDP(self, S, T):
        tmp = [[ 0 for i in xrange(len(T) + 1)] for i in xrange(len(S) + 1) ]
        # if length of T is 0, then count is 1 (remove all in S)
        for i in xrange(len(S)+1):
            tmp[i][0] = 1
        for i in xrange(1, len(S)+1):
            for j in xrange(1, len(T)+1):
                # NOTE this part basically same idea to the Back Tracking solution. 
                if S[i-1] == T[j-1]:
                    tmp[i][j] = tmp[i-1][j-1] + tmp[i-1][j]
                else:
                    tmp[i][j] = tmp[i-1][j]
        return tmp[-1][-1]

print Solution().numDistinctDP("rabbbit", "rabbit")
"""
for the test input, result is:
[1, 0, 0, 0, 0, 0, 0]
[1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0]
[1, 1, 1, 1, 0, 0, 0]
[1, 1, 1, 2, 1, 0, 0]
[1, 1, 1, 3, 3, 0, 0]
[1, 1, 1, 3, 3, 3, 0]
[1, 1, 1, 3, 3, 3, 3]
"""
