# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = float('-inf')
        self.findMax(root)
        return self.max

    def findMax(self, node):
        if node is None:
            return 0
        left = self.findMax(node.left)
        right = self.findMax(node.right)
        self.max = max(node.val + left + right, self.max)
        return max(node.val + max(left, right), 0)
