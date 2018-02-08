class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        h = dict()
        for c in s:
            if c in h:
                h[c] += 1
            else:
                h[c] = 1
        f = False
        for k, v in h.iteritems():
            if v % 2:
                if f:
                    return False
                else:
                    f = True
        return True
