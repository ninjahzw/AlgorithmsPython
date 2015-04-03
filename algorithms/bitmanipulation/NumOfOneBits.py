"""
Problem:

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011, so the function should return 3.

Solution:

"""

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = 0
        # NOTE the terminate condition is when n is <= 0.
        while n > 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count

print Solution().hammingWeight(11)
