"""
There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Idea:
Scan two times one from head to tail one from tail to head
If current is greater than previous, add current to be pre + 1
NOTE when traverse back, additional condition must added.
"""

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candies = [1 for i in xrange(len(ratings))]
        for i in xrange(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        total = candies[-1]
        for i in xrange(len(ratings)-2, -1, -1):
            # NOTE total += candies[i] has to be added here!!
            # e.g. 1, 2, 3, 4, 1, when go back, can not set 4 to 1 + 1, skip it.
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1
            total += candies[i]
        return total

print Solution().candy([2, 2])
