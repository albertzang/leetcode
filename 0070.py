class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        a = 1
        b = 1
        i = 2
        while i <= n:
            c = a + b
            a = b
            b = c
            i += 1
        return c
