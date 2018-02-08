class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x >= 0 else -1
        x = abs(x)
        bound = 214748364
        result = 0
        while x != 0:
            if result > bound:
                return 0
            if result == bound:
                if sign == 1 and x > 7:
                    return 0
                if sign == -1 and x > 8:
                    return 0
            result = result * 10 + x % 10
            x = x / 10
        return result * sign
