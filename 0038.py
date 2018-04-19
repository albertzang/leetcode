class Solution(object):
    def helper(self, s):
        d = s[0]
        c = 1
        res = ''
        for i in s[1:]:
            if i == d:
                c += 1
            else:
                res += '%d%s' % (c, d)
                d = i
                c = 1
        res += '%d%s' % (c, d)
        return res

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        while n > 1:
            res = self.helper(res)
            n -= 1
        return res
