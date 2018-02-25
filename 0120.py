class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if n == 0:
            return 0
        if n == 1:
            return triangle[0][0]
        for i in xrange(1, n):
            prev = triangle[i - 1]
            cur = triangle[i]
            res = None
            for j in xrange(i + 1):
                if j == 0:
                    cur[j] += prev[j]
                elif j == i:
                    cur[j] += prev[j - 1]
                else:
                    cur[j] += min(prev[j - 1:j + 1])
                if res is None:
                    res = cur[j]
                else:
                    res = min(res, cur[j])
        return res
