class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        n = len(g)
        m = len(s)
        i = 0
        j = 0
        res = 0
        while i < n and j < m:
            if s[j] >= g[i]:
                res += 1
                i += 1
            j += 1
        return res
