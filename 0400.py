class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        d = 1
        while n > 9 * d * i:
            n -= 9 * d * i
            i += 1
            d *= 10
        x = d + (n - 1) / i
        n = (n - 1) % i
        while n > 0:
            x %= d
            d /= 10
            n -= 1
        return x / d
