# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if len(intervals) <= 1:
            return True
        intervals = sorted(intervals, key=lambda interval: interval.start)
        e = intervals[0].end
        for i in intervals[1:]:
            if i.s < e:
                return False
            else:
                e = i.e
        return True
