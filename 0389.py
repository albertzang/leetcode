class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letters = [0] * 26
        for c in s:
            letters[ord(c) - ord('a')] += 1
        for c in t:
            idx = ord(c) - ord('a')
            if not letters[idx]:
                return c
            else:
                letters[idx] -= 1
