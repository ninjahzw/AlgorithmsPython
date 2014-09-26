# Problem:
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this in place with constant memory.
# 
# For example,
# Given input array A = [1,1,2],
# 
# Your function should return length = 2, and A is now [1,2].
#
# Idea:
# NOTE find the first dup and init the vacant space 
# then every element after will move forward (ignore dups)

class removeDupSortedArray:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        result = 1
        if A is None or len(A) == 0:
            return 0 
        pre = A[0]
        vacant = None
        for i in xrange(1,len(A)):
            # init vacant to be the first dup and ignore latter dups.
            if A[i] == pre:
                A[i] = None
                # init the vacant to the first dup
                if vacant is None : vacant = i
                continue
            pre = A[i]
            # if no dup, then move forward if there was a previous dup.
            if vacant is not None:
                A[vacant] = A[i]
                A[i] =None
                vacant += 1
            result += 1
        return result

A = [1,1,2,3,3]
print removeDupSortedArray().removeDuplicates(A)
print A   
