class Solution(object):
    def size(self, node, n):
        size = 0
        next = node + 1
        while node <= n:
            size += min(next, n + 1) - node
            node *= 10
            next *= 10
        return size

    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        node = 1
        while k > 1:
            size = self.size(node, n)
            if size < k:
                node += 1
                k -= size
            else:
                node *= 10
                k -= 1
        return node
