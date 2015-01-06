"""
Problem:
Compare two version numbers version1 and version1.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

"""


class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        a = version1.split('.')
        b = version2.split('.')
        i = 0
        while i < len(a) and i < len(b):
            num_a = int(a[i])
            num_b = int(b[i])
            if num_a > num_b:
                return 1
            elif num_a < num_b:
                return -1
            i += 1
            if len(a) == len(b):
                return 0                
            if i == len(a):
                while i < len(b):
                    if int(b[i]) > 0:
                        return -1
                    i += 1
                return 0
            if i == len(b):
                while i < len(a):
                    if int(a[i]) > 0:
                        return 1
                    i += 1
                return 0
print Solution().compareVersion('1.0','1')
