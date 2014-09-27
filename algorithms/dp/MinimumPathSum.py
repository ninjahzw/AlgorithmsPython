# Given a m x n grid filled with non-negative numbers, 
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Idea:
# NOTE: This problem is same to the UniPaths but different to Triangle.

class MinimumPathSum:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        row = len(grid)
        col = len(grid[0])
        tmp = [[0 for x in xrange(col)] for x in xrange(row)]
        tmp[0][0] = grid[0][0]
        # init:
        for i in xrange(1,row):
            tmp[i][0] = tmp[i-1][0] + grid[i][0]
        for j in xrange(1,col):
            tmp[0][j] = tmp[0][j-1] + grid[0][j]
        for i in xrange(1,row):
            for j in xrange(1,col):
                leftVal = tmp[i][j-1]
                topVal = tmp[i-1][j]
                tmp[i][j] = min(leftVal,topVal) + grid[i][j]
        return tmp[row-1][col-1]
a = [[1,2,5],[3,2,1]]
print MinimumPathSum().minPathSum(a)
