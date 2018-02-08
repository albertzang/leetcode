class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 1
        n = len(s)
        while i < n:
            if s[i - 1] != ' ' and s[i] == ' ':
                res += 1
            i += 1
        return res + int(i == n and s[i - 1] != ' ')
