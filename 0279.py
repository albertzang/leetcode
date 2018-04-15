class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [0] * (n + 1)
        squares = []
        i = 1
        while i * i <= n:
            s = i * i
            squares.append(s)
            table[s] = 1
            i += 1
        for i in xrange(1, n + 1):
            if table[i] == 0:
                for s in squares:
                    if s <= i:
                        num = 1 + table[i - s]
                        if table[i] == 0 or table[i] > num:
                            table[i] = num
                    else:
                        break
        return table[n]
