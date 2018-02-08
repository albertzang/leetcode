class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = n
        b = n
        while True:
            a = self.next(a)
            b = self.next(self.next(b))
            if a == 1:
                return True
            if a == b:
                return False

    def next(self, n):
        res = 0
        while n:
            res += pow(n % 10, 2)
            n /= 10
        return res
