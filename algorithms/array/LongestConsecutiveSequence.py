"""
Tags : Hashing
Problem:
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

Idea:
We can solve this problem by first sorting in O(n log(n))time
Use Hashing to achieve O(n)

First put the elements into a hash table and set the value default to 0
Use Hash table to find a consecutive list one by one.
for a value in the list recursively find x-1 x-1-1 x-1-1-1 ... and x+1 x+1+1 ... is in hash table

"""
__author__ = 'houzhaowei'
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        hash_table = dict()
        maximum = 0
        # value 0 : not visited
        # value 1 : visited
        for i, x in enumerate(num):
            hash_table[x] = 0
        for i, x in enumerate(num):
            if x not in hash_table:
                continue
            hash_table[x] = 1
            count = 1
            left = x - 1
            right = x + 1
            # while the value is in hash table and is not visited...
            while left in hash_table and hash_table[left] == 0:
                count += 1
                hash_table[left] = 1
                left -= 1
            while right in hash_table and hash_table[right] == 0:
                count += 1
                hash_table[right] = 1
                right += 1
            if count > maximum:
                maximum = count
        return maximum

print Solution().longestConsecutive([100, 4, 200, 1, 3, 2])