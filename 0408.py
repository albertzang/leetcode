class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        n = 0
        i = 0
        l = len(word)
        for c in abbr:
            if c == '0' and n == 0:
                return False
            if str.isdigit(str(c)):
                n += ord(c) - ord('0')
                n *= 10
            else:
                i += n / 10
                if i >= l or word[i] != c:
                    return False
                n = 0
                i += 1
        return i + n / 10 == l
