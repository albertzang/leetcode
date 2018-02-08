class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for c in s:
            digit = ord(c) - ord('A') + 1
            res *= 26
            res += digit
        return res
