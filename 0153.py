class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        e = len(nums) - 1
        while s < e:
            m = (s + e) / 2
            if nums[m] >= nums[e]:
                s = m + 1
            else:
                e = m
        return nums[s]
