class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
        s = 0
        e = n - 1
        while s < e:
            m = (s + e) / 2
            if nums[m] == target:
                return m
            if nums[m] >= nums[s]:
                if target >= nums[s] and target < nums[m]:
                    e = m - 1
                else:
                    s = m + 1
            else:
                if target > nums[m] and target <= nums[e]:
                    s = m + 1
                else:
                    e = m - 1
        return s if nums[s] == target else -1
