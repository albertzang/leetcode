class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = {}
        l = 0
        start = 0
        for i, c in enumerate(s):
            if c in h and h[c] >= start:
                start = h[c] + 1
            l = max(l, i - start + 1)
            h[c] = i
        return l
