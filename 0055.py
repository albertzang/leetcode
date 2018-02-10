class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        can = 0
        for i in xrange(len(nums)):
            if can < i:
                return False
            can = max(can, nums[i] + i)
        return True
