class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [1] * (n + 1)
        for i in xrange(1, n + 1):
            table[i] = sum(table[j] * table[i - 1 - j] for j in xrange(i))
        return table[n]
