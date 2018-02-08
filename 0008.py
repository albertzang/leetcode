class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        n = len(str)
        if n == 0:
            return 0
        i = 0
        while i < n and (str[i] == ' ' or str[i] == '\t'):
            i += 1
        sign = 1
        if str[i] == '+' or str[i] == '-':
            sign = 1 if str[i] == '+' else -1
            i += 1
        total = 0
        while i < n:
            digit = ord(str[i]) - ord('0')
            if digit > 9 or digit < 0:
                break
            if sign == 1:
                if total > 214748364 or total == 214748364 and digit >= 7:
                    return 2147483647
            else:
                if total > 214748364 or total == 214748364 and digit >= 8:
                    return -2147483648
            total = total * 10 + digit
            i += 1
        return total * sign
