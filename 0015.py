class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = list()
        n = len(nums)
        for i in xrange(n - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                s = -nums[i]
                l = i + 1
                r = n - 1
                while l < r:
                    if nums[l] + nums[r] < s:
                        l += 1
                    elif nums[l] + nums[r] > s:
                        r -= 1
                    else:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
        return res
