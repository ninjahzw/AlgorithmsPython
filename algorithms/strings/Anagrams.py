# Problem:
# Given an array of strings, return all groups of strings that are anagrams.
# 
# Note: All inputs will be in lower-case.
#
# Analysis:
# Anagrams is two strings are using the same characters. 
# One way to compare two strings is use sort(). e.g. 
# Store the ordered string to a hashmap.
# key : sorted words
# value: the index that the word 1st appears
# set value to -1 if the word at that index has already been added to the result
# the -1 will not be changed again

class Anagrams:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        result = []
        tmp = dict()
        for i,item in enumerate(strs):
            origin = item
            item = ''.join(sorted(item))
            if item not in tmp :
                tmp[item] = i
                continue
            # make sure the original of the first one will be included!
            if tmp[item] == -1 :
                result.append(origin)
                continue
            result.append(origin)
            result.append(strs[tmp[item]])
            tmp[item] = -1 
        return list(result)

print Anagrams().anagrams(["dabc","cba","bca"])

