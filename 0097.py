class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        table = [[False for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        for i in xrange(m + 1):
            for j in xrange(n + 1):
                if i == 0 and j == 0:
                    table[i][j] = True
                elif i == 0:
                    table[i][j] = table[i][j - 1] and s2[j - 1] == s3[j - 1]
                elif j == 0:
                    table[i][j] = table[i - 1][j] and s1[i - 1] == s3[i - 1]
                else:
                    table[i][j] = table[i][j - 1] and s2[j - 1] == s3[i + j - 1] or table[i - 1][j] and s1[i - 1] == s3[i + j - 1]
        return table[m][n]
