# Problem:
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?

# For example,
# Given sorted array A = [1,1,1,2,2,3],

# Your function should return length = 5, and A is now [1,1,2,2,3].
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
        times = 0
        for i in xrange(1,len(A)):
            # init vacant to be the first dup and ignore latter dups.
            if A[i] == pre:
                times = times + 1
            else:
                # if different, restart counter.
                times = 0
            
            # remove element and just continue.(NOTE initialize vacant if first time)
            if times > 1:
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

A = [1,1,1,1]
print removeDupSortedArray().removeDuplicates(A)
print A   
