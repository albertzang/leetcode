class Solution(object):

    def index(self, c):
        return ord(c) - ord('a')

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        table = [0] * 26
        for c in p:
            table[self.index(c)] += 1
        l = 0
        r = 0
        count = len(p)
        res = list()
        while r < len(s):
            if table[self.index(s[r])] > 0:
                count -= 1
            table[self.index(s[r])] -= 1
            r += 1
            if count == 0:
                res.append(l)
            if r - l == len(p):
                if table[self.index(s[l])] >= 0:
                    count += 1
                table[self.index(s[l])] += 1
                l += 1
        return res
