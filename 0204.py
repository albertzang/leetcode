class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [0] * n
        for i in xrange(2, n):
            primes[i] = 1
        i = 2
        while i * i < n:
            if primes[i]:
                for j in xrange(i * i, n, i):
                    primes[j] = 0
            i += 1
        return sum(primes)
