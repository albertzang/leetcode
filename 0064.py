class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j != 0:
                    grid[i][j] += grid[i][j - 1]
                if i != 0 and j == 0:
                    grid[i][j] += grid[i - 1][j]
                if i != 0 and j != 0:
                    grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        return grid[m - 1][n - 1]
