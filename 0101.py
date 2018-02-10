# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSame(self, a, b):
        if a is None and b is None:
            return True
        elif a is None or b is None:
            return False
        else:
            return a.val == b.val and self.isSame(a.left, b.right) and self.isSame(a.right, b.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSame(root.left, root.right)
