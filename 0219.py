class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        h = dict()
        for i, n in enumerate(nums):
            if n in h and i - h[n] <= k:
                return True
            h[n] = i
        return False
