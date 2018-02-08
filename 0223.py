class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        res = (C - A) * (D - B) + (G - E) * (H - F)
        if E >= C or A >= G or B >= H or F >= D:
            return res
        x = min(C, G) - max(A, E)
        y = min(D, H) - max(B, F)
        return res - x * y
