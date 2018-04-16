# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, node):
        if not node:
            return (0, 0)
        left = self.helper(node.left)
        right = self.helper(node.right)
        return (node.val + left[1] + right[1], max(left) + max(right))

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.helper(root))
