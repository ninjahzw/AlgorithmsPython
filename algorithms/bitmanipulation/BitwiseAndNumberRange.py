"""
Problem:
Given a range [m, n] where 0 <= m <= n <= 2147483647, 
return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

Idea:
For the 0, 2147483647 input, this doesn't work any more
"""

class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        result = 0
        # this is 32 bit number
        for i in xrange(1, 32):
            cur = 1
            for x in xrange(m, n+1):
                if (x >> i-1) & 1 == 0:
                    cur = 0
            result += (cur << i-1)
        return result

print Solution().rangeBitwiseAnd(0, 2147483647)

                        
