class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        b = 0
        res = 0
        for n in nums:
            res = max(a + n, b)
            a = b
            b = res
        return res
