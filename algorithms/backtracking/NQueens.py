# Problem:
# N-queens
# 
# Idea:
# 
# Naive Algorithm
# Generate all possible configurations of queens on board and print a configuration that satisfies the given constraints.
# 
# while there are untried conflagrations
# {
#    generate the next configuration
#    if queens don't attack in this configuration then
#    {
#       print this configuration;
#    }
# }
# Backtracking Algorithm
# The idea is to place queens one by one in different columns, starting from the leftmost column. 
# When we place a queen in a column, we check for clashes with already placed queens.
#  In the current column, if we find a row for which there is no clash, we mark this row and column as part of the solution. 
# If we do not find such a row due to clashes then we backtrack and return false.
#
# simpler solution:
# http://stackoverflow.com/questions/25052858/n-queens-backtracking-solution-implimented-by-python-generator
# but also much harder to understand.

class NQueens:
    result = []
	# @return a list of lists of string
    def solveNQueens(self, n):
        # Use '.'*n to create n '.' for each line of board and thus init n*n '.'s.
        board = ['.'*n for x in range(n)]
        self.solveNQRec(n,board,0)
        return self.result

    def solveNQRec(self,n,board,col):
        if col >= n:
            # on to the last of the col can lead to one result. 
            # here must append the clone of board WHY ?.
            print board
            self.result.append(board)
        for row in range(n):
            # if not safe, then no go deep.
            if self.safe(n, row, col, board):
                str = board[row]
                # replace the col index position to Q
                str = str[:col] + 'Q' + str[col+1:]
                board[row] = str
                self.solveNQRec(n,board,col + 1)
                # if backtrack to here, then set current value back to '.'.
                str = str[:col] + '.' + str[col+1:]
                board[row] = str

    def safe(self, n, row, col, queens):
        # do not need to check column since each loop goes on a single col.
        # check row on left side
        for i in range(1,col+1):
            if queens[row][col-i] == 'Q':
                return False
            if row-i >= 0 and queens[row-i][col-i] == 'Q':
                return False
            if row+i < n and queens[row+i][col-i] == 'Q':
                return False
        return True

print NQueens().solveNQueens(4)

