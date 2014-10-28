"""
Problem:
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, there are a total of 5 unique BST's.

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3

Idea:
In "Unique Binary Search Trees II", we need to generate all trees.
The algorithm has the same idea. But we don't just return the numbers.
We return the trees that n integers can from.
Then we use a nested for-loop to go through every possible combinations of left tree and right tree
for a given root. We will do it recursively because it's the same for the left tree and right tree of root.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class UniqueBSTs:
    # @return a list of tree node
    def generateTrees(self, n):
        tmp = [[None for i in xrange(n+2)] for j in xrange(n+2)]
        return self.rec(tmp,1,n)

    def rec(self,tmp,start,end):
        if start > end:
            # NOTE! must return [None]
            return [None]
        possibilities = []
        for j in range(start,end+1):
            lefts = self.rec(tmp,start,j-1) if tmp[start][j-1] is None else tmp[start][j-1]
            rights = self.rec(tmp,j+1,end) if tmp[j+1][end] is None else tmp[j+1][end]
            for left in lefts:
                for right in rights:
                    root = TreeNode(j)
                    root.left = left
                    root.right = right
                    possibilities.append(root)
        tmp[start][end] = possibilities
        return possibilities

list = UniqueBSTs().generateTrees(3)
for one in list:
    print one.val
