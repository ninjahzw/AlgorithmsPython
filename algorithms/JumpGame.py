# @param A, a list of integers
# @return a boolean
def canJump(self, A):
    index = 0
    length = len(A)
    while index < length:
        if index != length-1 and A[index] == 0:
            return False
            index = index + A[index]
            if index == length-1:
                return True
        return False
