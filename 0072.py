class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        table = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        for i in xrange(1, m + 1):
            table[i][0] = i
        for j in xrange(1, n + 1):
            table[0][j] = j
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                diff = int(word1[i - 1] != word2[j - 1])
                table[i][j] = min(table[i - 1][j - 1] + diff, table[i - 1][j] + 1, table[i][j - 1] + 1)
        return table[m][n]
