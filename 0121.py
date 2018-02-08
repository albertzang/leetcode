class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        n = len(prices)
        if n == 0:
            return profit
        else:
            start = prices[0]
            for i in xrange(1, n):
                start = min(start, prices[i])
                profit = max(profit, prices[i] - start)
        return profit
