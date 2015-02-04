"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.
"""

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        length = len(s)
        if s is None or length < 1:
            return True
        p1 = 0
        p2 = length - 1
        while p1 < p2:
            # NOTE skip non-alphanumeric chars.
            while not self.is_alph(s[p1]):
                p1 += 1
                # boundary condition
                if p1 > length-1: return True
            while not self.is_alph(s[p2]):
                p2 -= 1
                # boundary condition
                if p2 < 0: return True
            # boundary condition
            if p1 >= p2:
                return True

            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1
        return True

    # is a valid alphanumeric charactor
    def is_alph(self, c):
        # NOTE, in ascii table, a-z sequence and A-Z sequence are not consecutive.
        return ord('A') <= ord(c) <= ord('Z') \
            or ord('a') <= ord(c) <= ord('z') \
            or ord('0') <= ord(c) <= ord('9')

# print Solution().isPalindrome("A man, a plan, a canal: Panama")
print Solution().isPalindrome(".,")
        
                    
