"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] 
of gas to travel from station i to its next station (i+1). 
You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
(NOTE, means if there is a solution, it's unique, otherwise no sulutuon.)

Idea:
NOTE, do not quite understand!
http://blog.csdn.net/kenden23/article/details/14106137
http://fisherlei.blogspot.com/2013/11/leetcode-gas-station-solution.html
"""
__author__="HouZhaowei"
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        left = 0
        cur_sum = 0
        start_node = 0
        for i in xrange(0, len(gas)):
            current = gas[i]-cost[i]
            left += current
            cur_sum += current
            if cur_sum < 0 :
                start_node = i+1
                cur_sum = 0
        if left < 0:
            return -1
        return start_node
        
