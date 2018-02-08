class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        a = -1
        b = -1
        res = len(words)
        for i, word in enumerate(words):
            if word == word1:
                a = i
                if b != -1:
                    res = min(res, i - b)
            if word == word2:
                b = i
                if a != -1:
                    res = min(res, i - a)
        return res
