class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        table = [0] + [-1] * amount
        for i in xrange(1, amount + 1):
            for c in coins:
                if i >= c and table[i - c] != -1:
                    if table[i] == -1:
                        table[i] = table[i - c] + 1
                    else:
                        table[i] = min(table[i], table[i - c] + 1)
        return table[-1]
