# Problem:
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
# 
# Note: The sequence of integers will be represented as a string.
# 
# Idea:
# For a specific index i calculate its value based on i-1
# So this is a dynamic programming problem NOTE: not backtracking problem!
# According the defination, just count and combine.

class CountAndSay:
    # @return a string
    def countAndSay(self, n):
        if n < 1:
            return None
        if n == 1:
            return "1"
        pre = self.countAndSay(n-1)
        counter = 1
        result = ""
        for i in xrange(len(pre)):
            # NOTE just write like this can handle the end boundary 
            if i < len(pre)-1 and pre[i] == pre[i+1]:
                counter += 1
            else:
                result += str(counter)
                result += pre[i]
                # reset counter
                counter = 1
        return result

print CountAndSay().countAndSay(2)
