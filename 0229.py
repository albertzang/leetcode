class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        c1, c2, m1, m2 = 0, 0, None, None
        for n in nums:
            if n == m1:
                c1 += 1
            elif n == m2:
                c2 += 1
            elif c1 == 0:
                c1, m1 = 1, n
            elif c2 == 0:
                c2, m2 = 1, n
            else:
                c1 -= 1
                c2 -= 1
        return [x for x in [m1, m2] if nums.count(x) > len(nums) // 3]
