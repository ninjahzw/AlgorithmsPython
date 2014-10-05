# Problem:
# Follow up for "Unique Paths":
# 
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
# 
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
# 
# Note: m and n will be at most 100.
# Idea:
# Similiar to previous problem:UniPath
# This time I can only come out the recursion idea
# Also use an m*n extra space to store the paths on each grid.
# and then use DP to compute grid by grid.
# Note that if there is an obstacle set current grid in board to 0.
# because no paths can through this grid

class UniPathsObs:

    board = []
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        self.board = [[-1 for x in xrange(n)] for x in xrange(m)]
        return self.rec(m-1,n-1,obstacleGrid)
    def rec(self,i,j,obstacleGrid):
        # set to 1 if the position has a obstacle
        if obstacleGrid[i][j] == 1:
            return 0
        # for position 0,0 the possibility is 1
        # this time here has to be 'and' because considering the 
        # existence of obstacle the first row or col may not be all '1's.
        if i == 0 and j == 0:
            return 1
        if self.board[i][j] != -1:
            return self.board[i][j]
        # consider boundary conditions
        top = 0 if i-1 < 0 else self.rec(i-1,j,obstacleGrid)
        left = 0 if j-1 < 0 else self.rec(i,j-1,obstacleGrid)
        self.board[i][j] = top + left
        return self.board[i][j]
a = []
print UniPathsObs().uniquePathsWithObstacles(a)

