"""
Problem:
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Idea:
Traverse the matrix once and remember each coordinate(i and j)
iterate each pair of the coordinates and set each row and col to 0.
"""
__author__ = 'Hou Zhaowei'
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def set_zeroes(self, matrix):
        if matrix is None or len(matrix) == 0:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        tmp = []
        for i, row in enumerate(matrix):
            for j, one in enumerate(row):
                if one == 0:
                    # NOTE! we have to keep i j in an array
                    # instead of directly set current row and col to 0.
                    tmp.append([i, j])
        for x in tmp:
            for k in xrange(rows):
                matrix[k][x[1]] = 0
            for k in xrange(cols):
                matrix[x[0]][k] = 0


a = [[1, 2, 3] ,[4, 0, 6], [7, 8, 9]]
Solution().set_zeroes(a)
print a