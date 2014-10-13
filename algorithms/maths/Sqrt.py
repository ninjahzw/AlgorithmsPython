"""
Problem:
Implement int sqrt(int x).
Compute and return the square root of x.

Idea:
use binary search.
NOTE that this problem only need integer values which means sqrt(2)=1 and sqet(3)=2
it will become more simpler.

here is a more mathematics way to solve this problem:
http://www.cnblogs.com/AnnieKim/archive/2013/04/18/3028607.html
"""
__author__ = 'Zhaowei'
class Sqrt:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.result = 0

    def sqrt(self, x):
        self.rec(x, 0, x)
        return self.result

    def rec(self, x, start, end):
        if start >= end:
            self.result = start
            return
        # handle the condition that x = 1
        a = (start + end)/2+1
        if a*a == x:
            self.result = a
        elif a*a > x:
            self.rec(x, start, a-1)
        else:
            self.rec(x, a, end)

print Sqrt().sqrt(100)