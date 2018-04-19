class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [1] * n
        for i in xrange(1, n):
            for j in xrange(i):
                table[i] = max(table[i], (j + 1) * max(i - j, table[i - j - 1]))
            print table[i]
        return table[-1]
