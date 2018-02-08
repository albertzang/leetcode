class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = [chr(l) for l in xrange(ord('a'), ord('z') + 1)]
        indices = [s.index(l) for l in letters if s.count(l) == 1]
        return min(indices) if len(indices) else -1
