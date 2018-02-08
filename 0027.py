class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        i = 0
        j = n - 1
        while i <= j:
            if nums[j] == val:
                j = j - 1
            else:
                if nums[i] == val:
                    nums[i] = nums[i] + nums[j]
                    nums[j] = nums[i] - nums[j]
                    nums[i] = nums[i] - nums[j]
                    i = i + 1
                    j = j - 1
                else:
                    i = i + 1
        return i
