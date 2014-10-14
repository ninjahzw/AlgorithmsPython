"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.


Idea:
TODO..
"""
__author__ = 'Zhaowei'

class Solution:
    ## Solution from web
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        rowNum = len(matrix)
        colNum = len(matrix[0])
        leftI = leftJ = 0
        rightI = rowNum - 1
        rightJ = colNum - 1
        while leftI * colNum + leftJ <= rightI * colNum + rightJ:
            mid = ( leftI * colNum + leftJ + rightI * colNum + rightJ ) / 2
            midI = mid / colNum
            midJ = mid % colNum
            if matrix[midI][midJ] == target:
                return True
            elif matrix[midI][midJ] < target:
                leftI = (mid + 1) / colNum
                leftJ = (mid + 1) % colNum
            else:
                rightI = (mid - 1) / colNum
                rightJ = (mid - 1) % colNum
        return False



    ## TODO unfinished solution!
    def search_matrix(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])
        start = 1
        end = row * col
        while start < end:
            print start, end
            start_i, end_i = start % col, end % col
            start_j, end_j = start / col, end / col
            mid_i = (start_i + step) % col
            step = (end + start)/2 - 1
            mid_j = start_j + (start_i + step) / col
            mid = start + step

            print '-->', mid_i-1, mid_j-1, matrix[mid_i-1][mid_j-1]
            if matrix[mid_i-1][mid_j-1] > target:
                end = mid
            elif matrix[mid_i-1][mid_j-1] < target:
                start = mid
            else:
                return True
        return False
matrix = [
    [1,2,3],
    [10,22,33],
    [33,44,55]
]
print Solution().search_matrix(matrix, 22)