class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for n in nums:
            m = abs(n) - 1
            if nums[m] > 0:
                nums[m] *= -1
            else:
                res.append(m + 1)
        return res
