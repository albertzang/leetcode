class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        n = len(timeSeries)
        if n == 0:
            return 0
        res = duration
        s = timeSeries[0]
        for t in timeSeries[1:]:
            res += min(s + duration, t) - s
            s = t
        return res
