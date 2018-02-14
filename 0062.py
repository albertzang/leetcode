class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        N = m + n - 2
        k = min(m, n) - 1
        a = 1
        b = 1
        for i in xrange(k):
            a *= N - i
            b *= i + 1
        return a / b
