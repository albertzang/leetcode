class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        for i in xrange(2, numRows + 1):
            prev = res[-1]
            row = [1, 1]
            for j in xrange(1, i - 1):
                row.insert(j, prev[j - 1] + prev[j])
            res.append(row)
        return res
