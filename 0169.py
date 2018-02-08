class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 1
        res = nums[0]
        for i in xrange(1, len(nums)):
            if cnt == 0:
                cnt = 1
                res = nums[i]
            else:
                if res == nums[i]:
                    cnt += 1
                else:
                    cnt -= 1
        return res
