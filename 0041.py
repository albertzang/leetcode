class Solution(object):
    def swap(self, nums, i, j):
        nums[i] = nums[i] + nums[j]
        nums[j] = nums[i] - nums[j]
        nums[i] = nums[i] - nums[j]

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in xrange(n):
            while nums[i] >= 1 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                self.swap(nums, i, nums[i] - 1)
        for i in xrange(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
