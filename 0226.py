# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        return self.invert(root)

    def invert(self, root):
        if root.left is None and root.right is None:
            pass
        elif root.left is None:
            root.left = self.invert(root.right)
            root.right = None
        elif root.right is None:
            root.right = self.invert(root.left)
            root.left = None
        else:
            l = self.invert(root.right)
            r = self.invert(root.left)
            root.left = l
            root.right = r
        return root
