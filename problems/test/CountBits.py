import sys
def count_bits(n):
    while n > 0:
        print n & 1
        n = n >> 1
n = sys.argv[1]
count_bits(int(n))
