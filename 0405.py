class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        if num < 0:
            mask = 1 << 31
            num = -(num & mask) + (num & ~mask)
        res = ''
        while num:
            n = num & 15
            if n < 10:
                res = str(n) + res
            else:
                res = chr(ord('a') + n - 10) + res
            num = num % (1 << 32) >> 4
        return res
