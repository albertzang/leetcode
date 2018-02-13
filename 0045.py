class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reach = 0
        step = 0
        i = 0
        n = len(nums)
        while i < n:
            if reach < i:
                return -1
            if reach >= n - 1:
                return step
            reached = reach
            while i <= reached and i < n:
                reach = max(reach, nums[i] + i)
                i += 1
            step += 1
