class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        m = len(v1)
        n = len(v2)
        for i in xrange(max(m, n)):
            if i >= n:
                if v1[i] > 0:
                    return 1
                else:
                    continue
            if i >= m:
                if v2[i] > 0:
                    return -1
                else:
                    continue
            if v1[i] > v2[i]:
                return 1
            if v2[i] > v1[i]:
                return -1
        return 0
