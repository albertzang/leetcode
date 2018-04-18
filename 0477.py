class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dist = 0
        n = len(nums)
        for i in xrange(32):
            bit = 0
            for num in nums:
                if num & (1 << i):
                    bit += 1
            dist += bit * (n - bit)
        return dist
