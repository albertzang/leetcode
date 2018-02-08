class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        h = dict()
        for c in s:
            if c in h:
                h[c] += 1
            else:
                h[c] = 1
        for c in t:
            if c in h:
                if h[c] == 0:
                    return False
                else:
                    h[c] -= 1
            else:
                return False
        return len(s) == len(t)
