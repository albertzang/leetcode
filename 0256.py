class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0:
            return 0
        for i in xrange(1, n):
            costs[i] = [
                costs[i][0] + min(costs[i - 1][1], costs[i - 1][2]),
                costs[i][1] + min(costs[i - 1][0], costs[i - 1][2]),
                costs[i][2] + min(costs[i - 1][0], costs[i - 1][1])
            ]
        return min(costs[n - 1])
