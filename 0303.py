class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        l = len(nums)
        self.sums = [0] * (l + 1)
        for i, n in enumerate(nums):
            self.sums[i + 1] = self.sums[i] + n

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j + 1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
