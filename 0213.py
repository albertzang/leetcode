class Solution(object):
    def helper(self, nums):
        a = 0
        b = 0
        res = 0
        for n in nums:
            res = max(a + n, b)
            a = b
            b = res
        return res

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
