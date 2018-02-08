class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        from collections import defaultdict
        self.dict = defaultdict(set)
        for w in dictionary:
            self.dict[self.abbr(w)].add(w)

    def abbr(self, word):
        n = len(word)
        return word if n <= 2 else word[0] + str(n - 2) + word[-1]

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbr = self.abbr(word)
        if abbr in self.dict:
            if len(self.dict[abbr]) > 1:
                return False
            else:
                return word in self.dict[abbr]
        else:
            return True


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
