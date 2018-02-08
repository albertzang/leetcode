class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r2i = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        res = 0
        l = len(s)
        i = 0
        while i < l:
            if i + 1 < l and s[i:i+2] in r2i:
                res = res + r2i[s[i:i+2]]
                i = i + 2
            else:
                res = res + r2i[s[i]]
                i = i + 1
        return res
