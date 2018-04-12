class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        l = defaultdict(int)
        s = defaultdict(int)
        for num in reversed(nums):
            D, P, V = num / 100, num / 10 % 10, num % 10
            l[D, P] = (l[D + 1, P * 2 - 1] + l[D + 1, P * 2]) or 1
            s[D, P] = s[D + 1, P * 2 - 1] + s[D + 1, P * 2] + V * l[D, P]
        return s[1, 1]
