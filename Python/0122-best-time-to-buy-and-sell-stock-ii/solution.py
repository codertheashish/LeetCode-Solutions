class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        n=len(prices)
        for i in range(n-1):
            if prices[i+1]>prices[i]:
                profit+=prices[i+1]-prices[i]
        return profit