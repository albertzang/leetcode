class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s = map(int, secret)
        g = map(int, guess)
        count = [0] * 10
        bulls = 0
        cows = 0
        for i in xrange(len(s)):
            if s[i] == g[i]:
                bulls += 1
            else:
                if count[s[i]] < 0:
                    cows += 1
                if count[g[i]] > 0:
                    cows += 1
                count[s[i]] += 1
                count[g[i]] -= 1
        return '%dA%dB' % (bulls, cows)
