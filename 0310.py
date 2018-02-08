class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        adjacent = [set() for _ in xrange(n)]
        for u, v in edges:
            adjacent[u].add(v)
            adjacent[v].add(u)
        leaves = [i for i, adj in enumerate(adjacent) if len(adj) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                j = adjacent[i].pop()
                adjacent[j].remove(i)
                if len(adjacent[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves
