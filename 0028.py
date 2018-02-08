class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        i = 0
        while True:
            j = 0
            while True:
                if j == m:
                    return i
                if i + j == n:
                    return -1
                if haystack[i + j] != needle[j]:
                    break
                j = j + 1
            i = i + 1
