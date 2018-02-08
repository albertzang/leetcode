class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        adj = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                count += cell
                if cell:
                    if i > 0:
                        adj += grid[i - 1][j]
                    if j > 0:
                        adj += row[j - 1]
        return 4 * count - 2 * adj
