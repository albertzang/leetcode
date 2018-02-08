class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            lh = height[l]
            rh = height[r]
            if lh < rh:
                res = max(res, lh * (r - l))
                l += 1
            else:
                res = max(res, rh * (r - l))
                r -= 1
        return res
