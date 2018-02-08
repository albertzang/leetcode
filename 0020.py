class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        h = { '(': ')', '[': ']', '{': '}' }
        stack = []
        for c in list(s):
            if c in h:
                stack.append(c)
            else:
                if len(stack) == 0 or h[stack.pop()] != c:
                    return False
        return len(stack) == 0
