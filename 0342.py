class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return not bool(num & num - 1) and bool(num & 0x55555555)
