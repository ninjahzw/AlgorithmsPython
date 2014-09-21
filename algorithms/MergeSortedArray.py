# Problem
# Given two sorted integer arrays A and B, merge B into A as one sorted array.
# 
# Note:
# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B.
# The number of elements initialized in A and B are m and n respectively.
# 
# Idea:
# Typically Sort Merge Problem but a little different..
# we have to !! merge from B to A !!, 
# The definition of the problem had already gave us instruction :!! A has enough space !!
# So we can do this from back to front.
# If B has some elements left after A is done, also need to handle that case
# The takeaway message from this problem is that the loop condition. 
# This kind of condition is also used for merging two sorted linked list.

class MergeSortedArray: 
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        while m > 0 and n > 0:
            if A[m-1] >= B[n-1]:
                A[m+n-1] = A[m-1]
                m -= 1
            else:
                A[m+n-1] = B[n-1]
                n -=1
        # if B has some elements left.
        while n > 0:
            A[m+n-1] = B[n-1]
            n -= 1

A = [1,3,5,8,0,0,0,0,0] 
MergeSortedArray().merge(A,4,[2,4,6,7,9],5)
print A
