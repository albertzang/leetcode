class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 0
        for i, p in enumerate(points):
            hashmap = {}
            for j, q in enumerate(points):
                if i != j:
                    dist = math.pow(p[0] - q[0], 2) + math.pow(p[1] - q[1], 2)
                    if dist in hashmap:
                        hashmap[dist] += 1
                    else:
                        hashmap[dist] = 1
            for c in hashmap.values():
                count += c * (c - 1)
        return count
