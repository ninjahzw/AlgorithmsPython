"""
Problem
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".

Idea:
NOTE is same REMAINDER not decimal appears then repeat begains!
"""
class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        result = ""
        if 0 == numerator: return "0"
        if 0 == denominator: return ""
        # NOTE parenthesis is needed here
        # NOTE XOR is needed here!!
        if (numerator < 0) ^ (denominator < 0):
            result += "-"
        # NOTE negative to positive, in case of OVERFLOW, should convert to long.
        numerator = abs(long(numerator))
        denominator = abs(long(denominator))
        # whole number part
        result += str(numerator/denominator)
        # check remainder
        remainder = numerator%denominator
        if remainder == 0:
            return result

        # fraction part
        hashmap = dict()
        result += "."
        while remainder != 0:
            if remainder in hashmap:
                result = result[:hashmap[remainder]] + "(" + result[hashmap[remainder]:] + ")"
                return result
            # put remainder to hash map and its index as value
            hashmap[remainder] = len(result) 
            result += str(remainder * 10 / denominator)
            remainder = (remainder * 10) % denominator

        return result

print Solution().fractionToDecimal(1 ,333)

