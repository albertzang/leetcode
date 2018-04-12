# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find(self, node, target, so_far, cache):
        if node:
            complement = so_far + node.val - target
            if complement in cache:
                self.result += cache[complement]
            cache[so_far + node.val] += 1
            self.find(node.left, target, so_far + node.val, cache)
            self.find(node.right, target, so_far + node.val, cache)
            cache[so_far + node.val] -= 1

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        from collections import defaultdict
        cache = defaultdict(int)
        cache[0] = 1
        self.find(root, sum, 0, cache)
        return self.result
