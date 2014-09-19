# Follow up for N-Queens problem.
# Now, instead outputting board configurations, return the total number of distinct solutions.
#
# Idea: 
# Also follow up N-Queen problem, on change the result to count. 

class NQueens:
    count = 0
	# @return an integer 
    def totalNQueens(self, n):
        # Use '.'*n to create n '.' for each line of board and thus init n*n '.'s.
        board = ['.'*n for x in range(n)]
        self.solveNQRec(n,board,0)
        return self.count

    def solveNQRec(self,n,board,col):
        if col >= n:
            # on to the last of the col can lead to one result.
            self.count += 1
        for row in range(n):
            # if not safe, then no go deep.
            if self.safe(n, row, col, board):
                str = board[row]
                # replace the col index position to 
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

print NQueens().totalNQueens(4)

