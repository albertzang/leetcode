class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n = x ^ y
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res
