class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        matrix = map(lambda row: map(int, row), matrix)
        res = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j]:
                    if i > 0 and j > 0:
                        matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
                    res = max(res, matrix[i][j])
        return res ** 2
