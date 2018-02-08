class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = map(int, num1)
        num2 = map(int, num2)
        n = len(num1)
        m = len(num2)
        c = 0
        res = ''
        while n or m or c:
            a = 0
            b = 0
            if n > 0:
                a = num1[n - 1]
                n -= 1
            if m > 0:
                b = num2[m - 1]
                m -= 1
            s = a + b + c
            res = str(s % 10) + res
            c = s / 10
        return res
