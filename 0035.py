class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s = 0
        e = len(nums)
        while s < e:
            m = (e + s) / 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                s = m + 1
            else:
                e = m
        return e
