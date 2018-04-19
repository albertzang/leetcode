class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        b = 0
        while (1 << b) * (1 << b) <= x:
            b += 1
        b -= 1
        res = 1 << b
        while b:
            b -= 1
            if (res | (1 << b)) * (res | (1 << b)) <= x:
                res |= 1 << b
        return res
