"""
Problem:
Given an integer n, return the number of trailing zeroes in n!.
Note: Your solution should be in logarithmic time complexity.

Idea:
The stupid solution to this problem is calculate the factorial and then calculate the 
number of zeros, however this solution is easy to overflow!

NOTE:  We count 5s in PRIME factors, we are done
Trailing 0s in n! = Count of 5s in prime factors of n!
                  = floor(n/5) + floor(n/25) + floor(n/125) + ....
NOTE: The time complexity is log5(n)!

Ref: http://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/
"""

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        total = 0
        while n > 0:
            n = n/5
            total += n
        return total
