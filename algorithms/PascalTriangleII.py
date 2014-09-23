# Problem:
# Given an index k, return the kth row of the Pascal's triangle.
# 
# For example, given k = 3,
# Return [1,3,3,1].
# 
# Note:
# Could you optimize your algorithm to use only O(k) extra space?
#
# Idea:
# Just use extra spase to store the prevous row
# NOTE this is basically the PascalTriangle problem but when k=3 actually output the 4th row
# of prerious result!! 
# this problem k start from 0! the PascalTriangle problem k start from 1!
# So I have to modify a little bit to adjust this range.


class PascalTriangleII:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex is None:
            return []

        previous = [1]
        for i in xrange(0,rowIndex):
            row = [1]
            if i > 0:
                for j in xrange(i):
                    row.append(previous[j] + previous[j+1])
            row.append(1)
            previous = row
        return previous

print PascalTriangleII().generate(0)


