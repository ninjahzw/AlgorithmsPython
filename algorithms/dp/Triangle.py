# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
# 
# For example, given the following triangle
# [
#     [2],
#    [3,4],
#   [6,5,7],
#  [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# Note:
# Bonus point if you are able to do this using only O(n) extra space, 
# where n is the total number of rows in the triangle.
# 
# IDEA
# NOTE NOTE USE Bottom-Up Dynamic Programming!
# Top-down will use more space and thus is not prefered to solve this problem.
# this solution is awesome!
# NOTE for each element, its children are only the adj 2 in the next row
# NOTE start from the last row to the first row.

class Triangle:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        # init the tmp storage to be the last row of the triangle
        row = triangle[-1]
        for layer in xrange(len(triangle)-2,-1,-1 ):
            for one in xrange(0,layer+1):
                # update the tmp storage to be the current row
                # with each element being current smallest to now.
                row[one] = min(row[one],row[one+1]) + triangle[layer][one]
        return row[0]
               
        

a = [[-1],[2,3],[1,-1,-3]]
print Triangle().minimumTotal(a)
