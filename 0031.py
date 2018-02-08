class Solution(object):
    def swap(self, nums, i, j):
        if i != j:
            nums[i] = nums[i] + nums[j]
            nums[j] = nums[i] - nums[j]
            nums[i] = nums[i] - nums[j]

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                j = i
                while j < n and nums[j] > nums[i - 1]:
                    j += 1
                self.swap(nums, i - 1, j - 1)
                break
            i -= 1
        j = i
        k = n - 1
        while j < k:
            self.swap(nums, j, k)
            j += 1
            k -= 1
