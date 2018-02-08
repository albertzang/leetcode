class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = None
        b = None
        c = None
        for n in nums:
            if a is None or n > a:
                c = b
                b = a
                a = n
            elif n != a and (b is None or n > b):
                c = b
                b = n
            elif n != a and n != b and (c is None or n > c):
                c = n
        return a if c is None else c
