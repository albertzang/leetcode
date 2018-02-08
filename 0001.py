class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, n in enumerate(nums):
            if target - n in h:
                return [h[target - n], i]
            h[n] = i
