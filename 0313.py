class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        l = len(primes)
        idx = [0] * l
        val = [1] * l
        res = [1]
        ugly = 1
        for _ in xrange(n - 1):
            prev = ugly
            ugly = None
            for i in xrange(l):
                if val[i] == prev:
                    val[i] = primes[i] * res[idx[i]]
                    idx[i] += 1
                if ugly is None or ugly > val[i]:
                    ugly = val[i]
            res.append(ugly)
        return res[-1]
