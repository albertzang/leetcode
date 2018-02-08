class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        table = [[False for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        table[0][0] = True
        for j in xrange(1, n + 1):
            table[0][j] = j > 1 and p[j - 1] == '*' and table[0][j - 2]
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if p[j - 1] == '*':
                    table[i][j] = table[i][j - 2] or (table[i - 1][j] and (p[j - 2] == '.' or p[j - 2] == s[i - 1]))
                else:
                    table[i][j] = table[i - 1][j - 1] and (p[j - 1] == '.' or p[j - 1] == s[i - 1])
        return table[m][n]
