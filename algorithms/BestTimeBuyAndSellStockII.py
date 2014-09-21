# Problem:
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. 
# You may complete as many transactions as you like 
# (ie, buy one and sell one share of the stock multiple times). 
# However, you may not engage in multiple transactions at the same time 
# (ie, you must sell the stock before you buy again).
#
# Idea:
# Complex Idea:
# Buy at each local pit and sell at each local peek.
# DO NOT miss-consider the last element, It's always a local peak or pit
# if it's a local peak then if holding stock, sell. do nothing otherwise.
# 
# Simple Idea:
# JUST SEE THE CODE!
# basically this is the most profit.

class BestTimeBuyAndSellStock:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        # 0 or 1 elements will not have any profit. 
        if prices is None or len(prices) < 2:
            return 0
        buy = False
        profit = 0
        buyprice = 0
        for i in xrange(1,len(prices)):
            pre = prices[i-1]
            now = prices[i]
            # buy at local pit
            if not buy and now > pre:
                buyprice = pre
                buy = True
            # sell at local peak
            if buy and now < pre:
                sellprice = pre
                profit += (sellprice-buyprice)
                buy = False
            # if holding stock, must sell it at the end of day
            if buy and i == len(prices)-1:
                profit += (prices[i] - buyprice)

        return profit
            
    def maxProfitSimplified(self, prices):
        profit = 0
        for i in xrange(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
                     


print BestTimeBuyAndSellStock().maxProfit([2,4,5,2,10,23,1,24,1,2])


