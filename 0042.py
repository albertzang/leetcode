class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 3:
            return 0
        l = 0
        r = n - 1
        ml = height[l]
        mr = height[r]
        res = 0
        while l <= r:
            ml = max(ml, height[l])
            mr = max(mr, height[r])
            if ml < mr:
                res += ml - height[l]
                l += 1
            else:
                res += mr - height[r]
                r -= 1
        return res
