class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = list([-1])
        n = len(heights)
        maxarea = 0
        for i in xrange(n + 1):
            while stack[-1] != -1 and (i == n or heights[stack[-1]] >= heights[i]):
                maxarea = max(maxarea, heights[stack.pop()] * (i - 1 - stack[-1]))
            stack.append(i)
        return maxarea
