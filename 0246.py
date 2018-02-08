class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        i = 0
        j = n - 1
        while i <= j:
            if i == j:
                return num[i] in ('0', '1', '8')
            else:
                if ((num[i] == '0' and num[j] == '0') or
                    (num[i] == '1' and num[j] == '1') or
                    (num[i] == '8' and num[j] == '8') or
                    (num[i] == '6' and num[j] == '9') or
                    (num[i] == '9' and num[j] == '6')):
                    i += 1
                    j -= 1
                else:
                    return False
        return True
