class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        h = defaultdict(int)
        res = list()
        for n in nums1:
            h[n] += 1
        for n in nums2:
            if n in h and h[n]:
                res.append(n)
                h[n] -= 1
        return res
