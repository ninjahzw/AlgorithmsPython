# Problem:
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock)
# Design an algorithm to find the maximum profit.
#
# Idea:
# At first glance, you might think that finding the minimum and maximum value would do,
# but it does have a hidden restriction, that is: !! You must buy before you can sell !!.
class BestTimeBuyAndSellStock:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices): 
        if prices is None or len(prices) == 0:
            return 0
        min = float("inf") # infinity
        maxDiff = 0
        
        # Make sure the sell value must after the buy value!
        for i in prices:
            # always keep the smallest value
            if i < min: 
                min = i
            else: 
                # means this value could be the sell value
                if i-min > maxDiff:
                    maxDiff = i-min
        return maxDiff

print BestTimeBuyAndSellStock().maxProfit([2,4,5,2,10,23,1,24])

