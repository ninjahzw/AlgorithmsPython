# Problem:
# Given numRows, generate the first numRows of Pascal's triangle.
# 
# For example, given numRows = 5,
# Return
# 
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
# Idea:
# just follow the role:
# the 2nd value of this row is the sum of the 1st and 2nd value of the last row
# the 3rd value of this row ...... 2nd and 3rd row of the last row
# ......
# and the first and last value of a row is always 1

class PascalTriangle:

    # @return a list of lists of integers
    def generate(self, numRows):
        result = []
        if numRows is None or numRows == 0:
            return result

        result.append([1])
        for i in xrange(1,numRows):
            row = [1]
            if i > 1:
                for j in xrange(i-1):
                    row.append(result[i-1][j] + result[i-1][j+1])
            row.append(1)
            result.append(row)
        return result

print PascalTriangle().generate(4)


