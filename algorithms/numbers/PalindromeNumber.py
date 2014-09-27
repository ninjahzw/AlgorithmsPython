# Problem:
# Determine whether an integer is a palindrome. Do this without extra space.
#
# Idea:
# NOTE compair each two sides one by one to the middle.
# problems involve in integers always use % and / operation to optimize.
# See also 'reverse integers' problem.
class PalindromeNumber:
    # @return a boolean
    def isPalindrome(self, x):  
        if x < 0:
            return False
        if x / 10 == 0:
            return True
        start = 10
        end = 1
        a = x
        while a >= 10:
            a = a/10
            end *= 10
        while start <= end:
            if start == 10:
                if x % start != x / end:
                    return False
            elif (0 if x % start < start/10 else x % start / (start/10)) != x / end % 10:
                return False 
            start *=10
            end /=10
        return True

print PalindromeNumber().isPalindrome(313) 
