class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        zz = []
        n = len(s)
        l = numRows - 1
        for i in range(0, n, l):
            z = s[i : i + l].ljust(numRows)
            if i / l % 2:
                zz.append(list(reversed(z)))
            else:
                zz.append(list(z))
        res = ''
        for i in range(numRows):
            for z in zz:
                if z[i] != ' ':
                    res += z[i]
        return res
