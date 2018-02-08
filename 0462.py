class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        res = 0
        while i < j:
            res += nums[j] - nums[i]
            i += 1
            j -= 1
        return res
