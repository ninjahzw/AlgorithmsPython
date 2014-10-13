"""
Problem:
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

Idea:
This is more complex than Transpose, because each point will trigger 4 points' move.
So we only deal with the left-up quarter points, and for each points find the related other points to swap.
NOTE: to find the rule of other related indices of current point, try to make examples like when n = 3 and n = 4

See also:
http://www.programcreek.com/2013/01/leetcode-rotate-image-java/
http://www.cnblogs.com/TenosDoIt/p/3768734.html
"""
__author__ = 'HouZhaowei'

class RotateImage:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        range_j = n/2 if n % 2 == 0 else n/2 + 1
        for i in xrange(0, n/2):
            for j in xrange(0, range_j):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1] = tmp
        return matrix

    # NOTE this approach is transpose, not rotate!
    def transpose(self, matrix):
        for i in xrange(1,len(matrix)):
            for j in xrange(len(matrix[i]) - i):
                tmp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = tmp


a = [[1,2,3],[4,5,6],[7,8,9]]
RotateImage().rotate(a)
print a