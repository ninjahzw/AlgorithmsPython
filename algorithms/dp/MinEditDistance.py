# Problem:
# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
# 
# You have the following 3 operations permitted on a word:
# 
# a) Insert a character
# b) Delete a character
# c) Replace a character
#
# Idea:
# This is an IMPORTANT and CLASSIC problem.
# Use Dynamic Programming
# for each pair of charater, we either choose one or choose both
# 
class EditDistance:
    tmp = []
    # @return an integer
    def minDistance(self, word1, word2):
        if len(word1) == 0:
            return word2
        if len(word2) == 0:
            return word1
        self.tmp = [[0 for x in word2] for x in word1]
        return self.rec(word1,word2,len(word1)-1,len(word2)-1)
    def rec(self,word1,word2,i,j):
        # if word is empty string then i or j is -1 so must have '<' here.
        if i <= 0:
            return j
        if j <= 0:
            return i
        if self.tmp[i][j] != 0:
            print "aaa"
            return self.tmp[i][j]
        self.tmp[i][j] = min( self.rec(word1,word2,i-1,j) + 1,\
                    self.rec(word1,word2,i,j-1) + 1,\
                    # if equal then + 0, if not, + 1
                    self.rec(word1,word2,i-1,j-1) + int(word1[i] != word2[j]))
        return self.tmp[i][j]
        
    # Notice that in this implementation:
    # the 'Edge' of the table is 1 size larger than the size of the array.
    # because we need to take 0 into consideration.
    # e.g. input = ('a','b') the result in tmp will be: [[0, 1], [1, 1]]
    def minDistanceNoneRecur(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        # init phase:
        tmp = [[0 for x in xrange(len2+1)] for x in xrange(len1+1)]
        for i in xrange(1,len1+1):
            tmp[i][0] = i
        for j in xrange(1,len2+1):
            tmp[0][j] = j
        # process phase:
        for i in xrange(1,len1+1):
            for j in xrange(1,len2+1):
                tmp[i][j] = min(tmp[i-1][j]+1 \
                               ,tmp[i][j-1]+1 \
                               ,tmp[i-1][j-1]+ int(word1[i-1] != word2[j-1]))
        return tmp[len1][len2]




print EditDistance().minDistanceNoneRecur("abcd","bcda")
"""
Element in tmp if imput is "abcd","bcda"
[0, 1, 2, 3, 4]
[1, 1, 2, 3, 3]
[2, 1, 2, 3, 4]
[3, 2, 1, 2, 3]
[4, 3, 2, 1, 2]
"""                

