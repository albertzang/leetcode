class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        l = 1
        r = 1
        while x / l >= 10:
            l = l * 10
        while l > r:
            left = x / l % 10
            right = x % (10 * r) / r
            if left != right:
                return False
            l = l / 10
            r = r * 10
        return True
