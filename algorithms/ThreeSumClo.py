# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, 
# target. Return the sum of the three integers. 
# You may assume that each input would have exactly one solution.
# 
# For example, given array S = {-1 2 1 -4}, and target = 1.
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2). 
# 
# Idea:
# basically same idea to the Three sum.
# keep the minimum diff, each time compair the abs(sum-target) to diff.
# NOTE  the increment or decrement condition is compair sum to target!
class ThreeSumClo:
    # @return an integer
    def threeSumClosest(self, num, target):
        if len(num)<3:
            return []
        num.sort()
        length = len(num)
        result = 0
        row = []
        dif = float('inf')
        for k,x in enumerate(num):
            # NOTE! start from k+1,not 0!
            i = k+1
            j = length-1
            # skip dup
            if k!=0 and x == num[k-1]:
                continue
            while (i < j):
                s =  num[i] + num[j] + x
                if s == target:
                    return s
                if abs(s - target) < dif:
                    dif = abs(s - target)
                    result = s
                if s < target:
                    i += 1
                else:
                    j -= 1
        return result

print ThreeSumClo().threeSumClosest([0,1,2],3)
