class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        idx = -1
        for i, n in enumerate(nums):
            if n == 0 and idx == -1:
                idx = i
            if n != 0 and idx != -1:
                nums[i] = 0
                nums[idx] = n
                idx += 1
