# Problem:
# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
# 
# Note:
# You may not engage in multiple transactions at the same time 
# (ie, you must sell the stock before you buy again).
# 
# Idea:
# It's really easy to solve this problem use O(n^2) approach:
# for each i in range of the input, calculate max profit of [0...i] and [i+1...n] respectively
# and sum them up as the result of i
# compair each result (i) to find the maxmum
# Note that each max profit calculation takes O(n) so the total time cost is O(n^2)
# 
# Better Idea? Yes!
# Use Dynamic Programming!
# We know that for each i we don't have to recalculate [0...i-1],[0...i-2] and so on.
# For each step, we calculate current max profit and store it to an array.[0...i]
# then reversely do the same thing [n-1...i+1]
# at the same time, compair each sum =  maxprofit([n-1...i+1]) + maxprofit([0...i])

class BestTimeBuyAndSellStockIII():
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices is None or len(prices) < 2:
            return 0
        profits = [0 for x in xrange(len(prices))]
        min = prices[0]
        maxProfit = 0
        for i,item in enumerate(prices):
            if item < min:
                min = item
            else:
                if item - min > maxProfit:
                    maxProfit = item - min
            profits[i] = maxProfit
        # initialize result to maxProfit
        result = maxProfit

        #########
        # reversely calculate the profit from i to len(prices-1) and,
        # compair the sum of each pair of i(reverse) and i-1(normal) 
        # in the temp storage 'profits' to current maxmum,
        # which is initialized to the max profit of transaction once (0 to len-1).
        maxProfit = 0
        max = prices[len(prices) -1]
        for i in xrange(len(prices)-2,-1,-1):
            if prices[i] > max:
                max = prices[i]
            else:
                if max - prices[i] > maxProfit:
                    maxProfit = max - prices[i]
            profits[i] = maxProfit
            if i > 0 and profits[i] + profits[i-1] > result:
                result = profits[i] + profits[i-1]
        return result 

print BestTimeBuyAndSellStockIII().maxProfit([2,4,5,2,10,23,1,24])
