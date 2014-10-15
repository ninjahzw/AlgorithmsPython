"""
Problem:
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

Idea:
IMPORTANT PROBLEM!
No trick for this problem.
Just find the pattern and apply the pattern for each 'spiral'
NOTE two dimensional array operation!
"""
__author__ = 'Zhaowei'
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if matrix is None or len(matrix) == 0:
            return []
        start_row = 0
        end_row = len(matrix) - 1
        start_col = 0
        end_col = len(matrix[0]) - 1
        result = []
        while True:
            if start_row > end_row or start_col > end_col:
                break
            for j in range(start_col, end_col + 1):
                result.append(matrix[start_row][j])
            for i in range(start_row + 1, end_row + 1):
                result.append(matrix[i][end_col])
            # NOTE! IMPORTANT!
            # if do not have the following two rows, then repeat will occur.
            # this can make sure if only one line left, won't process it twice(force and back)
            if start_row == end_row or start_col == end_col:
                break
            for j in range(end_col-1, start_col-1, -1):
                result.append(matrix[end_row][j])
            for i in range(end_row-1, start_row, -1):
                result.append(matrix[i][start_col])
            start_row += 1
            end_row -= 1
            start_col += 1
            end_col -= 1
        return result

a = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print Solution().spiralOrder(a)