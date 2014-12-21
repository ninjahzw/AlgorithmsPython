"""
Problem
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.
For example, Given s = "eceba",
T is "ece" which its length is 3.

"""

class Solution:
    # @param s, a string
    # @return an integer
    # NOTE wrong solution
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if s is None or len(s) == 0:
            return 0
        char_map = [-1 for i in range(256)]
        index = 0
        num_distinct = 0
        max_length = 0
        cur_length = 0
        for i, x in enumerate(s):
            print x
            if char_map[ord(x)] == -1 or char_map[ord(x)] < index:
                print '--', x
                num_distinct += 1
            char_map[ord(x)] = i
            cur_length += 1
            if num_distinct > 2:
                cur_length -= 1
                index = i
                if cur_length > max_length:
                    max_length = cur_length
                cur_length = 1
                num_distinct = 1
        if cur_length > max_length:
            max_length = cur_length
        return max_length

print Solution().lengthOfLongestSubstringTwoDistinct("bacc")
