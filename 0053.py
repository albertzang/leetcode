class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        m = nums[0]
        res = m
        for i in xrange(1, n):
            if m > 0:
                m = m + nums[i]
            else:
                m = nums[i]
            if m > res:
                res = m
        return res
