class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        res = strs[0]
        for i in xrange(len(res)):
            for s in strs[1:]:
                if i == len(s) or res[i] != s[i]:
                    return res[:i]
        return res
