# Problem:
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
#  Find all unique triplets in the array which gives the sum of zero.
# 
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <=c)
# The solution set must not contain duplicate triplets.
# For example, given array S = {-1 0 1 2 -1 -4},
# 
# A solution set is:
# (-1, 0, 1)
# (-1, -1, 2)
#
# Idea:
# for 2 sum, can be solved in n + nlgn time:
# sort the array first and then use head and tail pointer 
# for 3 sum, we can use the same intuition
# sort first, and maintain two pointers (head and tail)
# and an outer for loop to loop through the dataset
# for each each element of the dataset position at i:
# head = i+1, tail = leng-1
# then compair num[head]+num[tail] to -num[i]
# if geater then reduce tail if smaller then increase head (same to 2sum)
# NOTE do not forget tho skip duplicate.
 
class ThreeSum:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num)<3:
            return []
        num.sort()
        length = len(num)
        result = []
        row = []
        for k,x in enumerate(num):
            # NOTE! start from k+1,not 0!
            i = k+1
            j = length-1
            # skip dup
            if k!=0 and x == num[k-1]:
                continue
            while (i < j):
                if num[i] + num[j] == -x:
                    row = [x,num[i],num[j]]
                    result.append(row) 
                    i = i+1
                    j = j-1
                    # skip dup value at adjacent position 
                    while j > i and num[j] == num[j+1]:
                        j = j-1
                    while i < j and num[i] == num[i-1]:
                        i = i+1
                elif num[i] + num[j] < -x:
                    i = i+1
                else:
                    j = j-1
                           
        return list(result)

print ThreeSum().threeSum([0,0,0])
