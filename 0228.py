class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if not nums:
            return res
        s = nums[0]
        e = nums[0]
        for n in nums[1:]:
            if n - e == 1:
                e = n
            else:
                if s == e:
                    res.append(str(s))
                else:
                    res.append('%d->%d' % (s, e))
                s = n
                e = n
        if s == e:
            res.append(str(s))
        else:
            res.append('%d->%d' % (s, e))
        return res
