class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0 or k <= 0:
            return False
        d = dict()
        w = t + 1
        for i, n in enumerate(nums):
            b = n / w
            if b in d:
                return True
            if b - 1 in d and n - d[b - 1] < w:
                return True
            if b + 1 in d and d[b + 1] - n < w:
                return True
            d[b] = n
            if i >= k:
                del d[nums[i - k] / w]
        return False
