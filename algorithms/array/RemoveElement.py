# Problem:
# Given an array and a value, remove all instances of that value in place and return the new length.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Idea:
# NOTE find the first same element and init the vacant space 
# then every element after will move forward (ignore the same)

class RemoveElement:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        result = 0
        if A is None or len(A) == 0:
            return 0 
        vacant = None
        for i in xrange(len(A)):
            # init vacant to be the first same and ignore latter sames.
            if A[i] == elem:
                A[i] = None
                # init the vacant to the first same
                if vacant is None : vacant = i
                continue
            # if no same, then move forward if there was a previous same.
            if vacant is not None:
                A[vacant] = A[i]
                A[i] =None
                vacant += 1
            result += 1
        return result

A = [1,1,2,3,3]
print RemoveElement().removeElement(A,2)
print A   
