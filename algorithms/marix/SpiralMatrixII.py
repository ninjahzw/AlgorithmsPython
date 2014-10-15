"""
Problem:
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

Idea:
basically same approach as 'SpiralMatrix'
"""
__author__ = 'Zhaowei'
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix = [[0 for i in xrange(n)] for i in xrange(n)]
        start_row = 0
        end_row = n - 1
        start_col = 0
        end_col = n - 1
        x = 1
        while x <= n*n:
            if start_row > end_row or start_col > end_col:
                break
            for j in range(start_col, end_col + 1):
                matrix[start_row][j] = x
                x += 1
            for i in range(start_row + 1, end_row + 1):
                matrix[i][end_col] = x
                x +=1
            # NOTE! IMPORTANT!
            # if do not have the following two rows, then repeat will occur.
            # this can make sure if only one line left, won't process it twice(force and back)
            if start_row == end_row or start_col == end_col:
                break
            for j in range(end_col-1, start_col-1, -1):
                matrix[end_row][j] = x
                x += 1
            for i in range(end_row-1, start_row, -1):
                matrix[i][start_col] = x
                x += 1
            start_row += 1
            end_row -= 1
            start_col += 1
            end_col -= 1
        return matrix

print Solution().generateMatrix(3)