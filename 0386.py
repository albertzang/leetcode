class Solution(object):
    def dfs(self, node):
        if node <= self.n:
            self.res.append(node)
            for i in xrange(10):
                child = 10 * node + i
                if child <= self.n:
                    self.dfs(child)
                else:
                    break

    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        self.res = []
        self.n = n
        for i in xrange(1, 10):
            self.dfs(i)
        return self.res
