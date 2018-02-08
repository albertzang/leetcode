class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        l = list(s)
        while i < j:
            t = l[i]
            l[i] = l[j]
            l[j] = t
            i += 1
            j -= 1
        return ''.join(l)
