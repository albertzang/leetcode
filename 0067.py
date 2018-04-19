class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        m = len(a)
        n = len(b)
        c = 0
        i = 1
        while c or i <= max(m, n):
            ai = int(a[-i]) if i <= m else 0
            bi = int(b[-i]) if i <= n else 0
            s = ai + bi + c
            c, d = s / 2, s % 2
            res = str(d) + res
            i += 1
        return res
