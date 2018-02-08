class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letters = [0] * 26
        for c in magazine:
            letters[ord(c) - ord('a')] += 1
        for c in ransomNote:
            idx = ord(c) - ord('a')
            if not letters[idx]:
                return False
            else:
                letters[idx] -= 1
        return True
