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

print plus_one([9,9,9])