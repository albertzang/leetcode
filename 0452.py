class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        res = 0
        pos = None
        for l, r in points:
            if pos is None or l > pos:
                pos = r
                res += 1
            else:
                pos = min(pos, r)
        return res
