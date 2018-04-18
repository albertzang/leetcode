class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in xrange(n):
            j = abs(nums[i]) - 1
            if nums[j] > 0:
                nums[j] *= -1
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i + 1)
        return res
