"""
Problem:
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon.
The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) 
was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. 
If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) 
upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2(K)  -3  3
-5    -10  1
10    30  -5(P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
"""
import sys

class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    # NOTE NOTE wrong solution!!!
    # why? for example -3, 5 outputs 1 but actually knight dies at -3 if initialized as 1.
    def calculateMinimumHP_Wrong(self, dungeon):
        if dungeon is None or len(dungeon) < 1:
            return None
        # NOTE important initialize row and column
        row = len(dungeon)
        col = len(dungeon[0])
        # NOTE important! way to initialize tmp!
        tmp = [[0 for i in xrange(col)] for i in xrange(row)]
        # initialization phase!
        tmp[0][0] = dungeon[0][0]
        for i in xrange(1, row):
            tmp[i][0] = dungeon[i][0] + tmp[i-1][0]
        for j in xrange(1, col):
            tmp[0][j] = dungeon[0][j] + tmp[0][j-1]
        # DP phase!
        for i in xrange(1, row):
            for j in xrange(1, col):
                tmp[i][j] = max(tmp[i-1][j],  tmp[i][j-1]) + dungeon[i][j]
        result = 0 - tmp[row-1][col-1] + 1
        return result if result > 0 else 1

    # NOTE Correct shoter Solution:
    def calculateMinimumHP_sim(self, dungeon):
        if dungeon is None or len(dungeon) < 1:
            return None
        max_min = 0
        # NOTE important initialize row and column
        row = len(dungeon)
        col = len(dungeon[0])
        # NOTE add a dummy row and col at bottom and right side. 
        # an extra dummy row ald col can make code cleaner.(without initialize last row and col)
        # NOTE must be initialized as max int!!
        tmp = [[sys.maxint for i in xrange(col+1)] for i in xrange(row+1)]
        # NOTE NOTE ! knight came at least 1 health
        tmp[row][col-1] = 1
        tmp[row-1][col] = 1
        for i in xrange(row-1, -1, -1):
            for j in xrange(col-1, -1, -1):
                min_health = min(tmp[i+1][j], tmp[i][j+1]) - dungeon[i][j]
                tmp[i][j] = min_health if min_health > 0 else 1
        return tmp[0][0]

    # Correct regular Solution:
    def calculateMinimumHP(self, dungeon):
        if dungeon is None or len(dungeon) < 1:
            return None
        # NOTE important initialize row and column
        row = len(dungeon)
        col = len(dungeon[0])
        tmp = [[0 for i in xrange(col)] for i in xrange(row)]
        # Initialize phase:
        # NOTE here must have 1- 
        tmp[row-1][col-1] = 1 - dungeon[row-1][col-1] if 1 - dungeon[row-1][col-1] > 0 else 1
        for i in xrange(row-2, -1, -1):
            # NOTE here doesn't need 1- because potentially previous has covered 1
            cur = tmp[i+1][col-1] - dungeon[i][col-1]
            tmp[i][col-1] = cur if cur > 0 else 1
        for j in xrange(col-2, -1, -1):
            cur = tmp[row-1][j+1] - dungeon[row-1][j]
            tmp[row-1][j] = cur if cur > 0 else 1
        for i in xrange(row-2, -1, -1):
            for j in xrange(col-2, -1, -1):
                # NOTE here doesn't need 1- because potentially previous has covered 1
                min_health = min(tmp[i+1][j], tmp[i][j+1]) - dungeon[i][j]
                tmp[i][j] = min_health if min_health > 0 else 1
        return tmp[0][0]

print Solution().calculateMinimumHP([[-3, 5]])
print Solution().calculateMinimumHP([[0]])
        
