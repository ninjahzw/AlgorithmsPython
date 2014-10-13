# Problem:
# Given two binary strings, return their sum (also a binary string).
# 
# For example,
# a = "11"
# b = "1"
# Return "100".
# 
# Idea:
# Just calculate bit by bit...

class AddBinary:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        nextbit = 0
        result = ''

        while len(a) > 0 and len(b) > 0:
            sum = int(a[-1]) + int (b[-1]) + nextbit
            if sum == 0:
                nextbit = 0
                result = '0'+result
            elif sum == 1:
                nextbit = 0
                result = '1'+result
            elif sum == 2:
                nextbit = 1
                result = '0'+result
            elif sum == 3:
                nextbit = 1
                result = '1'+result
            a = a[:-1]
            b = b[:-1]
        left = a if len(b) == 0 else b

        while len(left) > 0:
            sum = int(left[-1]) + nextbit 
            if sum == 0:
                nextbit = 0
                result = '0'+result
            elif sum == 1:
                nextbit = 0
                result = '1'+result
            elif sum == 2:
                nextbit = 1
                result = '0'+result
            left = left[:-1] 
        if nextbit == 1:
            result = '1'+result
        
        return result
        
print AddBinary().addBinary('101111','10')
