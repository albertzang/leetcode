class Solution(object):
    def play(self, nums, desired):
        key = str(nums)
        if key in self.cache:
            return self.cache[key]
        if nums[-1] >= desired:
            return True
        else:
            for i in xrange(len(nums)):
                if not self.play(nums[:i] + nums[i + 1:], desired - nums[i]):
                    self.cache[key] = True
                    return True
            self.cache[key] = False
            return False

    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        nums = list(xrange(1, maxChoosableInteger + 1))
        if sum(nums) < desiredTotal:
            return False
        else:
            self.cache = {}
            return self.play(nums, desiredTotal)
