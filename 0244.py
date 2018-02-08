class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.h = dict()
        self.n = len(words)
        for i, w in enumerate(words):
            if w in self.h:
                self.h[w].append(i)
            else:
                self.h[w] = [i]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pos1 = self.h[word1]
        pos2 = self.h[word2]
        res = self.n
        for p1 in pos1:
            for p2 in pos2:
                res = min(res, abs(p1 - p2))
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
