class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        s = sum(A)
        f = sum([i * A[i] for i in xrange(n)])
        m = f
        for i in xrange(n - 1, 0, -1):
            f = f + s - n * A[i]
            m = max(m, f)
        return m
