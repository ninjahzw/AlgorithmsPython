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
# 
class UnitPaths:
    total = 0
    # @return an integer
    def uniquePaths(self, m, n):
        self.rec(0,0,m,n) 
        return self.total
    def rec(self,i,j,m,n):
        if i == m-1 and j == n-1:
            self.total += 1
            return
        if i == m-1:
            self.rec(i,j+1,m,n)
            return
        if j == n-1:
            self.rec(j,i+1,m,n)
            return
        self.rec(i,j+1,m,n)
        self.rec(j,i+1,m,n)
        self.rec(j+1,i+1,m,n)

    def uniquePathsDp(self, m, n):
        


print UnitPaths().uniquePaths(100,100)            

