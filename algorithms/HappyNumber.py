"""
Problem:
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 02 = 1


Idea:
NOTE the key idea is to use a hashset to store already processed numbers,
incase run into same number processed before, it will goes to infinite loop, 
so return False at this point
"""
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        s = set()
        while n != 1:
            total = 0
            while n!= 0:
                total += (n%10)**2
                n  = n/10
            n = total
            if n in s:
                return False
            s.add(n)
        return True

print Solution().isHappy(19)


