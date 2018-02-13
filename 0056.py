# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = list()
        if not intervals:
            return res
        intervals.sort(key=lambda i: i.start)
        s = intervals[0].start
        e = intervals[0].end
        for i in intervals:
            if e < i.start:
                res.append(Interval(s, e))
                s = i.start
                e = i.end
            else:
                e = max(i.end, e)
        res.append(Interval(s, e))
        return res
