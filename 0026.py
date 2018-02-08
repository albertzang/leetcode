class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        l = 1
        tail = nums[0]
        for i in xrange(1, n):
            if nums[i] > tail:
                if i != l:
                    nums[i] = nums[i] + nums[l]
                    nums[l] = nums[i] - nums[l]
                    nums[i] = nums[i] - nums[l]
                tail = nums[l]
                l = l + 1
        return l
