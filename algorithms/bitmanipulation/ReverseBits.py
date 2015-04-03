"""
Problem:

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), 
return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer

Idea:

NOTE
1. this is 32 bit, so we must supplement the 0s after n is consumed.
e.g., the example above, for the input binary, the preceding 6 0s must be trailing 0s of the result.

2. The + and - has higher priority than bit manipulation operations!!
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        index = 0
        while index < 32:
            # left shift the result and add the last binary of the input to its tail.
            # NOTE The + and - has higher priority than bit manipulation operations!
            result = (result << 1) + (n & 1)
            n = n >> 1
            index += 1
        return result

print Solution().reverseBits(43261596)
