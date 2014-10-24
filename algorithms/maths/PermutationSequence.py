"""
Problem:
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
Note: Given n will be between 1 and 9 inclusive.

Idea:

"""

__author__ = 'HouZhaowei'
class Permutations:

    """
    if the question asks about A(n,k) then the solution is like the following
    this is almost same as 'Combinations.py'
    """
    # @return a list of lists of integers
    def permutation(self, n, k):
        array = [x for x in range(n)]
        return self.rec(array, k)

    def rec(self, array, k):
        if len(array) == 1:
            return [array]
        if k == 1:
            return [[x] for x in array]
        result = []
        for i, x in enumerate(array):
            sub = self.rec(array[0:i] + array[i+1:len(array)], k-1)
            for y in sub:
                result.append([x] + y)
        return result

    #######################

    def __init__(self):
        self.result = []
    def get_permutation(self, n, k):
        array = [x for x in range(n)]
        return self.rec(array, n, k)
    def rec(self, array, n, k):
        sub = 1
        for i in range(1, n):
            sub *= i
        cur = k/sub
        print k,sub,cur
        self.result.append(array[cur])
        self.rec(array[:cur] + array[cur+1:], n-1, k % sub)


Permutations().get_permutation(8,31492)