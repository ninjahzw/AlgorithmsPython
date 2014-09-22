# Problem:
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# 
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# Above is a 3 x 7 grid. How many possible unique paths are there?
# 
# Note: m and n will be at most 100.
# 
# Idea:
# Use Dynamic Programming:
# board[i][j] = board[i-1][j] + board[i][j-1]
# Two dimensional array to store each position
#

class UnitPaths:
    # Nested loop approach
    # @return an integer
    def uniquePathsDp(self, m, n):
        board = [[0 for x in xrange(n)] for x in xrange(m)]
        # initialize first row and first col
        for i in xrange(n):
            board [0][i] = 1
        for i in xrange(m):
            board [i][0] = 1
        for i in xrange(1,m):
            for j in xrange(1,n):
                board[i][j] = board[i-1][j] + board[i][j-1]
        return board[m-1][n-1]

    # Recursive approach
    # NOTE!
    # DO NOT forget to use the tmp two dimensional array to store the already calculated value
    # otherwise the computation complexity will be Huuuuuuge !
    board = []
    def uniquePaths(self, m, n):
        self.board = [[0 for x in xrange(n)] for x in xrange(m)]
        return self.rec(m-1,n-1)
    def rec(self,i,j):
        # for position 0,0 the possibility is 1
        if i == 0 or j == 0:
            return 1
        if self.board[i][j] != 0:
            return self.board[i][j]
        self.board[i][j] = self.rec(i-1,j) + self.rec(i,j-1)
        return self.board[i][j]

print UnitPaths().uniquePaths(2,4)

