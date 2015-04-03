# Problem:
# Implement pow(x, n).
#
# Idea:
# NOTE NOTE Use divide and conquer to solve this Much Much Faster!
# reduce O(n) times multiplication to O(logn) times. log2(2147483647) = 31!
# Also do not forget the condition that n<0

class Pow:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n < 0:
            return 1.0/self.power(x, -n)
        else:
            return self.power(x, n)
    
    # NOTE: for input 0.00001,2147483647
    # this naive approach will take a very very long time..
    def powerInefficient(self, x, n):
        result = x
        for i in xrange(1,n):
            result = result*x
        return result

    # NOTE: Better solution: divide and conquer 
    def power(self, x, n):
        if n == 0:
            return 1
        value = self.power(x,n/2)
        if n % 2 == 0:
            return value*value
        else:
            return value*value*x
print Pow().pow(0.44528, 1)

