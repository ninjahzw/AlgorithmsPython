"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your MAXIMUM jump length at that position.
Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.

Idea:
NOTE: it's the maximum length, not jump length.
Use one dimension DP, but only need to keep one variable.
maintain a 'step' initialized as A[0]
traverse through the array, for each element:
compare current value and step if bigger, then set step to current
NOTE for every loop step = step - 1.

When 'step' becomes '0' which indicates current value and step variable are all 0.
then return False.
"""

# @param A, a list of integers
# @return a boolean
def canJump(A):
    if A is None or len(A) == 0:
        return False
    step = A[0]
    end = len(A)-1
    index = 0
    while index <= end:
        if index + step >= end:
            return True
        if A[index] > step:
            step = A[index]
        if step == 0:
            return False
        index += 1
        step -= 1
    return False

print canJump([0])