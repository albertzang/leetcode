class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        hs = set()
        for c in s:
            if c in hs:
                hs.remove(c)
                count += 1
            else:
                hs.add(c)
        return 2 * count + int(len(hs) != 0)
