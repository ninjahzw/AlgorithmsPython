# NOTE NOTE, the recursion method can not print the whole sequence!!!
# because it's time complexity is not O(n)!
def fib(n):
    return rec(n)
def rec(n):
    if n == 1 or n == 2:
        return 1
    value =  fib(n-1) + fib(n-2)
    return value

print fib(10)

def fib2(n):
    a, b = 1, 1
    index = 0
    while index < n:
        print a
        a, b = b, a+b
        index += 1
fib2(10)
