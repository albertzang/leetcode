class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        n = len(prices)
        for i in xrange(n - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]
        return profit
