"""
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
"""
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    # This method takes O(n) time.
    def rotate_On(self, nums, k):
        length = len(nums)
        if k >= length:
            # NOTE, k may exceed the length
            k = k % length
        start = length - k
        tmp = nums[start : length]
        index = length-1
        for i in xrange(length-k-1,-1,-1):
            nums[index] = nums[i]
            index -= 1
        for i in xrange(0, len(tmp)):
            nums[i] = tmp[i]
        print nums

    def rotate (self, nums, k):
        

Solution().rotate([1,2,3,4,5,6,7], 1)

                        
