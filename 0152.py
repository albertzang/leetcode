class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ma = nums[0]
        mi = nums[0]
        res = nums[0]
        for n in nums[1:]:
            ma_t = ma
            mi_t = mi
            ma = max(n, max(n * ma_t, n * mi_t))
            mi = min(n, min(n * ma_t, n * mi_t))
            res = max(ma, res)
        return res
