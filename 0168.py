class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while True:
            n = n - 1
            res = chr(ord('A') + (n % 26)) + res
            n = n / 26
            if n == 0:
                break
        return res
