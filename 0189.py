class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        k = k % n
        if k == 0:
            return
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start] = nums[start] + nums[end]
            nums[end] = nums[start] - nums[end]
            nums[start] = nums[start] - nums[end]
            start += 1
            end -= 1
