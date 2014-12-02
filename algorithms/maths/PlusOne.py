"""
Problem:
Given a non-negative number represented as an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.

Idea:
Reversely traverse the array, add digit by digit
NOTE don't forger to consider the last digit.
"""
__author__ = 'HouZhaowei'

def plus_one(digits):
    next_digit = 1
    for i in xrange(len(digits)-1,-1,-1):
        # break if the previous sum < 10
        if next_digit == 0:
            break
        digit = digits[i] + 1
        if digit >= 10:
            next_digit = 1
        else:
            next_digit = 0
        digits[i] = digit % 10

    # consider last digit
    if next_digit == 1:
        digits = [1] + digits
    return digits

def plus_one_simplified(digits):
    for i in xrange(len(digits)-1,-1,-1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    # if has not returned then the original data must be 999...
    # so just append a 0 and set 1 to the first element yields the result.
    digits.append(0)
    digits[0] = 1
    return digits

print plus_one_simplified([9, 9, 9])
