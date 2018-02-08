class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        n = len(s)
        if n == 0:
            return True
        i = 0
        j = n - 1
        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            if not s[i].isalnum():
                i += 1
            if not s[j].isalnum():
                j -= 1
        return True
