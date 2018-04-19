class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * length
        for (s, e, d) in updates:
            res[s] += d
            if e + 1 < length:
                res[e + 1] -= d
        for i in xrange(1, length):
            res[i] += res[i - 1]
        return res
