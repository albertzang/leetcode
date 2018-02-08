class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = 0
        start = 0
        end = 0
        for i in range(len(s)):
            l1 = self.expand(s, i, i)
            l2 = self.expand(s, i, i + 1)
            ll = max(l1, l2)
            if ll > l:
                l = ll
                start = i - (l - 1) / 2
                end = i + l / 2
        return s[start : end + 1]

    def expand(self, s, i, j):
        n = len(s)
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
        return j - i - 1
