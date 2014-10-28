# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
# 
# For example,
# Given board =
# 
# [
#  ["ABCE"],
#  ["SFCS"],
#  ["ADEE"]
# ]
# word = "ABCCED", -> returns True,
# word = "SEE", -> returns True,
# word = "ABCB", -> returns False.
#
# Idea:
# check the adjacent neighbors start from each element of the 2D array.
# start from each element do DFS to check the adjacent neighbors/
# use DFS and maintain a boolean a two dimentional array to record the save status.

class WordSearch:

    visited = []

    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        self.visited = [[0 for x in xrange(len(board[0]))] for x in xrange(len(board))]
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.check(board,i,j,word,0):
                    return True
        return False 
    
    # @param n the ith element of word.
    def check(self,board,i,j,word,n):
        if n == len(word):
            return True
        # self.check boundary
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False
        # self.check if visited
        if self.visited[i][j]:
            return False
        # self.check current valid
        if word[n] != board[i][j]:
            return False
        self.visited[i][j] = 1
        result = self.check(board,i,j + 1,word,n + 1) or self.check(board,i + 1,j,word,n + 1) \
                or self.check(board,i - 1,j,word,n + 1) or self.check(board,i,j - 1,word,n + 1)
        self.visited[i][j] = 0
        return result




a = [0,0]
a[0] = ['a','b']
a[1] = ['c','d']
print a[0]
print WordSearch().exist(a,'bacd')
