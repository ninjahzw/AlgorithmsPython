# Given an array with n objects colored red, white or blue, 
# sort them so that objects of the same color are adjacent, 
# with the colors in the order red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# 
# Note:
# You are not suppose to use the library's sort function for this problem.
# 
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's,
# then overwrite array with total number of 0's, then 1's and followed by 2's.
# 
# Could you come up with an one-pass algorithm using only constant space?
class SortColors:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        length = len(A)
        red = 0;
        blue = length - 1
        i = 0
        while i < length:
            if A[i] == 0 and i > red:
                tmp = A[red]
                A[red] = 0
                A[i] = tmp
                red += 1
                continue
            if A[i] == 2 and i < blue:
                tmp = A[blue]
                A[blue] = 2
                A[i] = tmp 
                blue -= 1
                continue
            # in the condition that A[i] is 1
            i += 1
A = [1,0]
SortColors().sortColors(A)
print A

