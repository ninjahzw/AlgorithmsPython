# Problem: 
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
# 
# click to show more practice.
# 
# More practice:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#
# Idea:
# Use Dynamic Programming
# How do we compute OPT(j) from OPT(j-1)?
# We can either add A[j] to the previous best sum, or we start with a new subsequence. Therefore
# NOTE OPT(j) = max (OPT(j - 1) + A[j], A[j]).
#
#
class MaximumSubarray:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if A is None or len(A) == 0:
            return 0
        tmp = [0 for x in A]
        tmp[0] = A[0]
        maximum = A[0]
        # NOTE: the core part
        for i in xrange(1,len(A)):
            tmp[i] = max(tmp[i-1] + A[i], A[i])
            maximum = max(maximum, tmp[i])
        return maximum
print MaximumSubarray().maxSubArray([1])
        
            


