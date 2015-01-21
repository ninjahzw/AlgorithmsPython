"""
Problem:
https://oj.leetcode.com/problems/valid-sudoku/

Idea:

"""
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        if board is None or len(board) < 1:
            return True0
        length = len(board)
        for i in xrange(length):
            tmpi = [0 for x in xrange(length+1)]
            tmpj = [0 for x in xrange(length+1)]
            tmpij = [0 for x in xrange(length+1)]
            for j in xrange(length):
                if board[i][j] != '.':
                    if tmpi[int(board[i][j])] == 0:
                        tmpi[int(board[i][j])] = 1
                    else:
                        return false
                if board[i][j] != '.':
                    if tmpj[int(board[i][j])] == 0:
                        tmpj[int(board[i][j])] = 1
                    else:
                        return false
                if board[3*(i/3) + j/3][3*(i%3) + j%3] != '.':
                    if tmpij[int(board[3*(i/3) + j/3][3*(i%3) + j%3])] == 0:
                        tmpij[int(board[3*(i/3) + j/3][3*(i%3) + j%3])] = 1
                    else:
                        return false
        return True

print Solution().isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
