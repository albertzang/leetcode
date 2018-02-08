class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        table = [True]
        for i in xrange(1, n + 1):
            t = False
            for j in xrange(i):
                if table[j] and s[j:i] in wordDict:
                    t = True
                    break
            table.append(t)
        return table[n]
